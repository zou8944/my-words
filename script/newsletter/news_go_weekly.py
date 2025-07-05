"""
GolangWeekly

https://cprss.s3.amazonaws.com/golangweekly.com.xml
"""

import os
from datetime import datetime
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
    """
    获取今天的Go Weekly新闻存储路径
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    day_dir, _ = news_utils.create_newsletter_directory_structure()

    filename = f"go_weekly_{current_date}.md"
    filepath = os.path.join(day_dir, filename)

    return filepath


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

    filepath = get_today_news_file()
    news_utils.save_markdown_to_file(content, filepath)
    logger.info(f"✓ 已保存最新的 Go Weekly 到: {filepath}")


def get_today_news_content() -> str:
    filepath = get_today_news_file()
    if os.path.exists(filepath):
        logger.info(f"今天的 Go Weekly 已经存在: {filepath}")
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()

    fetch_latest_weekly()
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    get_today_news_content()
