"""
https://36kr.com/feed
"""

import os
from datetime import datetime
from typing import Optional

import llm
from news_utils import (
    convert_html_to_markdown,
    create_newsletter_directory_structure,
    get_rss_entries,
    save_markdown_to_file,
    setup_logger,
)

logger = setup_logger(__name__)


def concurrent_summarize_content(contents: list[str]) -> list[Optional[str]]:
    system_prompt = """你是一个新闻摘要助手，请为36氪新闻内容生成简洁的摘要。

要求：
- 输出20-50字的简洁摘要
- 提取文章的核心信息和要点
- 语言简洁明了，易于理解
- 如果内容是广告或无实质内容，返回"无有效内容"
- 纯文本输出，不使用格式标记
- 直接输出内容，不需要额外的解释或格式化"""

    user_prompts = []
    for content in contents:
        user_prompts.append(f"请为以下内容生成20-50字的简洁摘要：\n\n{content}")

    return llm.concurrent_one_shoot([(system_prompt, user_prompt) for user_prompt in user_prompts])


def get_today_news_file():
    """
    获取今天的新闻存储路径
    """

    current_date = datetime.now().strftime("%Y-%m-%d")
    day_dir, _ = create_newsletter_directory_structure()

    raw_filename = f"36kr_raw_{current_date}.md"
    sum_filename = f"36kr_summary_{current_date}.md"

    raw_filepath = os.path.join(day_dir, raw_filename)
    sum_filepath = os.path.join(day_dir, sum_filename)

    return raw_filepath, sum_filepath


def fetch_news():
    """主函数：处理36氪新闻源"""
    logger.info("开始处理36氪新闻源")

    rss_url = "https://36kr.com/feed"
    entries = get_rss_entries(rss_url, limit=20)

    # 预处理内容并转换为Markdown
    md_summaries = []
    for entry in entries:
        raw_summary = entry.get("summary", "无摘要")
        md_summary = convert_html_to_markdown(raw_summary)
        md_summaries.append(md_summary)

    # 使用处理后的内容生成LLM摘要
    logger.info("开始使用LLM生成摘要")
    llm_summaries = concurrent_summarize_content(md_summaries)
    logger.info("LLM摘要生成完成")

    raw_contents = []
    sum_contents = []

    for i, entry in enumerate(entries):
        title = entry.get("title", "无标题")
        link = entry.get("link", "无链接")
        md_summary = md_summaries[i]
        llm_summary = llm_summaries[i] if llm_summaries[i] else "无摘要"
        if llm_summary:
            llm_summary = llm_summary.replace("\n", "\n> ")

        # 为原始内容添加预处理标记
        if md_summary == "广告推广内容":
            raw_contents.append(f"# {title}\n\n> [已过滤：疑似广告推广内容]\n\n[原文链接]({link})\n\n")
        else:
            raw_contents.append(f"# {title}\n\n> {md_summary}\n\n[原文链接]({link})\n\n")

        sum_contents.append(f"### {i + 1}. [{title}]({link})\n\n> {llm_summary}\n\n---\n\n")

    raw_filepath, sum_filepath = get_today_news_file()

    save_markdown_to_file("\n".join(raw_contents), raw_filepath)
    save_markdown_to_file("\n".join(sum_contents), sum_filepath)


def get_today_news_content() -> str:
    """
    获取今天的新闻
    """
    _, sum_filepath = get_today_news_file()

    # 如果今天的新闻文件存在，读取内容并返回；如果不在在，则调用 fetch_news() 写入然后再返回
    if os.path.exists(sum_filepath):
        logger.info(f"今天的36氪新闻已存在，直接返回: {sum_filepath}")
        with open(sum_filepath, "r", encoding="utf-8") as f:
            return f.read()

    fetch_news()
    with open(sum_filepath, "r", encoding="utf-8") as f:
        return f.read()  # 返回最新的内容


if __name__ == "__main__":
    fetch_news()
