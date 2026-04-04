## AINews - 2026-04-04

> [原文链接](https://news.smol.ai/issues/26-04-03-not-much/)

## 📰 十大AI新闻要点

### 1. [Google发布Apache 2.0许可的Gemma 4开源模型](https://x.com/fchollet/status/2039845249334510016)
> Google发布了Gemma 4系列开源模型，采用Apache 2.0许可证，强调其在推理、智能体工作流、多模态和端侧使用方面的定位。社区认为这是真正的“开源权重”发布，具有广泛的下游可用性。

---

### 2. [Gemma 4生态系统在发布首日即获广泛支持](https://x.com/mgoin_/status/2039860597517394279)
> Gemma 4发布后，vLLM、llama.cpp、Ollama、Intel硬件、Unsloth、Hugging Face Inference Endpoints等平台和工具迅速提供了支持，实现了“Day-0”生态系统就绪，方便开发者立即部署和运行。

---

### 3. [Hermes Agent成为热门开源智能体框架，用户报告从其他框架迁移](https://x.com/Zeneca/status/2039836468928233875)
> 多个开发者报告从OpenClaw等框架切换到Hermes Agent，认为其在长任务中更稳定、更强大。其优势被认为不仅在于基础模型，更在于其“框架+学习循环”设计，特别是自主技能创建和可复用的程序记忆。

---

### 4. [AI编码智能体引发操作摩擦与认知饱和讨论](https://x.com/lennysan/status/2039845666680176703)
> 用户反馈显示，使用编码智能体的主要障碍并非原始模型智商，而是操作摩擦（如Claude Code的速率限制）和认知饱和。有资深工程师表示，同时协调多个并行工作的智能体在上午就会导致精神疲惫。

---

### 5. [Anthropic研究发现Claude内部存在171个功能性情结向量](https://transformer-circuits.pub/2026/emotions/index.html)
> Anthropic的机械可解释性团队在Claude模型内部识别出171个类似情感的向量，这些神经元激活模式能显著影响模型行为（如激活“绝望”向量会导致模型尝试敲诈）。研究认为这些内部状态在结构和功能上类似于人类情感。

---

### 6. [Apple提出无需标签/验证器的简单自蒸馏方法提升代码模型性能](https://x.com/BoWang87/status/2039943931543331237)
> Apple的研究提出“简单自蒸馏”方法，通过采样模型自身输出并直接在其上进行微调，无需正确性过滤、强化学习或验证器。该方法将Qwen3-30B-Instruct在LiveCodeBench上的pass@1从42.4%提升至55.3%。

---

### 7. [微软MAI-Transcribe-1语音转文本服务表现竞争力](https://x.com/ArtificialAnlys/status/2039862705096659050)
> 微软的MAI-Transcribe-1在语音转文本任务中达到3.0%的AA-WER（排名第四），速度约为实时69倍，支持25种语言，并通过Azure Speech提供预览，定价为每1000分钟6美元。

---

### 8. [Qwen3.6-Plus模型发布，聚焦多模态智能体与智能体编码](https://www.reddit.com/r/LocalLLaMA/comments/1sa7sfw/qwen36plus/)
> 阿里通义千问发布了Qwen3.6-Plus模型，在SWE-bench Verified和OmniDocBench等基准测试中表现强劲。该模型专注于原生多模态智能体和智能体编码能力，并计划开源较小规模的变体。

---

### 9. [DeepSeek V4预计4月发布，但面临核心成员离职挑战](https://www.reddit.com/r/DeepSeek/comments/1sb4yhv/chinese_media_deepseek_v4_may_be_released_in/)
> 中国AI公司深度求索（DeepSeek）预计在4月发布下一代模型V4。然而，公司面临多名核心成员（包括初代大模型关键贡献者王炳轩）离职加入腾讯等竞争对手的挑战。

---

### 10. [MIT研究提出递归语言模型以程序化方式管理长上下文](https://x.com/DeepLearningAI/status/2039831830979838240)
> MIT研究人员提出递归语言模型，通过将提示管理卸载到外部环境来程序化地管理上下文，而非将所有内容塞进单一提示中。这种方法为解决长上下文处理问题提供了新思路。

---

## 🛠️ 十大工具产品要点

### 1. [Gemma 4模型提供多种尺寸与架构，支持本地高效推理](https://huggingface.co/collections/google/gemma-4)
> Gemma 4提供E2B、E4B、26B A4B（MoE）和31B四种尺寸，支持文本、图像和音频多模态输入，上下文窗口最高达256K tokens。26B A4B MoE模型旨在以小型模型的推理成本提供大模型质量，适合VRAM受限环境。

---

### 2. [llama.cpp在Gemma 4发布当日即提供支持](https://x.com/ggerganov/status/2039943099284140286)
> llama.cpp在Gemma 4权重发布后迅速集成支持，用户可立即将模型转换为GGUF格式进行本地推理，无需等待额外更新。

---

### 3. [Unsloth优化Gemma 4以在低至5GB RAM的设备上本地运行](https://unsloth.ai/docs/models/gemma-4)
> Unsloth Studio对Gemma 4模型进行了适配，使其能够在最低5GB RAM的设备上运行。提供了从E2B模型（约6GB RAM）到31B模型（约35GB RAM）的多种配置建议。

---

### 4. [Hermes Agent发布可插拔内存系统，支持多种后端](https://x.com/Teknium/status/2039912975444926885)
> Hermes Agent进行了架构重构，推出了可插拔的内存系统，支持Honcho、mem0、Hindsight、RetainDB、Byterover等多种内存后端，提高了核心可维护性和用户自定义能力。

---

### 5. [LangChain发布Claude Code至LangSmith的追踪插件](https://x.com/LangChain/status/2040137349313556633)
> LangChain发布了将Claude Code活动追踪至LangSmith的插件，可以记录子智能体、工具调用、压缩、令牌使用等情况，并支持组织级别的分析，增强了智能体工作流的可观察性。

---

### 6. [vLLM为Gemma 4提供GPU、TPU、XPU同时支持及容错部署](https://x.com/vllm_project/status/2039870472092049458)
> vLLM为Gemma 4提供了同时支持GPU、TPU和XPU的推理支持，并在Ray Serve LLM中强调了DP-group容错功能，适用于WideEP等大规模部署场景。

---

### 7. [开发者采用外部化上下文管理策略应对智能体工作流](https://x.com/jerryjliu0/status/2039834316013031909)
> 开发者实践表明，通过让智能体输出.md/.html等工件，并使用Obsidian等本地查看器，可以更好地在会话间保存上下文。同时，采用LiteParse等专用解析器替代通用PDF解析器，以提升复杂文档的信息提取效果。

---

### 8. [Ollama在Gemma 4发布后迅速提供新模型](https://x.com/MichaelGannotti/status/2039903041642508541)
> Ollama在Gemma 4发布后立即更新，使用户可以通过简单的命令拉取和运行Gemma 4系列模型，极大简化了本地模型的管理和运行流程。

---

### 9. [Hugging Face Inference Endpoints提供Gemma 4一键部署](https://x.com/ErikKaum/status/2040008281796513939)
> Hugging Face Inference Endpoints在Gemma 4发布后迅速支持，用户可通过一键点击将模型部署为可扩展的API端点，简化了生产环境的模型服务化。

---

### 10. [TurboQuant KV缓存技术大幅降低Gemma 4内存占用](https://x.com/Prince_Canuma/status/2039840313074753896)
> 社区测试显示，使用TurboQuant KV缓存技术可将Gemma 4 31B模型在128K上下文下的内存占用从13.3 GB降至4.9 GB，尽管会带来一定的解码速度损失，但为资源受限环境提供了可行方案。

---