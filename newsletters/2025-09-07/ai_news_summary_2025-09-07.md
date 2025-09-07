## AINews - 2025-09-07

> [原文链接](https://news.smol.ai/issues/25-09-05-1t-models/)

## 📰 十大AI新闻要点

### 1. [Qwen 3 Max发布1T参数模型](https://x.com/Alibaba_Qwen/status/1963991502440562976)
> 阿里巴巴推出首个1T参数模型Qwen 3 Max，专注于智能体任务，在对话质量、指令遵循和智能体行为方面显著超越前代Qwen模型。该模型通过Qwen Chat、阿里云API和OpenRouter提供，定价接近Claude/GPT等前沿模型水平。

---

### 2. [Kimi K2-0905升级256K上下文](https://twitter.com/bigeagle_xd/status/1963802450374369722)
> Moonshot AI发布Kimi K2-0905开源模型，上下文长度翻倍至256K，显著提升代码生成和工具调用能力，并优化与智能体框架（Cline、Claude Code、Roo）的集成。已在Hugging Face、Together AI、vLLM等多个平台部署。

---

### 3. [Meta推出Set Block Decoding技术](https://twitter.com/arankomatsuzaki/status/1963817987506643350)
> Meta的Set Block Decoding（SBD）技术可并行采样多个未来token，在不改变架构的情况下将前向传递次数减少3-5倍，且保持KV缓存兼容性。训练模型在下一token预测任务上匹配标准NTP性能。

---

### 4. [微软rStar2-Agent-14B实现前沿数学能力](https://twitter.com/omarsar0/status/1964045125115662847)
> 微软通过智能体强化学习在仅510步训练后，使14B参数模型在AIME24和AIME25数学竞赛中分别达到80.6和69.8分，实现前沿数学能力。模型生成更短、更可验证的思维链。

---

### 5. [OpenAI与Broadcom合作自研AI芯片](https://www.reuters.com/business/openai-set-start-mass-production-its-own-ai-chips-with-broadcom-ft-reports-2025-09-05/)
> OpenAI与Broadcom合作开始量产自研AI加速器，旨在减少对Nvidia GPU的依赖并降低训练/推理成本。此举模仿谷歌TPU策略，但面临高额NRE成本、制造良率和软件栈优化等风险。

---

### 6. [Together AI和Baseten各获1.5亿美元D轮融资](https://twitter.com/tuhinone/status/1963945981382451488)
> Together AI宣布由BOND领投的1.5亿美元D轮融资，用于扩展推理基础设施；Baseten同样获得1.5亿美元D轮融资，用于性能优化和EmbeddingGemma支持。

---

### 7. [PyTorch中ROCm质量回归问题](https://twitter.com/SemiAnalysis_/status/1963708743218339907)
> 分析显示PyTorch中ROCm专属跳过/禁用测试数量净增（自2025年6月以来各超200个），甚至核心transformer操作（如注意力机制）已被禁用数月，损害开发者信任。AMD领导层已重新优先处理修复。

---

### 8. [OpenAI推出对话分支功能](https://twitter.com/gdb/status/1963780952187965746)
> ChatGPT新增对话分支功能，允许用户探索不同对话路径。OpenAI的Responses API获得深度解读，AI SDK v5默认将OpenAI提供程序设置为Responses（Completions仍可用）。

---

### 9. [Google开源EmbeddingGemma本地嵌入模型](https://twitter.com/basetenco/status/1963724754315284720)
> Google开源EmbeddingGemma多语言嵌入编码器（300M参数），支持本地运行。报告显示在M2 Max上约80分钟嵌入140万份文档，免费且质量优于旧有大型付费模型。

---

### 10. [Salesforce因AI效率裁员4000人](https://www.cnbc.com/2025/09/02/salesforce-ceo-confirms-4000-layoffs-because-i-need-less-heads-with-ai.html)
> Salesforce CEO确认因AI驱动的Agentforce系统效率提升，裁员约4000名客户支持人员（从9000人减至5000人）。内部称AI处理高达50%的工作量，但评论质疑此举是后疫情过度招聘调整的借口。

---

## 🛠️ 十大工具产品要点

### 1. [Kimi K2-0905多平台部署支持](https://twitter.com/togethercompute/status/1963806032548843865)
> Kimi K2-0905已在Hugging Face、Together AI、vLLM、LMSYS SGLang runtime（60-100+ TPS）、Groq（200+ T/s，1.50美元/M token）和Cline等多个平台部署，提供全面推理支持。

---

### 2. [Qwen 3 Max通过OpenRouter提供](https://twitter.com/Alibaba_Qwen/status/1964004112149754091)
> Qwen 3 Max在OpenRouter上提供分级定价：输入≤128K上下文1.2美元，>128K上下文3美元；输出≤128K上下文6美元，>128K上下文15美元，支持超长上下文处理。

---

### 3. [LlamaIndex SemTools处理千篇论文](https://twitter.com/llama_index/status/1964009128973783135)
> LlamaIndex的SemTools结合UNIX工具和模糊语义搜索，可处理1000篇arXiv论文，在文档任务中超越临时RAG方案，提供高效语义检索能力。

---

### 4. [THUDM slime简化智能体RL实验](https://twitter.com/Zai_org/status/1963836843633332457)
> THUDM的slime提供简洁的rollout抽象，集成工具调用和状态转换，减少智能体强化学习实验中的胶水代码，提升实验效率。

---

### 5. [SQLite-vec + EmbeddingGemma离线检索](https://twitter.com/_philschmid/status/1963952204970078579)
> SQLite-vec结合EmbeddingGemma支持全离线跨语言/运行时检索，无需网络连接，为本地应用提供高效嵌入检索解决方案。

---

### 6. [Nunchaku v1.0.0发布低VRAM扩散推理](https://github.com/nunchaku-tech/nunchaku/releases/tag/v1.0.0)
> Nunchaku v1.0.0后端从C迁移至Python，添加异步CPU卸载，使Qwen-Image扩散在约3 GiB VRAM中运行且无性能损失。提供新wheel和ComfyUI节点。

---

### 7. [OpenAI Responses API详解](https://twitter.com/prashantmital/status/1963801236391772372)
> OpenAI Responses API获得深度解读，澄清其并非解锁更高模型智能，而是构建GPT-5级智能体的关键。OpenRouter多数OpenAI模型使用此API。

---

### 8. [LM Studio与MLX后端优化Apple Silicon性能](https://github.com/ml-explore/mlx)
> LM Studio使用Apple的MLX后端在Apple Silicon上提供更好可靠性和性能，优于其他选项，适合本地LLM推理优化。

---

### 9. [vLLM支持Kimi K2部署](https://twitter.com/vllm_project/status/1963805972352188895)
> vLLM已支持Kimi K2部署，提供分布式推理、spec decode和FlashInfer优化，同时宣布多伦多见面会讨论这些技术。

---

### 10. [Claude Code与Kimi K2-0905集成提示模板](https://gist.github.com/karminski/52a72d4726128c10a266bfb8270fe632)
> 社区提供Kimi K2-0905与Claude Code集成的具体提示模板（Gist链接），标准化系统指令和I/O格式，便于任务评估和演示复制。

---