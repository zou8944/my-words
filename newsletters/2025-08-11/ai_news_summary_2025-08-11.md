## AINews - 2025-08-11

> [原文链接](https://news.smol.ai/issues/25-08-08-not-much/)

## 📰 十大AI新闻要点

### 1. [GPT-5发布引发用户反弹，OpenAI恢复GPT-4o访问](https://news.ycombinator.com/item?id=44839842)
> OpenAI在GPT-5发布时意外宣布立即弃用GPT-4o，引发用户强烈反对后撤销决定。GPT-5采用统一路由体验设计，取消手动模型选择功能，导致Plus用户遭遇推理模型访问降级和请求限制问题。

---

### 2. [GPT-5学术基准表现创纪录但路由成本问题显现](https://twitter.com/EpochAIResearch/status/1953615906535313664)
> GPT-5在FrontierMath基准创下24.8%的新纪录，但在文档理解任务中消耗4-5倍于GPT-4.1的token量。Epoch研究显示其可能打破了"每代100倍训练计算"的传统增长模式。

---

### 3. [Qwen3模型实现100万token上下文支持](https://twitter.com/Alibaba_Qwen/status/1953760230141309354)
> 阿里云Qwen3-30B和Qwen3-235B通过Dual Chunk Attention和MInference技术支持百万token上下文，在长上下文场景下实现3倍速度提升，兼容vLLM/SGLang部署。

---

### 4. [微软宣布Copilot用户全部迁移至GPT-5](https://twitter.com/mustafasuleyman/status/1953608045533204690)
> 微软CEO Mustafa Suleyman确认所有Copilot用户已切换至GPT-5，OpenAI报告API流量在24小时内翻倍，峰值吞吐达20亿token/分钟。

---

### 5. [Google两周密集发布多项AI成果](https://twitter.com/demishassabis/status/1953887339094143156)
> Google DeepMind CEO Demis Hassabis展示包括Genie-3世界模拟器、Gemini 2.5 Pro Deep Think、AlphaEarth等在内的多项突破，其中NotebookLM视频概述功能获得好评。

---

### 6. [llama.cpp实现3倍性能提升](https://github.com/ggml-org/llama.cpp/pull/15157)
> llama.cpp通过合并注意力下沉(attention sinks)支持，在RTX 3090上实现GPT-OSS 120B模型的提示处理速度从300token/s提升至1300token/s。

---

### 7. [OpenAI开源模型被指战略"洗绿"](https://www.reddit.com/r/LocalLLaMA/comments/1mkcwiv/openai_open_washing/)
> 社区质疑OpenAI故意发布性能较弱的GPT-OSS开源模型转移批评，测试显示该模型在安全过滤任务表现优异(500次提示仅1次拒绝)，但存在知识盲区。

---

### 8. [Claude Code新增后台任务功能](https://twitter.com/_catwu/status/1953926541370630538)
> Anthropic为Claude Code添加长运行后台任务支持和可定制终端状态栏，显著提升代理编程的工作流体验。

---

### 9. [AI视频模型Wan 2.2工作流公开](https://github.com/AI-PET42/WanWorkflows/blob/main/Wan2.2-I2V-Workflow-080630.json)
> Wan 2.2图像转视频工作流细节曝光，使用RTX 4090完成生成后需FramePack Studio插帧和DaVinci Resolve剪辑，完整流程耗时约2小时。

---

### 10. [社区转向动态评估取代传统基准测试](https://twitter.com/nrehiew_/status/1953657627294224732)
> AI社区逐渐从静态基准测试转向关注失败模式、工具调用次数和经济指标等动态评估方法，对LLM作为评判者的可靠性持续质疑。

---

## 🛠️ 十大工具产品要点

### 1. [GPT-5优先处理API参数公布](https://twitter.com/kwindla/status/1953868672470331423)
> 使用service_tier:priority和reasoning_effort:minimal参数可实现P50 750ms的首token延迟，视觉输入的路由设计会增加2-3秒延迟。

---

### 2. [Cursor CLI集成GPT-5](https://twitter.com/embirico/status/1953590991870697896)
> ChatGPT付费用户现可通过Cursor CLI访问GPT-5，欧盟地区发布延迟，提供/logout缓解限制误用问题，每周+5小时重置周期。

---

### 3. [OpenAI自定义工具支持正则约束](https://twitter.com/sydneyrunkle/status/1953881101602038035)
> OpenAI新增正则/语法约束的工具参数功能，已集成至LangGraph和LangChain代理框架。

---

### 4. [Qwen Code CLI提供2000次免费运行](https://twitter.com/Alibaba_Qwen/status/1953835877555151134)
> 阿里云Qwen Code CLI每日提供2000次免费代码生成额度，支持"氛围编程"体验。

---

### 5. [Hugging Face Accelerate v1.10发布](https://twitter.com/m_sirovatka/status/1953800134598569987)
> 支持N维并行(轻松堆叠数据/张量/管道并行)和清晰配置，附带对比博客说明。

---

### 6. [Axolotl v0.12支持多节点训练](https://twitter.com/axolotl_ai/status/1953845149391630472)
> 新增多节点ND并行训练、FP8支持、GPT-OSS微调和TiledMLP的FSDP支持。

---

### 7. [PyTorch FlexAttention讨论升温](https://twitter.com/cHHillee/status/1953600887861211145)
> 社区热议无需自定义内核实现块稀疏与任意注意力掩码的技术路线。

---

### 8. [vLLM中国生态快速发展](https://twitter.com/PyTorch/status/1953607090670342359)
> 腾讯总部举办260+开发者大会，主要中国实验室分享采用vLLM进行规模部署的经验。

---

### 9. [Intel发布20B 2/4-bit GGUF模型](https://twitter.com/HaihaoShen/status/1953729639081554002)
> 英特尔推出20B参数的2位和4位GGUF格式量化模型，优化本地部署效率。

---

### 10. [Harmony数据集格式获HF支持](https://twitter.com/_lewtun/status/1953870411050959110)
> OpenAI Harmony数据集格式现可在Hugging Face Datasets中使用，促进开源模型训练数据标准化。

---