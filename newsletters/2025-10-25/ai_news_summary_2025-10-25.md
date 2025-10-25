## AINews - 2025-10-25

> [原文链接](https://news.smol.ai/issues/25-10-23-not-much/)

## 📰 十大AI新闻要点

### 1. [Anthropic与谷歌达成百万TPU超级交易](https://twitter.com/AnthropicAI/status/1981460118354219180)
> Anthropic计划在2026年扩展到"约100万个"谷歌云TPU和"超过"1GW容量，价值数百亿美元计算资源，大幅扩展训练/推理能力，这是AI基础设施领域最大规模的投资之一。

---

### 2. [LangSmith发布Insights Agent和多轮评估](https://twitter.com/LangChainAI/status/1981390300502487370)
> LangChain推出产品内代理，自动扫描跟踪以聚类使用模式和故障模式，加上多轮评估来评估完整对话中的目标完成情况。团队报告几乎立即获得对静默故障类别和用户意图集群的可见性，无需手动分类。

---

### 3. [Meta和Hugging Face推出OpenEnv标准化环境](https://twitter.com/_lewtun/status/1981380372748521929)
> 推出Gymnasium风格的API，专为容器/服务器执行设计，具有简单的HTTP接口，以及用于可重现"智能环境"的Hub。早期集成涵盖TRL、Unsloth、Atari和社区示例，旨在标准化环境打包和扩展分布式训练。

---

### 4. [LTX-2开源AI创意引擎发布](https://twitter.com/ltx_model/status/1981346235194683497)
> 开源AI创意引擎，具有同步音频+视频、原生4K、高达50fps和10秒序列，API优先设计，在消费级GPU上高效运行；权重将在今年晚些时候发布。

---

### 5. [OpenAI为ChatGPT企业版添加共享项目和公司知识](https://twitter.com/OpenAI/status/1981432799212249119)
> 为ChatGPT Business/Enterprise/Edu添加共享项目和"公司知识"功能，集成Slack、Drive、GitHub等企业工具，提升团队协作效率。

---

### 6. [Claude推出项目范围记忆功能](https://twitter.com/mikeyk/status/1981415275695394852)
> Claude为Pro和Max计划用户推出记忆功能，允许AI学习和保留用户的工作流程模式，包括工具使用、关键协作者和问题解决偏好，想法可以在对话间随时间积累。

---

### 7. [ScaleRL：面向可预测的RL扩展](https://twitter.com/TheTuringPost/status/1981487666714800356)
> Meta的新工作提出从小型运行预测LLM RL结果的方法论，声称能够准确推断高达10万GPU小时的结果，相比GRPO/DAPO/Magistral具有更好的效率。

---

### 8. [vLLM支持NVIDIA Nemotron Nano 2推理](https://twitter.com/vllm_project/status/1981553870599049286)
> vLLM现在支持NVIDIA的Nemotron Nano 2（9B混合Transformer-Mamba推理模型，开放权重，>9T tokens），具有可调"思考预算"以实现可预测的成本/延迟，声称比类似开放密集模型的"思考"token吞吐量快6倍。

---

### 9. [Google AI Studio新增注释模式](https://twitter.com/GoogleAIStudio/status/1981375306423554490)
> 新的注释模式允许用户在实时应用UI上"标记"，让Gemini应用代码更改，提升开发体验。

---

### 10. [Lookahead路由提升多LLM系统性能](https://twitter.com/omarsar0/status/1981360482813710384)
> 提出的"Lookahead"方法预测潜在响应的潜在表示，以廉价"窥视"每个模型会说什么，实现响应感知路由而无需完全解码。在7个基准测试中报告平均比SOTA路由提升+7.7%。

---

## 🛠️ 十大工具产品要点

### 1. [ClineBench发布真实世界可中断任务基准](https://twitter.com/cline/status/1981370535176286355)
> Cline发布ClineBench，包含真实世界、可中断的任务，同时强调相同开源模型在不同推理端点上的行为差异，建议通过系统提示缩减和提供商过滤来恢复稳定性。

---

### 2. [Firecrawl集成指南覆盖LangChain、n8n和MCP](https://twitter.com/firecrawl_dev/status/1981390679462072766)
> Firecrawl发布跨LangChain、n8n和MCP的集成指南，为开发者提供更便捷的网络数据抓取解决方案。

---

### 3. [Vercel推出useworkflow用于TypeScript持久异步任务](https://twitter.com/cramforce/status/1981399119559348290)
> Vercel发布"useworkflow"用于TypeScript中的持久异步任务，提升开发者在无服务器环境中的工作流管理能力。

---

### 4. [Argil Atom强调可控性和时间一致性](https://twitter.com/BrivaelLp/status/1981343140196778270)
> Argil宣布Atom视频生成工具，强调可控性和时间一致性，没有持续时间限制，加上"风格Tinder"用于外观选择。

---

### 5. [NVIDIA Gr00t N1.5机器人基础模型](https://twitter.com/LeRobotHF/status/1981334159801929947)
> NVIDIA的Gr00t N1.5是通过LeRobot发布的跨体现动作模型，具有视觉/语言/本体感觉输入和流匹配动作变换器，在真实/合成/互联网规模数据上训练。

---

### 6. [OCR/VLM模型爆发式增长](https://twitter.com/mervenoyann/status/1981396054634615280)
> OCR/VLM领域出现爆发式增长，包括LightOnOCR-1B（端到端VLM专注于速度/吞吐量）、OlmOCR-2依赖RLVR + 二进制单元测试进行快速迭代。

---

### 7. [Cerebras发布REAP修剪的GLM-4.6 MoE检查点](https://twitter.com/vithursant19/status/1981476324045967785)
> Cerebras发布REAP修剪的GLM-4.6 MoE检查点，压缩率为25/30/40%（FP8，A32B），目标是在保持生成质量的同时提高效率。

---

### 8. [Qdrant推出向量搜索"学院"](https://twitter.com/qdrant_engine/status/1981319267749679599)
> Qdrant启动向量搜索"学院"，为开发者提供向量数据库和搜索技术的学习资源。

---

### 9. [Modular发布Mojo GPU"谜题"](https://twitter.com/Modular/status/1981455872137318556)
> Modular发布Mojo GPU"谜题"，用于实践CUDA/Metal学习，帮助开发者更好地理解GPU编程。

---

### 10. [Runway推出"广告应用"集合](https://twitter.com/runwayml/status/1981380360249159783)
> Runway发布"广告应用"集合，将常见视频/图像工作流程产品化，无需复杂提示即可使用，降低创意工作的技术门槛。

---