好的，这是为您筛选和整理后的每日技术 Newsletter。

---

## 每日技术简报 - 2026-05-31

- **[多轮RL训练中的“Token-In, Token-Out”关键Bug被揭示](https://x.com/ClementDelangue/status/2060175330665508917)**（来源：Hugging Face）
  > 揭示了多轮RL训练中因重新分词导致梯度错误的静默Bug，提出“Token-In, Token-Out”修复原则，对RL训练实践有直接指导意义。

- **[StepFun发布Step 3.7 Flash，196B参数MoE模型可本地运行](https://www.reddit.com/r/LocalLLaMA/comments/1tqloii/stepfun_37_flash/)**（来源：Reddit r/LocalLLaMA）
  > 196B总参/11B激活的MoE模型，专为高吞吐代理设计，可在约128GB内存本地运行，性能强劲，已获llama.cpp支持。

- **[Starlette框架发现严重漏洞，影响vLLM、MCP服务器等大量AI工具](https://arstechnica.com/information-technology/2026/05/millions-of-ai-agents-imperiled-by-critical-vulnerability-in-open-source-package/)**（来源：Ars Technica）
  > “BadHost”漏洞（CVE-2026-48710）影响Starlette < 1.0.1，可绕过基于路径的授权，是LLM基础设施供应链风险的典型案例。

- **[Zai用ZCube网络架构替换GLM-5.1推理网络，性能大幅提升](https://z.ai/blog/zcube)**（来源：Zai Blog）
  > 用扁平化ZCube架构替换标准spine-leaf网络，成本降低33%，GPU推理吞吐量提升15%，首token P99延迟降低40.6%。

- **[llama.cpp推出官方应用llama.app，简化本地部署](https://x.com/ggerganov/status/2060394400237109567)**（来源：X / @ggerganov）
  > 为llama.cpp提供官方网站、统一安装器和单一入口点，标志着本地AI部署工具链的成熟和易用性提升。

- **[vLLM发布原生权重同步API和Rust BPE分词器fastokens](https://x.com/vllm_project/status/2060208480292843720)**（来源：X / @vllm_project）
  > 原生权重同步API改进异步RL，Rust BPE分词器旨在减少长上下文/代理工作负载中的CPU瓶颈，对大规模推理部署至关重要。

- **[LangChain Deep Agents v0.6：将工具配置文件作为一等公民](https://x.com/LangChain/status/2060349231722852680)**（来源：X / @LangChain）
  > 将工具配置文件（harness profiles）作为一等公民，使开源模型能以比前沿API低20倍以上的成本获得强劲性能，标志着代理设计向模型特定优化转变。

- **[Hugging Face新增“仅基础模型”筛选开关](https://www.reddit.com/r/LocalLLaMA/comments/1tq2ce9/hf_models_page_now_has_a_base_only_toggle_to/)**（来源：Reddit r/LocalLLaMA）
  > 模型页面新增“Base only”开关，过滤掉微调、量化等衍生版本，方便用户快速找到原始/基础模型检查点。

- **[SQLite：持久化工作流的唯一所需](https://news.ycombinator.com/item?id=48326802)**（来源：Hacker News）
  > 一篇深度文章，论证SQLite足以作为持久化工作流的后端，挑战了必须使用复杂数据库的常规认知，提供了轻量级方案。

- **[Show HN: Tiny-vLLM – 基于C++和CUDA的高性能LLM推理引擎](https://news.ycombinator.com/item?id=48328184)**（来源：Hacker News）
  > 一个轻量级、高性能的LLM推理引擎，使用C++和CUDA实现，适合对性能和资源控制有极致要求的场景。