## AINews - 2025-08-12

> [原文链接](https://news.smol.ai/issues/25-08-08-not-much/)

## 📰 十大AI新闻要点

### 1. [GPT-5发布引发用户反弹，OpenAI恢复GPT-4o访问](https://news.ycombinator.com/item?id=44839842)
> OpenAI在GPT-5发布时意外宣布立即弃用GPT-4o，引发用户强烈反对后迅速撤回决定。Sam Altman表示将恢复GPT-4o作为可选模型，并改进路由透明度。

---

### 2. [GPT-5统一用户体验引发开发者争议](https://twitter.com/nickaturley/status/1953568295774568582)
> OpenAI将GPT-5定位为"统一体验"，取消手动模型选择功能，引发开发者社区对"模型选择器"消失的强烈反应，特别是对专业用户工作流程的影响。

---

### 3. [GPT-5在学术推理基准测试中创下新纪录](https://twitter.com/EpochAIResearch/status/1953615906535313664)
> GPT-5在FrontierMath基准测试中创下24.8%的新纪录，但在某些长文本任务中达到100k token上限。LiveBench等测试也显示GPT-5处于领先地位。

---

### 4. [微软宣布所有Copilot用户已迁移至GPT-5](https://twitter.com/mustafasuleyman/status/1953608045533204690)
> 微软CEO Mustafa Suleyman宣布100%的Copilot用户现已运行在GPT-5上，OpenAI报告API流量在24小时内翻倍，峰值吞吐量达"20亿token/分钟"。

---

### 5. [Qwen3模型支持100万token上下文](https://twitter.com/Alibaba_Qwen/status/1953760230141309354)
> 阿里巴巴Qwen团队宣布Qwen3-30B和Qwen3-235B模型通过Dual Chunk Attention和MInference技术支持100万token上下文，在长上下文场景下速度提升3倍。

---

### 6. [Google密集发布多项AI成果](https://twitter.com/demishassabis/status/1953887339094143156)
> Google DeepMind CEO Demis Hassabis展示两周内发布的多个项目，包括Genie-3世界模拟器、Gemini 2.5 Pro Deep Think、AlphaEarth等，其中NotebookLM"视频概述"功能获得好评。

---

### 7. [OpenAI开源模型GPT-OSS引发争议](https://www.reddit.com/r/LocalLLaMA/comments/1mkcwiv/openai_open_washing/)
> 社区质疑OpenAI发布的GPT-OSS开源模型是"开放洗白"策略，故意发布较弱模型转移注意力。测试显示该模型在安全过滤方面表现优异，但在创意任务上受限。

---

### 8. [llama.cpp新增注意力下沉支持，性能提升3倍](https://github.com/ggml-org/llama.cpp/pull/15157)
> llama.cpp合并了对注意力下沉(attention sinks)的支持，在RTX 3090上使用GPT-OSS模型时，提示处理速度从300提升到1300 token/秒，实现3倍性能提升。

---

### 9. [Claude Code新增后台任务功能](https://twitter.com/_catwu/status/1953926541370630538)
> Anthropic为Claude Code添加长运行后台任务支持，可实时监控bash进程，并允许自定义终端状态行，显著提升编程代理的工作流体验。

---

### 10. [AI社区转向动态追踪评估](https://twitter.com/nrehiew_/status/1953657627294224732)
> AI社区评估标准正从静态基准测试转向动态追踪评估，更关注失败模式、工具调用次数和经济指标，对LLM作为评判者的可靠性持续存在质疑。

---

## 🛠️ 十大工具产品要点

### 1. [GPT-5优先处理服务层](https://twitter.com/jeffintime/status/1953857260729643136)
> GPT-5引入"Priority Processing"服务层，在高价套餐中提供更低的首token时间(TTFT)，可通过设置service_tier: priority等参数实现约750ms P50 TTFT。

---

### 2. [Cursor CLI集成GPT-5](https://twitter.com/embirico/status/1953590991870697896)
> Cursor/Codex CLI现已集成GPT-5，ChatGPT套餐用户可获得慷慨但不断调整的速率限制，开发者报告GPT-5在精确引导下能生成可靠、简洁的代码。

---

### 3. [LangChain集成OpenAI自定义工具](https://twitter.com/sydneyrunkle/status/1953881101602038035)
> OpenAI新增正则/语法约束工具参数支持，已集成到LangGraph和LangChain代理中，增强工具调用的精确控制能力。

---

### 4. [Qwen Code CLI提供2000次免费运行](https://twitter.com/Alibaba_Qwen/status/1953835877555151134)
> 阿里巴巴Qwen推出Code CLI工具，每天提供2000次免费代码生成运行，支持"氛围编程"(vibe coding)体验。

---

### 5. [Hugging Face Accelerate v1.10发布](https://twitter.com/m_sirovatka/status/1953800134598569987)
> 支持N维并行(轻松堆叠DP/TP/PP)和清晰配置，简化大规模模型训练部署流程，附带比较博客详细说明新特性。

---

### 6. [Axolotl v0.12支持多节点训练](https://twitter.com/axolotl_ai/status/1953845149391630472)
> 新增多节点ND并行训练、FP8支持、GPT-OSS微调和TiledMLP的FSDP支持，显著提升大规模训练效率。

---

### 7. [Wan 2.2图像转视频工作流](https://github.com/AI-PET42/WanWorkflows/blob/main/Wan2.2-I2V-Workflow-080630.json)
> 详细工作流使用RTX 4090(64GB RAM)，结合Pony Diffusion生成静态图像，通过FramePack Studio插帧(16fps→32fps)，最后用DaVinci Resolve编辑。

---

### 8. [vLLM中国生态系统快速发展](https://twitter.com/PyTorch/status/1953607090670342359)
> 腾讯总部举办260+开发者参与的vLLM生态会议，中国主要实验室分享采用vLLM进行规模部署的经验。

---

### 9. [LlamaIndex集成Anthropic原生引用](https://twitter.com/llama_index/status/1953859971072114766)
> Anthropic的"搜索结果作为内容块"功能现已支持原生引用，并已由LlamaIndex和LangChain集成，提升信息溯源能力。

---

### 10. [Google Jules代理主动网络搜索](https://twitter.com/julesagent/status/1953852699944136847)
> Google的Jules代理现在会主动搜索网络获取最新上下文，显著提升代码生成质量，特别是在依赖最新信息的场景下。