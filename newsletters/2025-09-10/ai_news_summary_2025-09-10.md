## AINews - 2025-09-10

> [原文链接](https://news.smol.ai/issues/25-09-08-cog-smol/)

## 📰 十大AI新闻要点

### 1. [Cognition完成4亿美元融资，估值达102亿美元](https://twitter.com/cognition/status/1965086655821525280)
> Cognition宣布完成4亿美元融资，投后估值102亿美元，由Founders Fund领投，Lux、8VC、Neo等跟投。资金将用于扩展AI编程代理Devin的规模，团队正在产品、基础设施和后训练领域招聘人才。

---

### 2. [Vercel推出开源"氛围编程平台"](https://twitter.com/rauchg/status/1964857952722133231)
> Vercel基于Vercel AI SDK、Gateway、Sandbox和调优的GPT-5代理循环构建了开源编程平台，支持文件IO、命令执行、包安装和自动修复等功能，单次演示即可用Go编写多人Pong游戏。

---

### 3. [Kimi K2-0905在Roo Code基准测试中达到94%](https://twitter.com/roo_code/status/1965098976677658630)
> Kimi K2-0905在Groq上运行达到94%的准确率，在Roo Code排行榜排名第7，成为首个突破90%的开源权重模型，同时也是前十名中最快且最便宜的模型。

---

### 4. [Meta推出Set Block Decoding技术，解码速度提升3-5倍](https://twitter.com/HuggingPapers/status/1965084731839513059)
> Meta的新解码技术无需改变模型架构即可实现3-5倍的速度提升，通过掩码/离散扩散公式实现并行生成，匹配NTP性能并保持精确的KV缓存。

---

### 5. [谷歌Veo 3正式上市，价格降低50%](https://twitter.com/googleaidevs/status/1965160822260318702)
> Veo 3和Veo 3 Fast现已在Gemini API中正式上市，价格降低约50%（0.40美元/秒和0.15美元/秒），支持1080p输出和9:16垂直视频，定位规模化生产。

---

### 6. [FAIR推出Exploratory Iteration方法提升推理时自我改进](https://twitter.com/MinqiJiang/status/1965055909605916892)
> FAIR的ExIt方法通过自动课程训练LLMs进行推理时自我改进，在竞赛数学、BFCLv3多轮任务和MLE基准测试中表现优于GRPO，仅训练单步改进。

---

### 7. [Google DeepMind推出多机器人规划系统RoboBallet](https://twitter.com/GoogleDeepMind/status/1965040645103407572)
> RoboBallet可编排最多8个机械臂进行无碰撞任务和运动规划，性能比传统方法高约25%，通过RL学习的协调原则在几秒内泛化到新工作流。

---

### 8. [Perplexity推出政府版服务](https://twitter.com/perplexity_ai/status/1965030156415980009)
> Perplexity for Government默认安全，零数据使用，提供高级模型访问且无需企业合同，同时Perplexity Finance已登陆iOS和Android平台。

---

### 9. [Anthropic支持加州SB 53法案](https://twitter.com/AnthropicAI/status/1965027311717388673)
> Anthropic支持由参议员Scott Wiener提出的加州SB 53法案，这是一个以透明度为重点的州级框架，用于在缺乏联邦标准的情况下管理前沿AI。

---

### 10. [OpenAI协助制作AI生成动画长片](https://i.redd.it/50fm7mb3cvnf1.jpeg)
> OpenAI正合作制作一部AI生成动画长片，计划2026年上映，预算约3000万美元，涉及端到端生成管道，包括AI辅助预可视化、场景生成和后期制作。

---

## 🛠️ 十大工具产品要点

### 1. [Vercel AI SDK构建的编程平台](https://twitter.com/rauchg/status/1964857952722133231)
> 基于Vercel AI SDK的工具平台支持文件IO、命令执行、包安装和自动修复，使用调优的GPT-5代理循环，演示了单次编写多人Pong游戏的能力。

---

### 2. [Claude Code简约代理循环设计](https://twitter.com/imjaredz/status/1965083721713041564)
> Claude Code采用极简设计：单主循环+异步缓冲区、直接工具和基于TODO的规划，简洁性在可调试性和可靠性上优于群体编排。

---

### 3. [Qwen3-ASR多语言转录模型](https://twitter.com/Alibaba_Qwen/status/1965068737297707261)
> 阿里云推出单模型支持多语言转录（中英文+9种语言），自动检测，抗背景音乐/噪音/说唱干扰，词错误率低于8%，支持自定义上下文偏置。

---

### 4. [AutoRound集成至SGLang](https://twitter.com/HaihaoShen/status/1964926924880523701)
> AutoRound量化工具现已集成到SGLang中，提供高效的模型量化支持，优化推理性能。

---

### 5. [QuTLASS v0.1.0发布，支持4位NVFP4微缩放](https://twitter.com/DAlistarh/status/1965157635617087885)
> QuTLASS v0.1.0为Blackwell GPU带来4位NVFP4微缩放和快速变换，提升量化效率和计算性能。

---

### 6. [AlgoPerf v0.6新增滚动排行榜和JAX jit支持](https://twitter.com/algoperf/status/1965044626626342993)
> AlgoPerf v0.6更新包括滚动排行榜、JAX jit支持和降低算法基准测试的计算成本，提升评测效率。

---

### 7. [ZeroGPU AOT编译内部文档](https://twitter.com/charlesbben/status/1965046090945954104)
> Hugging Face发布PyTorch的ZeroGPU AOT编译内部文档，帮助开发者优化GPU计算和编译流程。

---

### 8. [Nano Banana开源项目](https://twitter.com/arrakis_ai/status/1965001417716072877)
> 基于Gemini 2.5 Flash Image Preview的"Nano Banana"项目已开源，支持一键重用和创意混搭，社区报告了有趣的特例（如时钟总是显示10:10）。

---

### 9. [RAGGY开源REPL工具](https://twitter.com/HamelHusain/status/1965052554997600449)
> RAGGY提供开源REPL环境，支持RAG的假设迭代，推动将预生产测试与生产可观测性和人工审查集成。

---

### 10. [OpenPI的pi-05支持PyTorch](https://twitter.com/svlevine/status/1965161524722630734)
> OpenPI的pi-05模型现已支持PyTorch，提供开源硬件栈和灵巧操作能力，增强机器人开发工具生态。

---