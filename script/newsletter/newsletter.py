import os
import pathlib
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
    """获取昨天的 newsletter 内容"""
    # 昨天的内容从本地获取
    newsletter_dir = get_newsletter_directory()
    yesterday_formatted = news_utils.yesterday_date_formatted()
    _, summary_filename = get_newsletter_filename()
    yesterday_newsletter_path = os.path.join(newsletter_dir, yesterday_formatted, summary_filename)
    if os.path.exists(yesterday_newsletter_path):
        with open(yesterday_newsletter_path, "r", encoding="utf-8") as file:
            return file.read()
    return ""


def generate_newsletter_summary():
    _, summary_filename = get_newsletter_filename()
    if news_utils.get_file_from_r2_with_today(summary_filename):
        logger.info(f"今天的 newsletter 摘要 已经存在，不重复生成: {summary_filename}")
        return

    _ = news_v2ex.get_today_news_content()
    _ = news_meituan.get_today_posts_content()
    _ = news_go_weekly.get_today_news_content()
    last_newsletter_summary = get_last_newsletter_summary()
    ai_news_content = news_ai_news.get_today_news_content()
    github_trending_content = news_github_trending_daily.get_today_news_content()
    hacker_news_content = news_hacker_news.get_today_news_content()
    shaoshupai_content = news_shaoshupai.get_today_news_content()
    kr36_content = news_36kr.get_today_news_content()

    newsletter = create_final_newsletter(
        last_newsletter=last_newsletter_summary,
        ai_news=ai_news_content,
        github_trending=github_trending_content,
        hacker_news=hacker_news_content,
        shaoshupai=shaoshupai_content,
        kr36=kr36_content,
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

    current_datetime_formatted = news_utils.current_datetime_formatted()
    contents = [
        "## 今日技术 Newsletter",
        "\n<sub> 生成时间：{}</sub>\n".format(current_datetime_formatted),
        "\n---\n",
        "### AI 推荐要点\n",
        newsletter_summary,
        "\n---\n",
        "### 各渠道精选摘要",
        "- [AINews](./{})".format(news_ai_news.get_today_news_file()[1]),
        "- [GitHub Trending](./{})".format(news_github_trending_daily.get_today_news_file()),
        "- [少数派](./{})".format(news_shaoshupai.get_today_news_file()),
        "- [36Kr](./{})".format(news_36kr.get_r2_object_key()[1]),
        "- [V2EX 热门贴子](./{})".format(news_v2ex.get_today_news_file()),
        "- [美团技术团队](./{})".format(news_meituan.get_today_news_file()),
        "- [Go Weekly](./{})".format(news_go_weekly.get_today_news_file()),
    ]
    for slug, _, title in news_hacker_news.all_rss_urls():
        today_news_file = news_hacker_news.get_today_news_file(slug)
        contents.append(f"- [{title}](./{today_news_file})")

    if news_utils.put_file_to_r2_with_today(newsletter_filename, "\n".join(contents)):
        logger.info(f"✓ 今日技术 newsletter 已保存: {newsletter_filename}")
    else:
        logger.error(f"✗ 无法保存今日技术 newsletter: {newsletter_filename}")
        return


def generate_newsletter_profile():
    newsletter_dir = get_newsletter_directory()
    newsletter_files = list(pathlib.Path(newsletter_dir).glob("**/newsletter.md"))
    newsletter_files.sort(key=lambda x: x.parent.absolute(), reverse=True)

    if not newsletter_files:
        logger.warning("没有找到任何 newsletter 文件")
        return

    newsletter_homepage = []
    
    for i, file in enumerate(newsletter_files):
        date_formated = file.parent.name.split("/")[-1]
        
        if i == 0:  # 处理最新的newsletter
            content = file.read_text(encoding="utf-8")
            # 将 各渠道精选摘要 后面的链接前都加上一个 日期
            segments = content.split("### 各渠道精选摘要")
            if len(segments) > 1:
                segments[1] = segments[1].replace("](./", f"](./{date_formated}/")
                content = segments[0] + "### 各渠道精选摘要" + segments[1]
            newsletter_homepage.append(content)
        
        if i == 1:  # 在第二个文件前添加往日新闻标题
            newsletter_homepage.append("\n# 往日新闻\n")
        
        if i > 0:  # 从第二个文件开始添加链接
            newsletter_homepage.append(f"#### [{date_formated}](./{date_formated}/newsletter.md)\n")

    homepage_content = "\n".join(newsletter_homepage)

    homepage_file = os.path.join(newsletter_dir, "homepage.md")
    with open(homepage_file, "w", encoding="utf-8") as file:
        file.write(homepage_content)
        logger.info(f"✓ 已生成 newsletter 主页: {homepage_file}")


def load_all_files_from_r2():
    """将 r2 上当天的所有文件加载到本地"""
    newsletter_dir = get_newsletter_directory()
    if not os.path.exists(newsletter_dir):
        os.makedirs(newsletter_dir)

    today_formatted = news_utils.current_date_formatted()
    today_dir = os.path.join(newsletter_dir, today_formatted)
    if not os.path.exists(today_dir):
        os.makedirs(today_dir)

    r2_dir = news_utils.get_r2_dir_with_today()
    if news_utils.copy_from_r2(r2_dir, today_dir):
        logger.info(f"✓ 已将 R2 上的 {r2_dir} 目录内容复制到本地: {today_dir}")
    else:
        logger.error(f"✗ 无法将 R2 上的 {r2_dir} 目录内容复制到本地: {today_dir}")
        return


def try_generate_newsletter():
    # 生成摘要
    generate_newsletter_summary()
    # 生成最终的 newsletter
    generate_newsletter()
    # 加载到本地
    load_all_files_from_r2()
    # 生成主页
    generate_newsletter_profile()


if __name__ == "__main__":
    generate_newsletter_profile()
