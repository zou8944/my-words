"""
新闻抓取和处理的公共工具模块
"""

import logging
import os
from datetime import datetime, timedelta
from typing import List, Optional

import boto3
import feedparser
import html2text
import httpx
import pytz
from botocore.exceptions import ClientError
from bs4 import BeautifulSoup
from dateutil import parser as dateparser

import config


def setup_logger(name: str):
    """设置和获取logger"""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


logger = setup_logger(__name__)


def get_rss_entries(rss_url: str, limit: int = 1000) -> List[dict]:
    """
    获取RSS源的条目

    Args:
        rss_url (str): RSS源URL
        limit (int): 限制获取的条目数量

    Returns:
        List[dict]: RSS条目列表，每个条目包含title、link、summary等信息
    """
    response = httpx.get(rss_url, timeout=10)
    response.raise_for_status()

    feed = feedparser.parse(response.content)

    if not feed.entries:
        logger.warning(f"RSS源 {rss_url} 中没有找到任何条目")
        return []

    # 限制条目数量
    entries = feed.entries[:limit]

    # 转换为标准dict列表
    dict_entries = [dict(entry) for entry in entries]

    return dict_entries


def fetch_and_convert_to_markdown(url: str) -> Optional[str]:
    """
    抓取指定URL的网页内容，并将其转换为Markdown格式

    Args:
        url (str): 要抓取的网页URL

    Returns:
        Optional[str]: 转换后的Markdown内容，如果失败则返回None
    """

    # 设置请求头，模拟浏览器访问
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    # 获取网页内容
    response = httpx.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    # 解析HTML内容
    soup = BeautifulSoup(response.content, "html.parser")

    # 移除不需要的元素（如脚本、样式等）
    for script in soup(["script", "style", "nav", "header", "footer", "aside"]):
        script.decompose()

    # 尝试找到主要内容区域
    main_content = None

    # 常见的主要内容选择器
    content_selectors = [
        "article",
        ".content",
        ".post-content",
        ".entry-content",
        ".article-content",
        "main",
        "#content",
        ".main-content",
    ]

    for selector in content_selectors:
        main_content = soup.select_one(selector)
        if main_content:
            break

    # 如果找不到主要内容区域，使用整个body
    if not main_content:
        main_content = soup.find("body")

    if not main_content:
        logger.warning("无法找到页面主要内容")
        return None

    # 转换为Markdown
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # 不换行
    h.unicode_snob = True  # 使用unicode字符

    markdown_content = h.handle(str(main_content))

    return markdown_content.strip()


def convert_html_to_markdown(html_content: str) -> str:
    """
    将HTML内容转换为Markdown格式

    Args:
        html_content (str): 要转换的HTML内容

    Returns:
        str: 转换后的Markdown内容
    """
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # 不换行
    h.unicode_snob = True  # 使用unicode字符

    markdown_content = h.handle(html_content)
    return markdown_content.strip()


def create_newsletter_directory_structure(dt: datetime = datetime.now()) -> tuple[str, str]:
    """
    创建Newsletter目录结构

    Returns:
        tuple[str, str]: (日期目录, 日期文件)
    """
    base_dir = config.settings.newsletter_dir

    # 获取当前日期
    year_month = dt.strftime("%Y-%m")
    date = dt.strftime("%Y-%m-%d")

    # 构建目录路径
    month_dir = os.path.join(base_dir, year_month)
    day_dir = os.path.join(month_dir, f"{date}-news")
    day_file = os.path.join(month_dir, f"{date}.md")

    # 创建目录结构
    os.makedirs(day_dir, exist_ok=True)

    return day_dir, day_file


def save_markdown_to_file(markdown_content: str, filepath: str):
    """
    将Markdown内容保存到文件中

    Args:
        markdown_content (str): 要保存的Markdown内容
        filepath (str): 文件路径

    Returns:
        bool: 保存成功返回True，失败返回False
    """

    # 确保文件名以.md结尾
    if not filepath.endswith(".md"):
        filepath += ".md"

    # 创建输出目录（如果不存在）
    output_dir = os.path.dirname(filepath)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 保存文件
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    logger.info(f"Markdown内容已保存到: {filepath}")
    return True


def get_entry_datetime(entry) -> Optional[datetime]:
    if "published_parsed" in entry:
        published_parsed = entry["published_parsed"]
        return datetime(
            year=published_parsed.tm_year,
            month=published_parsed.tm_mon,
            day=published_parsed.tm_mday,
            hour=published_parsed.tm_hour,
            minute=published_parsed.tm_min,
            second=published_parsed.tm_sec,
        )
    elif "updated_parsed" in entry:
        return dateparser.parse(entry["updated_parsed"])
    elif "published" in entry:
        return dateparser.parse(entry["published"])
    elif "updated" in entry:
        return dateparser.parse(entry["updated"])
    return None


def get_entry_datetime_formated(entry) -> Optional[str]:
    dt = get_entry_datetime(entry)
    if dt:
        return dt.strftime("%Y-%m-%d %H:%M")
    return None


def get_date_formatted(delta: timedelta) -> str:
    beijing_tz = pytz.timezone("Asia/Shanghai")
    target_date = datetime.now(beijing_tz) + delta
    return target_date.strftime("%Y-%m-%d")


def current_date_formatted() -> str:
    return get_date_formatted(timedelta(days=0))


def current_datetime_formatted() -> str:
    beijing_tz = pytz.timezone("Asia/Shanghai")
    current_datetime = datetime.now(beijing_tz)
    return current_datetime.strftime("%Y-%m-%d %H:%M:%S")


def yesterday_date_formatted() -> str:
    return get_date_formatted(timedelta(days=-1))


def get_r2_dir_with_today() -> str:
    today_formatted = current_date_formatted()
    return f"newsletter/{today_formatted}"


def _handle_r2_key(key: str) -> str:
    key = key.strip("/")
    if key.startswith("newsletter/"):
        return key
    return f"newsletter/{key}"


def get_file_from_r2_with_today(object_key: str) -> Optional[str]:
    object_key = f"{current_date_formatted()}/{object_key}"
    return _get_file_from_r2(object_key)


def _get_file_from_r2(object_key: str) -> Optional[str]:
    object_key = _handle_r2_key(object_key)
    try:
        session = boto3.Session()
        s3 = session.client(
            service_name="s3",
            endpoint_url=config.settings.r2_endpoint,
            aws_access_key_id=config.settings.r2_access_key_id,
            aws_secret_access_key=config.settings.r2_secret_access_key,
            region_name="auto",  # R2不需要特定区域
        )
        response = s3.get_object(Bucket=config.settings.r2_bucket, Key=object_key)
        content = response["Body"].read().decode("utf-8")
        return content
    except ClientError as e:
        if e.response["Error"]["Code"] == "NoSuchKey":
            logger.warning(f"文件 {object_key} 在 R2 中不存在")
            return None
        else:
            logger.error(f"从 R2 读取 {object_key} 失败: {e}")
            return None
    except Exception as e:
        logger.error(f"从 R2 读取 {object_key} 失败: {e}")
        return None


def put_file_to_r2_with_today(object_key: str, content: str) -> bool:
    object_key = f"{current_date_formatted()}/{object_key}"
    return _put_file_to_r2(object_key, content)


def _put_file_to_r2(object_key: str, content: str) -> bool:
    if len(object_key) > 100:
        logger.error(f"我怀疑你把参数传反了: {object_key}")
        return False
    object_key = _handle_r2_key(object_key)
    try:
        session = boto3.Session()
        s3 = session.client(
            service_name="s3",
            endpoint_url=config.settings.r2_endpoint,
            aws_access_key_id=config.settings.r2_access_key_id,
            aws_secret_access_key=config.settings.r2_secret_access_key,
            region_name="auto",  # R2不需要特定区域
        )
        s3.put_object(Bucket=config.settings.r2_bucket, Key=object_key, Body=content)
        logger.info(f"文件 {object_key} 已成功上传到 R2")
        return True
    except Exception as e:
        logger.error(f"上传文件 {object_key} 到 R2 失败: {e}")
        return False


def copy_from_r2(prefix: str, target_dir: str) -> bool:
    try:
        session = boto3.Session()
        s3 = session.client(
            service_name="s3",
            endpoint_url=config.settings.r2_endpoint,
            aws_access_key_id=config.settings.r2_access_key_id,
            aws_secret_access_key=config.settings.r2_secret_access_key,
            region_name="auto",  # R2不需要特定区域
        )
        paginator = s3.get_paginator("list_objects_v2")
        for page in paginator.paginate(Bucket=config.settings.r2_bucket, Prefix=prefix):
            for obj in page.get("Contents", []):
                key = obj["Key"]
                if not key.endswith("/"):  # 跳过目录
                    local_path = os.path.join(target_dir, os.path.basename(key))
                    s3.download_file(config.settings.r2_bucket, key, local_path)
                    logger.info(f"已从 R2 下载 {key} 到 {local_path}")
        return True
    except Exception as e:
        logger.error(f"从 R2 复制文件失败: {e}")
        return False


if __name__ == "__main__":
    print(get_file_from_r2_with_today("example.txt"))
    print(put_file_to_r2_with_today("example.txt", "Hello, R2!"))
