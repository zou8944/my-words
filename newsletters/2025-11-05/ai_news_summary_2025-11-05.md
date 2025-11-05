## AINews - 2025-11-05

> [原文链接](https://news.smol.ai/issues/25-11-03-not-much/)

## 📰 十大AI新闻要点

### 1. [OpenAI与AWS达成380亿美元计算合作协议](https://twitter.com/gdb/status/1985378899648544947)
> OpenAI宣布与AWS建立战略合作伙伴关系，将部署"大量NVIDIA芯片"，涉及数十万块NVIDIA GB200和GB300芯片，这是价值380亿美元的重大计算协议，旨在大幅提升AI计算能力。

---

### 2. [阿里巴巴发布Qwen3-Max-Thinking预览版](https://twitter.com/Alibaba_Qwen/status/1985347830110970027)
> 阿里巴巴发布训练中的推理检查点，结合工具使用和测试时计算，在AIME 2025和HMMT基准测试中达到100%准确率，显示"思考"检查点加工具链可在复杂推理评估中取得突破性表现。

---

### 3. [MiniMax M2登顶开源WebDev排行榜](https://twitter.com/arena/status/1985465603206107318)
> 230B MoE参数的MIT许可模型MiniMax-M2在Arena的WebDev排行榜上成为排名第一的开源模型，整体排名与Claude Sonnet 4.5 Thinking 32k并列第四。

---

### 4. [LlamaIndex LIGHT框架在长上下文处理中表现卓越](https://twitter.com/omarsar0/status/1985348779193860414)
> LlamaIndex的LIGHT框架在100K-1M token长度上比长上下文LLM和RAG基线提升49-60%，在10M token长度上提升107-156%，在摘要任务中提升160.6%，多跳推理中提升27.2%。

---

### 5. [Kimi Linear线性注意力机制突破](https://www.reddit.com/r/singularity/comments/1on25fn/the_first_linear_attention_mechanism_on_that/)
> Kimi团队推出首个O(n)复杂度的线性注意力机制，在100万token解码速度上比传统O(n²)注意力快6倍，同时保持更高准确率，开源了KDA内核和模型检查点。

---

### 6. [微软获准向阿联酋出口NVIDIA GPU](https://twitter.com/AndrewCurran_/status/1985325278823125483)
> 微软获得美国商务部许可，可以向阿联酋运送NVIDIA GPU，计划在阿联酋数据中心投资79亿美元，这是地缘政治和AI基础设施布局的重要进展。

---

### 7. [OSWorld基准测试受到严格审查](https://twitter.com/EpochAIResearch/status/1985441059032478172)
> Epoch研究发现OSWorld任务过于简单，许多不需要GUI，指令模糊，基准随时间不稳定，约10%任务存在严重错误，不同提示集导致分数不可比较。

---

### 8. [NVIDIA举办NVFP4内核优化竞赛](https://twitter.com/a1zhang/status/1985434030473437213)
> NVIDIA与GPU MODE合作举办为期3个月的NVFP4内核优化竞赛，在Blackwell B200上进行，大奖为配备GB300的Dell Pro Max，旨在推动低比特量化优化技术。

---

### 9. [Google因诽谤指控从AI Studio下架Gemma](https://www.reddit.com/r/LocalLLaMA/comments/1on628o/google_pulls_gemma_from_ai_studio_after_senator/)
> 在参议员Blackburn指控模型诽谤后，Google从AI Studio移除了Gemma模型，但权重仍可在Hugging Face下载，凸显AI开发与监管审查之间的紧张关系。

---

### 10. [vLLM本地服务获得广泛采用](https://twitter.com/vllm_project/status/1985241134663405956)
> vLLM的本地服务能力持续扩展，知名YouTuber PewDiePie正在使用它本地服务LLM，随着模型和工具栈成熟，更多延迟敏感的智能体工作流将倾向本地部署。

---

## 🛠️ 十大工具产品要点

### 1. [vLLM本地LLM服务框架](https://twitter.com/vllm_project/status/1985241134663405956)
> vLLM项目持续获得采用，支持高效的本地LLM服务，PewDiePie等用户正在使用，为延迟敏感的智能体工作流提供高性能推理解决方案。

---

### 2. [Moonshot AI发布Kimi CLI技术预览版](https://xcancel.com/Kimi_Moonshot/status/1984207733177090274)
> Moonshot AI推出终端聚焦的Kimi CLI，支持Zsh集成和MCP，提供Zed编辑器原生钩子，VIP用户可免费获得"Kimi For Coding"附加功能。

---

### 3. [OpenAI预览Agent/Atlas模式](https://xcancel.com/OpenAI/status/1984304194837528864)
> OpenAI为ChatGPT Plus/Pro/Business用户推出Agent/Atlas模式预览，使模型能够浏览并为用户执行操作，引发对提示注入攻击和隐私边界的关注。

---

### 4. [LangChain推出DeepAgents CLI](https://xcancel.com/hwchase17/status/1984303925101735950)
> LangChain发布基于deepagents包的DeepAgents CLI，作为可定制智能体的"开放框架"，支持跨会话保留指令和指导，社区关注MCP集成和外部记忆源。

---

### 5. [Perplexity Comet增强隐私控制](https://twitter.com/perplexity_ai/status/1985376841021174184)
> Perplexity的Comet浏览器添加细粒度助手设置和本地凭证存储，阻止第三方跟踪器，提供新的透明度小部件，强化用户隐私保护。

---

### 6. [Firecrawl v2支持多模态爬取](https://twitter.com/_avichawla/status/1985233254694416743)
> Firecrawl v2端点可以爬取带过滤器（分辨率、宽高比、类型）的图像，为构建多模态应用和数据集提供强大工具。

---

### 7. [VS Code Insiders集成OpenAI Codex](https://twitter.com/code/status/1985449714540572930)
> VS Code Insiders现在可以在Copilot Pro+中使用OpenAI Codex，为开发者提供更强大的代码生成和补全能力。

---

### 8. [Windsurf推出"Fast Context"功能](https://twitter.com/SarahChieng/status/1985410447538114771)
> Windsurf的"Fast Context"以约20倍速度检索相关代码，支持保持工作流的导航体验，显著提升开发效率。

---

### 9. [mcp2py添加OAuth支持](https://twitter.com/MaximeRivest/status/1985200460194627948)
> mcp2py添加OAuth支持和简单的"2行Notion"体验，采用MIT许可证发布，简化MCP服务器的开发和使用。

---

### 10. [Gemini Docs MCP服务器发布](https://twitter.com/_philschmid/status/1985363147071386048)
> 本地STDIO服务器支持SQLite FTS5，可通过uvx运行，在Python/TS SDK文档查询中通过114/117个测试，为开发者提供高效的文档检索工具。

---