## AINews - 2025-08-23

> [原文链接](https://news.smol.ai/issues/25-08-21-cohere-command-a-reasoning/)

## 📰 十大AI新闻要点

### 1. [Cohere发布Command A Reasoning开源推理模型](https://x.com/cohere/status/1958542682890047511)
> Cohere推出企业级推理模型Command A Reasoning，提供开源权重供研究和私有部署，商业使用需Cohere许可。该模型在工具使用和智能体基准测试中表现强劲，强调安全性与实用性的平衡，减少过度拒绝。

---

### 2. [DeepSeek发布V3.1混合推理模型](https://twitter.com/deepseek_ai/status/1958417062008918312)
> DeepSeek-V3.1是671B参数的MoE模型，支持通过特殊标记切换"推理"和"非推理"模式，专注于智能体用例和编码工作流。在SWE-Bench Verified上达到66%（非推理模式），支持164K上下文窗口，API定价为$0.56/M输入和$1.68/M输出。

---

### 3. [Google公布Gemini推理能效提升33倍](https://twitter.com/JeffDean/status/1958525015722434945)
> Google详细展示了Gemini推理能效：中位数文本提示消耗约0.24 Wh和0.26 ml水。从2024年5月到2025年5月，每个提示的能耗下降33倍，碳足迹减少44倍，得益于模型/系统效率和清洁能源。

---

### 4. [Google搜索AI模式升级为多步骤智能体](https://twitter.com/Google/status/1958530316072534323)
> Google搜索的AI模式现在可以规划和执行多步骤任务（如跨网站餐厅预订），个性化结果并共享会话上下文，正在向180多个国家和地区的英语用户推出。

---

### 5. [OpenAI Responses API新增连接器和会话功能](https://twitter.com/OpenAIDevs/status/1958660207745409120)
> OpenAI Responses API新增"Connectors"功能，可单次调用从Gmail/Calendar/Dropbox等获取上下文；"Conversations"添加持久线程存储，无需自建聊天数据库。

---

### 6. [NVIDIA发布Nemotron Nano 2混合推理模型](https://twitter.com/_akhaliq/status/1958545622618788174)
> NVIDIA宣布Nemotron Nano 2作为混合Mamba-Transformer推理模型，虽然公开细节有限，但值得关注作为NVIDIA小规模推理产品线的发展。

---

### 7. [ByteDance发布Seed-OSS-36B开源模型](https://github.com/orgs/bytedance/repositories)
> ByteDance发布Seed-OSS-36B-Base-woSyn，这是一个36B密集模型，具有512K上下文窗口，在12T token上训练且无合成数据，专注于长上下文能力。

---

### 8. [新评估基准MM-BrowseComp发布](https://twitter.com/GeZhang86038849/status/1958381269617955165)
> MM-BrowseComp包含224个多模态网络任务（文本+图像+视频）用于智能体评估，提供代码、HF数据集和arXiv论文。

---

### 9. [DuPO双偏好优化方法实现自监督验证](https://twitter.com/iScienceLuvr/status/1958467512296939593)
> DuPO通过对偶性生成自监督反馈，实现可靠的自验证而无需外部标注，支持框架可逆性（如反向数学解恢复隐藏变量）。

---

### 10. [Perplexity Finance推出印度股票自然语言筛选](https://twitter.com/AravSrinivas/status/1958385027185877066)
> Perplexity Finance为印度股票推出自然语言筛选功能，覆盖多个界面，为用户提供智能投资分析工具。

---

## 🛠️ 十大工具产品要点

### 1. [DeepSeek-V3.1支持Anthropic API兼容](https://api-docs.deepseek.com/guides/anthropic_api)
> DeepSeek-V3.1实现与Anthropic API的完全兼容，允许现有Anthropic集成应用通过更改基础URL和模型名称无缝切换到DeepSeek后端，降低迁移成本。

---

### 2. [vLLM和SGLang支持DeepSeek-V3.1推理模式切换](https://twitter.com/vllm_project/status/1958580047658491947)
> vLLM和SGLang现已支持DeepSeek-V3.1的"思考/非思考"模式切换，为开发者提供灵活的推理配置选项。

---

### 3. [MLX生态系统新增多模态支持](https://twitter.com/Prince_Canuma/status/1958469233622327785)
> MLX-VLM 0.3.3添加GLM-4.5V和Command-A-Vision支持；JinaAI MLX-retrieval实现本地Gemma3-270m嵌入/重排，在M3 Ultra上达到约4000 token/秒。

---

### 4. [LlamaParse新增引用和智能体模式](https://twitter.com/VikParuchuri/status/1958520215844655576)
> LlamaParse现在支持引用生成和多种模式（成本效益/智能体/智能体+），提升文档解析和RAG应用的效果。

---

### 5. [Weaviate Elysia提供智能体RAG可视化](https://twitter.com/weaviate_io/status/1958568536420299184)
> Weaviate的Elysia功能提供决策树智能体RAG，带有实时推理可视化，增强检索增强生成的可解释性。

---

### 6. [Cursor与Linear集成直接启动智能体](https://twitter.com/cursor_ai/status/1958627514852811034)
> Cursor现在可与Linear问题跟踪系统集成，直接从问题/评论中启动AI智能体，提升开发工作流效率。

---

### 7. [Google推出Veo 3 Next.js视频工作室模板](https://twitter.com/googleaidevs/status/1958599306472206349)
> Google开发者发布Next.js模板，用于构建浏览器内AI视频工作室，使用Veo 3和Imagen 4技术。

---

### 8. [W&B Inference新增DeepSeek V3.1支持](https://twitter.com/weave_wb/status/1958681269484880026)
> Weights & Biases Inference现在支持DeepSeek V3.1模型，定价为$0.55/M输入和$1.65/M输出token。

---

### 9. [Chutes提供DeepSeek V3.1托管服务](https://twitter.com/chutes_ai/status/1958507978476106196)
> Chutes AI平台提供DeepSeek V3.1的定价托管服务，为开发者提供便捷的模型部署选项。

---

### 10. [Baseten优化DeepSeek V3.1延迟性能](https://twitter.com/basetenco/status/1958515897972232526)
> Baseten平台针对DeepSeek V3.1进行延迟优化跟踪，提供更高效的模型服务性能。

---