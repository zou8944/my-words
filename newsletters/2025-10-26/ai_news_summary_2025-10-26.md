## AINews - 2025-10-26

> [原文链接](https://news.smol.ai/issues/25-10-24-not-much/)

## 📰 十大AI新闻要点

### 1. [vLLM支持NVIDIA Nemotron系列](https://twitter.com/vllm_project/status/1981553870599049286)
> vLLM宣布对NVIDIA Nemotron系列提供一流支持，特别强调9B参数的"Nemotron Nano 2"采用混合Transformer-Mamba设计，具有可调"思考预算"功能，在vLLM下生成"思考"令牌比类似规模的开源密集模型快6倍

---

### 2. [斯坦福模型溯源检测技术突破](https://twitter.com/percyliang/status/1981612361309098383)
> 斯坦福新研究展示仅通过黑盒访问就能检测模型B是否源自模型A（如微调），具有强统计保证（p < 1e-8），该测试利用训练数据顺序的内置元数据，微调不会消除这些痕迹

---

### 3. [MiniMax M2模型表现强劲](https://twitter.com/zephyr_z9/status/1981695536987357382)
> 早期测试表明MiniMax M2与顶级中文模型竞争激烈，"与Sonnet 4.5不相上下"，社区将其升级为A/S级定位，该模型针对代理/编码场景优化，具有低延迟和低成本特点

---

### 4. [Mistral AI Studio生产平台发布](https://twitter.com/MistralAI/status/1981752578951233989)
> Mistral推出生产平台，提供代理运行时和全生命周期深度可观测性，旨在帮助用户从实验阶段过渡到生产环境

---

### 5. [Baseten实现GPT-OSS 120B高性能推理](https://twitter.com/basetenco/status/1981757270053494806)
> Baseten在NVIDIA硬件上实现GPT-OSS 120B模型650 TPS和0.11秒TTFT，相比发布时的450 TPS有显著提升，达到99.99%正常运行时间

---

### 6. [Karpathy发布nanochat端到端指南](https://twitter.com/karpathy/status/1981746327995465816)
> Karpathy发布从零构建类ChatGPT堆栈的详细指南，强调可读性、可修改性和个人所有权，展示如何通过合成任务、仔细标记化和Python解释器添加目标功能

---

### 7. [智谱GLM-4.6-Air开发进展](https://twitter.com/Zai_org/status/1981700688401879314)
> 智谱GLM-4.6-Air仍在训练中，公司优先考虑可靠性，由于GLM Coding使用量快速增长，正在扩展基础设施以满足推理需求

---

### 8. [Hugging Face InspectAI添加推理提供商集成](https://twitter.com/dvilasuero/status/1981688436735271283)
> Hugging Face InspectAI新增"推理提供商"集成功能，可在笔记本电脑上跨开源模型提供商运行评估，为公平比较提供路径

---

### 9. [OpenAI ChatGPT Atlas记忆功能](https://twitter.com/OpenAI/status/1981782134655520991)
> OpenAI的ChatGPT Atlas现在可以持久化浏览和任务历史作为用户记忆，提供更好的上下文和标签控制，这是相关性和隐私方面的有趣上下文工程挑战

---

### 10. [GitHub Copilot代码搜索嵌入模型升级](https://twitter.com/github/status/1981727394663731598)
> GitHub为VS Code推出新的Copilot嵌入模型，检索效果提升37.6%，吞吐量约2倍，索引大小缩小8倍，文章中详细介绍了架构和索引变化

---

## 🛠️ 十大工具产品要点

### 1. [Thinking Machines "Tinker"分布式微调抽象](https://twitter.com/DeepLearningAI/status/1981752540405301452)
> Thinking Machines推出"Tinker"，将开源权重LLM（Qwen3、Llama 3）的分布式微调抽象为类似单设备API，处理多GPU调度、分片和崩溃恢复

---

### 2. [OCR模型在vLLM中快速部署](https://twitter.com/vllm_project/status/1981579850436751611)
> OCR模型在vLLM中趋势明显，快速部署获得关注，Hugging Face Datasets现在可以一行代码加载PDF，对OCR管道很有用

---

### 3. [Mem0代理长期记忆构建教程](https://twitter.com/neural_avb/status/1981589315617714303)
> Mem0视频教程展示如何使用DSPy、向量搜索和工具调用构建长期记忆作为上下文工程问题，包含评估数据集

---

### 4. [AWS Bedrock AgentCore Memory集成LlamaIndex](https://twitter.com/llama_index/status/1981752598698008725)
> AWS Bedrock AgentCore Memory现在在LlamaIndex代理中得到支持，提供安全存储、访问控制和长/短期记忆功能

---

### 5. [Google AI Studio QoS优化](https://twitter.com/GoogleAIStudio/status/1981745399644950826)
> 当达到免费限制时，AI Studio可以临时切换到用户的Gemini API密钥，配额重置时恢复，保持迭代流程顺畅

---

### 6. [VideoAgentTrek GUI代理训练方法](https://twitter.com/huybery/status/1981728838024560669)
> VideoAgentTrek提出在人类计算机使用视频上进行预训练和代理调优来训练更强的GUI代理，已在Qwen3-VL训练中使用

---

### 7. [Together发布GPU集群训练推理指南](https://twitter.com/togethercompute/status/1981814480691761252)
> Together发布在即时GPU集群上进行训练和推理的分步指南，与Karpathy的nanochat项目配合使用

---

### 8. [Hugging Face数据集PDF加载功能](https://twitter.com/lhoestq/status/1981720383620358449)
> Hugging Face Datasets现在可以一行代码加载PDF，对OCR管道非常有用，简化了文档处理流程

---

### 9. [领域特定视觉语言模型适配](https://twitter.com/wjb_mattingly/status/1981736776076026044)
> 在CATmuS数据集上微调的Qwen3-VL-2B/4B/8B模型针对中世纪语言/脚本发布在HF上，展示了领域特定视觉语言适配的优秀示例

---

### 10. [Merve视觉语言模型微调教程](https://twitter.com/mervenoyann/status/1981657235785728010)
> Merve发布Kosmos2.5带定位和Florence-2在DocVQA上微调的实践教程，可与其他VLM即插即用