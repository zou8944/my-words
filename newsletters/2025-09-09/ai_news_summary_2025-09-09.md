## AINews - 2025-09-09

> [原文链接](https://news.smol.ai/issues/25-09-05-1t-models/)

## 📰 十大AI新闻要点

### 1. [Qwen 3 Max发布1T参数模型](https://x.com/Alibaba_Qwen/status/1963991502440562976)
> 阿里巴巴推出首个1T参数规模的Qwen 3 Max模型，专注于智能体任务，支持长达128K+上下文，现已在Qwen Chat、阿里云API和OpenRouter平台上线，定价接近Claude/GPT等前沿模型水平。

---

### 2. [Kimi K2-0905升级256K上下文](https://twitter.com/bigeagle_xd/status/1963802450374369722)
> Moonshot AI发布Kimi K2-0905开源模型，上下文长度翻倍至256K，显著提升代码生成和工具调用能力，并优化与Cline、Claude Code等智能体框架的集成，已在Hugging Face、Together AI、vLLM等平台部署。

---

### 3. [Meta推出Set Block Decoding技术](https://twitter.com/arankomatsuzaki/status/1963817987506643350)
> Meta的新解码技术SBD可并行采样多个未来token，无需架构修改即实现3-5倍前向传递加速，且保持KV缓存兼容性，在next-token预测任务上匹配标准NTP性能。

---

### 4. [微软rStar2-Agent-14B实现数学突破](https://twitter.com/omarsar0/status/1964045125115662847)
> 微软通过智能体强化学习在仅510步训练后，使14B模型在AIME24和AIME25数学竞赛中分别达到80.6和69.8分，采用更短且可验证的思维链，证明小模型通过专项训练可达到前沿水平。

---

### 5. [OpenAI与博通合作自研AI芯片](https://www.reuters.com/business/openai-set-start-mass-production-its-own-ai-chips-with-broadcom-ft-reports-2025-09-05/)
> OpenAI启动与博通合作的自研AI芯片量产计划，旨在降低对Nvidia GPU的依赖并减少训练/推理成本，此举类似谷歌TPU战略，但面临高额NRE成本和软件栈优化挑战。

---

### 6. [Together AI和Baseten各获1.5亿美元D轮融资](https://twitter.com/tuhinone/status/1963945981382451488)
> Together AI由BOND领投1.5亿美元用于扩展推理基础设施，Baseten同期也获1.5亿美元融资，重点支持EmbeddingGemma等模型部署，反映推理基础设施市场持续升温。

---

### 7. [PyTorch ROCm支持出现严重回归](https://twitter.com/SemiAnalysis_/status/1963708743218339907)
> 分析显示PyTorch中ROCm专属测试被跳过/禁用的数量超200项且自2025年6月以来持续增加，甚至核心transformer操作（如注意力机制）已被禁用数月，影响开发者信任，AMD已优先处理修复。

---

### 8. [Google开源EmbeddingGemma本地化部署突破](https://twitter.com/basetenco/status/1963724754315284720)
> EmbeddingGemma作为300M参数的多语言嵌入模型，在M2 Max上80分钟内可处理140万份文档，质量优于旧版大型付费模型，且结合SQLite-vec实现完全离线检索。

---

### 9. [混合后训练技术HPT超越基线表现](https://twitter.com/omarsar0/status/1963971173735448858)
> 研究提出统一视角显示SFT和RL优化相同奖励-KL目标，混合后训练（HPT）通过简单性能反馈在两者间切换，在多规模和模型家族中一致超越强基线。

---

### 10. [智能体评估框架面临实践挑战](https://twitter.com/swyx/status/1963725773355057249)
> 分析指出许多顶级代码智能体团队未采用正式评估而依赖内部试用和错误分析，呼吁开发更丰富的长周期能力评估（如数月任务、协议复制）和特定领域工作流测试。

---

## 🛠️ 十大工具产品要点

### 1. [Kimi K2-0905多平台集成](https://twitter.com/togethercompute/status/1963806032548843865)
> Kimi K2-0905已全面支持Hugging Face权重、Together AI云服务、vLLM部署指南、LMSYS SGLang运行时（60-100+ TPS）、Groq即时推理（200+ T/s，1.50美元/百万token）及Cline集成，提供多样化部署选择。

---

### 2. [OpenRouter上线Qwen 3 Max](https://openrouter.ai/qwen/qwen3-max)
> Qwen 3 Max在OpenRouter提供分级定价：输入≤128K为1.2美元，＞128K为3美元；输出≤128K为6美元，＞128K为15美元，直接对标前沿模型API价格策略。

---

### 3. [LlamaIndex SemTools处理千篇论文](https://twitter.com/llama_index/status/1964009128973783135)
> SemTools结合UNIX工具和模糊语义搜索，可处理1000篇arXiv论文，在文档任务中超越临时RAG方案，提供CLI优先的智能体操作体验。

---

### 4. [vLLM支持Kimi K2部署](https://twitter.com/vllm_project/status/1963805972352188895)
> vLLM发布Kimi K2专项部署指南，优化分布式推理和FlashInfer集成，同时宣布在多伦多举办相关技术见面会。

---

### 5. [Nunchaku v1.0迁移Python后端](https://github.com/nunchaku-tech/nunchaku/releases/tag/v1.0.0)
> Nunchaku v1.0将后端从C迁移至Python，增加异步CPU卸载，使Qwen-Image扩散模型在3GiB VRAM下运行无性能损失，并提供ComfyUI节点和4位量化模型。

---

### 6. [OpenAI Responses API详解](https://twitter.com/prashantmital/status/1963801236391772372)
> OpenAI Responses API获深度解读，AI SDK v5默认使用该提供商（Completions仍可用），但开发者指出其在实际无状态使用和上下文移植中存在复杂性。

---

### 7. [SQLite-vec离线检索方案](https://twitter.com/_philschmid/status/1963952204970078579)
> SQLite-vec结合EmbeddingGemma实现全离线跨语言/运行时检索，为边缘设备提供轻量级检索解决方案，突破网络依赖限制。

---

### 8. [THUDM slime简化智能体RL实验](https://twitter.com/Zai_org/status/1963836843633332457)
> slime提供清洁的rollout抽象，集成工具调用和状态转换，减少智能体强化学习实验中的胶水代码，提升开发效率。

---

### 9. [LM Studio优化Apple Silicon支持](https://github.com/ml-explore/mlx)
> LM Studio利用Apple MLX栈在Apple Silicon上提供更佳性能和可靠性，推荐与Docker中的Open WebUI结合实现认证和网络搜索功能。

---

### 10. [Codex CLI与Cursor IDE功能增强](https://twitter.com/dkundel/status/1963834846394147125)
> Codex CLI/IDE持续快速迭代，GPT-5 Pro版本在解决复杂工程问题时展现深度推理优势，开发者反馈“更智能比更快速更重要”成为核心体验。

---