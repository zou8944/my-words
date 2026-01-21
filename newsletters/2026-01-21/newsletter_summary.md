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