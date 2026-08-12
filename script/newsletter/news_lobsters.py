"""
Lobsters 技术社区 RSS
https://lobste.rs/rss

替代 V2EX，质量更高（有点赞/踩机制，技术内容集中）。
"""

import news_utils

logger = news_utils.setup_logger(__name__)

LOBSTERS_RSS_URL = "https://lobste.rs/rss"


def fetch_news():
    """抓取 Lobsters 技术社区热门内容"""
    logger.info("开始获取 Lobsters 技术社区内容...")
    entries = news_utils.get_rss_entries(LOBSTERS_RSS_URL, limit=30)
    if not entries:
        logger.warning("没有获取到任何文章")
        return

    contents = ["## Lobsters 技术社区\n"]
    for index, entry in enumerate(entries):
        title = entry.get("title", "无标题")
        link = entry.get("link", "无链接")
        author = entry.get("author", "无作者")
        published_format = news_utils.get_entry_datetime_formated(entry)
        summary = entry.get("summary", "")
        summary_md = news_utils.convert_html_to_markdown(summary) if summary else ""
        summary_md = summary_md.replace("\n", "\n> ") if summary_md else ""

        if summary_md and len(summary_md) > 5:
            contents.append(
                f"### {index + 1}. [{title}]({link})\n\n> {summary_md}\n\n"
                f"<sub>作者: {author} | 发布时间: {published_format}</sub>\n\n---\n\n"
            )
        else:
            contents.append(
                f"### {index + 1}. [{title}]({link})\n\n"
                f"<sub>作者: {author} | 发布时间: {published_format}</sub>\n\n---\n\n"
            )

    filename = get_today_news_file()
    final_content = "\n".join(contents)
    if news_utils.put_file_to_r2_with_today(filename, final_content):
        logger.info(f"Lobsters 内容已保存到: {filename}")
    else:
        logger.error(f"无法保存 Lobsters 内容到: {filename}")


def get_today_news_file():
    return f"lobsters_{news_utils.current_date_formatted()}.md"


def get_today_news_content() -> str:
    """获取今天的 Lobsters 内容"""
    filename = get_today_news_file()
    content = news_utils.get_file_from_r2_with_today(filename)
    if content:
        logger.info(f"今天的 Lobsters 内容已存在: {filename}")
        return content

    try:
        fetch_news()
    except Exception as e:
        logger.error(f"获取 Lobsters 内容失败: {e}")
        return ""

    content = news_utils.get_file_from_r2_with_today(filename)
    return content or ""


if __name__ == "__main__":
    fetch_news()
    logger.info("Lobsters 内容抓取完成")
