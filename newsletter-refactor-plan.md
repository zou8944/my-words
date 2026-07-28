# Newsletter 重构方案

> 基于 2026-07-25 对项目现状的完整审查，涵盖数据来源、提示词、存储、CI/CD 四个方面。

---

## 目录

- [1. 问题总结](#1-问题总结)
- [2. 数据来源重构](#2-数据来源重构)
- [3. 提示词重写](#3-提示词重写)
- [4. 存储改造](#4-存储改造)
- [5. 代码清理](#5-代码清理)
- [6. CI/CD 修复](#6-cicd-修复)
- [7. 改动文件清单](#7-改动文件清单)
- [8. 实施顺序](#8-实施顺序)

---

## 1. 问题总结

### 1.1 数据来源

| 现有来源 | 文件 | 质量评估 | 处置 |
|---|---|---|---|
| AINews (`news.smol.ai`) | `news_ai_news.py` | 低 —— 90% X/Twitter 推文链接，AI 产品公告，营销味重 | **降级**：移出主精选，放入独立的"AI 资讯"子栏目 |
| GitHub Trending 全语言总榜 | `news_github_trending_daily.py` | 中 —— 混入 README 模板、玩具项目 | **改造**：按语言/主题过滤 |
| HN Frontpage | `news_hacker_news.py` | 中高 | 保留 |
| HN Best | `news_hacker_news.py` | 中 | 保留 |
| HN Best Comments | `news_hacker_news.py` | 低 —— 碎片化评论片段 | **删除** |
| HN Ask | `news_hacker_news.py` | 低 —— 质量波动大 | **删除** |
| HN Show | `news_hacker_news.py` | 中低 | **删除** |
| HN Audio Tech | `news_hacker_news.py` | 低 —— 过于细分 | **删除** |
| Reddit AMA | `news_reddit.py` | 零 —— 与技术无关 | **删除** |
| Reddit AskReddit | `news_reddit.py` | 零 —— 与技术无关 | **删除** |
| Reddit Showerthoughts | `news_reddit.py` | 零 —— 与技术无关 | **删除** |
| Reddit TIL | `news_reddit.py` | 零 —— 与技术无关 | **删除** |
| Reddit ELI5 | `news_reddit.py` | 低 —— 面向新手 | **删除** |
| Reddit DevOps | `news_reddit.py` | 中 | 保留 |
| Reddit Programming | `news_reddit.py` | 中 | 保留 |
| Reddit Golang | `news_reddit.py` | 中高 | 保留 |
| Reddit Rust | `news_reddit.py` | 中 | 保留 |
| Reddit ML | `news_reddit.py` | 中 | 保留 |
| V2EX 热榜 | `news_v2ex.py` | 低 —— 大量"求推荐"、"吐槽"、订阅问题 | **删除** |
| 少数派 | `news_shaoshupai.py` | 低 —— 生活方式/消费科技 | **删除** |
| 美团技术团队 | `news_meituan.py` | 高（但不稳定，无文章时生成空文件） | **保留并修复空文件问题** |
| Go Weekly | `news_go_weekly.py` | 内容意义不大 | **停用** |
| 36Kr | `news_36kr.py` | 已废弃（代码注释掉了） | **删除文件** |

### 1.2 提示词问题

当前 `newsletter.py:30` 的 `user_prompt`：
- 筛选范围泛泛，未针对后端/AI 工程师的深度需求
- "最多 10 条"硬限制导致 LLM 在低质量素材里勉强凑数
- 无来源权重区分，高质量（美团、Go Weekly）与低质量（Reddit 吹水）平等对待
- 未要求 LLM 解释"为什么值得看"，导致摘要空洞
- LLM 输出常包含额外开场白（"好的，这是为您筛选和整理后的..."），污染格式

### 1.3 存储问题

- 每日生成 22-24 个文件，240 天累计 4403 个文件
- 源文件（`reddit_*.md`、`hacker_news_*.md`、`v2ex_*.md`）对读者无独立价值，却永久进入 Git 历史
- `tokenizer.json`（7.8MB）在 Git 中是不必要的 blob
- 根目录 28MB PDF 未追踪但占本地空间
- Git blob 总大小约 54MB，且线性增长

### 1.4 CI/CD 问题

- 工作流最后成功运行是 2026-06-03，此后完全断裂
- 使用 PAT token push main，PAT 过期后无法恢复
- 2026-05-01 至 2026-05-27 有 26 天空窗期，说明问题早有征兆

---

## 2. 数据来源重构

### 2.0 最终数据来源总览

经 RSS 可达性验证，以下为最终推荐来源（全部 HTTP 200，URL 可用）：

| 来源 | URL | 文件 | 用途 | RSS 状态 |
|---|---|---|---|---|
| **Hacker News 首页** | `https://hnrss.org/frontpage` | `news_hacker_news.py` | 技术热点，英语技术社区核心 | ✅ 200 |
| **Hacker News Best** | `https://hnrss.org/best` | `news_hacker_news.py` | 高质量讨论精选 | ✅ 200 |
| **GitHub Trending (Kotlin)** | `https://mshibanami.github.io/GitHubTrendingRSS/daily/kotlin.xml` | `news_github_trending_daily.py` | 关注语言 | ✅ 200 |
| **GitHub Trending (Java)** | `https://mshibanami.github.io/GitHubTrendingRSS/daily/java.xml` | `news_github_trending_daily.py` | 关注语言 | ✅ 200 |
| **GitHub Trending (Golang)** | `https://mshibanami.github.io/GitHubTrendingRSS/daily/go.xml` | `news_github_trending_daily.py` | 关注语言 | ✅ 200 |
| **GitHub Trending (JS)** | `https://mshibanami.github.io/GitHubTrendingRSS/daily/javascript.xml` | `news_github_trending_daily.py` | 关注语言 | ✅ 200 |
| **GitHub Trending (Python)** | `https://mshibanami.github.io/GitHubTrendingRSS/daily/python.xml` | `news_github_trending_daily.py` | 关注语言 | ✅ 200 |
| **Cloudflare Blog** | `https://blog.cloudflare.com/rss/` | `news_engineering_blogs.py` | 网络/边缘计算/Workers 深度技术 | ✅ 200 |
| **AWS Architecture Blog** | `https://aws.amazon.com/blogs/architecture/feed/` | `news_engineering_blogs.py` | 分布式系统架构模式 | ✅ 200 |
| **Netflix Tech Blog** | `https://netflixtechblog.com/feed` | `news_engineering_blogs.py` | 大规模系统工程实践 | ✅ 200 |
| **Stripe Engineering** | `https://stripe.com/blog/feed.rss` | `news_engineering_blogs.py` | 支付系统/代码质量/基础设施 | ✅ 200 |
| **Meta Engineering** | `https://engineering.fb.com/feed/` | `news_engineering_blogs.py` | 大规模基础设施/AI Infra | ✅ 200 |
| **GitHub Engineering** | `https://github.blog/engineering/feed/` | `news_engineering_blogs.py` | Git/GitHub 基础设施演进 | ✅ 200 |
| **美团技术团队** | `https://tech.meituan.com/feed/` | `news_meituan.py` | 中文后端工程深度文章 | ✅ 200 |
| **PingCAP** | `https://www.pingcap.com/blog/feed/` | `news_engineering_blogs.py` | 分布式数据库/Go 工程实践 | ✅ 200 |
| **Lobsters** | `https://lobste.rs/rss` | `news_lobsters.py` | 技术社区精选，替代 V2EX | ✅ 200 |
| **AINews** | `https://news.smol.ai/rss.xml` | `news_ai_news.py` | AI 产品/模型动态（降级使用，见说明） | ✅ 200 |
| **OpenAI Blog** | `https://openai.com/blog/rss.xml` | `news_engineering_blogs.py` | AI 工程化方向参考 | ✅ 200 |
| **Reddit (5 个技术频道)** | `https://www.reddit.com/r/{channel}/top/.rss` | `news_reddit.py` | 技术讨论 | ⚠️ 见说明 |

### 来源分级与说明

**Tier 1 — 每日必抓，作为精选主体**

- Hacker News Frontpage + Best：英语技术社区最高信噪比来源
- GitHub Trending（5 语言）：按 Kotlin/Java/Golang/JS/Python 过滤，避免全语言总榜中的 README 模板和玩具项目

**Tier 2 — 每周抓取，作为工程深度补充**

- 工程博客（Cloudflare / AWS Architecture / Netflix / Stripe / Meta / GitHub / PingCAP / OpenAI）：发布频率低但单篇深度高，每周抓一次足够
- 美团技术团队：已有独立抓取逻辑，保留

**Tier 3 — 补充来源**

- Lobsters（`https://lobste.rs/rss`）：技术社区精选，替代 V2EX，质量更高、有 downvote 过滤机制
- AINews：**降级使用**。当前系统中 AINews 占据主精选 90% 的内容，这是"看不下去"的核心原因。改造后 AINews 只作为独立子栏目呈现，不参与主精选的竞争

**移除的来源**

| 来源 | 文件 | 移除原因 |
|---|---|---|
| Go Weekly | `news_go_weekly.py` | 内容意义不大 |
| V2EX 热榜 | `news_v2ex.py` | 低质量用户闲聊 |
| 少数派 | `news_shaoshupai.py` | 生活方式/消费科技，与目标读者不匹配 |
| 36Kr | `news_36kr.py` | 已废弃 |
| HN Best Comments | `news_hacker_news.py` | 碎片化评论片段，无独立阅读价值 |
| HN Ask / Show / Audio Tech | `news_hacker_news.py` | 质量波动大或过于细分 |
| Reddit 吹水频道（AMA / AskReddit / Showerthoughts / TIL / ELI5） | `news_reddit.py` | 与技术完全无关 |

### Reddit 来源可靠性说明

**现状**：从当前网络环境测试，Reddit RSS 对所有频道返回 HTTP 000（连接失败/超时）。Reddit 近年来对无登录状态的 RSS 请求做了越来越严格的限制，在 GitHub Actions 环境中能否正常访问无法在本地验证。

**处理策略**：
- 保留 `news_reddit.py` 但降低其在 `create_final_newsletter()` 中的权重
- 在 GitHub Actions 恢复后观察 Reddit 抓取是否正常工作
- 如果 Reddit RSS 持续不可用，整体移除 `news_reddit.py`，用 Lobsters 和工程博客替代其价值

### 2.1 新增来源：工程博客聚合

创建新文件 `script/newsletter/news_engineering_blogs.py`：

```python
"""
工程博客 RSS 聚合
已验证可达的 RSS 源，统一抓取、去重、摘要。
"""

BLOG_SOURCES = [
    # (slug, rss_url, title, fetch_frequency)

    # === 工程博客（每周抓取，单篇深度高） ===
    ("cloudflare_blog",   "https://blog.cloudflare.com/rss/",               "Cloudflare Blog",     "weekly"),
    ("aws_architecture",  "https://aws.amazon.com/blogs/architecture/feed/", "AWS Architecture Blog","weekly"),
    ("netflix_tech",      "https://netflixtechblog.com/feed",               "Netflix Tech Blog",    "weekly"),
    ("stripe_engineering","https://stripe.com/blog/feed.rss",               "Stripe Engineering",   "weekly"),
    ("meta_engineering",  "https://engineering.fb.com/feed/",               "Meta Engineering",     "weekly"),
    ("github_engineering","https://github.blog/engineering/feed/",          "GitHub Engineering",   "weekly"),
    ("pingcap",           "https://www.pingcap.com/blog/feed/",             "PingCAP",              "weekly"),
    ("openai_blog",       "https://openai.com/blog/rss.xml",               "OpenAI Blog",          "weekly"),
]
```

实现要点：
- 每个来源独立抓取，结果存 R2（`blog_{slug}_{date}.md`）
- 通过 LLM 为每篇文章生成摘要（50 字内，突出工程价值）
- 只抓取最近 7 天内发布的文章（避免旧文重复）
- 各来源合并后在主筛选阶段统一参与筛选

### 2.2 新增来源：Lobsters

创建 `script/newsletter/news_lobsters.py`，逻辑与 `news_v2ex.py` 类似：

```python
"""
Lobsters 技术社区 RSS
https://lobste.rs/rss

替代 V2EX，质量更高（有点赞/踩机制，技术内容集中）。
"""

LOBSTERS_RSS_URL = "https://lobste.rs/rss"

def fetch_news():
    entries = news_utils.get_rss_entries(LOBSTERS_RSS_URL, limit=30)
    # ... 转 markdown、摘要 ...
```

### 2.3 改造 GitHub Trending 过滤逻辑

修改 `script/newsletter/news_github_trending_daily.py`：

当前问题：使用 `https://mshibanami.github.io/GitHubTrendingRSS/daily/all.xml` 全语言总榜，混入大量非技术项目。

改造方案：按关注语言分别抓取，合并后筛选：

```python
GITHUB_TRENDING_URLS = [
    ("kotlin",     "https://mshibanami.github.io/GitHubTrendingRSS/daily/kotlin.xml"),
    ("java",       "https://mshibanami.github.io/GitHubTrendingRSS/daily/java.xml"),
    ("golang",     "https://mshibanami.github.io/GitHubTrendingRSS/daily/go.xml"),
    ("javascript", "https://mshibanami.github.io/GitHubTrendingRSS/daily/javascript.xml"),
    ("python",     "https://mshibanami.github.io/GitHubTrendingRSS/daily/python.xml"),
]
```

每个语言取前 10，合并后由 LLM 按"对后端/AI 工程师的实践价值"筛选，只保留 Top 10。

### 2.4 精简 HN 源

修改 `script/newsletter/news_hacker_news.py` 中 `all_rss_urls()`：

```python
def all_rss_urls() -> list[tuple[str, str, str]]:
    return [
        ("hacker_news_frontpage", "https://hnrss.org/frontpage", "Hacker News 首页"),
        ("hacker_news_best",      "https://hnrss.org/best",      "Hacker News 近期最佳"),
    ]
```

删除：`bestcomments`、`ask`、`show`、`audio_tech` 四个 RSS 源。

### 2.5 精简 Reddit 频道

修改 `script/newsletter/news_reddit.py` 中 `all_reddit_channels()`，只保留技术频道：

```python
def all_reddit_channels() -> list[tuple[str, str, str]]:
    tech_channels = [
        ("devops",          "Reddit DevOps"),
        ("programming",     "Reddit Programming"),
        ("golang",          "Reddit Golang"),
        ("rust",            "Reddit Rust"),
        ("MachineLearning", "Reddit ML"),
    ]
    # 已删除：AMA、AskReddit、Showerthoughts、TIL、ELI5
    channels = []
    for channel, title in tech_channels:
        slug = f"reddit_{channel.lower()}"
        rss_url = f"https://www.reddit.com/r/{channel}/top/.rss"
        channels.append((slug, rss_url, title))
    return channels
```

### 2.6 停用 V2EX、少数派、Go Weekly

- `newsletter.py:130`：删除 `v2ex = news_v2ex.get_today_news_content()`
- `newsletter.py:131`：删除 `_ = news_go_weekly.get_today_news_content()`
- `newsletter.py:138`：删除 `shaoshupai_content = news_shaoshupai.get_today_news_content()`
- `create_final_newsletter` 函数签名移除 `shaoshupai`、`v2ex` 参数
- 保留 `news_v2ex.py`、`news_shaoshupai.py`、`news_go_weekly.py` 文件但不调用

### 2.7 AINews 降级使用

**现状问题**：当前 AINews 是主精选的唯一输入源，每天输出 10 条 AI 产品/模型发布公告，90% 链接指向 X/Twitter，占据了精选列表的大部分席位。

**改造方案**：
- AINews 内容从主精选输入中移出，改为独立的"AI 资讯"子栏目
- 主精选（`create_final_newsletter`）只接收：工程博客、GitHub Trending、HN、Reddit、Lobsters
- AINews 的 10 条摘要在 newsletter.md 中单独列出（类似"AI 动态速览"），不参与主精选竞争
- 降低 AINews 在 LLM 筛选中的权重，避免 AI 产品公告挤占工程深度内容

### 2.8 修复美团空文件问题

修改 `script/newsletter/news_meituan.py`：

当前问题：无文章时仍然生成文件，内容为"今天没有新的文章发布"，出现在 newsletter 索引中。

```python
# news_meituan.py
def fetch_news():
    # ... 现有逻辑 ...
    if not final_contents:
        logger.info("美团技术团队今天没有发布新文章，跳过保存")
        return  # 不写文件
    # ... 原有保存逻辑 ...
```

`newsletter.py` 中对美团返回值做空检查，空时不在索引中显示链接。

---

## 3. 提示词重写

### 3.1 主筛选提示词（`newsletter.py`）

替换 `create_final_newsletter` 中的 `system_prompt` 和 `user_prompt`：

```python
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
```

AINews 内容不传入主筛选提示词，而是在 `generate_newsletter()` 中作为独立的"AI 动态速览"子栏目直接拼接到 newsletter.md 中，不经过 LLM 筛选。

关键改动：
- `system_prompt` 明确读者画像（5 年+后端工程师），限制输出风格
- 加入"严格禁止开场白"指令，解决 LLM 输出 `好的，这是为您...` 的格式污染
- 筛选标准改为"满足任一条件"的正向标准，而非泛泛的"覆盖范围"
- 增加明确排除项，针对当前最常见的低质量内容类型
- 输出格式强调"直接输出列表"，减少格式噪音

### 3.2 LLM 模型选择

当前使用 `deepseek-chat`（`llm.py:86`），建议评估：

- 如果内容筛选需要更好的判断力，考虑换用 `deepseek-reasoner` 或 `claude-sonnet-4-6`
- 成本：当前 DeepSeek 定价极低（¥2/M input，¥8/M output），换更强模型成本增加但质量提升明显
- 建议：先用当前模型跑一轮新提示词，观察质量，不满意再换模型

---

## 4. 存储改造

### 4.1 核心原则

**Git 只存读者会打开的文件，源文件只存 R2（或直接丢弃）。**

读者会打开的文件：
- `newsletters/{date}/newsletter.md` —— 每日摘要索引
- `newsletters/{date}/newsletter_summary.md` —— 精选内容
- `newsletters/homepage.md` —— 主页

源文件（`reddit_*.md`、`hacker_news_*.md`、`github_trending_*.md` 等）不需要进入 Git。

### 4.2 改造 `newsletter.py` 中的 `load_all_files_from_r2()`

**当前行为**（`newsletter.py:254-269`）：将 R2 上当天的**所有**文件下载到本地 `newsletters/{date}/` 目录，然后 workflow 将整个 `newsletters/` 目录 commit。

**改造后**：只下载 `newsletter.md` 和 `newsletter_summary.md`：

```python
def load_all_files_from_r2():
    """将 R2 上当天的精选文件加载到本地（不加载源文件）"""
    newsletter_dir = get_newsletter_directory()
    os.makedirs(newsletter_dir, exist_ok=True)

    today_formatted = news_utils.current_date_formatted()
    today_dir = os.path.join(newsletter_dir, today_formatted)
    os.makedirs(today_dir, exist_ok=True)

    # 只下载 newsletter 核心文件，不下载源文件
    newsletter_filename, summary_filename = get_newsletter_filename()
    for filename in [newsletter_filename, summary_filename]:
        content = news_utils.get_file_from_r2_with_today(filename)
        if content:
            filepath = os.path.join(today_dir, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            logger.info(f"✓ 已保存 {filename} 到 {today_dir}")
        else:
            logger.warning(f"✗ R2 上不存在 {filename}")
```

### 4.3 改造 `generate_newsletter()` 中的索引链接

由于源文件不再下载到本地，`generate_newsletter()` 中引用源文件的链接需要改为绝对 R2 链接或去掉。

当前 `newsletter.py:176-201` 中生成的"各渠道精选摘要"、"Hacker News 精选"、"Reddit 精选频道"等部分包含大量指向源文件的相对链接（如 `./reddit_askreddit_2026-06-03.md`），这些文件将不再存在于本地。

**方案 A（推荐）：精简 newsletter.md，只保留精选摘要索引**

删除 newsletter.md 中"各渠道精选摘要"、"Hacker News 精选"、"Reddit 精选频道"等部分。newsletter.md 只包含：
- 生成时间
- AI 推荐要点（精选列表）
- 每周一看（外部链接）

改造 `generate_newsletter()`：

```python
def generate_newsletter():
    generate_newsletter_summary()

    _, summary_filename = get_newsletter_filename()
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

    contents.extend([
        "\n---\n",
        "### 推荐阅读",
        "- [Cloudflare Blog](https://blog.cloudflare.com/zh-cn/)",
        "- [美团技术团队](https://tech.meituan.com)",
    ])

    newsletter_filename, _ = get_newsletter_filename()
    if news_utils.put_file_to_r2_with_today(newsletter_filename, "\n".join(contents)):
        logger.info(f"✓ 今日技术 newsletter 已保存: {newsletter_filename}")
    else:
        logger.error(f"✗ 无法保存今日技术 newsletter: {newsletter_filename}")
```

**方案 B（备选）：保留链接但改为 R2 URL**

如果希望保留各渠道源文件链接，需要在 `news_utils.py` 中增加生成 R2 公开 URL 的函数，将相对链接改为绝对 URL。

### 4.4 改造 `generate_newsletter_profile()`

`newsletter.py:219-251` 的 `generate_newsletter_profile()` 读取本地所有 `newsletter.md` 生成 `homepage.md`。

改造后：由于只保留了精选文件，链接重写逻辑需简化：

```python
def generate_newsletter_profile():
    newsletter_dir = get_newsletter_directory()
    newsletter_files = sorted(
        pathlib.Path(newsletter_dir).glob("**/newsletter.md"),
        key=lambda x: x.parent.name,
        reverse=True,
    )

    if not newsletter_files:
        logger.warning("没有找到任何 newsletter 文件")
        return

    homepage = []
    for i, file in enumerate(newsletter_files):
        date = file.parent.name
        content = file.read_text(encoding="utf-8")
        # 无需再做 link rewrite，因为 newsletter.md 已无相对源文件链接
        if i == 0:
            homepage.append(content)
        else:
            if i == 1:
                homepage.append("\n# 往日新闻\n")
            homepage.append(f"#### [{date}](./{date}/newsletter.md)\n")

    homepage_file = os.path.join(newsletter_dir, "homepage.md")
    homepage_file.write_text("\n".join(homepage), encoding="utf-8")
    logger.info(f"✓ 已生成 newsletter 主页: {homepage_file}")
```

### 4.5 `.gitignore` 补充

```gitignore
# newsletter 源文件（只存 R2）
newsletters/*/reddit_*.md
newsletters/*/hacker_news_*.md
newsletters/*/github_trending_*.md
newsletters/*/v2ex_*.md
newsletters/*/shaoshupai_*.md
newsletters/*/ai_news_*.md
newsletters/*/ai_news_summary_*.md
newsletters/*/lobsters_*.md
newsletters/*/meituan_*.md
newsletters/*/blog_*.md
```

> **注意**：`.gitignore` 只能阻止新增文件进入 Git，已经 commit 的历史文件不受影响。若要彻底移除历史中的源文件，需用 `git filter-repo`（见第 5 节）。

---

## 5. 代码清理

### 5.1 删除无用文件

| 文件 | 原因 |
|---|---|
| `script/newsletter/news_36kr.py` | 已废弃（`newsletter.py:139` 注释掉了），历史 `36kr_raw_*.md` 占用大量 Git 空间 |
| `script/newsletter/final_news_letter.py` | 空文件（0 字节） |
| `script/newsletter/tokenizer/tokenizer.json` | 7.8MB，应在运行时下载而非存入 Git |

### 5.2 `tokenizer.json` 处理

`tokenizer.json` 是 LLM token 计费用的，文件 7.8MB，不应该存在 Git 中。

**方案**：改用 Python 包管理（`tiktoken`）替代本地 tokenizer 文件，或在运行时自动下载。

修改 `script/newsletter/tokenizer/` 目录下的代码（如存在 `__init__.py`），改为：
- 方案 A：使用 `tiktoken` 库（`pip install tiktoken`），直接在 `llm.py` 中使用
- 方案 B：在 Dockerfile / CI 中增加下载步骤，从 R2 或 GitHub Release 下载

### 5.3 清理 Git 历史中的大文件（可选，高风险）

如果要彻底缩小 `.git` 体积：

```bash
# 1. 安装 git-filter-repo
pip install git-filter-repo

# 2. 删除历史中的大文件
git filter-repo --invert-paths \
  --path newsletters/*/36kr_raw_*.md \
  --path script/newsletter/tokenizer/tokenizer.json

# 3. 强制推送（需团队协调）
git push origin --force --all
```

> **警告**：这会重写所有 commit hash，协作者需要重新 clone。如果只有你一个人使用此仓库，风险较低。

### 5.4 根目录 PDF

`3B-3802 方案设计修改意见.pdf`（28MB）未被 Git 追踪，但占本地空间。建议移至其他存储位置。

---

## 6. CI/CD 修复

### 6.1 诊断当前失败原因

```bash
# 在 GitHub repo 的 Actions 页面查看 generate-newsletter 工作流的最近失败记录
# 或使用 gh CLI：
gh run list --workflow=generate-newsletter.yml --limit 5
gh run view <run-id> --log-failed
```

常见失败原因：
- PAT token 过期（最常见）
- `OPENAI_BASE_URL` 指向的 DeepSeek 端点不可达
- R2 凭据失效
- RSS 源临时不可用（如 Reddit 屏蔽 GitHub Actions IP）

### 6.2 改用 Fine-grained PAT

当前 workflow 使用 `secrets.PAT`，这是一个 classic PAT，过期后会静默失败。

建议：
- 创建 fine-grained personal access token
- Scope 限定为：`Contents: Read and Write`（仅此仓库）
- 设置合理的过期时间（如 90 天），并设置日历提醒续期

### 6.3 Workflow 改进

修改 `.github/workflows/generate-newsletter.yml`：

```yaml
    - name: Generate newsletter
      run: |
        cd script/newsletter
        uv run main.py
      env:
        OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        R2_ENDPOINT: ${{ secrets.R2_ENDPOINT }}
        R2_ACCESS_KEY_ID: ${{ secrets.R2_ACCESS_KEY_ID }}
        R2_SECRET_ACCESS_KEY: ${{ secrets.R2_SECRET_ACCESS_KEY }}
        R2_BUCKET: ${{ secrets.R2_BUCKET }}
        PUSH_DEER_KEY: ${{ secrets.PUSH_DEER_KEY }}
      timeout-minutes: 15  # 增加超时保护，防止 LLM 调用卡死

    - name: Notify failure
      if: failure()
      run: |
        curl -s "https://api2.pushdeer.com/message/push?pushkey=${{ secrets.PUSH_DEER_KEY }}&text=Newsletter生成失败，请检查Actions日志&type=markdown"
```

增加失败通知：当生成失败时，通过 PushDeer 发送告警，避免静默失败。

---

## 7. 改动文件清单

| 文件 | 改动类型 | 改动内容 |
|---|---|---|
| `script/newsletter/newsletter.py` | **修改** | 重写提示词、精简 newsletter.md 结构、修改 `load_all_files_from_r2()`、修改 `generate_newsletter()`、修复 `generate_newsletter_profile()`、移除 Go Weekly/V2EX/少数派调用、添加 Lobsters 调用 |
| `script/newsletter/news_engineering_blogs.py` | **新增** | 工程博客 RSS 聚合（Cloudflare / AWS / Netflix / Stripe / Meta / GitHub / PingCAP / OpenAI） |
| `script/newsletter/news_lobsters.py` | **新增** | Lobsters 技术社区 RSS，替代 V2EX |
| `script/newsletter/news_hacker_news.py` | **修改** | `all_rss_urls()` 只保留 frontpage + best |
| `script/newsletter/news_reddit.py` | **修改** | `all_reddit_channels()` 只保留技术频道 |
| `script/newsletter/news_github_trending_daily.py` | **修改** | 改用按语言的 RSS 源（Kotlin/Java/Go/JS/Python） |
| `script/newsletter/news_meituan.py` | **修改** | 无文章时不生成空文件 |
| `script/newsletter/news_go_weekly.py` | **不调用** | 不删除文件，但从 `newsletter.py` 移除调用 |
| `script/newsletter/news_36kr.py` | **删除** | 已废弃 |
| `script/newsletter/final_news_letter.py` | **删除** | 空文件 |
| `script/newsletter/tokenizer/tokenizer.json` | **删除** | 改用 tiktoken 或运行时下载 |
| `.github/workflows/generate-newsletter.yml` | **修改** | 增加 timeout、失败通知 |
| `.gitignore` | **修改** | 增加 newsletter 源文件忽略规则 |

---

## 8. 实施顺序

按风险和依赖关系排序，建议按以下顺序执行：

### Phase 1：止血（1天）

1. 去 GitHub Actions 查看最近失败日志，确认失败原因
2. 检查/更新 PAT token
3. 手动触发一次 workflow 验证恢复

### Phase 2：数据来源改造（1-2天）

4. 创建 `news_engineering_blogs.py`（新增工程博客 RSS 聚合）
5. 创建 `news_lobsters.py`（新增 Lobsters 技术社区，替代 V2EX）
6. 修改 `news_hacker_news.py`：精简 HN 源
7. 修改 `news_reddit.py`：删除吹水频道
8. 修改 `news_github_trending_daily.py`：按语言过滤（Kotlin/Java/Go/JS/Python）
9. 修改 `news_meituan.py`：修复空文件
10. 修改 `newsletter.py`：移除 Go Weekly/V2EX/少数派调用，添加 Lobsters/工程博客调用

### Phase 3：提示词重写（半天）

11. 修改 `newsletter.py` 中 `create_final_newsletter()` 的提示词
12. 修改 `generate_newsletter()` 精简 newsletter.md 结构
13. 修改 `generate_newsletter_profile()` 适配新结构

### Phase 4：存储改造（半天）

14. 修改 `load_all_files_from_r2()` 只下载精选文件
15. 更新 `.gitignore`
16. 本地测试验证

### Phase 5：代码清理（半天）

17. 删除 `news_36kr.py`、`final_news_letter.py`
18. 处理 `tokenizer.json`（改用 tiktoken 或运行时下载）
19. 更新 `pyproject.toml` 依赖

### Phase 6：CI/CD 改进（可选）

20. 改用 fine-grained PAT
21. 更新 workflow 增加 timeout 和失败通知
22. 清理 Git 历史中的大文件（如需要）

---

## 附录：预期改造后的每日文件结构

```
newsletters/
├── homepage.md
├── 2026-07-25/
│   ├── newsletter.md              ← 精选摘要索引（~2KB）
│   └── newsletter_summary.md      ← 精选内容详情（~5KB）
├── 2026-07-24/
│   ├── newsletter.md
│   └── newsletter_summary.md
...
```

对比当前每天 22+ 个文件，改造后每天仅 2 个文件，Git 体积增长速度降低约 90%。
