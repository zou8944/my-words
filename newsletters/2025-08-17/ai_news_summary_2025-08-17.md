## AINews - 2025-08-17

> [原文链接](https://news.smol.ai/issues/25-08-15-not-much/)

## 📰 十大AI新闻要点  

### 1. [GPT-5 成为 ChatGPT 默认模型，新增 Auto/Fast/Thinking 模式](https://twitter.com/OpenAI/status/1956212769365352758)  
> OpenAI 宣布 GPT-5 成为 ChatGPT 默认模型，提供 Auto/Fast/Thinking 三种模式。Plus/Team 用户每周可使用 3000 条 GPT-5 Thinking 消息，企业/教育版也已上线。  

---

### 2. [OpenAI 推出更“温暖”的 GPT-5 默认人格](https://twitter.com/OpenAI/status/1956461718097494196)  
> OpenAI 调整 GPT-5 的默认人格，使其更友好（如“Good question”），但声称不会增加“奉承”行为，用户仍可通过 Custom Instructions 自定义风格。  

---

### 3. [LMSYS 更新竞技场排名：GPT-5 表现参差](https://twitter.com/lmarena_ai/status/1956399522688692608)  
> GPT-5 默认版本（gpt-5-chat）排名第5，而 GPT-5-High 仍居榜首。评测指出其在编码任务上逊于部分中文模型，且对“奉承”敏感。  

---

### 4. [Google 发布 Imagen 4 和 Gemma 3 270M](https://twitter.com/_philschmid/status/1956351654753673252)  
> Imagen 4 支持 2K 分辨率图像生成，速度提升 10 倍；Gemma 3 270M 专为边缘计算优化，在 iPad Air M3 上达 200 tok/s。  

---

### 5. [XLANG 开源 OpenCUA 计算机使用代理框架](https://twitter.com/xywang626/status/1956400403911962757)  
> OpenCUA 提供 7B/32B 模型及 22.6K 轨迹数据集，在 OSWorld 基准测试中达到 34.8%，媲美商业模型。  

---

### 6. [NVIDIA 开放 Granary 语音数据集及 Canary-1b-v2 模型](https://twitter.com/Tu7uruu/status/1956350036343701583)  
> 包含欧盟最大开源语音数据集和 25 种语言的 ASR/翻译模型，Argmax 已提供 Parakeet v3 支持。  

---

### 7. [DeepSeek-V3 成本仅为 GPT-4o 的 10%](https://i.redd.it/o5jfkiky14jf1.png)  
> DeepSeek-V3 在多数基准测试中优于 GPT-4o，输入/输出成本分别为 $0.27/$1.10（GPT-4o 为 $2.50/$10.00）。  

---

### 8. [Meta 发布 DINOv3：自监督视觉模型](https://ai.meta.com/dinov3/)  
> 无需标注数据，在分割、深度估计等任务上达到 SOTA，7B 参数版本引入“Gram Anchoring”技术防止特征退化。  

---

### 9. [ClipTagger-12B 开源视频标注模型超越 Claude 4 Sonnet](https://www.reddit.com/r/LocalLLaMA/comments/1mqi092/we_built_a_12b_model_that_beats_claude_4_sonnet/)  
> 基于 Gemma-12B，评测得分 3.53（Claude 4 Sonnet 为 3.16），成本低 17 倍（$335/百万帧）。  

---

### 10. [中国电网优势或成 AI 竞赛关键](https://fortune.com/2025/08/14/data-centers-china-grid-us-infrastructure/)  
> 中国电网储备容量达 80-100%，远超美国的 15%，可轻松支持 AI 数据中心扩张，而美国面临基础设施瓶颈。  

---

## 🛠️ 十大工具产品要点  

### 1. [OpenAI 开发者面板新增“Quick Eval”功能](https://twitter.com/OpenAIDevs/status/1956410610914414904)  
> 支持对比 GPT-5 变体性能，内置评分器可评估模型响应质量。  

---

### 2. [OpenAI 发布《GPT-5 编码六技巧》及开发者门户](http://developers.openai.com/)  
> 提供优化提示、路由策略等建议，整合 Playground 的向量存储和评估工具。  

---

### 3. [Guardrails 推出 Snowglobe 代理压力测试工具](https://twitter.com/godofprompt/status/1956359876109652297)  
> 模拟数百种人格对话以暴露代理缺陷，将失败转化为训练信号。  

---

### 4. [Cursor CLI 新增 MCP 和 Review Mode](https://twitter.com/cursor_ai/status/1956458242655281339)  
> 支持工具增强编码，引入 `/compress` 和 `@-file` 引用功能。  

---

### 5. [LangGraph Studio 推出“Trace Mode”](https://twitter.com/LangChainAI/status/1956411858312949946)  
> 实时集成 LangSmith 追踪数据，便于调试多模态工作流。  

---

### 6. [Windsurf Wave 12 IDE 更新](https://windsurf.com/changelog)  
> 新增 DeepWiki 悬停解释、Vibe & Replace 批量编辑，支持 Dev Containers。  

---

### 7. [LlamaIndex 发布股票代理与法律知识图谱模板](https://t.co/fQDNPIQoqR)  
> 结合 CopilotKit 和 Neo4j，提供端到端 RAG 解决方案。  

---

### 8. [MLX Knife 本地 OpenAI 兼容服务器](https://github.com/mzau/mlx-knife)  
> 支持 Apple Silicon 设备快速部署和测试本地模型。  

---

### 9. [Nous Research 推出“Token 效率”基准](https://nousresearch.com/measuring-thinking-efficiency-in-reasoning-models-the-missing-benchmark/)  
> 评测显示开源模型token消耗为闭源的1.5-4倍，影响生产成本。  

---

### 10. [1.58 位 Transformer 训练方法论文](https://arxiv.org/html/2411.06360v3)  
> 通过 α,1-稀疏性实现近无损低比特训练，有望降低推理成本。  

---