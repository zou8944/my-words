## AINews - 2025-09-08

> [原文链接](https://news.smol.ai/issues/25-09-05-1t-models/)

## 📰 十大AI新闻要点

### 1. [Qwen 3 Max发布1T参数模型](https://x.com/Alibaba_Qwen/status/1963991502440562976)
> 阿里巴巴推出迄今为止最大的模型Qwen 3 Max，参数规模超过1万亿，专注于代理任务行为，现已通过Qwen Chat、阿里云API和OpenRouter提供。社区反应认为这是"美国级前沿模型"，具有竞争力的定价和吞吐量。

---

### 2. [Kimi K2-0905发布256K上下文升级](https://twitter.com/bigeagle_xd/status/1963802450374369722)
> Moonshot AI发布Kimi K2-0905，上下文长度翻倍至256K，改进了编码和工具调用能力，优化了与代理框架的集成。已在多个平台部署，包括Hugging Face、Together AI、vLLM等，社区强调代理任务需要超长上下文来保证稳定性。

---

### 3. [Meta推出Set Block Decoding技术](https://twitter.com/arankomatsuzaki/status/1963817987506643350)
> Meta的Set Block Decoding技术可并行采样多个未来token，减少3-5倍前向传递，无需架构更改且兼容KV缓存。训练模型在下一token预测上匹配标准NTP性能。

---

### 4. [微软rStar2-Agent-14B达到前沿数学水平](https://twitter.com/omarsar0/status/1964045125115662847)
> 微软使用代理强化学习在仅510步内使rStar2-Agent-14B达到前沿数学水平（AIME24 80.6分，AIME25 69.8分），具有更短、更可验证的思维链。

---

### 5. [OpenAI与Broadcom合作生产自研AI芯片](https://www.reuters.com/business/openai-set-start-mass-production-its-own-ai-chips-with-broadcom-ft-reports-2025-09-05/)
> OpenAI将与Broadcom合作开始大规模生产自研AI加速器，旨在减少对Nvidia GPU的依赖，降低训练和推理成本，确保供应链安全。

---

### 6. [Together AI和Baseten各完成1.5亿美元D轮融资](https://twitter.com/tuhinone/status/1963945981382451488)
> Together AI宣布由BOND领投的1.5亿美元D轮融资，用于扩展推理基础设施；Baseten也完成1.5亿美元D轮融资，推出性能工作和EmbeddingGemma支持。

---

### 7. [ChatGPT新增对话分支功能](https://twitter.com/gdb/status/1963780952187965746)
> OpenAI为ChatGPT添加对话分支支持功能，允许用户创建不同的对话路径，Sam Altman称这是"非常受欢迎的功能"。

---

### 8. [Google发布EmbeddingGemma嵌入模型](https://twitter.com/basetenco/status/1963724754315284720)
> Google开源EmbeddingGemma多语言嵌入编码器，报告显示在M2 Max上约80分钟可嵌入140万文档，质量优于旧的付费大模型，支持完全离线检索。

---

### 9. [ROCm在PyTorch中出现质量回归](https://twitter.com/SemiAnalysis_/status/1963708743218339907)
> 分析显示PyTorch中ROCm专属跳过/禁用测试数量增加（各超过200个），核心transformer操作（如注意力）已被禁用数月，影响开发者信任度。

---

### 10. [Salesforce因AI效率裁员4000人](https://www.cnbc.com/2025/09/02/salesforce-ceo-confirms-4000-layoffs-because-i-need-less-heads-with-ai.html)
> Salesforce CEO确认因AI驱动的Agentforce系统效率提升，裁减约4000个客户支持岗位，支持人员从9000人减少至5000人，AI reportedly处理高达50%的工作量。

---

## 🛠️ 十大工具产品要点

### 1. [Kimi K2-0905多平台部署支持](https://twitter.com/togethercompute/status/1963806032548843865)
> Kimi K2-0905已在Hugging Face、Together AI、vLLM、LMSYS SGLang runtime、Groq等多个平台部署，Groq即时推理达到200+ tokens/秒，价格1.50美元/百万tokens。

---

### 2. [OpenAI Responses API深度解析](https://twitter.com/prashantmital/status/1963801236391772372)
> OpenAI Responses API获得深度解释，AI SDK v5现在默认将OpenAI提供商设置为Responses（Completions仍可用），改进持续对话中的"思维链保持"。

---

### 3. [LlamaIndex SemTools处理千篇论文](https://twitter.com/llama_index/status/1964009128973783135)
> LlamaIndex展示SemTools使用UNIX工具和模糊语义搜索处理1000篇arXiv论文，CLI优先代理加语义搜索在文档任务上优于临时RAG。

---

### 4. [vLLM支持Kimi K2部署](https://twitter.com/vllm_project/status/1963805972352188895)
> vLLM发布Kimi K2部署指南，同时宣布在多伦多举办分布式推理、spec decode和FlashInfer的meetup活动。

---

### 5. [SQLite-vec + EmbeddingGemma离线检索方案](https://twitter.com/_philschmid/status/1963952204970078579)
> SQLite-vec结合EmbeddingGemma可在各种语言和运行时中完全离线运行，为设备上检索提供便捷解决方案。

---

### 6. [Nunchaku v1.0.0发布](https://github.com/nunchaku-tech/nunchaku/releases/tag/v1.0.0)
> Nunchaku v1.0.0后端从C迁移到Python，添加异步CPU卸载，使Qwen-Image扩散在约3GiB VRAM中运行，无性能损失，提供新wheel和ComfyUI节点。

---

### 7. [THUDM slime提供清洁rollout抽象](https://twitter.com/Zai_org/status/1963836843633332457)
> THUDM的slime提供集成工具调用和状态转换的清洁rollout抽象，减少代理强化学习实验中的胶水代码。

---

### 8. [OpenRouter提供Qwen 3 Max接入](https://openrouter.ai/qwen/qwen3-max)
> OpenRouter现在提供Qwen 3 Max模型接入，定价按上下文长度分层：输入1.2美元（≤128K）/3美元（>128K），输出6美元（≤128K）/15美元（>128K）。

---

### 9. [LMSYS SGLang runtime实现60-100+ TPS](https://twitter.com/lmsysorg/status/1963806184747491717)
> LMSYS SGLang runtime为Kimi K2提供支持，实现60-100+ TPS（每秒处理事务数）的高吞吐量性能。

---

### 10. [Cline集成Kimi K2](https://twitter.com/cline/status/1963804927584833725)
> Cline宣布集成Kimi K2，优化代理框架的协同工作，提升工具编排和任务执行的稳定性。

---