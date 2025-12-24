"""
V2EX RSS Feed

只看最热门
https://rsshub.app/v2ex/tab/hot
"""


import news_utils

logger = news_utils.setup_logger(__name__)


def fetch_news():
    logger.info("获取 V2EX 论坛最热门消息...")
    entries = news_utils.get_rss_entries("https://www.v2ex.com/feed/tab/tech.xml", limit=100)
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

    filename = get_today_news_file()
    final_content = "\n".join(contents)
    if news_utils.put_file_to_r2_with_today(filename, final_content):
        logger.info(f"V2EX 热门帖子内容已保存到: {filename}")
    else:
        logger.error(f"无法保存 V2EX 热门帖子内容到: {filename}")
        return


def get_today_news_file():
    return f"v2ex_hot_{news_utils.current_date_formatted()}.md"


def get_today_news_content() -> str:
    filename = get_today_news_file()
    content = news_utils.get_file_from_r2_with_today(filename)
    if content:
        logger.info(f"今天的 V2EX 热门新闻已存在: {filename}")
        return content
    
    fetch_news()
    
    content = news_utils.get_file_from_r2_with_today(filename)
    assert content
    return content


if __name__ == "__main__":
    fetch_news()
    logger.info("V2EX 论坛消息抓取完成")
