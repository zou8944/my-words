"""
工程博客 RSS 聚合

已验证可达的 RSS 源，统一抓取、去重、摘要。
每周抓取一次，单篇深度高。
"""

from datetime import datetime, timedelta
from typing import Optional

import llm
import news_utils

logger = news_utils.setup_logger(__name__)

BLOG_SOURCES = [
    # (slug, rss_url, title)
    ("cloudflare_blog",    "https://blog.cloudflare.com/rss/",               "Cloudflare Blog"),
    ("aws_architecture",   "https://aws.amazon.com/blogs/architecture/feed/", "AWS Architecture Blog"),
    ("netflix_tech",       "https://netflixtechblog.com/feed",               "Netflix Tech Blog"),
    ("stripe_engineering", "https://stripe.com/blog/feed.rss",               "Stripe Engineering"),
    ("meta_engineering",   "https://engineering.fb.com/feed/",               "Meta Engineering"),
    ("github_engineering", "https://github.blog/engineering/feed/",          "GitHub Engineering"),
    ("pingcap",            "https://www.pingcap.com/blog/feed/",             "PingCAP"),
    ("openai_blog",        "https://openai.com/blog/rss.xml",               "OpenAI Blog"),
]


def concurrent_summarize_content(contents: list[str]) -> list[Optional[str]]:
    system_prompt = """你是一位资深的技术内容分析师，专门为后端/AI 工程师撰写博客文章摘要。

## 任务目标：
将工程博客文章的内容转换为简洁有力的中文摘要。

## 输出要求：
- **字数限制**：50字左右
- **内容重点**：核心技术创新点、架构设计、实践价值
- **语言风格**：专业、简洁、易懂
- **格式要求**：纯文本，不使用Markdown

## 关注要点：
1. 解决了什么技术问题
2. 使用了什么架构或方法
3. 对后端/AI工程师有什么参考价值
4. 有什么独特的工程洞察

请确保摘要突出工程价值，而非泛泛而谈。"""

    user_prompts = [
        f"""请为以下工程博客文章生成专业摘要：

---
文章内容：
{content[:10000]}
---

要求：
1. 提取核心技术创新点
2. 用50字以内简洁描述
3. 突出对后端/AI工程师的实践价值
4. 使用中文输出

开始总结："""
        for content in contents
    ]

    return llm.concurrent_one_shoot([(system_prompt, user_prompt) for user_prompt in user_prompts])


def get_today_news_file(slug: str) -> str:
    return f"blog_{slug}_{news_utils.current_date_formatted()}.md"


def fetch_blog_source(slug: str, rss_url: str, title: str):
    """抓取单个工程博客源"""
    logger.info(f"开始获取工程博客: {title}")
    entries = news_utils.get_rss_entries(rss_url, limit=20)

    if not entries:
        logger.warning(f"没有获取到 {title} 的文章")
        return

    # 只保留最近 7 天的文章
    seven_days_ago = datetime.now() - timedelta(days=7)
    recent_entries = []
    for entry in entries:
        pub_dt = news_utils.get_entry_datetime(entry)
        if pub_dt and pub_dt >= seven_days_ago:
            recent_entries.append(entry)

    if not recent_entries:
        logger.info(f"{title} 最近 7 天没有新文章")
        return

    # 预处理摘要
    for entry in recent_entries:
        summary = entry.get("summary", "无摘要")
        entry["summary_md"] = news_utils.convert_html_to_markdown(summary)

    # LLM 摘要
    summaries = concurrent_summarize_content([entry["summary_md"] for entry in recent_entries])

    # 构建内容
    current_date = datetime.now().strftime("%Y-%m-%d")
    final_contents = [f"## {title} - {current_date}\n\n"]
    for index, entry in enumerate(recent_entries):
        entry_title = entry.get("title", "无标题")
        link = entry.get("link", "无链接")
        summary = summaries[index] if summaries[index] else "无摘要"
        publish_date_str = news_utils.get_entry_datetime_formated(entry)

        final_contents.append(
            f"### [{entry_title}]({link})\n"
            f"> {summary}\n"
            f"\n<sub>发布于: {publish_date_str}</sub>\n\n"
            f"---\n"
        )

    filename = get_today_news_file(slug)
    final_content = "\n".join(final_contents)
    if news_utils.put_file_to_r2_with_today(filename, final_content):
        logger.info(f"✓ {title} 博客已保存到 R2: {filename}")
    else:
        logger.error(f"✗ 无法保存 {title} 博客到 R2: {filename}")


def get_today_news_content() -> str:
    """获取所有工程博客的今日内容"""
    content = []
    for slug, rss_url, title in BLOG_SOURCES:
        filename = get_today_news_file(slug)
        _content = news_utils.get_file_from_r2_with_today(filename)
        if _content:
            logger.info(f"今天的 {title} 博客已存在，直接读取: {filename}")
            content.append(_content)
            continue

        fetch_blog_source(slug, rss_url, title)
        _content = news_utils.get_file_from_r2_with_today(filename)
        if _content:
            content.append(_content)
    return "\n".join(content)


if __name__ == "__main__":
    get_today_news_content()
