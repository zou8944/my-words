## AINews - 2025-09-06

> [原文链接](https://news.smol.ai/issues/25-09-04-not-much/)

## 📰 十大AI新闻要点

### 1. [Google发布EmbeddingGemma-300M多语言嵌入模型](https://twitter.com/GoogleDeepMind/status/1963635422698856705)
> Google DeepMind推出308M参数的多语言嵌入模型，支持100+语言，在MTEB基准测试中排名500M参数以下开源模型第一。支持Matryoshka嵌入（输出维度768→128），量化后内存占用<200MB，EdgeTPU延迟<15ms，获得Hugging Face、Ollama、MLX等生态系统的即时支持。

---

### 2. [Hugging Face发布FineVision多模态数据集](https://twitter.com/lusxvr/status/1963609337546293448)
> 包含1730万图像、2430万样本、8890万对话轮次和95亿答案token的大规模VLM训练数据集，覆盖200+精选数据源。在10个基准测试中平均提升20%以上，新增GUI导航、指向和计数等能力。

---

### 3. [MiniCPM-V 4.5视频图像VLM发布](https://twitter.com/_akhaliq/status/1963587749400727980)
> 8B参数模型在OpenCompass 8个基准测试中平均得分77.0，声称超越GPT-4o-latest和Gemini-2.0 Pro。采用统一3D-Resampler和激进视频token压缩技术（96×压缩比），6帧448×448视频仅需64个token。

---

### 4. [OpenAI推出对话分支功能](https://twitter.com/OpenAI/status/1963697012014215181)
> ChatGPT新增原生对话分支探索功能，支持用户进行探索性工作流，该功能基于约100行代码的Responses API实现，发布后获得极高用户关注度（17.1k点赞）。

---

### 5. [Perplexity Comet广泛推送](https://twitter.com/AravSrinivas/status/1963633205351010795)
> Perplexity Comet向"超过100万用户"开放访问，移动端预购已上线，新版iOS应用流畅渲染表格、Markdown和中间步骤，标志着大规模AI搜索产品的商业化推进。

---

### 6. [微软VibeVoice仓库突然下架](https://www.reddit.com/r/LocalLLaMA/comments/1n7zk45/vibevoice_rip_what_do_you_think/)
> 微软突然删除官方VibeVoice GitHub仓库并从Hugging Face移除VibeVoice-Large和VibeVoice-Large-Preview模型，原因未知。社区镜像仍存在于ModelScope，MIT许可证允许继续分发已发布版本。

---

### 7. [深度优化器基准研究发布](https://twitter.com/konstmish/status/1963535545721917725)
> 斯坦福综合研究比较Muon、Soap、Mars、Sophia等优化器在0.1B-1.2B模型规模的表现。研究发现：经过仔细调优后，在大规模模型上相对AdamW的加速效果减弱（约10%），但基于矩阵的方法在小规模模型中仍领先。

---

### 8. [LangGraph生产级智能体运行时设计深度解析](https://twitter.com/LangChainAI/status/1963646974315606428)
> 详细阐述构建生产级智能体运行时的关键设计原则：最小抽象、结构化执行/状态、恢复/持久性，以及匹配实际运维需求的控制界面，为团队部署生产环境智能体提供重要参考。

---

### 9. [DeepMind深度循环整形技术登顶《科学》杂志](https://twitter.com/GoogleDeepMind/status/1963664018515849285)
> 该技术改进LIGO干涉仪控制，将噪声降低30-100倍，消除了LIGO最不稳定环路作为重要噪声源的问题，展示了AI在实验物理学领域的重大突破。

---

### 10. [Ilya Sutskever称赞革命性突破](https://twitter.com/ilyasut/status/1963627458244350015)
> OpenAI联合创始人Ilya Sutskever发布推文称"这是我见过的最革命性的突破之一"，获得19.2k点赞，引发业界对AI技术重大突破的广泛猜测和关注。

---

## 🛠️ 十大工具产品要点

### 1. [EmbeddingGemma-300M本地部署方案](https://huggingface.co/unsloth/embeddinggemma-300m-GGUF)
> 社区提供GGUF量化版本（Q4_0、Q8_0、BF16），支持llama.cpp本地推理，Q4_0最小化内存占用，Q8_0平衡尺寸与精度，BF16保持最高质量，同时计划发布RAG微调和基准测试笔记。

---

### 2. [Jina AI代码嵌入模型发布](https://twitter.com/JinaAI_/status/1963637135439007824)
> 推出0.5B/1.5B参数代码专用嵌入模型，支持1-4bit GGUF量化，在15+语言和5个任务（nl2code、code2code等）上声称达到SOTA检索性能，基于Qwen2.5-Coder在5.5T token上预训练。

---

### 3. [UI-TARS-2多模态智能体系统](https://twitter.com/TsingYoga/status/1963629621326614940)
> 统一GUI/手机/浏览器/终端/工具使用智能体，在OSWorld 47.5、WindowsAgentArena 50.6等基准测试中表现优异，支持混合动作流（点击、终端、API调用组合）。

---

### 4. [Atla智能体失败分析平台](https://twitter.com/Atla_AI/status/1963586200305836264)
> 自动发现重复失败模式并为智能体系统提供针对性修复方案，帮助提升智能体系统的可靠性和性能。

---

### 5. [Groq Compound智能体系统正式发布](https://twitter.com/GroqInc/status/1963635205899710798)
> 经过500万+请求测试后正式GA，提供高性能智能体系统解决方案，支持大规模部署和生产环境使用。

---

### 6. [Gadio MCP服务器一键部署](https://twitter.com/Gradio/status/1963636954999754955)
> 新增单命令将MCP服务器部署到Google Cloud的功能，简化模型部署流程，提升开发效率。

---

### 7. [Together AI新增欧洲GPU区域](https://twitter.com/togethercompute/status/1963498998720872686)
> 在瑞典新增GPU区域，提供更低延迟和数据驻留解决方案，满足欧洲用户的合规需求。

---

### 8. [SkyPilot多云部署方案](https://twitter.com/skypilot_org/status/1963637217055646139)
> 展示从SLURM迁移到多云架构，实现K8s级可靠性的快速开发周期，支持更灵活的算力调度。

---

### 9. [HF MCP服务器新增OpenAI Codex CLI支持](https://twitter.com/reach_vb/status/1963599978909008321)
> 扩展模型协作协议功能，增加对OpenAI Codex命令行界面的支持，提升开发工具链的完整性。

---

### 10. [slime RL框架大幅优化权重更新](https://twitter.com/ZhihuFrontier/status/1963532501336695282)
> 将Qwen3-30B-A3B权重更新时间从60秒缩短至7秒，支持GLM-4.5-355B-A32B FP8更新约100秒完成，正在进行异步/零冗余优化，寻求合作机会。

---