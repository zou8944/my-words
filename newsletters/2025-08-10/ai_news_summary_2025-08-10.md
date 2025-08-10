## AINews - 2025-08-10

> [原文链接](https://news.smol.ai/issues/25-08-08-not-much/)

## 📰 十大AI新闻要点

### 1. [GPT-5发布引发用户反弹，OpenAI恢复GPT-4o访问](https://news.ycombinator.com/item?id=44839842)
> OpenAI在GPT-5发布时意外宣布立即弃用GPT-4o，这一决定引发强烈反对后被撤销。用户批评新模型取消了手动选择功能，且Plus用户的使用限制大幅减少。

---

### 2. [GPT-5性能表现：推理能力强劲但路由系统存在问题](https://twitter.com/EpochAIResearch/status/1953615906535313664)
> GPT-5在FrontierMath等学术基准测试中创下新纪录，但在实际使用中因路由系统不稳定导致性能波动。OpenAI承诺将修复自动切换器并提高模型透明度。

---

### 3. [微软Copilot已全面迁移至GPT-5](https://twitter.com/mustafasuleyman/status/1953608045533204690)
> 微软宣布所有Copilot用户现已使用GPT-5，OpenAI报告API流量在24小时内翻倍，峰值吞吐量达到每分钟20亿token。

---

### 4. [Qwen3支持100万token上下文窗口](https://twitter.com/Alibaba_Qwen/status/1953760230141309354)
> 阿里云的Qwen3-30B和Qwen3-235B模型通过Dual Chunk Attention和MInference技术支持100万token上下文，在长文本处理速度上提升3倍。

---

### 5. [Google两周内密集发布多项AI成果](https://twitter.com/demishassabis/status/1953887339094143156)
> Google在短时间内发布了Genie-3世界模拟器、Gemini 2.5 Pro Deep Think等多款产品，其中NotebookLM的"视频概述"功能获得好评。

---

### 6. [OpenAI开源模型GPT-OSS引发争议](https://www.reddit.com/r/LocalLLaMA/comments/1mkcwiv/openai_open_washing/)
> 社区质疑OpenAI故意发布性能较弱的开源模型GPT-OSS来应对缺乏开源承诺的批评，尽管该模型在安全过滤任务中表现优异。

---

### 7. [llama.cpp实现3倍性能提升](https://github.com/ggml-org/llama.cpp/pull/15157)
> llama.cpp通过支持attention sinks技术，在GPT-OSS模型上实现高达3倍的提示处理速度提升，使大模型在消费级硬件上运行更加可行。

---

### 8. [Claude Code新增后台任务功能](https://twitter.com/_catwu/status/1953926541370630538)
> Anthropic为Claude Code添加了长期运行的后台任务支持和可定制的终端状态行，提升了编程代理的工作流体验。

---

### 9. [AI社区转向动态评估方法](https://twitter.com/nrehiew_/status/1953657627294224732)
> 业界逐渐从单一基准测试转向关注失败模式、工具调用次数和经济指标等动态评估方法，对LLM作为评判者的可靠性持怀疑态度。

---

### 10. [Google研究称主动学习可大幅减少微调数据需求](https://twitter.com/Dr_Singularity/status/1953573112726839663)
> Google Research的实验显示，通过专家标签的主动学习可将微调数据从10万例减少到不足500例，同时保持或提升模型质量。

---

## 🛠️ 十大工具产品要点

### 1. [GPT-5新增"优先处理"服务层级](https://twitter.com/jeffintime/status/1953857260729643136)
> GPT-5引入按价格层级区分的"优先处理"选项，使用"service_tier: priority"等参数可将P50 TTFT降至约750ms。

---

### 2. [Qwen Code CLI提供2000次免费运行](https://twitter.com/Alibaba_Qwen/status/1953835877555151134)
> 阿里云为Qwen Code CLI用户提供每日2000次免费运行额度，支持"氛围编程"体验。

---

### 3. [Cursor CLI集成GPT-5](https://twitter.com/embirico/status/1953590991870697896)
> Cursor/Codex CLI现已支持GPT-5，为ChatGPT计划用户提供慷慨但动态调整的速率限制，欧盟地区上线略有延迟。

---

### 4. [OpenAI发布自定义工具功能](https://twitter.com/sydneyrunkle/status/1953881101602038035)
> 新增支持正则表达式/语法约束的工具参数，并与LangGraph和LangChain代理集成。

---

### 5. [Hugging Face Accelerate v1.10发布](https://twitter.com/m_sirovatka/status/1953800134598569987)
> 支持N维并行(轻松堆叠DP/TP/PP)和清晰配置，简化大规模模型训练部署。

---

### 6. [Axolotl v0.12支持多节点训练](https://twitter.com/axolotl_ai/status/1953845149391630472)
> 新增多节点ND并行训练、FP8支持、GPT-OSS微调和TiledMLP的FSDP支持。

---

### 7. [PyTorch FlexAttention讨论](https://twitter.com/cHHillee/status/1953600887861211145)
> 社区探讨无需自定义内核实现块稀疏与任意注意力掩码的技术方案。

---

### 8. [Harmony数据集格式支持](https://twitter.com/_lewtun/status/1953870411050959110)
> OpenAI的Harmony数据集格式现已在Hugging Face Datasets上得到支持。

---

### 9. [vLLM中国生态系统快速发展](https://twitter.com/PyTorch/status/1953607090670342359)
> 腾讯总部举办260+开发者会议，中国主要实验室分享采用vLLM进行规模部署的经验。

---

### 10. [Wan 2.2图像转视频工作流](https://github.com/AI-PET42/WanWorkflows/blob/main/Wan2.2-I2V-Workflow-080630.json)
> 详细工作流展示如何使用RTX 4090(64GB RAM)运行Wan2.2模型，结合FramePack Studio和DaVinci Resolve进行后期处理。