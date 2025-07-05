import os
from datetime import datetime, timedelta
from typing import Optional

import llm
import news_36kr
import news_ai_news
import news_github_trending_daily
import news_go_weekly
import news_hacker_news
import news_meituan
import news_shaoshupai
import news_utils
import news_v2ex
import push

logger = news_utils.setup_logger(__name__)


def create_final_newsletter(
    last_newsletter: str,
    ai_news: str,
    github_trending: str,
    hacker_news: str,
    shaoshupai: str,
    kr36: str,
) -> Optional[str]:
    system_prompt = (
        """你是一个专业且负责的技术内容编辑助手，擅长从大量信息中提取关键点，生成清晰、结构化的技术 newsletter。"""
    )
    user_prompt = f"""你是一个技术内容编辑助手，目标是为一位专注于后端和 AI 的工程师制作一篇高价值的每日技术 newsletter，帮助他在有限时间内掌握最值得关注的行业动态和技术变化。

【请务必遵循以下要求】：
- 只输出 10 条最重要、最有价值的消息，覆盖行业动态、技术趋势、重大开源/工具/模型更新等（不再分模块）。
- 每条消息需包含标题、来源频道、原文链接（如有）、一句话简要总结（50字内）。
- 优先选择能帮助工程师快速了解行业发生了什么、有哪些值得关注的技术变化的内容。
- 忽略重复、无效、泛科技娱乐、面向新手、无关紧要的小更新等信息。
- 如果消息在昨天的 newsletter 中已经出现过，则不再重复。
- 直接输出 markdown 列表，每条格式如下：
  - **[标题](<原文链接>)**（来源：XXX）  
    > 简要总结

---

以下是昨天的 newsletter 内容：
<<<
{last_newsletter}
>>>

以下是 markdown 原始内容：
<<<

### AINews

```markdown
{ai_news}
```

### GitHub Trending

```markdown
{github_trending}
```

### Hacker News

```markdown
{hacker_news}
```

### 少数派

```markdown
{shaoshupai}
```

### 36 Kr
```markdown
{kr36}
```

>>>
"""
    return llm.one_shoot(system_prompt, user_prompt)


def get_last_newsletter_content() -> str:
    """获取昨天的 newsletter 内容"""
    yesterday = datetime.now() - timedelta(days=1)
    _, yesterday_file = news_utils.create_newsletter_directory_structure(yesterday)

    if os.path.exists(yesterday_file):
        with open(yesterday_file, "r", encoding="utf-8") as file:
            return file.read()
    return ""


def try_generate_newsletter():
    _, day_file = news_utils.create_newsletter_directory_structure()
    if os.path.exists(day_file):
        logger.info(f"今天的 newsletter 已经存在，不重复生成: {day_file}")
        return

    newsletter = create_final_newsletter(
        last_newsletter=get_last_newsletter_content(),
        ai_news=news_ai_news.get_today_news_content(),
        github_trending=news_github_trending_daily.get_today_news_content(),
        hacker_news=news_hacker_news.get_today_news_content(),
        shaoshupai=news_shaoshupai.get_today_news_content(),
        kr36=news_36kr.get_today_news_content(),
    )
    if not newsletter:
        logger.error("生成 newsletter 失败")
        return
    
    # 需要单独触发生成的内容
    news_v2ex.get_today_news_content()
    news_meituan.get_today_posts_content()
    news_go_weekly.get_today_news_content()

    contents = [
        "## 今日技术 Newsletter",
        "\n<sub> 生成时间：{}</sub>\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        "\n---\n",
        "### AI 推荐要点\n",
        newsletter,
        "\n---\n",
        "### 各渠道精选摘要",
        "- [AINews]({})".format(os.path.relpath(news_ai_news.get_today_news_file()[1], os.path.dirname(day_file))),
        "- [GitHub Trending]({})".format(
            os.path.relpath(news_github_trending_daily.get_today_news_file(), os.path.dirname(day_file))
        ),
        "- [少数派]({})".format(os.path.relpath(news_shaoshupai.get_today_news_file(), os.path.dirname(day_file))),
        "- [36Kr]({})".format(os.path.relpath(news_36kr.get_today_news_file()[1], os.path.dirname(day_file))),
        "- [V2EX 热门贴子]({})".format(os.path.relpath(news_v2ex.get_today_news_file(), os.path.dirname(day_file))),
        "- [美团技术团队]({})".format(os.path.relpath(news_meituan.get_today_news_file(), os.path.dirname(day_file))),
        "- [Go Weekly]({})".format(os.path.relpath(news_go_weekly.get_today_news_file(), os.path.dirname(day_file))),
    ]
    for slug, _, title in news_hacker_news.all_rss_urls():
        today_news_file = news_hacker_news.get_today_news_file(slug)
        contents.append(f"- [{title}]({os.path.relpath(today_news_file, os.path.dirname(day_file))})")

    news_utils.save_markdown_to_file("\n".join(contents), day_file)

    # 输出LLM使用统计
    logger.info(llm.get_llm_stats())


def main():
    try:
        try_generate_newsletter()
        push.push_deer("今日技术 newsletter 已生成")
    except Exception as e:
        logger.error(f"生成 newsletter 过程中发生错误: {e}")
        push.push_deer(f"生成 newsletter 失败: {e}")
        raise e


if __name__ == "__main__":
    try_generate_newsletter()
