"""
GolangWeekly

https://cprss.s3.amazonaws.com/golangweekly.com.xml
"""

from typing import Optional

import llm
import news_utils

logger = news_utils.setup_logger(__name__)


def summarize_go_weekly(content: str) -> Optional[str]:
    system_prompt = """你是一位资深的 Go 语言专家，擅长从技术资讯中提炼关键信息，生成高价值、简明扼要的摘要。"""
    user_prompt = f"""请从以下 Go Weekly 内容中，筛选出最值得关注的技术动态、趋势、工具或最佳实践，提炼为简洁摘要，帮助工程师快速掌握本期重点。

【输出要求】：
- 每条需包含标题、原文链接和一句话总结（50字内），突出亮点或实用性。
- 忽略琐碎、重复、泛泛而谈或无关紧要的信息。
- 包含两个模块，模块一是精选的 5 条最重要的内容，模块二是除精选五条外的其它所有内容
- 输出 markdown 列表，格式如下：


## 精选

### 1. [标题](<原文链接>)
> 简要总结（50字内）

---

### 2. [标题](<原文链接>)
> 简要总结（50字内）

---

### 3. ...

## 其它

### 1. [标题](<原文链接>)
> 简要总结（50字内）

---

### 2. [标题](<原文链接>)
> 简要总结（50字内）

---

### 3. ...

---

如下是 Go Weekly 内容：

>>>
{content}
<<<

"""
    return llm.one_shoot(system_prompt, user_prompt)


def get_today_news_file():
    return f"go_weekly_{news_utils.current_date_formatted()}.md"


def fetch_latest_weekly():
    logger.info("正在获取最新的 Go Weekly...")
    entries = news_utils.get_rss_entries("https://cprss.s3.amazonaws.com/golangweekly.com.xml", 10)
    if not entries:
        logger.warning("未能获取 Golang Weekly 的最新条目")
        return []

    entry = entries[0]
    _ = entry.get("title")
    link = entry.get("link")
    summary = entry.get("summary", "").strip()
    publish_format = news_utils.get_entry_datetime_formated(entry)
    summary_md = news_utils.convert_html_to_markdown(summary)
    logger.info("对最新一期 Go Weekly 进行摘要处理...")
    summary_llm = summarize_go_weekly(summary_md)

    content = f"""<sub>{publish_format}</sub>\n\n
[原文链接]({link})\n\n
{summary_llm}
    """

    filename = get_today_news_file()
    if news_utils.put_file_to_r2_with_today(filename, content):
        logger.info(f"✓ 已保存最新的 Go Weekly 到 R2: {filename}")
    else:
        logger.error("✗ 保存最新的 Go Weekly 到 R2 失败")


def get_today_news_content() -> str:
    filename = get_today_news_file()
    content = news_utils.get_file_from_r2_with_today(filename)
    if content:
        logger.info(f"今天的 Go Weekly 已经存在: {filename}")
        return content

    fetch_latest_weekly()

    content = news_utils.get_file_from_r2_with_today(filename)
    assert content
    return content


if __name__ == "__main__":
    get_today_news_content()
