## AINews - 2026-04-26

> [原文链接](https://news.smol.ai/issues/26-04-24-deepseek-v4/)

## 📰 十大AI新闻要点

### 1. [DeepSeek发布V4系列：1M上下文、MIT许可、混合推理模式](https://x.com/ArtificialAnlys/status/2047735160544841953)
> DeepSeek正式发布**DeepSeek-V4 Pro**和**DeepSeek-V4 Flash**，这是自V3以来的首次重大架构更新。核心亮点包括：**1M-token上下文**（V3.2为128K）、混合推理/非推理模式、**MIT开源许可**，以及一份被多位研究者称为“年度最重要AI论文之一”的详细技术报告。V4 Pro拥有**1.6T总参数/49B激活参数**，V4 Flash为**284B总参数/13B激活参数**，训练数据量达**32T-33T tokens**。

---

### 2. [V4 Pro在开放权重模型中排名第二，接近闭源前沿模型](https://x.com/ArtificialAnlys/status/2047735160544841953)
> 独立基准测试显示，V4 Pro在Artificial Analysis Intelligence Index上得分**52**（V3.2为42），成为**#2开放权重推理模型**，仅次于Kimi K2.6（54）。在代理性真实工作测试GDPval-AA中，V4 Pro以**1554分**领先所有开放权重模型，超越Kimi K2.6（1484）和GLM-5.1（1535）。综合评估认为V4 Pro大致处于**Claude Sonnet级到Opus级**之间，但整体仍落后于GPT-5.x/Opus 4.7等顶级闭源模型。

---

### 3. [V4采用革命性长上下文注意力架构，KV缓存缩小8.7倍](https://x.com/ZhihuFrontier/status/2047664976215839021)
> V4的技术报告详细描述了一种全新的混合注意力系统：包括**共享KV向量**、**压缩KV流**（c4a约4倍压缩、c128a约128倍压缩）、**top-k稀疏注意力**以及**128-token滑动窗口**。这使得1M上下文的KV缓存仅需**9.62 GiB/序列（bf16）**，比DeepSeek V3.2的83.9 GiB缩小了**8.7倍**。此外，FP4索引缓存+FP8注意力缓存可再实现约**2倍**缩减。多位研究者认为，**长上下文系统设计的贡献可能比原始基准位置更重要**。

---

### 4. [V4定价极具竞争力，Flash版性价比突出](https://x.com/ArtificialAnlys/status/2047735160544841953)
> V4 Pro定价为**$1.74/$3.48每百万输入/输出tokens**，V4 Flash仅为**$0.14/$0.28**。然而，独立评估揭示了一个重要警告：V4在AA Index上消耗了**1.9亿输出tokens**（Pro版）和**2.4亿输出tokens**（Flash版），意味着低价并不等于低总成本。DeepSeek表示，一旦**华为昇腾950超节点**在H2大规模部署，Pro版价格可能大幅下降。

---

### 5. [GPT-5.5发布：1M上下文、更强编码能力、Token效率提升](https://openai.com/index/introducing-gpt-5-5/)
> OpenAI推出**GPT-5.5**和**GPT-5.5 Pro**，配备**1M上下文窗口**。定价为$5/$30每百万输入/输出tokens（Pro版加倍）。在CursorBench上以**72.8%** 位居第一，在Terminal-Bench上以**82.7**排名第一。用户反馈集中在**更好的编码质量和Token效率**：GPT-5.5 medium在LisanBench上比GPT-5.4 medium减少**45.6%的tokens**且得分更高。Perplexity Computer在复杂任务上看到**56%更少的tokens**。

---

### 6. [Qwen 3.6 27B在代理性指数上与Sonnet 4.6持平](https://www.reddit.com/r/LocalLLaMA/comments/1strodp/qwen_36_27b_makes_huge_gains_in_agency_on/)
> Qwen 3.6 27B在Artificial Analysis的**Agentic Index**上达到与**Sonnet 4.6**持平的水平，超越了Gemini 3.1 Pro Preview、GPT 5.2/5.3和MiniMax 2.7。该模型在本地运行表现出色，多位用户报告在MacBook Pro和RTX 5090等设备上运行良好。社区对即将推出的**Qwen 3.6 122B**版本充满期待，认为小型模型正在接近前沿能力。

---

### 7. [Google计划向Anthropic投资高达400亿美元](https://x.com/FT/status/2047715653553942997)
> 据英国《金融时报》报道，Google计划向Anthropic投资高达**400亿美元**。这一消息引发了关于Anthropic计算承诺规模的广泛讨论。同时，Cohere与Aleph Alpha宣布了**加拿大/德国主权AI合作伙伴关系**，专注于企业级和隐私安全。

---

### 8. [DeepSeek发布DeepEP V2和TileKernels：开源并行化技术](https://github.com/deepseek-ai/DeepEP/pull/605)
> DeepSeek开源了**DeepEP V2**和**TileKernels**，这两项技术专注于AI模型优化和并行化。TileKernels引入了一种据称**线性扩展**的新型并行化技术——即计算能力翻倍，处理速度也翻倍。社区评论认为DeepSeek正在扮演OpenAI曾被期望扮演的角色：推进研究并公开分享发现。

---

### 9. [ComfyUI以5亿美元估值融资3000万美元](https://x.com/yoland_yan/status/2047731043000627263)
> ComfyUI完成**3000万美元**融资，估值达**5亿美元**，同时保持核心/开源-本地定位。此外，Mechanize宣布以**5亿美元投后估值**融资**910万美元**。Arcee AI聘请Cody Blakeney担任研究主管，强调开放权重美国前沿模型。

---

### 10. [MIT Hyperloop Transformers：用50%更少参数超越传统Transformer](https://x.com/TheTuringPost/status/2047720038342476187)
> MIT研究人员提出**Hyperloop Transformers**，混合循环和普通Transformer块，在**240M/1B/2B**参数规模下，使用约**50%更少的参数**却超越了传统Transformer。同时，一项关于“工具注意力”的研究声称可实现**95%的工具Token减少**（从47.3k降至2.4k/轮），通过动态门控和惰性模式加载实现。

---

## 🛠️ 十大工具产品要点

### 1. [DeepSeek-V4 Pro / Flash - HuggingFace开放权重](https://huggingface.co/collections/deepseek-ai/deepseek-v4)
> DeepSeek V4系列已在HuggingFace上发布，包括**V4 Pro（1.6T参数/49B激活）** 和**V4 Flash（284B参数/13B激活）**。两者均支持**1M token上下文**，采用**MIT许可**。检查点使用**混合FP4+FP8精度**，MoE专家权重为FP4，注意力/归一化/路由器为FP8，完整模型可适配单个**8×B200节点**。

---

### 2. [vLLM - 对DeepSeek V4的Day-0支持](https://x.com/vllm_project/status/2047843293447500069)
> vLLM项目在DeepSeek V4发布当天即提供支持。NVIDIA发布了在**Blackwell Ultra**上使用vLLM的V4 Pro性能帕累托曲线，显示可实现**150+ TPS/用户**的交互式代理工作流。SemiAnalysis在**H200、MI355、B200、B300、GB200/300**上进行了Day-0基准测试。

---

### 3. [Hugging Face ML Intern - 开源CLI AI实习生](https://x.com/MillieMarconnni/status/2047639632859500691)
> Hugging Face推出**ML Intern**，一个开源的CLI“AI实习生”，专为ML工作设计。它可以研究论文、编写代码、运行实验、使用HF数据集/作业、搜索GitHub，并可迭代多达**300步**。同时，HF的**$9 Pro**订阅层被认为具有异常高的性价比。

---

### 4. [Hermes Agent v0.11.0 - 重写React TUI和插件系统](https://x.com/WesRoth/status/2047646749427216385)
> Nous/Hermes发布**Hermes Agent v0.11.0**，引入重写的React TUI、仪表板插件、主题系统、更多推理提供商、图像后端和QQBot支持。该版本同时支持**DeepSeek V4**和**GPT-5.5**。此外，一个使用**bubblewrap + cgroups v2**的原生Linux沙箱后端被发布，用于Deep Agents。

---

### 5. [Qwen 3.6 27B - 本地编码性能惊人](https://www.reddit.com/r/LocalLLaMA/comments/1steip4/qwen_36_27b_is_a_beast/)
> Qwen 3.6 27B在本地运行表现卓越。用户报告在**RTX 5090（24GB VRAM）** 上使用llama.cpp的q4_k_m量化运行良好。另一用户使用**PI Coding Agent**配合Qwen3.6 35B在**8GB VRAM+32GB RAM**的笔记本上实现**15-30 tokens/秒**。多位用户表示已取消IDE和Claude订阅。

---

### 6. [DeepSeek V4 Flash - 可在256GB Mac上运行](https://x.com/Prince_Canuma/status/2047685898163147125)
> DeepSeek V4 Flash被证明可在**256GB Mac**上运行，MLX量化版本也已发布。社区正在探索在更小RAM的Mac上运行的可能性。然而，重要提醒：**llama.cpp/Ollama/LM Studio不支持张量并行**，多GPU用户需转向vLLM。

---

### 7. [GPT-5.5 - 在Cursor、Copilot、Codex等平台立即可用](https://x.com/OpenAI/status/2047743592278745425)
> GPT-5.5发布后立即在**Cursor、GitHub Copilot、Codex/OpenAI API、OpenRouter、Perplexity、Devin、Droid、Fleet、Deep Agents**等平台上线。Cursor报告GPT-5.5在**CursorBench上以72.8%** 位居第一。Cline报告在**Terminal-Bench上以82.7**排名第一。

---

### 8. [DeepEP V2 / TileKernels - DeepSeek开源并行化工具](https://github.com/deepseek-ai/TileKernels)
> DeepSeek开源**DeepEP V2**（增强模型效率与准确性）和**TileKernels**（线性扩展并行化技术）。这些工具旨在优化大规模MoE模型的训练和推理。社区评论认为这些技术可能实现**线性扩展**——计算能力翻倍直接带来处理速度翻倍。

---

### 9. [Chappie - 四台Mac Mini M4 Pro组成的分布式AI系统](https://github.com/exo-explore/exo)
> 一位开发者使用**四台Mac Mini M4 Pro**构建了名为“Chappie”的分布式AI系统，组成**256GB统一内存、56 CPU核心、80 GPU核心、64神经引擎核心**的集群。系统使用**Exo**进行分布式推理，**Qdrant向量数据库**进行内存共享，可自主生成问题、阅读arXiv论文、开发新技能，并设有“委员会”评审模型进行质量控制。

---

### 10. [Atomic.Chat - 本地模型托管与比较平台](https://github.com/AtomicBot-ai/Atomic-Chat)
> Atomic.Chat提供了一个平台，用于在MacBook Pro M5 MAX上托管和比较不同模型。用户使用该平台对比了Qwen 3.6 35B（**72 TPS**）和27B（**18 TPS**）的编码性能，发现虽然35B更快，但27B在编码任务中产生更精确的结果。该平台支持多种模型和量化配置的比较。