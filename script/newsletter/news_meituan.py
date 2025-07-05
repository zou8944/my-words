"""
美团技术团队

https://tech.meituan.com/feed/

处理逻辑：获取发布日期为今天的那篇文章的链接
"""

import os
from datetime import datetime, timedelta
from typing import Optional

import llm
import news_utils

logger = news_utils.setup_logger(__name__)


def get_today_news_file():
    """
    获取今天的GitHub Trending新闻存储路径
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    day_dir, _ = news_utils.create_newsletter_directory_structure()

    filename = f"meituan_{current_date}.md"
    filepath = os.path.join(day_dir, filename)

    return filepath


def summarize_content(content: str) -> Optional[str]:
    system_prompt = """你是一位专业的技术内容分析师，擅长从复杂的技术文章中提取核心价值。

你的任务是：
1. 识别文章的核心技术主题和创新点
2. 提炼关键的技术方案、架构设计或实践经验
3. 突出对读者有实际价值的技术洞察
4. 用简洁专业的语言进行总结

总结要求：
- 长度控制在100-150字
- 使用技术术语但保持可读性
- 重点突出技术亮点和实用价值
- 避免冗余表述，确保信息密度高"""

    user_prompt = f"""请对以下技术文章进行专业总结：

【文章内容】
{content}

【输出要求】
- 普通文本格式
- 重点突出技术创新点和实践价值
- 100字左右的精炼总结"""

    return llm.one_shoot(system_prompt, user_prompt)


def fetch_news():
    logger.info("开始抓取美团技术团队今天发布的文章")
    entries = news_utils.get_rss_entries("https://tech.meituan.com/feed/", limit=30)
    if not entries:
        logger.warning("没有获取到任何文章")
        return

    final_contents = []
    for entry in entries:
        published_datetime = news_utils.get_entry_datetime(entry)
        if not published_datetime:
            raise Exception("无法获取文章的发布日期")

        published_date = published_datetime.strftime("%Y-%m-%d")
        current_date = datetime.now().strftime("%Y-%m-%d")
        yesterday_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        if published_date != current_date and published_date != yesterday_date:
            continue

        title = entry.get("title", "无标题")
        link = entry.get("link", "")

        logger.info(f"找到今天的文章: {title} ({link})")
        content = news_utils.fetch_and_convert_to_markdown(link)
        if not content:
            raise Exception(f"无法获取文章内容: {link}")

        logger.info("开始对文章内容进行总结")
        summary = summarize_content(content)
        if not summary:
            raise Exception(f"无法获取文章摘要: {link}")
        logger.info("总结完成")
        final_contents.append(f"### {title}\n\n> {published_date}\n\n{summary}\n\n[阅读全文]({link})\n\n")

    if not final_contents:
        logger.info("美团技术团队今天没有发布新文章，将写一个空文件")
        final_contents = ["今天没有新的文章发布"]

    # 获取文件路径并保存
    filepath = get_today_news_file()

    full_content = "\n".join(final_contents)
    news_utils.save_markdown_to_file(full_content, filepath)
    logger.info(f"美团技术团队内容已保存: {filepath}")


def get_today_posts_content():
    filepath = get_today_news_file()
    if os.path.exists(filepath):
        logger.info("今日美图技术团队文章已存在，直接读取内容")
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()

    fetch_news()
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

    return None


if __name__ == "__main__":
    print(get_today_posts_content())
