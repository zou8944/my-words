## AINews - 2026-03-19

> [原文链接](https://news.smol.ai/issues/26-03-16-not-much/)

## 📰 十大AI新闻要点

### 1. [Moonshot AI发布“注意力残差”架构，引发学术讨论](https://x.com/Kimi_Moonshot/status/2033378587878072424)
> Moonshot AI发布论文《Attention Residuals》，提出用输入依赖的跨层注意力机制替代传统的固定残差连接，并引入Block AttnRes以保持实用性。据称，该架构在Kimi Linear 48B模型上验证，可获得1.25倍的计算优势，推理延迟开销低于2%。该成果引发了关于其创新性（是否与DeepCrossAttention等前人工作重叠）以及前沿规模验证重要性的广泛讨论。

---

### 2. [OpenAI Codex用户数激增，GPT-5.4 API收入达10亿美元年化](https://x.com/sama/status/2033599375256207820)
> OpenAI CEO Sam Altman表示，“硬核开发者”正在转向使用Codex。同时，OpenAI总裁Greg Brockman透露，GPT-5.4 API在发布一周内达到每日5万亿令牌的处理量，并创造了10亿美元的年化新增收入。Codex的周活跃用户数已超过200万，年内增长近4倍，并新增了子代理功能。

---

### 3. [Perplexity推出“Computer”代理，可控制本地浏览器](https://x.com/AravSrinivas/status/2033561054324953432)
> Perplexity将其AI代理“Computer”扩展至Android平台，并赋予其控制本地浏览器的能力。该功能允许Computer直接操作浏览器（如点击、滚动、填写表单），无需通过连接器或MCP，同时保留本地Cookie，用户可查看所有操作。这标志着代理执行能力从云端集成扩展到受权限控制的本地环境。

---

### 4. [Google发布多模态嵌入模型Gemini Embedding 2](https://x.com/Google/status/2033631279925891078)
> Google通过Gemini API和Vertex AI公开发布Gemini Embedding 2预览版。该模型为文本、图像、视频和音频提供了一个统一的嵌入空间，支持100多种语言。这种基础多模态原语对于生产级的搜索和检索系统可能比前沿聊天模型的基准测试更具实际意义。

---

### 5. [微软开源GigaTIME模型，用5美元病理切片预测空间蛋白质组学](https://x.com/AnishA_Moonka/status/2033344818475360562)
> 微软、普罗维登斯医疗集团和华盛顿大学的研究人员开发了GigaTIME模型，能够从一张价值约5美元的标准病理切片中，预测出类似多重免疫荧光技术才能获得的空间蛋白质组学信息。模型在4000万个细胞上训练，应用于51家医院的14,256名患者，生成了约30万个虚拟蛋白质图谱，并验证了1,234个关联。该模型已开源，旨在规模化普及癌症免疫分析。

---

### 6. [NVIDIA更新Nemotron模型许可，移除限制性条款](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license/)
> NVIDIA更新了Nemotron Super 3 122B A12B模型的许可证，移除了关于模型修改、护栏要求、品牌使用和归属的严格限制性条款。新的“NVIDIA Nemotron开放模型许可证”简化了合规要求，允许更自由的模型修改和再分发，使其从特殊用途转向更通用的应用场景。

---

### 7. [开源代理生态分化：Hermes易用性获赞，OpenClaw整合Ollama](https://x.com/ollama/status/2033339501872116169)
> 开源AI代理领域出现分化。社区反馈显示，Hermes Agent在设置简便性和鲁棒性上被认为优于OpenClaw。与此同时，OpenClaw生态系统仍在扩展，Ollama宣布成为其官方模型提供商，Comet为其发布了可观测性插件。这表明开源代理生态正在形成类似经典软件栈的格局。

---

### 8. [P-EAGLE技术突破推测解码瓶颈，实现单次生成K个草稿令牌](https://x.com/i/status/2033634407634927624)
> 一项名为P-EAGLE的新系统研究移除了推测解码中的顺序瓶颈，能够单次生成K个草稿令牌。据报道，在B200 GPU上，其速度比EAGLE-3快达1.69倍。该技术已集成到vLLM v0.16.0中，是提升大模型推理效率的重要进展。

---

### 9. [Claude Code成功逆向工程13年老游戏，破解社区未解难题](https://github.com/philparkinson1204/InfinityUnlocked)
> 一位开发者使用Claude Code在24小时内，在没有源代码和符号表的情况下，逆向分析了2013年的游戏《迪士尼无限1.0》的二进制文件。通过追踪`FindPlaysetForCharacter`函数并分析x86汇编，成功应用了17个二进制补丁和修改了3个数据文件，解除了角色与游戏场景绑定的限制，解决了困扰模组社区十多年的问题。项目已在GitHub开源。

---

### 10. [NVIDIA GTC大会强调“推理拐点”已至](https://x.com/basetenco/status/2033622003018830198)
> 在NVIDIA GTC大会上，CEO黄仁勋明确表示，AI领域的重心已从训练转向推理，即“推理拐点”。这一论断被广泛引用，标志着行业基础设施和生态系统的关注点正在发生根本性转变。

---

## 🛠️ 十大工具产品要点

### 1. [LangChain推出LangGraph CLI及开源Deep Agents参考框架](https://x.com/LangChain/status/2033596690171629582)
> LangChain发布了基于终端的LangGraph CLI，用于代理的部署和开发流程。同时，生态系统开源了“Deep Agents”，这是一个MIT许可的参考框架，复现了顶级编码代理的工作流，包括规划/待办事项、文件系统操作、Shell访问、子代理和上下文管理。这标志着行业从单纯发布模型转向发布“参考工具链”。

---

### 2. [Context Hub扩展为支持代理反馈循环的开放CLI](https://x.com/AndrewYNg/status/2033577583200354812)
> 吴恩达推广的Context Hub（chub）已扩展为一个开放的CLI工具，不仅提供最新的API文档，现在还支持对文档的“代理反馈循环”。这有助于确保编码代理使用的知识是最新的，而非陈旧的训练先验。

---

### 3. [AssemblyAI发布面向Claude Code等代理的“技能”](https://x.com/AssemblyAI/status/2033514383914283118)
> AssemblyAI发布了一个为Claude Code、Codex、Cursor等兼容代理维护的“技能”，使这些代理能够调用当前最新的API模式，而不是依赖过时的训练数据。这是构建代理工具栈中“技能文件”层的一部分。

---

### 4. [开源工具GraphZero v0.2实现零拷贝图引擎，避免OOM](https://github.com/KrishSingaria/graphzero)
> GraphZero v0.2是一个C++零拷贝图引擎，专为处理图神经网络的大数据集而设计。它将原始CSV编译为优化的二进制格式，并使用POSIX `mmap`直接从SSD内存映射文件，绕过系统RAM，从而避免内存溢出错误。它通过`nanobind`与PyTorch进行零拷贝集成，支持在高达50GB的数据集上进行训练。

---

### 5. [研究实现从GitHub仓库自动提取代理技能](https://x.com/dair_ai/status/2033546855376916735)
> 一项研究提出了从GitHub仓库中自动提取代理技能并标准化为`SKILL.md`文件的方法。据称，这种方法可以实现40%的知识转移增益，为构建由仓库挖掘的程序性知识驱动的代理工具栈奠定了基础。

---

### 6. [Recon：用于在tmux中监控Claude Code代理的仪表盘](https://github.com/gavraz/recon)
> Recon是一个用Rust编写、基于Ratatui库的tmux原生仪表盘工具，可将Claude Code代理可视化为像素艺术风格的“拓麻歌子”，实时显示其“输入中”、“工作中”、“空闲”等状态。用户可以在tmux会话中高效切换和管理多个代理。

---

### 7. [Claude技能“prompt-master”可自动生成优化提示](https://github.com/nidhinjs/prompt-master)
> 一款名为“prompt-master”的Claude技能，可自动为GPT、Claude Code、Midjourney等AI工具生成优化提示。该技能旨在通过为特定工具定制提示并利用记忆来减少信用额浪费和重复提示。用户可通过GitHub下载并上传至Claude的技能部分使用。

---

### 8. [工具可检查Claude API在本地时区的非高峰时段](https://www.reddit.com/r/ClaudeAI/comments/1runy7i/i_made_a_tool_to_check_claudes_offpeak_hours_in/)
> 有开发者创建了一个工具，帮助用户根据本地时区查询Claude API的非高峰（促销）时段。该工具提供了一个清晰的界面，显示当前是否为“Claude促销时间”以及距离高峰时段恢复的倒计时，解决了非美国用户手动转换太平洋时间的麻烦。

---

### 9. [SeedFold推出基于扩散模型的蛋白质设计工具SeedProteo](https://x.com/SeedFold/status/2033515503839514771)
> SeedFold推出了SeedProteo，这是一个用于从头开始进行全原子蛋白质设计的工具，基于扩散模型。这代表了AI在科学发现，特别是计算生物学领域的一个具体应用进展。

---

### 10. [vLLM发布OCI生产环境部署指南](https://x.com/vllm_project/status/2033560408980914550)
> 高性能推理框架vLLM发布了在Oracle Cloud Infrastructure (OCI) 上部署生产环境的指南。这反映了随着推理成为重心，主流推理框架正在积极完善其在不同云平台上的企业级部署方案。