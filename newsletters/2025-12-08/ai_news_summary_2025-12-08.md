## AINews - 2025-12-08

> [原文链接](https://news.smol.ai/issues/25-12-05-not-much/)

## 📰 十大AI新闻要点

### 1. [vLLM 0.12.0发布，支持DeepSeek-V3.2“思考”模式](https://twitter.com/vllm_project/status/1996947370588946861)
> vLLM发布了0.12.0版本，包含多项重大更新：为DeepSeek-V3.2的“思考”模式提供了优化的推理方案（包括正确的tokenizer和工具调用解析器），新增了实验性的GPU Model Runner V2（支持GPU持久化块表和Triton原生采样器），为长上下文预填充奠定了基础，并改进了EAGLE推测解码和多种量化方案（NVFP4/W4A8/AWQ）。新版本要求PyTorch 2.9.0 + CUDA 12.9。

---

### 2. [NVIDIA推出CUDA Tile，革新GPU编程范式](https://twitter.com/TheTuringPost/status/1997096340611019089)
> NVIDIA推出了CUDA Tile IR和cuTile Python库，将GPU编程从线程级的SIMT范式转向基于“Tile”的核函数。这种新范式能更好地映射到Tensor Cores和TMA（Tensor Memory Accelerator），旨在实现跨GPU世代的向前兼容性能。目前该工具主要面向Blackwell级GPU，对现有硬件的可移植性有限。

---

### 3. [Hugging Face Transformers v5 RC引入多模态“任意到任意”管道](https://twitter.com/mervenoyann/status/1996908863673737450)
> Hugging Face发布了Transformers v5的候选版本，引入了`AutoModelForMultimodalLM`和一个“任意到任意”的管道，支持两种或更多种输入和输出模态的组合（例如，Gemma3n支持所有模态到文本的转换，Qwen3-Omni支持文本+音频输入）。

---

### 4. [Kling Video 2.6成为首个支持原生同步音频的模型](https://twitter.com/arena/status/1996744741564961206)
> 昆仑万维的Kling Video 2.6模型在Video Arena上线，这是其首个支持原生、同步音频（包括语音、音效和环境音）生成的视频模型。同时，Kling O1的“元素/主体库”功能增加了持久的主体记忆和一致性，并推出了前后对比模板。

---

### 5. [阿里发布Qwen3-TTS，支持49+种声音和10种语言](https://twitter.com/Alibaba_Qwen/status/1996947806138126547)
> 阿里巴巴发布了Qwen3-TTS（11-27版本），提供超过49种声音、10种语言及多种中文方言，拥有高度自然的韵律。该模型提供了实时和离线API，并在Hugging Face和ModelScope上提供了演示。

---

### 6. [OpenRouter数据显示推理模型使用量超50%，中文闭源模型流量激增](https://twitter.com/scaling01/status/1996976986577584320)
> 根据OpenRouter的最新研究和数据看板，推理风格模型（如o1）的使用量在发布后不到一年内已超过其总token使用量的50%。同时，中文训练的闭源模型（如DeepSeek、Qwen3、Kimi K2、GLM）占据了相当大的流量份额，而开源模型的token使用量趋于平稳。

---

### 7. [FLUX.2 [dev]登顶开源文生图榜单，并发布Apache-2.0商业版本](https://twitter.com/ArtificialAnlys/status/1996801917196841345)
> Black Forest Labs的FLUX.2 [dev]在Artificial Analysis图像竞技场中，位列开源权重文生图模型榜首，并在图像编辑榜单中排名第二。该权重采用非商业开发许可证发布。同时，团队宣布了采用Apache-2.0许可证的FLUX.2 [klein]版本，可供商业使用。

---

### 8. [生产环境Agent研究：生产力提升显著，但可靠性是最大障碍](https://twitter.com/melissapan/status/1996975916971626763)
> 一项由伯克利、斯坦福、UIUC、IBM和Intesa等机构联合进行的“生产环境Agent测量”（MAP）研究发现，尽管AI代理能带来生产力提升，但可靠性仍是阻碍其部署的首要因素。目前生产环境主要依赖简单可控的模式和大量的人工监督。

---

### 9. [OpenAI研究员项目开放申请，谷歌举办Gemini 3 Vibe Coding黑客松](https://twitter.com/willdepue/status/1996755929296261147)
> OpenAI的研究员项目开放申请，多个团队招募具备扎实机器学习基础的工程师。同时，谷歌启动了Gemini 3 Vibe Coding黑客松，提供总计50万美元的API积分作为奖励，要求提交2分钟演示视频。

---

### 10. [Sakana AI“连续思考机器”在NeurIPS引关注，采用神经ODE实现测试时计算扩展](https://twitter.com/yasuotabei/status/1996784916319949138)
> 在NeurIPS会议上，Sakana AI的“连续思考机器”吸引了大量关注。该模型通过连续动力学（神经ODE）而非增加Transformer深度来实现测试时计算扩展，为推理模型的设计提供了新思路。

---

## 🛠️ 十大工具产品要点

### 1. [LangChain发布DeepAgents CLI，在Terminal Bench 2.0上表现优异](https://twitter.com/LangChainAI/status/1997006806904984002)
> LangChain发布了DeepAgents命令行工具，在一个开源的沙盒化评估设置中，其在Terminal Bench 2.0上的得分约为42.7%，与Claude Code在该测试套件上的表现相当。

---

### 2. [SonarSource发布SonarQube MCP服务器，将企业级代码分析引入AI编程工具](https://twitter.com/_avichawla/status/1996829765207314735)
> SonarSource发布了SonarQube的MCP（模型上下文协议）服务器，可以将企业级的静态代码分析（如bug、漏洞、覆盖率检测）通过MCP协议集成到Claude Code、Cursor等AI编程工具中，用成熟的代码分析器增强AI代码生成。

---

### 3. [Together AI与Meta合作，在TorchForge上推出生产级强化学习支持](https://twitter.com/togethercompute/status/1996982138068258929)
> Together AI与Meta的AI团队合作，通过Together的平台在TorchForge上启动生产级强化学习，旨在支持长周期的智能体工作流。

---

### 4. [Kimi CLI通过ACP协议集成至JetBrains IDE](https://twitter.com/Kimi_Moonshot/status/1996953835080966390)
> 月之暗面的Kimi CLI现已通过Agent Client Protocol（ACP）集成到JetBrains系列IDE中，方便开发者在编码环境中直接调用。

---

### 5. [Cline代码助手新增GPT-5.1-Codex-Max模型选项](https://twitter.com/cline/status/1997028990050292166)
> AI代码助手Cline新增了GPT-5.1-Codex-Max模型作为选项，定价为每百万输入token 1.25美元，每百万输出token 10美元。

---

### 6. [PaperDebugger：多智能体Overleaf插件，辅助论文写作与修改](https://twitter.com/LiorOnAI/status/1997023854997504332)
> PaperDebugger是一个多智能体Overleaf插件，集成了批评家、重写器、研究者和评分员等角色，并通过MCP工具链进行文献搜索和引用表格生成，可直接操作文档状态和修订版本。

---

### 7. [通用程序化工具调用编排器大幅减少token消耗](https://github.com/Brainwires/tool-orchestrator)
> 一个模型无关的工具编排器发布，它实现了Anthropic的程序化工具调用模式，允许任何LLM生成Rhai脚本来编排工具调用。基准测试显示，相比简单的顺序工具调用，该方法能减少97-99%的token消耗。

---

### 8. [AnswerDotAI推出clipmd Chrome扩展，将网页DOM转换为Markdown](https://twitter.com/jeremyphoward/status/1997095883079553352)
> AnswerDotAI发布了一款Chrome扩展程序clipmd，可以将网页的DOM（文档对象模型）复制为Markdown格式和截图，便于在LLM工作流中使用。

---

### 9. [TinyCorp展示密集1U服务器，内置8块水冷GPU](https://twitter.com/__tinygrad__/status/1996815573427028106)
> TinyCorp（由George Hotz创立）展示了一款密集的1U服务器设计，内部紧凑地集成了8块水冷GPU，引发了社区对其冷却设计、PCIe瓶颈和访问方式的讨论。

---

### 10. [MAX框架发布：硬件无关的高性能AI推理框架](来源：文章内容)
> Modular公司的Chris Lattner介绍了MAX框架，这是一个旨在实现高性能、硬件无关的AI推理框架，支持GPU和CPU，兼容超过500个模型。其Model API将进行更新，采用纯MAX/Mojo栈，不依赖PyTorch或NumPy等外部框架。

---