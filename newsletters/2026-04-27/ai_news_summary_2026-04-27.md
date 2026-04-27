## AINews - 2026-04-27

> [原文链接](https://news.smol.ai/issues/26-04-24-deepseek-v4/)

好的，作为资深的科技新闻分析师，我已从您提供的 AINews 内容中提取了最有价值的信息点，并按照指定格式整理如下。

---

## 📰 十大AI新闻要点

### 1. [DeepSeek发布V4系列模型，架构重大革新](https://x.com/ArtificialAnlys/status/2047735160544841953)
> DeepSeek 正式发布 **DeepSeek-V4 Pro** 和 **DeepSeek-V4 Flash** 两款模型，这是自 V3 以来首次重大架构更新。V4 Pro 拥有 **1.6T 总参数 / 49B 激活参数**，V4 Flash 为 **284B 总参数 / 13B 激活参数**，均支持 **100万 token 上下文**，并采用 **MIT 开源协议**。其技术报告因细节详尽，被多位研究者誉为年度最重要的模型论文之一。

---

### 2. [V4 Pro 性能跻身开源模型顶尖，但仍落后于闭源前沿](https://x.com/ArtificialAnlys/status/2047735160544841953)
> 独立评测显示，V4 Pro 在 Artificial Analysis 智能指数上得分为 **52**，成为仅次于 Kimi K2.6（54分）的**第二强开源推理模型**。在代理任务基准 GDPval-AA 上，V4 Pro 以 **1554** 分领先所有开源模型。然而，其整体能力仍被认为落后于 GPT-5.x、Opus 4.7 等顶级闭源模型，差距约为 **4-5个月**。

---

### 3. [V4 核心创新：革命性的长上下文注意力架构](https://x.com/ZhihuFrontier/status/2047664976215839021)
> V4 的技术核心在于全新的混合注意力系统，通过共享KV向量、压缩KV流、稀疏注意力和滑动窗口等技术，将 **1M 上下文的 KV 缓存从 V3.2 的 83.9 GiB 大幅缩减至 9.62 GiB**，实现了 **8.7倍** 的降低。这一突破使得在开源模型中实现可操作的百万级上下文成为现实。

---

### 4. [V4 Flash 模型性价比极高，或成主流选择](https://x.com/arena/status/2047774037204742255)
> 尽管 Pro 模型性能更强，但多位评论者认为 **V4 Flash** 对实际应用更为重要。其 API 定价仅为 **$0.14 / $0.28 每百万输入/输出 token**，远低于 Pro 模型。评测显示，Flash 在推理任务上的最高表现可媲美 Pro 的高水平，且能在 **256GB Mac** 上本地运行，极大地推动了本地化部署的可能性。

---

### 5. [OpenAI 发布 GPT-5.5，聚焦编码效率与安全性](https://openai.com/index/introducing-gpt-5-5/)
> OpenAI 推出 **GPT-5.5** 及 **GPT-5.5 Pro**，支持 **100万 token 上下文**。新模型在编码和知识工作方面进行了优化，声称在复杂工作流中提供最先进的准确性，并具备更低的延迟和 token 使用量。在 CursorBench 上，GPT-5.5 以 **72.8%** 的成绩登顶，并在 Terminal-Bench 上获得 **82.7** 的最高分。

---

### 6. [GPT-5.5 定价翻倍，但用户反馈编码质量显著提升](https://x.com/almmaasoglu/status/2047745168141324559)
> GPT-5.5 的定价为 **$5 / $30 每百万输入/输出 token**，是 GPT-5.4 的两倍。尽管价格高昂，但早期用户反馈普遍积极，认为其编码质量更好，更简洁，且 token 效率更高。有开发者称其为“从 LLM 中读到的最好的代码”，并能捕捉到复杂的边缘案例。

---

### 7. [谷歌计划向 Anthropic 投资高达 400 亿美元](https://x.com/FT/status/2047715653553942997)
> 据《金融时报》报道，谷歌计划向 AI 公司 Anthropic 投资高达 **400 亿美元**。这一巨额投资传闻引发了业界对 Anthropic 算力承诺规模的广泛讨论，凸显了顶级 AI 公司之间对资本和算力的激烈争夺。

---

### 8. [Qwen 3.6 27B 模型在代理能力上追平 Sonnet 4.6](https://www.reddit.com/r/LocalLLaMA/comments/1strodp/qwen_36_27b_makes_huge_gains_in_agency_on/)
> 阿里巴巴的 **Qwen 3.6 27B** 模型在 Artificial Analysis 的代理指数上取得了与 **Sonnet 4.6** 持平的成绩，超越了 Gemini 3.1 Pro Preview、GPT 5.2/5.3 等更大模型。这表明小型模型在特定任务上正迅速接近前沿能力，社区对即将发布的 **Qwen 3.6 122B** 模型充满期待。

---

### 9. [Hugging Face 发布开源 CLI 工具 ML Intern](https://x.com/MillieMarconnni/status/2047639632859500691)
> Hugging Face 推出了 **ML Intern**，一个开源的命令行“AI实习生”，专为机器学习工作设计。它可以研究论文、编写代码、运行实验、使用 Hugging Face 数据集和任务、搜索 GitHub，并能迭代多达 **300 步**。这进一步降低了 ML 工作的门槛。

---

### 10. [ComfyUI 以 5 亿美元估值融资 3000 万美元](https://x.com/yoland_yan/status/2047731043000627263)
> 流行的 AI 图像生成工具 ComfyUI 宣布完成 **3000 万美元** 融资，估值达到 **5 亿美元**。该公司表示将保持其核心的开源和本地优先定位，这反映了市场对强大且可定制的本地 AI 工具的巨大需求。

---

## 🛠️ 十大工具产品要点

### 1. [DeepSeek-V4 Pro / Flash 模型](https://huggingface.co/collections/deepseek-ai/deepseek-v4)
> DeepSeek 发布的两款新模型。V4 Pro（1.6T参数）和 V4 Flash（284B参数）均支持 **1M token 上下文**，采用 **MIT 协议**。V4 Pro 定价 $1.74/$3.48 每百万 token，V4 Flash 定价 $0.14/$0.28。来源：HuggingFace 模型集合。

---

### 2. [GPT-5.5 / GPT-5.5 Pro 模型](https://openai.com/index/introducing-gpt-5-5/)
> OpenAI 发布的最新模型，定价 $5/$30 每百万输入/输出 token。在 CursorBench 和 Terminal-Bench 上取得领先成绩，并已集成到 Cursor、GitHub Copilot、Codex 等主流开发工具中。来源：OpenAI 官方博客。

---

### 3. [Qwen 3.6 27B / 35B 模型](https://www.reddit.com/r/LocalLLaMA/comments/1steip4/qwen_36_27b_is_a_beast/)
> 阿里巴巴 Qwen 系列的最新模型。27B 版本在代理能力上表现惊人，35B 版本在本地推理速度上可达 **72 TPS**。社区反馈其编码能力接近 Opus 级别，是本地部署的强力候选。来源：Reddit 社区讨论。

---

### 4. [Hermes Agent v0.11.0](https://x.com/WesRoth/status/2047646749427216385)
> Nous Research 发布的代理框架重大更新，引入了重写的 React TUI、仪表盘插件、主题系统、更多推理提供商支持、图像后端和 QQBot 支持。已快速支持 DeepSeek V4 和 GPT-5.5。来源：Twitter/X 推文。

---

### 5. [DeepEP V2 和 TileKernels](https://github.com/deepseek-ai/DeepEP/pull/605)
> DeepSeek 开源的两个基础设施项目。DeepEP V2 专注于模型效率优化，而 **TileKernels** 引入了一种据称能实现**线性扩展**的新型并行化技术，即算力翻倍，处理速度也翻倍。来源：GitHub Pull Request。

---

### 6. [ML Intern (Hugging Face)](https://x.com/MillieMarconnni/status/2047639632859500691)
> Hugging Face 推出的开源 CLI 工具，可自主进行 ML 研究、编码和实验。它能够迭代多达 **300 步**，并深度集成 HF 生态系统，为 ML 开发者提供了一个强大的自动化助手。来源：Twitter/X 推文。

---

### 7. [PI Coding Agent + Qwen3.6 35B](https://www.reddit.com/r/LocalLLaMA/comments/1stjwg5/been_using_pi_coding_agent_with_local_qwen36_35b/)
> 一个结合了自定义“计划优先”技能文件的本地编码代理。它通过强制要求 `TODO.md` 审批流程来确保结构化工作流，在 **8GB VRAM** 的笔记本上即可实现 **15-30 TPS** 的推理速度，展示了本地编码代理的实用性。来源：Reddit 社区分享。

---

### 8. [Chappie 分布式 AI 系统 (Exo)](https://github.com/exo-explore/exo)
> 一位开发者使用 **4 台 Mac Mini M4 Pro** 构建的分布式 AI 系统，总统一内存达 **256GB**。该系统利用 **Exo** 框架进行分布式推理，并使用 Qdrant 向量数据库进行记忆共享，能自主阅读论文、生成问题并开发新技能。来源：GitHub 仓库 (Exo)。

---

### 9. [GPT Image 2 + Seedance 2 工作流](https://x.com/_OAK200/status/2047616640448078167)
> 结合 OpenAI 的图像生成和视频生成模型的工作流，能够生成高保真的图像到视频管线。有用户报告称，通过实验性 API 已可获得 **2K/4K** 分辨率的图像，展示了多模态内容创作的最新进展。来源：Twitter/X 推文。

---

### 10. [Kling AI 原生 4K 输出](https://x.com/Kling_ai/status/2047676942317678879)
> AI 视频生成平台 Kling 宣布支持原生 **4K 输出**，并举办 **$25,000** 的短片竞赛。这标志着 AI 视频生成在分辨率和质量上又迈出了一大步，向专业级内容创作工具靠近。来源：Twitter/X 推文。