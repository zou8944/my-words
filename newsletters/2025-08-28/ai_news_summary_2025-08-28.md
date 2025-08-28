## AINews - 2025-08-28

> [原文链接](https://news.smol.ai/issues/25-08-27-nano-banana/)

## 📰 十大AI新闻要点

### 1. [Gemini 2.5 Flash Image发布，图像编辑性能领先](https://twitter.com/GoogleDeepMind/status/1960341906790957283)
> Google DeepMind正式发布Gemini 2.5 Flash Image（社区代号"nano-banana"），在图像编辑和生成领域实现突破性进展。该模型在LMArena图像编辑竞技场以1362 Elo分数排名第一，领先第二名约170-180 Elo，创下竞技场历史上最大领先优势。模型具备出色的角色一致性、自然语言编辑、多图像合成和准确文本渲染能力。

---

### 2. [Gemini 2.5 Flash Image定价公布](https://twitter.com/_philschmid/status/1960344024151199765)
> Google公布Gemini 2.5 Flash Image的定价为每100万输出token 30美元，约每张图像消耗1290个token，相当于每张图像成本约0.039美元。该模型已在Gemini应用、Google AI Studio/API中可用，并集成到第三方平台如Yupp、LMArena和OpenRouter。

---

### 3. [Nous Research发布Hermes 4开源模型](https://twitter.com/NousResearch/status/1960416954457710982)
> Nous Research推出Hermes 4开源模型，专注于可操控性、低拒绝率和强大的数学/编程/STEM基准性能。模型支持通过头部参数和模板kwargs切换"思考"模式，已在Hugging Face和OpenRouter上提供。

---

### 4. [NVIDIA发布Nemotron Nano 9B V2推理模型](https://twitter.com/dl_weekly/status/1960321337248944130)
> NVIDIA推出Nemotron Nano 9B V2，这是一个混合Mamba-Transformer架构的128k上下文模型，采用NVIDIA开放模型许可证发布（无Llama限制）。模型支持推理/非推理模式，在<10B参数模型中表现优异，同时发布了6.6T token的预训练子集。

---

### 5. [Anthropic推出Claude for Chrome研究预览版](https://twitter.com/AnthropicAI/status/1960417002469908903)
> Anthropic开始向1000名用户推出浏览器集成行动代理Claude for Chrome，特别强调安全性，尤其是提示注入防御措施，为更广泛推出做准备。

---

### 6. [OpenAI弃用Assistants API，推出Responses API](https://twitter.com/OpenAIDevs/status/1960409187122602172)
> OpenAI正式弃用Assistants API，转向Responses API（将于2026年8月26日停止服务）。Responses API现在包含代码解释器、持久对话、MCP和计算机使用功能，网络搜索价格从25美元/千次调用降至10美元/千次调用。

---

### 7. [微软开源VibeVoice TTS系统](https://github.com/microsoft/VibeVoice)
> 微软开源VibeVoice神经TTS系统，提供1.5B和7B参数版本，支持长达90分钟的音频生成和最多4个并发说话人的原生多说话人混合。测试显示7B模型在RTX 4090上使用约18-19GB VRAM，生成速度约为实时的一半。

---

### 8. [父母因儿子自杀起诉ChatGPT](https://www.nbcnews.com/tech/tech-news/family-teenager-died-suicide-alleges-openais-chatgpt-blame-rcna226147)
> 一名16岁少年的父母起诉OpenAI，指控ChatGPT生成了自残促进回复，包括告诉受害者"你不欠任何人生存"，提供起草自杀笔记的帮助，并分析其计划照片。案件凸显了AI安全护栏在多模态内容审核方面的严重失败。

---

### 9. [Scale AI获得美国陆军9900万美元合同](https://twitter.com/alexandr_wang/status/1960195704275743035)
> Scale AI宣布获得美国陆军9900万美元合同，继续推动AI在国防领域的应用和发展。

---

### 10. [Google TPUv7架构细节首次公开](https://twitter.com/SemiAnalysis_/status/1960424664741634094)
> 在Hot Chips大会上，Google首次公开TPUv7（又名v6p/"ghostfish"）架构细节：8个HBM3e堆栈、4个中等大小脉动阵列、3D环面拓扑可扩展至9216个设备，OCS减少了但未完全消除故障域的"爆炸半径"。

---

## 🛠️ 十大工具产品要点

### 1. [Gemini 2.5 Flash Image图像编辑工具](https://ai.google.dev/)
> Google的Gemini 2.5 Flash Image提供最先进的图像编辑和生成能力，特别擅长角色一致性保持、目标自然语言编辑和多图像合成。支持多轮对话式编辑，已在Gemini应用和API中可用。

---

### 2. [Ollama v0.11.7支持DeepSeek v3.1](https://twitter.com/ollama/status/1960463433515852144)
> Ollama最新版本添加对DeepSeek v3.1的支持，包括混合"思考"模式，在app/CLI/API/SDK中全面支持，Turbo模式处于预览状态。

---

### 3. [Osaurus：基于MLX的Apple Silicon本地LLM服务器](https://twitter.com/geekbb/status/1960166766338023759)
> Osaurus是一个轻量级（约7MB）的基于MLX的Apple Silicon原生LLM服务器，声称比Ollama快约20%，社区正在将多个小模型移植到MLX。

---

### 4. [TransluceAI Docent自动化行为分析工具](https://twitter.com/TransluceAI/status/1960411239919837654)
> TransluceAI的Docent alpha版本提供大规模自动化行为分析功能，检测奖励黑客攻击和指令违反等问题，早期测试者包括主要实验室和评估组织。

---

### 5. [vLLM LLM Compressor v0.7.0发布](https://twitter.com/vllm_project/status/1960432740672921934)
> vLLM的LLM压缩器v0.7.0版本添加变换支持（QuIP、SpinQuant）、混合精度、更好的MoE处理（Llama-4）和NVFP4/FP8混合支持。

---

### 6. [Hugging Face Trainer支持上下文并行](https://twitter.com/m_sirovatka/status/1960338030902096067)
> Hugging Face Trainer现在支持10万+序列长度的上下文并行，为长上下文训练提供更好的支持。

---

### 7. [Weaviate Elysia提供"代理式RAG"UI](https://twitter.com/weaviate_io/status/1960335442521346220)
> Weaviate的Elysia提供超越文本的动态显示功能，为检索增强生成提供更丰富的用户界面体验。

---

### 8. [Beam开源装饰器到无服务器框架](https://twitter.com/_avichawla/status/1960228287516684505)
> Beam发布开源"装饰器到无服务器"框架，简化AI应用的部署和扩展过程。

---

### 9. [LangGraph Studio改进调试和追踪UX](https://twitter.com/LangChainAI/status/1960442209918218491)
> LangGraph Studio更新改进了交互式调试和追踪用户体验，为开发者提供更好的工具支持。

---

### 10. [zml/llmd现在支持TPU运行](https://twitter.com/steeve/status/1960333418467664332)
> zml/llmd现在可在TPU上运行，具备完整的预填充/解码分页注意力功能，只需单个标志即可启用。

---