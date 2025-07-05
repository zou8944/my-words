"""
V2EX RSS Feed

只看最热门
https://rsshub.app/v2ex/tab/hot
"""

import os
from datetime import datetime

import news_utils

logger = news_utils.setup_logger(__name__)


def fetch_news():
    logger.info("获取 V2EX 论坛最热门消息...")
    entries = news_utils.get_rss_entries("https://rsshub.app/v2ex/tab/hot", limit=100)
    if not entries:
        logger.warning("没有获取到任何文章")
        return None

    contents = ["## V2EX 热门帖子\n"]
    for index, entry in enumerate(entries):
        title = entry.get("title", "无标题")
        link = entry.get("link", "无链接")
        author = entry.get("author", "无作者")
        published_format = news_utils.get_entry_datetime_formated(entry)
        summary = entry.get("summary", "无摘要")
        summary_md = news_utils.convert_html_to_markdown(summary)
        summary_md = summary_md.split("#1: ")[0]  # 只保留第一段内容
        summary_md = summary_md.replace("\n", "\n> ")  # 去除换行符，保持单行格式

        contents.append(f"### {index + 1}. [{title}]({link})\n\n> {summary_md} \n\n")
        contents.append(f"<sub>作者: {author} | 发布时间: {published_format}</sub>\n\n")
        contents.append("---\n\n")

    filepath = get_today_news_file()
    final_content = "\n".join(contents)
    news_utils.save_markdown_to_file(final_content, filepath)
    logger.info(f"V2EX 热门帖子内容已保存: {filepath}")


def get_today_news_file():
    """
    获取今天的V2EX热门新闻存储路径
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    day_dir, _ = news_utils.create_newsletter_directory_structure()

    filename = f"v2ex_hot_{current_date}.md"
    filepath = os.path.join(day_dir, filename)

    return filepath


def get_today_news_content() -> str:
    filepath = get_today_news_file()
    if os.path.exists(filepath):
        logger.info(f"今天的V2EX热门新闻已存在，直接返回: {filepath}")
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()

    fetch_news()
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    fetch_news()
    logger.info("V2EX 论坛消息抓取完成")
