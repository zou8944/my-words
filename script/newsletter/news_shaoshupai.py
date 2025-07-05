"""
https://sspai.com/feed
"""

import os
from datetime import datetime

import news_utils

logger = news_utils.setup_logger(__name__)


def fetch_news():
    """主函数：获取少数派新闻"""
    logger.info("开始获取少数派内容")
    entries = news_utils.get_rss_entries("https://sspai.com/feed", limit=30)
    if not entries:
        logger.warning("没有获取到任何文章")
        return

    file_contents = []

    for index, entry in enumerate(entries):
        title = entry.get("title", "无标题")
        link = entry.get("link", "无链接")
        summary = entry.get("summary", "无摘要")
        author = entry.get("author", "无作者")
        publish_time = news_utils.get_entry_datetime_formated(entry)

        # 预处理摘要内容
        if summary:
            summary = news_utils.convert_html_to_markdown(summary)
            if not summary.strip():
                summary = "无有效内容"

        file_contents.append(
            f"### {index + 1}. [{title}]({link})\n\n"
            f"> {summary} \n\n"
            f"<sub>作者: {author} | 发布时间: {publish_time}</sub>\n\n"
            f"---\n\n"
        )

    # 获取文件路径并保存
    filepath = get_today_news_file()
    full_content = "\n".join(file_contents)
    news_utils.save_markdown_to_file(full_content, filepath)
    logger.info(f"少数派内容已保存: {filepath}")


def get_today_news_file():
    """
    获取今天的少数派新闻存储路径
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    day_dir, _ = news_utils.create_newsletter_directory_structure()

    filename = f"shaoshupai_{current_date}.md"
    filepath = os.path.join(day_dir, filename)

    return filepath


def get_today_news_content() -> str:
    """
    获取今天的少数派新闻内容
    """
    filepath = get_today_news_file()
    # 如果今天的新闻文件存在，读取内容并返回；如果不存在，则调用 fetch_news() 写入然后再返回
    if os.path.exists(filepath):
        logger.info(f"今天的少数派新闻已存在，直接返回: {filepath}")
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()

    fetch_news()
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    print(fetch_news())
