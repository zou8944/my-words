"""
这里有各种各样的 Hacker News RSS 源: https://hnrss.github.io/，从中选择比较 OK 的总结到我的日报中吧。
首页文章(热点)：https://hnrss.org/frontpage
ask(看看别人交流的啥): https://hnrss.org/ask
show(看看别人展示了啥): https://hnrss.org/show
过去几天最好的: https://hnrss.org/best
高赞评论 RSS: https://hnrss.org/bestcomments
"""

from datetime import datetime
from typing import Optional

import llm
import news_utils

logger = news_utils.setup_logger(__name__)


def concurrent_translate_title(titles: list[str]) -> list[Optional[str]]:
    system_prompt = """你是一位资深的技术文章翻译专家，负责将英文技术文章标题翻译成中文。

## 任务目标：
将以下 Hackernews 的文章标题翻译成简洁流畅的中文标题。

## 输出要求：
- **语言风格**：专业、简洁、易懂
- **格式要求**：纯文本，不使用Markdown
- 如果标题中包含 "Show HN" "Tell HN" "Ask HN"，请保留他们不翻译
"""

    user_prompts = [
        f"""请将以下英文标题翻译成中文：

---
英文标题：
{title}
---

开始翻译："""
        for title in titles
    ]

    return llm.concurrent_one_shoot([(system_prompt, user_prompt) for user_prompt in user_prompts])


def concurrent_translate_comments(comments: list[str]) -> list[Optional[str]]:
    system_prompt = """你是一位资深的技术社区评论翻译专家，专门处理Hacker News的高质量评论内容。

## 任务目标：
将Hacker News的精选评论翻译成自然流畅的中文，保持原评论的技术深度和讨论价值。

## 翻译原则：
1. **保持技术准确性**：确保专业术语和概念翻译准确
2. **自然的中文表达**：避免生硬的直译，使用符合中文习惯的表达
3. **保留语气风格**：维持原评论的语气（质疑、赞同、分析等）
4. **简洁明了**：去除冗余表达，保持核心观点清晰

## 处理规则：
- 专业术语优先使用通用的中文译名
- 保留关键的英文术语（如API、SDK等）并加中文注释
- 对于口语化或俚语表达，转换为相应的中文习惯表达
- 如果评论包含代码或链接，保持原样不变

## 输出要求：
- **语言风格**：专业、自然、易读
- **格式要求**：纯文本，不使用Markdown
- **长度控制**：保持原意的前提下尽量简洁

请确保翻译既专业又易懂，适合中文技术社区的阅读习惯。"""

    user_prompts = [
        f"""请将以下Hacker News评论翻译成中文：

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💬 英文评论：
{comment}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

翻译要求：
1. 保持技术术语的准确性
2. 使用自然的中文表达方式
3. 保留原评论的语气和观点
4. 确保翻译简洁易读
5. 直接输出翻译结果，不需要额外的解释或格式化

开始翻译："""
        for comment in comments
    ]

    return llm.concurrent_one_shoot([(system_prompt, user_prompt) for user_prompt in user_prompts])


def concurrent_summarize_content(contents: list[str]) -> list[Optional[str]]:
    system_prompt = """你是一位资深的技术新闻分析师，专门处理Hacker News的RSS概览内容。

## 任务目标：
对Hacker News的RSS概览进行智能分析和总结。

## 处理规则：
1. **内容判断**：
   - 如果内容只包含链接（通常少于50字符且主要是URL），直接返回"无摘要"
   - 如果内容包含实质性描述或介绍，进行总结

2. **总结要求**：
   - **字数限制**：严格控制在50字以内
   - **语言风格**：简洁、准确、易懂
   - **格式要求**：纯文本，不使用Markdown
   - **内容重点**：提取核心观点和关键信息

## 质量标准：
- 忽略无关的元数据（点赞数、评论数等）
- 专注于技术价值和实用信息
- 保持客观中立的表述
- 如果内容质量不高或信息不足，直接返回"无摘要"

请根据以上规则进行处理。"""

    user_prompts = [
        f"""请分析以下Hacker News RSS概览内容：

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 概览内容：
{content}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

处理要求：
1. 判断内容是否只包含链接（如果是，返回"无摘要"）
2. 如果有实质内容，用50字以内总结核心要点
3. 专注于技术价值和关键信息
4. 使用简洁的中文表达

开始分析："""
        for content in contents
    ]

    return llm.concurrent_one_shoot([(system_prompt, user_prompt) for user_prompt in user_prompts])


def process_top_hn(rss_url: str, slug: str, file_title: str):
    logger.info(f"开始获取 Hacker News RSS 源: {slug}")
    entries = news_utils.get_rss_entries(rss_url, 20)

    for entry in entries:
        entry["summary_md"] = news_utils.convert_html_to_markdown(entry.get("summary", "无摘要"))

    logger.info("开始并发处理 Hacker News 文章标题翻译")
    translated_titles = concurrent_translate_title([entry.get("title", "无标题") for entry in entries])
    logger.info("开始并发处理 Hacker News 文章摘要翻译")
    if rss_url.endswith("bestcomments"):
        summaries = concurrent_translate_comments([entry.get("summary_md", "无摘要") for entry in entries])
    else:
        summaries = concurrent_summarize_content([entry.get("summary_md", "无摘要") for entry in entries])

    current_date = datetime.now().strftime("%Y-%m-%d")

    final_contents = [f"## {file_title} - {current_date}\n\n"]
    for index, entry in enumerate(entries):
        translated_title = translated_titles[index] if translated_titles[index] else "无标题"
        # link = entry.get("link", "无链接")
        comments = entry.get("comments", "无评论链接")
        translated_summary = summaries[index] if summaries[index] else "无摘要"
        translated_summary_md = translated_summary.replace("\n", "\n> ")  # type: ignore # 去除换行符，保持单行格式
        author = entry.get("author", "无作者")
        publish_date_str = news_utils.get_entry_datetime_formated(entry)
        if len(translated_summary_md) < 5:
            final_contents.append(
                f"### {index + 1}. [{translated_title}]({comments})\n"
                f"\n<sub>作者: {author} | 发布于: {publish_date_str}</sub>\n\n"
                f"---\n"
            )
        else:
            final_contents.append(
                f"### {index + 1}. [{translated_title}]({comments})\n"
                f"> {translated_summary_md}\n"
                f"\n<sub>作者: {author} | 发布于: {publish_date_str}</sub>\n\n"
                f"---\n"
            )

    filename = get_today_news_file(slug)
    final_content = "\n".join(final_contents)
    if news_utils.put_file_to_r2_with_today(filename, final_content):
        logger.info(f"✓ {file_title} 新闻已保存到 R2: {filename}")
    else:
        logger.error(f"✗ 无法保存 {file_title} 新闻到 R2: {filename}")


def get_today_news_file(slug: str) -> str:
    return f"{slug}_{news_utils.current_date_formatted()}.md"


def all_rss_urls() -> list[tuple[str, str, str]]:
    return [
        ("hacker_news_frontpage", "https://hnrss.org/frontpage", "Hacker News 首页"),
        ("hacker_news_best", "https://hnrss.org/best", "Hacker News 近期最佳"),
        ("hacker_news_top_comments", "https://hnrss.org/bestcomments", "Hacker News 高赞评论"),
        ("hacker_news_ask", "https://hnrss.org/ask", "Hacker News 问答"),
        ("hacker_news_show", "https://hnrss.org/show", "Hacker News 展示"),
        ("hacker_news_audio_tech", "https://hnrss.org/newest?q=asr+OR+tts+OR+stt", "Hacker News 音频技术"),
    ]


def get_today_news_content() -> str:
    # 把几个都加成一个
    content = []
    for slug, url, title in all_rss_urls():
        filename = get_today_news_file(slug)
        _content = news_utils.get_file_from_r2_with_today(filename)
        if _content:
            logger.info(f"今天的 {title} 新闻已存在，直接读取: {filename}")
            content.append(_content)
            continue

        process_top_hn(url, slug, title)
        _content = news_utils.get_file_from_r2_with_today(filename)
        assert _content
        content.append(_content)
    return "\n".join(content)


if __name__ == "__main__":
    get_today_news_content()
