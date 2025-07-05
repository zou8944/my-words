import os
from datetime import datetime
from typing import Optional

import llm
from news_utils import (
    create_newsletter_directory_structure,
    fetch_and_convert_to_markdown,
    get_rss_entries,
    save_markdown_to_file,
    setup_logger,
)

logger = setup_logger(__name__)


def get_latest_link() -> Optional[str]:
    first_entry = get_rss_entries("https://news.smol.ai/rss.xml", limit=1)
    first_entry_link = first_entry[0].get("link")
    return first_entry_link


def get_latest_news_as_markdown() -> Optional[str]:
    # 获取最新链接
    link = get_latest_link()
    if not link:
        return None

    logger.info(f"正在抓取新闻: {link}")

    return fetch_and_convert_to_markdown(link)


def summarize(markdown_content: str) -> Optional[str]:
    system_prompt = """你是一位资深的科技新闻分析师，专门为高质量Newsletter撰写内容摘要。你的任务是从 AINews 中提取最有价值的信息点。

分析目标：
- 新闻要点分析: 提取10个最重要的新闻要点
- 工具产品分析: 如果文章涉及工具或产品，再单独提取10个工具相关要点

关注重点：
人工智能技术突破、AI产品发布、机器学习研究、AI公司动态

重要说明：
- 来源链接：必须从文章内容中提取真实的原始链接，如：
  - Twitter/X 的推文链接
  - GitHub 仓库链接  
  - 公司官网链接
  - 新闻发布页面链接
  - 博客文章链接
- 禁止使用：本Newsletter自身的链接作为来源
- 如无原始链接：写"来源：文章内容"

Markdown输出格式如下（以 ``` 包围提供的，但在生成时候请将该 ``` 去除）：
```
## 📰 十大AI新闻要点

### 1. [要点标题](原始消息源链接，如 https://twitter.com/xxx 或 https://github.com/xxx)
> [详细描述]

---

### 2. ...

---

### 3. ...

---
...

## 🛠️ 十大工具产品要点（如适用）

### 1. [工具要点标题](原始消息源链接)
> [详细描述]

---

### 2. ...

---

### 3. ...

---
```

筛选优先级：
- 重大技术突破或产品发布
- 行业趋势变化和市场动态
- 投资并购和商业决策
- 政策法规和监管变化
- 具体数据和研究结果
- 工具功能特性和使用价值"""

    user_prompt = f"""请深度分析以下 AINews 内容，按照指定格式提取关键信息：

📄 AINews内容：

{markdown_content}

"""
    return llm.one_shoot(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
    )


def fetch_news():
    logger.info("开始抓取 AINews 最新内容")
    # 获取第一个链接 -> 抓取第一个链接转换成 markdown -> 保存到文件 -> 做 LLM 总结
    link = get_latest_link()
    if not link:
        return None
    news_content = fetch_and_convert_to_markdown(link)
    if not news_content:
        logger.error("获取最新新闻内容失败")
        return

    # 从 get_today_news_file 获取文件路径
    _, sum_filepath = get_today_news_file()
    current_date = datetime.now().strftime("%Y-%m-%d")

    # 保存原文到文件
    news_content = f"> [原文链接]({link})\n\n" + news_content
    news_content = f"# AINews - {current_date}\n\n" + news_content

    # 对原文进行总结
    logger.info("开始使用 LLM 进行内容总结")
    summarized_content = summarize(news_content[:65535])  # 限制内容长度，避免过大
    if not summarized_content:
        logger.error("LLM 总结失败")
        return
    logger.info("LLM 总结完成")

    # 保存总结到文件
    summarized_content = f"> [原文链接]({link})\n\n" + summarized_content
    summarized_content = f"## AINews - {current_date}\n\n" + summarized_content
    if save_markdown_to_file(summarized_content, sum_filepath):
        logger.info(f"✓ 总结已保存: {sum_filepath}")
    else:
        logger.error("✗ 保存总结失败")
        return


def get_today_news_file():
    """
    获取今天的AI新闻存储路径
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    day_dir, _ = create_newsletter_directory_structure()

    raw_filename = f"ai_news_{current_date}.md"
    sum_filename = f"ai_news_summary_{current_date}.md"

    raw_filepath = os.path.join(day_dir, raw_filename)
    sum_filepath = os.path.join(day_dir, sum_filename)

    return raw_filepath, sum_filepath


def get_today_news_content() -> str:
    """
    获取今天的AI新闻内容
    """
    _, sum_filepath = get_today_news_file()

    # 如果今天的新闻文件存在，读取内容并返回；如果不存在，则调用 fetch_news() 写入然后再返回
    if os.path.exists(sum_filepath):
        logger.info(f"今天的AI新闻摘要已存在: {sum_filepath}, 直接读取")
        with open(sum_filepath, "r", encoding="utf-8") as f:
            return f.read()

    fetch_news()
    with open(sum_filepath, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    fetch_news()
