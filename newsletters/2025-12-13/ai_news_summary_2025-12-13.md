## AINews - 2025-12-13

> [原文链接](https://news.smol.ai/issues/25-12-11-gpt-52/)

## 📰 十大AI新闻要点

### 1. [OpenAI发布GPT-5.2，庆祝成立十周年](https://openai.com/index/introducing-gpt-5-2/)
> OpenAI在成立十周年之际发布了GPT-5.2模型系列（包括Instant/Thinking/Pro）。该版本带来了全面的性能提升，特别是在科学推理、知识工作和经济价值任务（GDPval）上表现突出，知识截止日期更新至2025年8月31日。API定价大幅上调，输入/输出价格分别上涨40%。

---

### 2. [GPT-5.2在关键基准测试中表现强劲，但存在局限性](https://twitter.com/arcprize/status/1999182732845547795)
> 根据评测，GPT-5.2 Pro (X-High)在ARC-AGI-1上达到90.5%的准确率，在GDPval任务上以超过专家11倍的速度和低于1%的成本完成工作。然而，在SWE-bench等编码基准测试中，其表现落后于Claude Opus 4.5，且存在工具调用和安全评估提升有限的问题。

---

### 3. [迪士尼与OpenAI达成多年内容合作协议](https://twitter.com/TheRealAdamG/status/1999118075879129140)
> 迪士尼与OpenAI签署了一项为期多年的内容协议，将使用Sora视频生成器以及图像生成技术，在迪士尼设定的护栏下，创作包含迪士尼、皮克斯、漫威、星球大战等200多个角色的内容。生成的AI视频将在Disney+上出现。

---

### 4. [Google推出统一的Interactions API及首个代理“Gemini Deep Research”](https://twitter.com/GoogleDeepMind/status/1999165701811015990)
> Google发布了统一的Interactions API，用于访问模型和代理，支持服务器端状态、后台执行和MCP。同时推出了首个代理“Gemini Deep Research”，并在DeepSearchQA基准上取得了先进成果。Google还开源了DeepSearchQA以评估深度网络搜索代理。

---

### 5. [智谱AI开源移动端智能体框架AutoGLM](https://twitter.com/Zai_org/status/1999118106543919203)
> 智谱AI开源了AutoGLM，这是一个能够理解手机屏幕并执行自主操作的多模态语言模型（VLM）。模型权重采用MIT许可，代码采用Apache-2.0许可，旨在让“每部手机都成为AI手机”。

---

### 6. [Google DeepMind宣布在英国建立首个“自动化研究实验室”](https://twitter.com/demishassabis/status/1999111337151013326)
> Google DeepMind宣布与英国政府合作，将于2026年在英国建立首个“自动化研究实验室”。该合作还包括优先获取AI-for-Science模型、合作开发教育工具、与AI安全研究所进行安全研究等内容。

---

### 7. [Cohere发布Rerank 4，具备自学习能力](https://twitter.com/cohere/status/1999162791966745079)
> Cohere发布了新一代重排序模型Rerank 4，具备顶级的关联性排名能力和自学习功能，可以在没有标注数据的情况下自适应特定领域。该模型已在Cohere平台、AWS SageMaker和Azure Foundry上提供。

---

### 8. [研究揭示多智能体系统（MAS）的扩展定律](https://twitter.com/_philschmid/status/1998957966343446844)
> 一项由Google和MIT进行的研究评估了180种多智能体配置，发现：对于可并行任务，集中式协调能带来+80.9%的性能提升；一旦单智能体基线准确率超过~45%，增加更多智能体通常会产生负面影响。研究强调应根据任务可分解性和工具复杂性来匹配架构，而非默认增加智能体数量。

---

### 9. [Cursor和VS Code推出新的AI辅助开发功能](https://twitter.com/cursor_ai/status/1999147953609736464)
> Cursor发布了“在IDE内设计”功能，允许用户可视化选择和修改UI并自动生成代码。VS Code则增加了“无缝智能体协作”功能，并预告了年终版本更新。这些更新旨在提升开发者的AI辅助工作流体验。

---

### 10. [Mistral AI在华沙开设新办公室并扩大招聘](https://twitter.com/GuillaumeLample/status/1999136182475579591)
> Mistral AI宣布在波兰华沙开设新办公室，并正在招聘AI科学家和研究工程师。此举被视为该公司在欧洲扩大业务和人才储备的重要一步。

---

## 🛠️ 十大工具产品要点

### 1. [GPT-5.2 API定价与集成](https://twitter.com/OpenAIDevs/status/1999184812389859689)
> GPT-5.2 API定价为输入token $1.75/M，输出token $14/M，并提供90%的缓存折扣。模型已集成到ChatGPT、Microsoft Copilot、VS Code、Cursor和Perplexity等平台中。

---

### 2. [Unsloth发布3倍速训练打包技术](https://docs.unsloth.ai/new/3x-faster-training-packing)
> Unsloth发布了新的训练打包技术，声称比之前的版本快3倍，比FA3快10倍，并使得在仅3.9GB VRAM上训练Qwen3-4B模型成为可能，大幅降低了微调门槛。

---

### 3. [llama.cpp支持实时模型切换](https://huggingface.co/blog/ggml-org/model-management-in-llamacpp)
> llama.cpp的最新更新引入了路由器模式，支持动态加载、卸载和切换模型，而无需重启服务器。该功能采用多进程架构来隔离模型崩溃，提高了稳定性和工作流灵活性。

---

### 4. [LangChain推出智能体调试工具“Polly”](https://twitter.com/hwchase17/status/1998976734692253724)
> LangChain在LangSmith中推出了名为“Polly”的智能体工程师工具，提供轨迹调试、线程分析和提示编辑功能。同时发布了`langsmith-fetch`库，用于将轨迹数据反馈给编码智能体。

---

### 5. [Qdrant的ACORN技术提升向量数据库过滤鲁棒性](https://twitter.com/qdrant_engine/status/1998976425018405322)
> Qdrant的ACORN技术通过增强HNSW索引，引入第二跳探索机制，避免了在严格过滤条件下出现“零结果”的问题，从而恢复了混合（向量+元数据）搜索的召回率。

---

### 6. [基于WebGPU的本地全栈语音聊天应用](https://huggingface.co/spaces/RickRossTN/ai-voice-chat)
> 一个Hugging Face Space演示了完全在浏览器内运行的AI语音聊天应用，利用WebGPU本地执行语音识别（STT）、语音活动检测（VAD）、文本转语音（TTS）和大语言模型（LLM）推理，无需调用任何第三方API，注重隐私。

---

### 7. [GLM-ASR Nano挑战Whisper](https://huggingface.co/spaces/YatharthS/GLM-ASR-Nano)
> 智谱推出的GLM-ASR Nano语音识别模型被社区认为是“SOTA”，并在演示中表现优于OpenAI的Whisper模型，展示了在轻量级语音识别任务上的竞争力。

---

### 8. [Hugging Face TGI进入维护期，推荐vLLM和SGLang](https://twitter.com/LysandreJik/status/1999137874378125436)
> Hugging Face的Text Generation Inference（TGI）项目已进入维护模式，官方推荐用户转向vLLM、SGLang以及llama.cpp/MLX等本地推理引擎，标志着开源模型服务栈的演变。

---

### 9. [SkyPilot v0.11瞄准企业级千卡GPU集群管理](https://twitter.com/skypilot_org/status/1999167910179463678)
> SkyPilot发布了v0.11版本，专注于为企业级规模的上千个GPU集群提供集群管理解决方案，旨在简化大规模AI训练和推理任务的基础设施部署。

---

### 10. [Mistral Vibe CLI支持200K上下文窗口](https://www.reddit.com/r/LocalLLaMA/comments/1pjw7rj/mistrals_vibe_cli_now_supports_a_200k_token/)
> Mistral的Vibe CLI通过简单的配置更新，将支持的上下文窗口从100K令牌提升至200K令牌。不过，社区讨论指出，许多模型在超过100K令牌后的实际性能仍有待观察。