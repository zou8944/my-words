"""
https://sspai.com/feed
"""

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
    filename = get_today_news_file()
    full_content = "\n".join(file_contents)
    if news_utils.put_file_to_r2_with_today(filename, full_content):
        logger.info(f"少数派内容已保存到: {filename}")
    else:
        logger.error(f"无法保存少数派内容到: {filename}")
        return


def get_today_news_file():
    return f"shaoshupai_{news_utils.current_date_formatted()}.md"


def get_today_news_content() -> str:
    """
    获取今天的少数派新闻内容
    """
    filename = get_today_news_file()
    content = news_utils.get_file_from_r2_with_today(filename)
    if content:
        logger.info(f"今天的少数派新闻已存在: {filename}")
        return content

    fetch_news()

    content = news_utils.get_file_from_r2_with_today(filename)
    assert content
    return content


if __name__ == "__main__":
    print(fetch_news())
