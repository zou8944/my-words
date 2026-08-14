import os
from typing import Optional

import llm
import news_ai_news
import news_engineering_blogs
import news_github_trending_daily
import news_hacker_news
import news_lobsters
import news_meituan
import news_reddit
import news_utils

logger = news_utils.setup_logger(__name__)


def create_final_newsletter(
    last_newsletter: str,
    engineering_blogs: str,
    github_trending: str,
    hacker_news: str,
    lobsters: str,
    reddit_tech: str,
    meituan: str,
) -> Optional[str]:
    system_prompt = """你是一位专注于后端系统与AI基础设施的技术编辑。
你的读者是一位有5年+经验的后端工程师，日常工作涉及 Go、PostgreSQL、LLM 应用、分布式系统和云原生架构。

你的目标：从原始素材中筛选出对这位工程师**真正有学习价值**的内容，帮助他在碎片时间里提升技术认知。

严格禁止：
- 输出"好的，这是为您..."等开场白，直接输出列表
- 重复标题中的来源信息
- 将同一条新闻在不同来源中重复推荐"""

    user_prompt = f"""请从以下素材中筛选出最有价值的技术内容，生成今日 Newsletter。

【筛选标准】—— 只选满足以下任一条件的内容：
1. 对后端/分布式系统工程师有直接参考价值的深度文章或项目
2. Go、PostgreSQL、Redis、Kafka、gRPC 等技术栈的重要更新
3. LLM 应用层的工程实践（推理优化、RAG 架构、Agent 编排、评估方法）
4. 一线工程团队（美团、Cloudflare、Stripe、Netflix 等）的实战总结
5. 有深度技术讨论的 HN/Lobsters/Reddit 帖子（不是产品公告）

【明确排除】：
- AI 产品发布公告（如"X 发布 Y 模型"）—— 除非含具体架构/性能数据
- 融资新闻、商业动态
- 面向新手的入门内容
- 昨天已出现过的内容

【输出格式】—— 直接输出 Markdown 列表，不要任何开场白：
- **[标题](链接)**（来源：XXX）
  > 一句话总结，突出技术细节或实践价值（50字内）

---

以下是昨天已推送的内容（用于去重）：
<<<
{last_newsletter}
>>>

以下是今日原始素材：

### 工程博客精选
```markdown
{engineering_blogs}
```

### GitHub Trending
```markdown
{github_trending}
```

### Hacker News
```markdown
{hacker_news}
```

### Lobsters
```markdown
{lobsters}
```

### Reddit 技术频道
```markdown
{reddit_tech}
```

### 美团技术团队
```markdown
{meituan}
```
"""
    return llm.one_shoot(system_prompt, user_prompt)


def get_newsletter_filename() -> tuple[str, str]:
    return "newsletter.md", "newsletter_summary.md"


def get_newsletter_directory() -> str:
    """获取 newsletter 的目录"""
    newsletter_dir = os.path.dirname(__file__)
    newsletter_dir = os.path.dirname(newsletter_dir)
    newsletter_dir = os.path.dirname(newsletter_dir)
    newsletter_dir = os.path.join(newsletter_dir, "newsletters")
    logger.info("newsletter目录: %s", newsletter_dir)
    return newsletter_dir


def get_last_newsletter_summary() -> str:
    """获取昨天的 newsletter 内容（从 R2 读取）"""
    yesterday_formatted = news_utils.yesterday_date_formatted()
    _, summary_filename = get_newsletter_filename()
    content = news_utils.get_file_from_r2_with_date(yesterday_formatted, summary_filename)
    if content:
        logger.info(f"从 R2 获取到昨天的 newsletter 摘要: {yesterday_formatted}/{summary_filename}")
        return content
    logger.info("昨天的 newsletter 摘要不存在，跳过去重")
    return ""


def generate_newsletter_summary():
    _, summary_filename = get_newsletter_filename()
    if news_utils.get_file_from_r2_with_today(summary_filename):
        logger.info(f"今天的 newsletter 摘要 已经存在，不重复生成: {summary_filename}")
        return

    # 获取各来源内容
    last_newsletter_summary = get_last_newsletter_summary()
    engineering_blogs_content = news_engineering_blogs.get_today_news_content()
    github_trending_content = news_github_trending_daily.get_today_news_content()
    hacker_news_content = news_hacker_news.get_today_news_content()
    lobsters_content = news_lobsters.get_today_news_content()
    reddit_tech_content = news_reddit.get_today_news_content()
    meituan_content = news_meituan.get_today_posts_content()

    # 触发 AINews 抓取（不传入主筛选，但需要确保数据已生成）
    _ = news_ai_news.get_today_news_content()

    newsletter = create_final_newsletter(
        last_newsletter=last_newsletter_summary,
        engineering_blogs=engineering_blogs_content,
        github_trending=github_trending_content,
        hacker_news=hacker_news_content,
        lobsters=lobsters_content,
        reddit_tech=reddit_tech_content,
        meituan=meituan_content,
    )
    if not newsletter:
        logger.error("生成 newsletter 失败")
        return

    if news_utils.put_file_to_r2_with_today(summary_filename, newsletter):
        logger.info(f"✓ 今日技术 newsletter 摘要 已保存: {summary_filename}")
    else:
        logger.error(f"✗ 无法保存今日技术 newsletter 摘要: {summary_filename}")
        return


def generate_newsletter():
    # 先生成 newsletter 摘要
    generate_newsletter_summary()

    # 生成 newsletter
    newsletter_filename, summary_filename = get_newsletter_filename()
    newsletter_summary = news_utils.get_file_from_r2_with_today(summary_filename)
    if not newsletter_summary:
        logger.error("无法获取 newsletter 摘要")
        return

    # AINews 作为独立子栏目，不经过主筛选
    ai_news_content = news_ai_news.get_today_news_content()

    current_datetime_formatted = news_utils.current_datetime_formatted()
    contents = [
        "## 今日要闻",
        f"\n<sub> 生成时间：{current_datetime_formatted}</sub>\n",
        "\n---\n",
        newsletter_summary,
    ]

    # AI 动态速览（独立子栏目，不参与主精选竞争）
    if ai_news_content:
        contents.extend([
            "\n---\n",
            "### AI 动态速览",
            ai_news_content,
        ])

    # 推荐阅读
    meituan_file = news_meituan.get_today_news_file()
    contents.extend([
        "\n---\n",
        "### 推荐阅读",
        "- [Cloudflare Blog](https://blog.cloudflare.com/zh-cn/)",
        f"- [美团技术团队](./{meituan_file})" if news_utils.get_file_from_r2_with_today(meituan_file) else "",
    ])

    if news_utils.put_file_to_r2_with_today(newsletter_filename, "\n".join(contents)):
        logger.info(f"✓ 今日技术 newsletter 已保存: {newsletter_filename}")
    else:
        logger.error(f"✗ 无法保存今日技术 newsletter: {newsletter_filename}")
        return


def generate_newsletter_profile():
    """生成 homepage.md，内容从 R2 获取"""
    newsletter_dir = get_newsletter_directory()
    os.makedirs(newsletter_dir, exist_ok=True)

    today_formatted = news_utils.current_date_formatted()
    newsletter_filename, _ = get_newsletter_filename()
    today_content = news_utils.get_file_from_r2_with_today(newsletter_filename)

    if not today_content:
        logger.warning("今天的 newsletter 不存在，无法生成主页")
        return

    # 将相对链接替换为 R2 静态资源绝对链接
    static_base = "https://static.zou8944.com/newsletter"
    homepage_content = today_content.replace("](./", f"]({static_base}/{today_formatted}/")

    # 追加往日新闻（过去 30 天）
    all_dates = news_utils.list_r2_newsletter_dates()
    recent_dates = [d for d in all_dates if d != today_formatted][:30]
    if recent_dates:
        homepage_content += "\n\n# 往日新闻\n\n"
        for date in recent_dates:
            homepage_content += f"#### [{date}]({static_base}/{date}/newsletter.md)\n\n"

    homepage_file = os.path.join(newsletter_dir, "homepage.md")
    with open(homepage_file, "w", encoding="utf-8") as file:
        file.write(homepage_content)
        logger.info(f"✓ 已生成 newsletter 主页: {homepage_file}")


def try_generate_newsletter():
    # 生成摘要
    generate_newsletter_summary()
    # 生成最终的 newsletter
    generate_newsletter()
    # 生成主页
    generate_newsletter_profile()


if __name__ == "__main__":
    try_generate_newsletter()
