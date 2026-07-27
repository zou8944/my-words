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
| Go Weekly | `news_go_weekly.py` | 高（但一周一期，每日重复抓取浪费） | **保留，改为每周只抓一次** |
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

### 2.1 新增来源：后端/系统工程博客 RSS

创建新文件 `script/newsletter/news_blogs.py`：

```python
"""
工程博客 RSS 聚合

每个来源按固定频率抓取（每周一次或每日一次），通过 RSS 获取最新文章。
"""

BLOG_SOURCES = [
    # (slug, rss_url, title, fetch_frequency)
    # fetch_frequency: "daily" | "weekly"

    # === 高频（每日） ===
    ("cloudflare_blog",      "https://blog.cloudflare.com/rss/",               "Cloudflare Blog",      "daily"),
    ("aws_architecture",     "https://aws.amazon.com/blogs/architecture/feed/", "AWS Architecture Blog", "daily"),
    ("netflix_tech",         "https://netflix.github.io/feed.xml",             "Netflix Tech Blog",    "weekly"),
    ("uber_engineering",     "https://www.uber.com/blog/engineering/rss/",     "Uber Engineering",      "weekly"),
    ("stripe_engineering",   "https://stripe.com/blog/engineering/feed.rss",   "Stripe Engineering",    "weekly"),
    ("cloudflare_workers",   "https://blog.cloudflare.com/tag/developers/feed/","Cloudflare Developers", "daily"),

    # === 中文工程博客（每周） ===
    ("meituan_tech",         "https://tech.meituan.com/feed/",                "美团技术团队",          "weekly"),
    ("pingcap",              "https://www.pingcap.com/blog/feed/",            "PingCAP",               "weekly"),
    ("planetscale",          "https://planetscale.com/blog.rss",              "PlanetScale Blog",      "weekly"),
    ("supabase",             "https://supabase.com/blog/rss.xml",             "Supabase Blog",         "weekly"),
]
```

创建 `script/newsletter/news_engineering_blogs.py`，实现：
- 每个来源独立抓取，结果存 R2（`blog_{slug}_{date}.md`）
- 通过 LLM 生成单条摘要（50 字内）
- 只抓取最近 7 天内的文章（避免旧文重复）

### 2.2 改造 GitHub Trending 过滤逻辑

修改 `script/newsletter/news_github_trending_daily.py`：

当前问题：使用 `https://mshibanami.github.io/GitHubTrendingRSS/daily/all.xml`，全语言总榜。

改造方案：
- 改用按语言的 RSS 源，只关注目标技术栈：

```python
# 修改 all_rss_urls 或直接改 fetch_news 的 URL
GITHUB_TRENDING_URLS = [
    # 后端 + AI Infra 相关语言
    ("golang", "https://mshibanami.github.io/GitHubTrendingRSS/daily/go.xml"),
    ("python", "https://mshibanami.github.io/GitHubTrendingRSS/daily/python.xml"),
    ("rust",   "https://mshibanami.github.io/GitHubTrendingRSS/daily/rust.xml"),
    ("javascript", "https://mshibanami.github.io/GitHubTrendingRSS/daily/javascript.xml"),
]
```

- 每个语言取前 10，合并后由 LLM 按"对后端/AI 工程师的实践价值"筛选，只保留 Top 10

### 2.3 精简 HN 源

修改 `script/newsletter/news_hacker_news.py` 中 `all_rss_urls()`：

```python
def all_rss_urls() -> list[tuple[str, str, str]]:
    return [
        ("hacker_news_frontpage", "https://hnrss.org/frontpage", "Hacker News 首页"),
        ("hacker_news_best", "https://hnrss.org/best", "Hacker News 近期最佳"),
    ]
```

删除：`bestcomments`、`ask`、`show`、`audio_tech` 四个 RSS 源。

### 2.4 精简 Reddit 频道

修改 `script/newsletter/news_reddit.py` 中 `all_reddit_channels()`：

```python
def all_reddit_channels() -> list[tuple[str, str, str]]:
    # 只保留技术相关频道
    tech_channels = [
        ("devops",          "Reddit DevOps"),
        ("programming",     "Reddit Programming"),
        ("golang",          "Reddit Golang"),
        ("rust",            "Reddit Rust"),
        ("MachineLearning", "Reddit ML"),
    ]
    # 删除：AMA、AskReddit、Showerthoughts、TIL、ELI5

    channels = []
    for channel, title in tech_channels:
        slug = f"reddit_{channel.lower()}"
        rss_url = f"https://www.reddit.com/r/{channel}/top/.rss"
        channels.append((slug, rss_url, title))
    return channels
```

### 2.5 停用 V2EX 和少数派

- `newsletter.py:130`：删除 `v2ex = news_v2ex.get_today_news_content()`
- `newsletter.py:138`：删除 `shaoshupai_content = news_shaoshupai.get_today_news_content()`
- `create_final_newsletter` 函数签名移除 `shaoshupai` 和 `v2ex` 参数
- 保留 `news_v2ex.py` 和 `news_shaoshupai.py` 文件但不调用（方便以后重新启用）

### 2.6 Go Weekly 改为抓取逻辑

修改 `script/newsletter/news_go_weekly.py`：

当前问题：Go Weekly 一周一期，但每天都会重新抓取（实际每天拿到的是同一期）。

改造方案：
- 在 `fetch_latest_weekly()` 中检查当前期号是否与 R2 中已存的一致
- 一致则跳过，不一致才重新抓取并生成摘要
- 具体实现：读取最新 RSS entry 的 title（格式如 "Golang Weekly Issue #603"），与 R2 中已存的对比

```python
def fetch_latest_weekly():
    entries = news_utils.get_rss_entries("https://cprss.s3.amazonaws.com/golangweekly.com.xml", 10)
    if not entries:
        return

    entry = entries[0]
    title = entry.get("title", "")
    current_issue = get_today_news_file()  # go_weekly_{date}.md

    # 检查当前期是否已存在（按 issue 标题去重）
    existing = news_utils.get_file_from_r2_with_today(current_issue)
    if existing and title in existing:
        logger.info(f"Go Weekly {title} 已存在，跳过")
        return

    # ... 原有抓取逻辑
```

### 2.7 修复美团空文件问题

修改 `script/newsletter/news_meituan.py`：

当前问题：无文章时仍然生成文件，内容为"今天没有新的文章发布"，并出现在 newsletter 索引中。

改造方案：
- `fetch_news()` 无文章时不写 R2 文件
- `get_today_posts_content()` 返回空字符串（而非空文件内容）
- `newsletter.py` 中对美团返回值做空检查，空时不在索引中显示链接

```python
# news_meituan.py
def fetch_news():
    # ... 现有逻辑 ...
    if not final_contents:
        logger.info("美团技术团队今天没有发布新文章，跳过保存")
        return  # 不写文件
    # ... 原有保存逻辑 ...
```

---

## 3. 提示词重写

### 3.1 主筛选提示词（`newsletter.py`）

替换 `create_final_newsletter` 中的 `system_prompt` 和 `user_prompt`：

```python
def create_final_newsletter(
    last_newsletter: str,
    engineering_blogs: str,
    ai_news: str,
    github_trending: str,
    hacker_news: str,
    reddit_tech: str,
    meituan: str,
    go_weekly: str,
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
5. 有深度技术讨论的 HN/Reddit 帖子（不是产品公告）

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

### AI 资讯
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

### Reddit 技术频道
```markdown
{reddit_tech}
```

### 美团技术团队
```markdown
{meituan}
```

### Go Weekly
```markdown
{go_weekly}
```
"""
    return llm.one_shoot(system_prompt, user_prompt)
```

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

    current_datetime_formatted = news_utils.current_datetime_formatted()
    contents = [
        "## 今日要闻",
        f"\n<sub> 生成时间：{current_datetime_formatted}</sub>\n",
        "\n---\n",
        newsletter_summary,
        "\n---\n",
        "### 每周一看",
        "- [Cloudflare Blog](https://blog.cloudflare.com/zh-cn/)",
        "- [美团技术团队](https://tech.meituan.com)",
        "- [Go Blog](https://go.dev/blog/)",
    ]

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
newsletters/*/go_weekly_*.md
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
| `script/newsletter/newsletter.py` | **修改** | 重写提示词、精简 newsletter.md 结构、修改 `load_all_files_from_r2()`、修改 `generate_newsletter()`、修复 `generate_newsletter_profile()` |
| `script/newsletter/news_hacker_news.py` | **修改** | `all_rss_urls()` 只保留 frontpage + best |
| `script/newsletter/news_reddit.py` | **修改** | `all_reddit_channels()` 只保留技术频道 |
| `script/newsletter/news_github_trending_daily.py` | **修改** | 改用按语言的 RSS 源 |
| `script/newsletter/news_meituan.py` | **修改** | 无文章时不生成空文件 |
| `script/newsletter/news_go_weekly.py` | **修改** | 增加去重逻辑，避免重复抓取同一期 |
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

4. 修改 `news_hacker_news.py`：精简 HN 源
5. 修改 `news_reddit.py`：删除吹水频道
6. 修改 `news_github_trending_daily.py`：按语言过滤
7. 修改 `news_meituan.py`：修复空文件
8. 修改 `news_go_weekly.py`：增加去重
9. 创建 `news_engineering_blogs.py`（新增工程博客 RSS 源）

### Phase 3：提示词重写（半天）

10. 修改 `newsletter.py` 中 `create_final_newsletter()` 的提示词
11. 修改 `generate_newsletter()` 精简 newsletter.md 结构
12. 修改 `generate_newsletter_profile()` 适配新结构

### Phase 4：存储改造（半天）

13. 修改 `load_all_files_from_r2()` 只下载精选文件
14. 更新 `.gitignore`
15. 本地测试验证

### Phase 5：代码清理（半天）

16. 删除 `news_36kr.py`、`final_news_letter.py`
17. 处理 `tokenizer.json`（改用 tiktoken 或运行时下载）
18. 更新 `pyproject.toml` 依赖

### Phase 6：CI/CD 改进（可选）

19. 改用 fine-grained PAT
20. 更新 workflow 增加 timeout 和失败通知
21. 清理 Git 历史中的大文件（如需要）

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
