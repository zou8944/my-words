## AINews - 2025-09-11

> [原文链接](https://news.smol.ai/issues/25-09-09-not-much/)

## 📰 十大AI新闻要点

### 1. [Cognition完成4亿美元融资，估值达102亿美元](https://twitter.com/cognition/status/1965086655821525280)
> Cognition宣布完成4亿美元融资，由Founders Fund领投，估值达102亿美元，旨在扩展AI编程代理Devin。团队强调客户扩张和Windsurf团队加入，正在招聘产品、基础设施和后训练岗位。

---

### 2. [Vercel推出开源"氛围编程平台"](https://twitter.com/rauchg/status/1964857952722133231)
> Vercel基于Vercel AI SDK、Gateway、Sandbox和调优的GPT-5代理循环构建了开源编程平台，支持文件IO、命令执行、包安装和自动修复功能，单次演示即在Go中编写了多人Pong游戏。

---

### 3. [Kimi K2-0905在编码评估中达到94%准确率](https://twitter.com/roo_code/status/1965098976677658630)
> Kimi K2-0905在Groq上运行，在Roo Code评估中达到94%准确率，排名第7，成为首个突破90+的开源权重模型，同时是前十名中最快且最便宜的模型。

---

### 4. [Meta推出Set Block Decoding技术](https://twitter.com/HuggingPapers/status/1965084731839513059)
> Meta的Set Block Decoding技术可在不改变架构的情况下将现有语言模型的解码速度提升3-5倍，匹配NTP性能并保持精确的KV缓存，通过掩码/离散扩散公式实现并行生成。

---

### 5. [Google Veo 3正式上市并降价50%](https://twitter.com/googleaidevs/status/1965160822260318702)
> Google的Veo 3和Veo 3 Fast现已在Gemini API中正式上市，价格降低约50%（0.40美元/秒和0.15美元/秒），支持1080p输出和9:16垂直视频，定位为规模化生产。

---

### 6. [FAIR推出Exploratory Iteration自我改进方法](https://twitter.com/MinqiJiang/status/1965055909605916892)
> FAIR的Exploratory Iteration方法通过自动课程训练LLMs进行推理时自我改进，从模型先前的响应中引导，优先处理高回报方差的局部历史，在竞赛数学、BFCLv3多轮任务和MLE-bench上超越GRPO。

---

### 7. [Google DeepMind推出多机器人规划系统RoboBallet](https://twitter.com/GoogleDeepMind/status/1965040645103407572)
> Google DeepMind与Intrinsic和UCL合作开发的RoboBallet可编排多达8个机器人臂进行无碰撞任务和运动规划，比传统方法性能提升约25%，通过RL学习的协调原则在几秒内泛化到新工作流。

---

### 8. [Perplexity推出政府版服务](https://twitter.com/perplexity_ai/status/1965030156415980009)
> Perplexity推出"Perplexity for Government"，默认安全、零数据使用、提供高级模型访问且无需企业合同，同时将Perplexity Finance扩展到iOS/Android平台。

---

### 9. [Anthropic支持加州SB 53AI透明度框架](https://twitter.com/AnthropicAI/status/1965027311717388673)
> Anthropic支持加州参议员Scott Wiener提出的SB 53法案，这是一个以透明度为重点的州级框架，用于在缺乏联邦标准的情况下治理前沿AI。

---

### 10. [Qwen3-Next系列发布新架构](https://qwenlm.github.io/blog/qwen3_next/)
> 阿里巴巴的Qwen3-Next系列引入混合注意力堆栈（门控DeltaNet + 门控注意力）、高稀疏度MoE（1:50激活比）和多令牌预测等架构变化，Qwen3-Next-80B-A3B据称在下游任务上以<1/10训练成本超越Qwen3-32B。

---

## 🛠️ 十大工具产品要点

### 1. [Claude新增文件创建和编辑功能](https://www.anthropic.com/news/create-files)
> Anthropic宣布Claude现在可以本地创建和编辑常见办公文件（Excel、Word、PowerPoint、PDF等），为Claude Max和Team/Enterprise用户提供即用型输出，无需复制粘贴。

---

### 2. [Qwen3-ASR多语言转录模型发布](https://twitter.com/Alibaba_Qwen/status/1965068737297707261)
> 阿里巴巴的Qwen3-ASR发布单一模型支持多语言转录（中英文+9种语言），自动检测，抗BGM/噪声/说唱干扰，词错误率<8%，支持自定义上下文偏置，在ModelScope/Hugging Face提供演示和API。

---

### 3. [AutoRound集成至SGLang](https://twitter.com/HaihaoShen/status/1964926924880523701)
> AutoRound现已在SGLang中集成，提供高效的量化优化功能，提升模型推理效率。

---

### 4. [QuTLASS v0.1.0发布支持Blackwell GPU](https://twitter.com/DAlistarh/status/1965157635617087885)
> QuTLASS v0.1.0为Blackwell GPU带来4位NVFP4微缩放和快速变换功能，优化量化性能。

---

### 5. [AlgoPerf v0.6新增滚动排行榜和JAX jit](https://twitter.com/algoperf/status/1965044626626342993)
> AlgoPerf v0.6添加滚动排行榜、JAX jit支持和更低计算成本的算法基准测试功能。

---

### 6. [ZeroGPU AOT编译内部文档发布](https://twitter.com/charlesbben/status/1965046090945954104)
> Hugging Face文档化了ZeroGPU的Ahead-of-Time编译内部机制，为PyTorch提供优化支持。

---

### 7. [ROMA开源深度研究框架](https://github.com/sentient-agi/ROMA)
> ROMA开源深度研究框架结合递归规划和多代理架构，在SEAL-0和FRAMES基准测试中声称超越闭源平台，提供即插即用系统和网络搜索工具。

---

### 8. [PyDevMini-1编码模型发布](https://huggingface.co/bralynn/pydevmini1)
> PyDevMini-1是基于Qwen的约4B参数微调模型，专注于Python和Web开发编码，声称在1/400大小下达到GPT-4水平，可在单个游戏GPU上运行。

---

### 9. [Tencent HunyuanImage-2.1图像生成系统](https://hunyuan.tencent.com/)
> 腾讯的HunyuanImage-2.1是基于多模态DiT骨干的开源文本到图像系统，支持高效2K生成，采用多模态LLM和ByT5双文本编码器，需要≥59GB GPU内存进行2K生成。

---

### 10. [RAGGY开源RAG评估工具](https://twitter.com/HamelHusain/status/1965052554997600449)
> RAGGY是开源的REPL工具，支持RAG的假设迭代，推动将预生产测试与生产可观察性和人工审查集成，而非作为独立孤岛处理。

---