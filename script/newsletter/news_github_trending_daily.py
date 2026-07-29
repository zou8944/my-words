"""
GitHub 每日趋势 RSS 源（按语言过滤）
https://mshibanami.github.io/GitHubTrendingRSS/daily/{language}.xml

只关注目标语言：Kotlin、Java、Go、JavaScript、Python
"""

from typing import Optional

import llm
import news_utils

logger = news_utils.setup_logger(__name__)

# 按关注语言分别抓取，避免全语言总榜中的 README 模板和玩具项目
GITHUB_TRENDING_URLS = [
    ("kotlin",     "https://mshibanami.github.io/GitHubTrendingRSS/daily/kotlin.xml"),
    ("java",       "https://mshibanami.github.io/GitHubTrendingRSS/daily/java.xml"),
    ("golang",     "https://mshibanami.github.io/GitHubTrendingRSS/daily/go.xml"),
    ("javascript", "https://mshibanami.github.io/GitHubTrendingRSS/daily/javascript.xml"),
    ("python",     "https://mshibanami.github.io/GitHubTrendingRSS/daily/python.xml"),
]


def concurrent_summarize_content(contents: list[str]) -> list[Optional[str]]:
    system_prompt = """你是一位资深的开源项目分析师，专门为后端/AI工程师撰写GitHub项目摘要。

## 任务目标：
将GitHub Trending项目的描述转换为简洁有力的中文摘要，适合技术人员快速了解项目价值。

## 输出要求：
- **字数限制**：50字左右
- **内容重点**：核心功能、技术特点、应用场景
- **语言风格**：专业、简洁、易懂
- **格式要求**：纯文本，不使用Markdown

## 关注要点：
1. 项目解决了什么问题
2. 使用了什么技术栈或方法
3. 适用于什么场景或人群
4. 有什么独特优势或创新点

请确保摘要既准确又吸引人，让读者能快速判断项目是否值得关注。"""

    user_prompts = [
        f"""请为以下GitHub项目生成专业摘要：

---
项目信息：
{content[:10000]}
---

要求：
1. 提取项目的核心价值和功能特点
2. 用50-100字简洁描述
3. 突出技术亮点和应用价值
4. 使用中文输出，纯文本格式

开始总结："""
        for content in contents
    ]

    return llm.concurrent_one_shoot([(system_prompt, user_prompt) for user_prompt in user_prompts])


def fetch_news():
    logger.info("开始获取 GitHub 每日趋势（按语言过滤）")

    all_entries = []
    seen_links = set()

    for lang, rss_url in GITHUB_TRENDING_URLS:
        logger.info(f"获取 {lang} 语言趋势")
        entries = news_utils.get_rss_entries(rss_url=rss_url, limit=10)
        for entry in entries:
            link = entry.get("link", "")
            if link not in seen_links:
                seen_links.add(link)
                entry["language"] = lang
                all_entries.append(entry)

    if not all_entries:
        logger.warning("没有获取到任何 GitHub Trending 项目")
        return

    # 预处理所有entry的描述
    for entry in all_entries:
        description = entry.get("summary", "无描述")
        entry["description_md"] = news_utils.convert_html_to_markdown(description)

    logger.info(f"共获取 {len(all_entries)} 个项目，开始并发处理摘要")
    summaries = concurrent_summarize_content([entry["description_md"] for entry in all_entries])
    logger.info("GitHub项目描述摘要处理完成")

    # 构建最终内容
    final_content = ["## GitHub Trending\n\n"]

    for index, entry in enumerate(all_entries):
        title = entry.get("title", "无标题")
        link = entry.get("link", "无链接")
        lang = entry.get("language", "")
        summary = summaries[index] if summaries[index] else "无摘要"
        final_content.append(f"### {index + 1}. [{title}]({link}) `{lang}`\n> {summary}\n---\n")

    # 获取文件路径并保存
    filename = get_today_news_file()
    if news_utils.put_file_to_r2_with_today(filename, "\n".join(final_content)):
        logger.info(f"GitHub Trending（按语言过滤）已保存到: {filename}")
    else:
        logger.error(f"无法保存GitHub Trending摘要到: {filename}")


def get_today_news_file():
    """获取今天的GitHub Trending新闻存储路径"""
    current_date = news_utils.current_date_formatted()
    return f"github_trending_{current_date}.md"


def get_today_news_content() -> str:
    """获取今天的GitHub Trending新闻内容"""
    filename = get_today_news_file()

    content = news_utils.get_file_from_r2_with_today(filename)
    if content:
        logger.info(f"今天的GitHub Trending新闻已存在，直接返回: {filename}")
        return content

    logger.info(f"今天的GitHub Trending新闻不存在，开始抓取: {filename}")
    fetch_news()

    content = news_utils.get_file_from_r2_with_today(filename)
    assert content
    return content


if __name__ == "__main__":
    print(fetch_news())
