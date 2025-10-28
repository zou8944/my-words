## AINews - 2025-10-28

> [原文链接](https://news.smol.ai/issues/25-10-24-not-much/)

## 📰 十大AI新闻要点

### 1. [vLLM支持NVIDIA Nemotron系列模型](https://twitter.com/vllm_project/status/1981553870599049286)
> vLLM宣布对NVIDIA Nemotron系列提供一流支持，特别强调新的9B参数"Nemotron Nano 2"模型，采用混合Transformer-Mamba架构，开放权重，使用超过9T token的开放数据。在vLLM下，该模型生成"思考"token的速度比类似规模的开源密集模型快6倍。

---

### 2. [Mistral AI Studio生产平台发布](https://twitter.com/MistralAI/status/1981752578951233989)
> Mistral推出生产平台，提供代理运行时和全生命周期深度可观测性，旨在帮助用户从实验阶段过渡到生产环境，专注于代理和可观测性功能。

---

### 3. [Baseten实现GPT-OSS 120B高性能推理](https://twitter.com/basetenco/status/1981757270053494806)
> Baseten在NVIDIA硬件上为GPT-OSS 120B模型实现了650 TPS（每秒token数）和0.11秒TTFT（首token时间），相比发布时的450 TPS有显著提升，同时保持99.99%的正常运行时间。

---

### 4. [斯坦福开发模型溯源检测方法](https://twitter.com/percyliang/status/1981612361309098383)
> 斯坦福新研究显示，仅通过黑盒访问就能检测可疑模型B是否源自模型A（如微调），具有强统计保证（p < 1e-8）。该方法利用训练数据顺序的内置元数据，微调不会消除这些痕迹。

---

### 5. [MiniMax M2模型表现强劲](https://twitter.com/zephyr_z9/status/1981695536987357382)
> 早期测试表明MiniMax M2与顶级中文模型竞争激烈，与Sonnet 4.5"旗鼓相当"，促使社区将其升级至A/S级定位。该模型针对代理/编码场景优化，具有低延迟和低成本特点。

---

### 6. [智谱GLM-4.6-Air持续训练中](https://twitter.com/Zai_org/status/1981700688401879314)
> 智谱仍在训练GLM-4.6-Air，优先考虑可靠性和扩展基础设施，以应对GLM Coding使用量的快速增长。非官方预期该模型将带来类似近期Qwen更新的重大改进。

---

### 7. [Karpathy发布nanochat端到端指南](https://twitter.com/karpathy/status/1981746327995465816)
> Karpathy的端到端类ChatGPT堆栈nanochat强调可读性、可修改性和个人所有权。新指南详细介绍了通过合成任务、仔细分词和Python解释器添加目标能力的方法，以及如何混合SFT和RL以获得鲁棒性。

---

### 8. [Hugging Face InspectAI添加推理提供商集成](https://twitter.com/dvilasuero/status/1981688436735271283)
> Hugging Face InspectAI新增"推理提供商"集成功能，可在笔记本电脑上跨开源模型提供商运行评估，为公平比较提供良好路径。

---

### 9. [复旦提出BAPO强化学习优化方法](https://twitter.com/TheTuringPost/status/1981860282629837136)
> 复旦引入动态PPO裁剪方法BAPO（带自适应裁剪的平衡策略优化），稳定离策略强化学习并保持探索。32B模型在AIME24/AIME25上分别达到87.1/80.0分，与o3-mini和Gemini 2.5相当。

---

### 10. [OCR模型采用浪潮](https://twitter.com/ErikKaum/status/1981750508982268330)
> 紧凑OCR模型快速采用，支持在HF Inference Endpoints中一键部署，vLLM也看到快速部署趋势。HF Datasets现在可以一行代码加载PDF，对OCR管道非常有用。

---

## 🛠️ 十大工具产品要点

### 1. [Thinking Machines "Tinker"分布式微调抽象](https://twitter.com/DeepLearningAI/status/1981752540405301452)
> Thinking Machines的"Tinker"在类似单设备API后面抽象了开源权重LLM（Qwen3、Llama 3）的分布式微调，处理多GPU调度、分片和崩溃恢复。

---

### 2. [GitHub Copilot新嵌入模型](https://twitter.com/github/status/1981727394663731598)
> GitHub为VS Code引入新的Copilot嵌入模型，检索性能提升37.6%，吞吐量约2倍，索引大小缩小8倍，改进了架构和索引变更。

---

### 3. [AWS Bedrock AgentCore Memory集成LlamaIndex](https://twitter.com/llama_index/status/1981752598698008725)
> AWS Bedrock AgentCore Memory现在在LlamaIndex Agents中得到支持，提供安全存储、访问控制和长/短期记忆功能。

---

### 4. [Google AI Studio QoS功能](https://twitter.com/GoogleAIStudio/status/1981745399644950826)
> 当达到免费限制时，AI Studio可以临时切换到用户的Gemini API密钥，在配额重置时恢复，保持迭代流程顺畅。

---

### 5. [Mem0长期记忆构建教程](https://twitter.com/neural_avb/status/1981589315617714303)
> Mem0视频教程展示如何使用DSPy、向量搜索和工具调用构建长期记忆作为上下文工程问题，包含评估数据集。

---

### 6. [Pacific-Prime模型升级](https://huggingface.co/Pacific-Prime/pacific-prime)
> Pacific-Prime模型升级至1.1B参数，使用6GB VRAM获得10%增益，具有"零遗忘"特性，能够保留对话细节作为上下文丰富的记忆。

---

### 7. [Cursor Ultra预算管理问题](https://discord.com/channels/1074847526655643750)
> Cursor Ultra用户报告预算预测不准确，400美元预算在几天内耗尽，尽管定价为200美元，使其对月度编码不可靠。

---

### 8. [aider社区分叉添加新功能](https://github.com/dwash96/aider-ce)
> aider-ce等社区分叉添加RAG和导航器模式，复兴停滞的原始项目开发，用户转向GPT-5上的Codex以获得无限上下文。

---

### 9. [DSPy在结构化任务中优于Langchain](https://discord.com/channels/1161519468141355160)
> 团队从Langchain迁移到DSPy处理结构化任务，避免模型升级时的提示重写问题，DSPy在结构化任务和优化方面表现优异。

---

### 10. [LM Studio平台差异问题](https://discord.com/channels/1110598183144399058)
> LM Studio在macOS上支持JSON响应格式但在Windows上不支持，导致使用OpenAI SDK时出现400错误，凸显跨平台服务器接口差异。