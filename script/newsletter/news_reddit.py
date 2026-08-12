"""
Reddit 频道 RSS 源获取
频道 RSS 源格式: https://www.reddit.com/r/{channel}/top/.rss

包含以下频道：
- 吹水类:
  - AMA - Ask Me Anything
  - AskReddit
  - Showerthoughts
  - todayilearned
- 技术类:
  - devops
  - programming
  - explainlikeimfive
  - golang
  - rust
  - MachineLearning
"""

from datetime import datetime

import llm
import news_utils

logger = news_utils.setup_logger(__name__)


def concurrent_translate_title(titles: list[str]) -> list[str | None]:
    system_prompt = """你是一位资深的 Reddit 帖子翻译专家，负责将英文帖子标题翻译成中文。

## 任务目标：
将以下 Reddit 的帖子标题翻译成简洁流畅的中文标题。

## 输出要求：
- **语言风格**：自然、简洁、易懂
- **格式要求**：纯文本，不使用Markdown
- 保持原标题的语气和风格（提问、陈述、分享等）
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


def concurrent_summarize_content(contents: list[str]) -> list[str | None]:
    system_prompt = """你是一位资深的 Reddit 内容分析师，专门处理 Reddit 帖子的概览内容。

## 任务目标：
对 Reddit 帖子的 RSS 概览进行智能分析和总结。

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
- 专注于核心价值和实用信息
- 保持客观中立的表述
- 如果内容质量不高或信息不足，直接返回"无摘要"

请根据以上规则进行处理。"""

    user_prompts = [
        f"""请分析以下 Reddit 帖子概览内容：

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 概览内容：
{content}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

处理要求：
1. 判断内容是否只包含链接（如果是，返回"无摘要"）
2. 如果有实质内容，用50字以内总结核心要点
3. 专注于核心价值和关键信息
4. 使用简洁的中文表达

开始分析："""
        for content in contents
    ]

    return llm.concurrent_one_shoot([(system_prompt, user_prompt) for user_prompt in user_prompts])


def process_reddit_channel(rss_url: str, slug: str, file_title: str):
    logger.info(f"开始获取 Reddit 频道: {slug}")
    entries = news_utils.get_rss_entries(rss_url, 20)

    for entry in entries:
        entry["summary_md"] = news_utils.convert_html_to_markdown(entry.get("summary", "无摘要"))

    logger.info(f"开始并发处理 Reddit {slug} 频道标题翻译")
    translated_titles = concurrent_translate_title([entry.get("title", "无标题") for entry in entries])
    logger.info(f"开始并发处理 Reddit {slug} 频道摘要翻译")
    summaries = concurrent_summarize_content([entry.get("summary_md", "无摘要") for entry in entries])

    current_date = datetime.now().strftime("%Y-%m-%d")

    final_contents = [f"## {file_title} - {current_date}\n\n"]
    for index, entry in enumerate(entries):
        translated_title = translated_titles[index] if translated_titles[index] else "无标题"
        link = entry.get("link", "无链接")
        translated_summary = summaries[index] if summaries[index] else "无摘要"
        translated_summary_md = translated_summary.replace("\n", "\n> ")  # type: ignore
        author = entry.get("author", "无作者")
        publish_date_str = news_utils.get_entry_datetime_formated(entry)

        if len(translated_summary_md) < 5:
            final_contents.append(
                f"### {index + 1}. [{translated_title}]({link})\n"
                f"\n<sub>作者: {author} | 发布于: {publish_date_str}</sub>\n\n"
                f"---\n"
            )
        else:
            final_contents.append(
                f"### {index + 1}. [{translated_title}]({link})\n"
                f"> {translated_summary_md}\n"
                f"\n<sub>作者: {author} | 发布于: {publish_date_str}</sub>\n\n"
                f"---\n"
            )

    filename = get_today_news_file(slug)
    final_content = "\n".join(final_contents)
    if news_utils.put_file_to_r2_with_today(filename, final_content):
        logger.info(f"✓ {file_title} 频道内容已保存到 R2: {filename}")
    else:
        logger.error(f"✗ 无法保存 {file_title} 频道内容到 R2: {filename}")


def get_today_news_file(slug: str) -> str:
    return f"{slug}_{news_utils.current_date_formatted()}.md"


def all_reddit_channels() -> list[tuple[str, str, str]]:
    """返回 Reddit 技术频道配置: (slug, rss_url, title)"""
    # 只保留技术相关频道
    tech_channels = [
        ("devops", "Reddit DevOps"),
        ("programming", "Reddit Programming"),
        ("golang", "Reddit Golang"),
        ("rust", "Reddit Rust"),
        ("MachineLearning", "Reddit ML"),
    ]

    channels = []
    for channel, title in tech_channels:
        slug = f"reddit_{channel.lower()}"
        rss_url = f"https://www.reddit.com/r/{channel}/top/.rss"
        channels.append((slug, rss_url, title))

    return channels


def get_today_news_content() -> str:
    """获取所有 Reddit 频道的今日内容"""
    content = []
    for slug, url, title in all_reddit_channels():
        filename = get_today_news_file(slug)
        _content = news_utils.get_file_from_r2_with_today(filename)
        if _content:
            logger.info(f"今天的 {title} 频道内容已存在，直接读取: {filename}")
            content.append(_content)
            continue

        try:
            process_reddit_channel(url, slug, title)
        except Exception as e:
            logger.error(f"获取 {title} 频道失败: {e}")
            continue
        _content = news_utils.get_file_from_r2_with_today(filename)
        if _content:
            content.append(_content)
    return "\n".join(content)


if __name__ == "__main__":
    get_today_news_content()
