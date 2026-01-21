## 今日要闻

<sub> 生成时间：2026-01-21 08:15:22</sub>


---

### AI 推荐要点

- **[STEM架构：无需MoE路由即可扩展Transformer参数记忆](https://twitter.com/TheTuringPost/status/2013011864880660495)**（来源：AINews）
  > 用静态嵌入查找替换部分FFN层，将模型容量与每token计算开销解耦，实现CPU卸载和异步预取，避免动态路由开销。

- **[DeepSeek发布Engram：为LLM引入可扩展的确定性O(1)查找记忆](https://github.com/deepseek-ai/Engram/blob/main/Engram_paper.pdf)**（来源：AINews）
  > 通过哈希N-gram嵌入实现确定性O(1)查找，将模式重建从神经计算中卸载，在等计算量下持续提升知识、推理和代码任务性能。

- **[NVIDIA提出端到端测试时训练方法，允许模型在推理时实时更新权重](https://github.com/test-time-training/e2e)**（来源：AINews）
  > 将上下文窗口视为训练集，在推理时通过元学习实时更新特定MLP层权重，对128K上下文推理速度比完全注意力快2.7倍。

- **[华为/中国推理系统“2025旗舰作品”总结，聚焦端到端系统设计](https://twitter.com/ZhihuFrontier/status/2013127635589800172)**（来源：AINews）
  > 针对KV缓存容量墙、混合调度、缓存亲和性等系统设计理念的深度总结，强调从孤立内核转向端到端服务等级目标设计。

- **[google/langextract：利用LLM从非结构化文本中提取结构化信息](https://github.com/google/langextract)**（来源：GitHub Trending）
  > Python库，支持精确源文本定位和交互式可视化，高效处理长文档，无需微调即可快速定制临床报告、文学分析等提取任务。

- **[PostgreSQL非常规优化技巧](https://news.ycombinator.com/item?id=46692116)**（来源：Hacker News）
  > 介绍PostgreSQL索引、查询优化和性能调优的实用非常规方法，为后端工程师提供可直接实践的深度调优思路。

- **[Fence – 带网络和文件系统限制的沙盒化命令行工具](https://news.ycombinator.com/item?id=46695467)**（来源：Hacker News）
  > 命令行沙盒工具，默认阻断网络并限制文件写入，用于安全运行半可信代码或管理AI代理权限，提升本地执行安全性。

- **[从数据看，使用AI反而降低了我的工作效率](https://news.ycombinator.com/item?id=46698729)**（来源：Hacker News）
  > 开发者实测使用AI后PR数量锐减，从月均15-30个降至4个，引发对AI工具实际工程效率与精神消耗的深度反思。

- **[Ask HN：边缘云计算是否需要独立性和自主性？](https://news.ycombinator.com/item?id=46698275)**（来源：Hacker News）
  > 提出边缘云作为设备数据第一跳的新架构，探讨通过分布式边缘节点就近处理数据以提升安全与韧性，避免被大云控制。

- **[我们能否停止在 `package.json` 中使用 `^` 符号](https://news.ycombinator.com/item?id=46695541)**（来源：Hacker News）
  > 为保障供应链安全，建议在package.json中避免使用^符号，改用精确版本或锁定依赖，防止自动更新引入未审查代码。

---

### 各渠道精选摘要
- [少数派](./2026-01-21/shaoshupai_2026-01-21.md)
- [美团技术团队](./2026-01-21/meituan_2026-01-21.md)

---

### 渠道精选
- [AINews](./2026-01-21/ai_news_summary_2026-01-21.md)
- [GitHub Trending](./2026-01-21/github_trending_2026-01-21.md)
- [V2EX 技术版](./2026-01-21/v2ex_hot_2026-01-21.md)

---

### Hacker News 精选
- [Hacker News 首页](./2026-01-21/hacker_news_frontpage_2026-01-21.md)
- [Hacker News 近期最佳](./2026-01-21/hacker_news_best_2026-01-21.md)
- [Hacker News 高赞评论](./2026-01-21/hacker_news_top_comments_2026-01-21.md)
- [Hacker News 问答](./2026-01-21/hacker_news_ask_2026-01-21.md)
- [Hacker News 展示](./2026-01-21/hacker_news_show_2026-01-21.md)
- [Hacker News 音频技术](./2026-01-21/hacker_news_audio_tech_2026-01-21.md)

---

### Reddit 精选频道
- [Reddit AMA](./2026-01-21/reddit_ama_2026-01-21.md)
- [Reddit AskReddit](./2026-01-21/reddit_askreddit_2026-01-21.md)
- [Reddit Showerthoughts](./2026-01-21/reddit_showerthoughts_2026-01-21.md)
- [Reddit TIL](./2026-01-21/reddit_todayilearned_2026-01-21.md)
- [Reddit DevOps](./2026-01-21/reddit_devops_2026-01-21.md)
- [Reddit Programming](./2026-01-21/reddit_programming_2026-01-21.md)
- [Reddit ELI5](./2026-01-21/reddit_explainlikeimfive_2026-01-21.md)
- [Reddit Golang](./2026-01-21/reddit_golang_2026-01-21.md)
- [Reddit Rust](./2026-01-21/reddit_rust_2026-01-21.md)
- [Reddit ML](./2026-01-21/reddit_machinelearning_2026-01-21.md)

---

### 每周一看
- [Cloudflare Blog](https://blog.cloudflare.com/zh-cn/)
- [少数派](./2026-01-21/shaoshupai_2026-01-21.md)
- [美团技术团队](./2026-01-21/meituan_2026-01-21.md)

# 往日新闻

#### [2026-01-20](./2026-01-20/newsletter.md)

#### [2026-01-19](./2026-01-19/newsletter.md)

#### [2026-01-18](./2026-01-18/newsletter.md)

#### [2026-01-17](./2026-01-17/newsletter.md)

#### [2026-01-16](./2026-01-16/newsletter.md)

#### [2026-01-15](./2026-01-15/newsletter.md)

#### [2026-01-14](./2026-01-14/newsletter.md)

#### [2026-01-13](./2026-01-13/newsletter.md)

#### [2026-01-12](./2026-01-12/newsletter.md)

#### [2026-01-11](./2026-01-11/newsletter.md)

#### [2026-01-10](./2026-01-10/newsletter.md)

#### [2026-01-08](./2026-01-08/newsletter.md)

#### [2026-01-07](./2026-01-07/newsletter.md)

#### [2026-01-05](./2026-01-05/newsletter.md)

#### [2026-01-04](./2026-01-04/newsletter.md)

#### [2026-01-03](./2026-01-03/newsletter.md)

#### [2026-01-02](./2026-01-02/newsletter.md)

#### [2026-01-01](./2026-01-01/newsletter.md)

#### [2025-12-31](./2025-12-31/newsletter.md)

#### [2025-12-30](./2025-12-30/newsletter.md)

#### [2025-12-29](./2025-12-29/newsletter.md)

#### [2025-12-28](./2025-12-28/newsletter.md)

#### [2025-12-27](./2025-12-27/newsletter.md)

#### [2025-12-26](./2025-12-26/newsletter.md)

#### [2025-12-25](./2025-12-25/newsletter.md)

#### [2025-12-24](./2025-12-24/newsletter.md)

#### [2025-12-23](./2025-12-23/newsletter.md)

#### [2025-12-22](./2025-12-22/newsletter.md)

#### [2025-12-21](./2025-12-21/newsletter.md)

#### [2025-12-20](./2025-12-20/newsletter.md)

#### [2025-12-19](./2025-12-19/newsletter.md)

#### [2025-12-18](./2025-12-18/newsletter.md)

#### [2025-12-17](./2025-12-17/newsletter.md)

#### [2025-12-16](./2025-12-16/newsletter.md)

#### [2025-12-15](./2025-12-15/newsletter.md)

#### [2025-12-14](./2025-12-14/newsletter.md)

#### [2025-12-13](./2025-12-13/newsletter.md)

#### [2025-12-12](./2025-12-12/newsletter.md)

#### [2025-12-11](./2025-12-11/newsletter.md)

#### [2025-12-10](./2025-12-10/newsletter.md)

#### [2025-12-09](./2025-12-09/newsletter.md)

#### [2025-12-08](./2025-12-08/newsletter.md)

#### [2025-12-07](./2025-12-07/newsletter.md)

#### [2025-12-06](./2025-12-06/newsletter.md)

#### [2025-12-05](./2025-12-05/newsletter.md)

#### [2025-11-14](./2025-11-14/newsletter.md)

#### [2025-11-13](./2025-11-13/newsletter.md)

#### [2025-11-12](./2025-11-12/newsletter.md)

#### [2025-11-10](./2025-11-10/newsletter.md)

#### [2025-11-07](./2025-11-07/newsletter.md)

#### [2025-11-06](./2025-11-06/newsletter.md)

#### [2025-11-05](./2025-11-05/newsletter.md)

#### [2025-11-04](./2025-11-04/newsletter.md)

#### [2025-11-02](./2025-11-02/newsletter.md)

#### [2025-11-01](./2025-11-01/newsletter.md)

#### [2025-10-31](./2025-10-31/newsletter.md)

#### [2025-10-30](./2025-10-30/newsletter.md)

#### [2025-10-29](./2025-10-29/newsletter.md)

#### [2025-10-28](./2025-10-28/newsletter.md)

#### [2025-10-27](./2025-10-27/newsletter.md)

#### [2025-10-26](./2025-10-26/newsletter.md)

#### [2025-10-25](./2025-10-25/newsletter.md)

#### [2025-10-24](./2025-10-24/newsletter.md)

#### [2025-10-23](./2025-10-23/newsletter.md)

#### [2025-10-22](./2025-10-22/newsletter.md)

#### [2025-10-21](./2025-10-21/newsletter.md)

#### [2025-10-20](./2025-10-20/newsletter.md)

#### [2025-10-19](./2025-10-19/newsletter.md)

#### [2025-10-18](./2025-10-18/newsletter.md)

#### [2025-10-17](./2025-10-17/newsletter.md)

#### [2025-10-16](./2025-10-16/newsletter.md)

#### [2025-10-14](./2025-10-14/newsletter.md)

#### [2025-10-13](./2025-10-13/newsletter.md)

#### [2025-10-12](./2025-10-12/newsletter.md)

#### [2025-10-11](./2025-10-11/newsletter.md)

#### [2025-10-10](./2025-10-10/newsletter.md)

#### [2025-10-09](./2025-10-09/newsletter.md)

#### [2025-10-08](./2025-10-08/newsletter.md)

#### [2025-10-07](./2025-10-07/newsletter.md)

#### [2025-10-06](./2025-10-06/newsletter.md)

#### [2025-10-05](./2025-10-05/newsletter.md)

#### [2025-10-04](./2025-10-04/newsletter.md)

#### [2025-10-03](./2025-10-03/newsletter.md)

#### [2025-10-02](./2025-10-02/newsletter.md)

#### [2025-10-01](./2025-10-01/newsletter.md)

#### [2025-09-30](./2025-09-30/newsletter.md)

#### [2025-09-29](./2025-09-29/newsletter.md)

#### [2025-09-28](./2025-09-28/newsletter.md)

#### [2025-09-27](./2025-09-27/newsletter.md)

#### [2025-09-26](./2025-09-26/newsletter.md)

#### [2025-09-25](./2025-09-25/newsletter.md)

#### [2025-09-24](./2025-09-24/newsletter.md)

#### [2025-09-23](./2025-09-23/newsletter.md)

#### [2025-09-22](./2025-09-22/newsletter.md)

#### [2025-09-21](./2025-09-21/newsletter.md)

#### [2025-09-20](./2025-09-20/newsletter.md)

#### [2025-09-19](./2025-09-19/newsletter.md)

#### [2025-09-14](./2025-09-14/newsletter.md)

#### [2025-09-13](./2025-09-13/newsletter.md)

#### [2025-09-12](./2025-09-12/newsletter.md)

#### [2025-09-11](./2025-09-11/newsletter.md)

#### [2025-09-10](./2025-09-10/newsletter.md)

#### [2025-09-09](./2025-09-09/newsletter.md)

#### [2025-09-08](./2025-09-08/newsletter.md)

#### [2025-09-07](./2025-09-07/newsletter.md)

#### [2025-09-06](./2025-09-06/newsletter.md)

#### [2025-09-05](./2025-09-05/newsletter.md)

#### [2025-09-04](./2025-09-04/newsletter.md)

#### [2025-09-02](./2025-09-02/newsletter.md)

#### [2025-09-01](./2025-09-01/newsletter.md)

#### [2025-08-31](./2025-08-31/newsletter.md)

#### [2025-08-30](./2025-08-30/newsletter.md)

#### [2025-08-29](./2025-08-29/newsletter.md)

#### [2025-08-28](./2025-08-28/newsletter.md)

#### [2025-08-27](./2025-08-27/newsletter.md)

#### [2025-08-26](./2025-08-26/newsletter.md)

#### [2025-08-25](./2025-08-25/newsletter.md)

#### [2025-08-24](./2025-08-24/newsletter.md)

#### [2025-08-23](./2025-08-23/newsletter.md)

#### [2025-08-21](./2025-08-21/newsletter.md)

#### [2025-08-20](./2025-08-20/newsletter.md)

#### [2025-08-19](./2025-08-19/newsletter.md)

#### [2025-08-18](./2025-08-18/newsletter.md)

#### [2025-08-17](./2025-08-17/newsletter.md)

#### [2025-08-16](./2025-08-16/newsletter.md)

#### [2025-08-15](./2025-08-15/newsletter.md)

#### [2025-08-14](./2025-08-14/newsletter.md)

#### [2025-08-13](./2025-08-13/newsletter.md)

#### [2025-08-12](./2025-08-12/newsletter.md)

#### [2025-08-11](./2025-08-11/newsletter.md)

#### [2025-08-10](./2025-08-10/newsletter.md)

#### [2025-08-09](./2025-08-09/newsletter.md)

#### [2025-08-08](./2025-08-08/newsletter.md)

#### [2025-08-07](./2025-08-07/newsletter.md)

#### [2025-08-05](./2025-08-05/newsletter.md)

#### [2025-08-04](./2025-08-04/newsletter.md)

#### [2025-08-03](./2025-08-03/newsletter.md)

#### [2025-08-02](./2025-08-02/newsletter.md)

#### [2025-08-01](./2025-08-01/newsletter.md)

#### [2025-07-31](./2025-07-31/newsletter.md)

#### [2025-07-30](./2025-07-30/newsletter.md)

#### [2025-07-29](./2025-07-29/newsletter.md)

#### [2025-07-28](./2025-07-28/newsletter.md)

#### [2025-07-27](./2025-07-27/newsletter.md)

#### [2025-07-26](./2025-07-26/newsletter.md)

#### [2025-07-25](./2025-07-25/newsletter.md)

#### [2025-07-24](./2025-07-24/newsletter.md)

#### [2025-07-23](./2025-07-23/newsletter.md)

#### [2025-07-22](./2025-07-22/newsletter.md)

#### [2025-07-21](./2025-07-21/newsletter.md)

#### [2025-07-19](./2025-07-19/newsletter.md)

#### [2025-07-18](./2025-07-18/newsletter.md)

#### [2025-07-17](./2025-07-17/newsletter.md)

#### [2025-07-16](./2025-07-16/newsletter.md)

#### [2025-07-15](./2025-07-15/newsletter.md)

#### [2025-07-14](./2025-07-14/newsletter.md)

#### [2025-07-13](./2025-07-13/newsletter.md)

#### [2025-07-12](./2025-07-12/newsletter.md)

#### [2025-07-11](./2025-07-11/newsletter.md)

#### [2025-07-10](./2025-07-10/newsletter.md)

#### [2025-07-08](./2025-07-08/newsletter.md)

#### [2025-07-07](./2025-07-07/newsletter.md)

#### [2025-07-06](./2025-07-06/newsletter.md)

#### [2025-07-05](./2025-07-05/newsletter.md)

#### [2025-07-04](./2025-07-04/newsletter.md)

#### [2025-07-02](./2025-07-02/newsletter.md)

#### [2025-07-01](./2025-07-01/newsletter.md)

#### [2025-06-30](./2025-06-30/newsletter.md)

#### [2025-06-28](./2025-06-28/newsletter.md)

#### [2025-06-27](./2025-06-27/newsletter.md)

#### [2025-06-26](./2025-06-26/newsletter.md)

#### [2025-06-25](./2025-06-25/newsletter.md)

#### [2025-06-24](./2025-06-24/newsletter.md)

#### [2025-06-23](./2025-06-23/newsletter.md)

#### [2025-06-22](./2025-06-22/newsletter.md)
