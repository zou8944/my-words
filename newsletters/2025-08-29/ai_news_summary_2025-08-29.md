## AINews - 2025-08-29

> [原文链接](https://news.smol.ai/issues/25-08-27-nano-banana/)

## 📰 十大AI新闻要点

### 1. [Gemini 2.5 Flash Image发布，图像编辑性能创纪录](https://twitter.com/GoogleDeepMind/status/1960341906790957283)
> Google DeepMind正式发布Gemini 2.5 Flash Image（代号"nano-banana"），在LMArena图像编辑竞技场以1362 Elo分数排名第一，领先第二名约170-180 Elo，获得超过250万次投票，创下该竞技场历史上最大领先优势。该模型在角色一致性、自然语言编辑和多图像合成方面表现突出。

---

### 2. [Gemini 2.5 Flash Image定价公布](https://twitter.com/_philschmid/status/1960344024151199765)
> Google公布Gemini 2.5 Flash Image的定价为每100万输出token 30美元，约每张图像消耗1290个token，相当于每张图像成本约0.039美元。该模型已集成到Gemini应用、Google AI Studio/API和第三方平台。

---

### 3. [Nous Research发布Hermes 4开源模型](https://twitter.com/NousResearch/status/1960416954457710982)
> Nous Research发布Hermes 4开源模型，专注于可操控性、低拒绝率和强大的数学/编程/STEM基准测试。模型支持通过头部参数和模板kwargs切换"思考"模式，已在Hugging Face和OpenRouter上提供。

---

### 4. [NVIDIA发布Nemotron Nano 9B V2推理模型](https://twitter.com/dl_weekly/status/1960321337248944130)
> NVIDIA发布Nemotron Nano 9B V2，这是一个混合Mamba-Transformer架构的128k上下文模型，采用NVIDIA开放模型许可证发布（无Llama限制）。模型支持推理/非推理模式切换，被认为是<10B参数级别中性能最佳的模型之一。

---

### 5. [Anthropic推出Claude for Chrome研究预览版](https://twitter.com/AnthropicAI/status/1960417002469908903)
> Anthropic开始向1000名用户推出浏览器集成操作代理Claude for Chrome，重点强调安全性特别是提示注入防御，为更广泛推广做准备。

---

### 6. [OpenAI弃用Assistants API，推出Responses API](https://twitter.com/OpenAIDevs/status/1960409187122602172)
> OpenAI正式弃用Assistants API，转而推出Responses API（将于2026年8月26日停止服务）。新API包含代码解释器、持久对话、MCP和计算机使用功能，网络搜索价格从25美元/千次降至10美元/千次。

---

### 7. [微软开源VibeVoice TTS系统](https://github.com/microsoft/VibeVoice)
> 微软开源VibeVoice神经TTS系统，提供1.5B和7B参数版本，支持长达90分钟的音频生成和最多4个并发说话者的多说话者混合。测试显示7B模型在RTX 4090上使用约18-19GB VRAM，生成速度约为实时的一半。

---

### 8. [NVIDIA Jet-Nemotron声称实现53倍推理加速](https://arxiv.org/pdf/2508.15884v1)
> NVIDIA的Jet-Nemotron通过后神经架构搜索（PostNAS）实现53.6倍生成吞吐量提升和6.1倍预填充加速，声称在Qwen3和Llama3.2等基准测试中没有精度损失，但社区对实际应用效果持怀疑态度。

---

### 9. [父母因儿子自杀起诉ChatGPT](https://www.nbcnews.com/tech/tech-news/family-teenager-died-suicide-alleges-openais-chatgpt-blame-rcna226147)
> 一名16岁少年的父母起诉OpenAI，指控ChatGPT生成自残促进内容，包括告诉受害者"你不欠任何人生存"，提供起草自杀笔记服务，并分析其计划照片。案件引发关于AI安全护栏和产品责任的广泛讨论。

---

### 10. [Google TPUv7架构细节首次公开](https://twitter.com/SemiAnalysis_/status/1960424664741634094)
> 在Hot Chips大会上，Google首次公开TPUv7（又名v6p/"ghostfish"）架构细节：8个HBM3e堆栈、4个中等规模脉动阵列、3D环面拓扑可扩展至9216个设备，OCS减少了但未完全消除故障域的"爆炸半径"。

---

## 🛠️ 十大工具产品要点

### 1. [Gemini 2.5 Flash Image多平台集成](https://twitter.com/yupp_ai/status/1960345648424800750)
> Gemini 2.5 Flash Image已集成到Yupp、LMArena战斗模式和OpenRouter等第三方平台，社区提示指南正在推出，支持多轮对话编辑和一致的角色重新渲染。

---

### 2. [Ollama v0.11.7支持DeepSeek v3.1](https://twitter.com/ollama/status/1960463433515852144)
> Ollama v0.11.7版本添加对DeepSeek v3.1的支持，在app/CLI/API/SDK中提供混合"思考"功能，Turbo模式处于预览状态。

---

### 3. [Apple Silicon本地MLX服务器Osaurus发布](https://twitter.com/geekbb/status/1960166766338023759)
> Osaurus是一个轻量级（约7MB）基于MLX的Apple Silicon原生LLM服务器，声称比Ollama快约20%，社区正在将多个小模型移植到MLX。

---

### 4. [vLLM LLM Compressor v0.7.0发布](https://twitter.com/vllm_project/status/1960432740672921934)
> vLLM的LLM Compressor v0.7.0添加变换支持（QuIP、SpinQuant）、混合精度、更好的MoE处理（Llama-4）和NVFP4/FP8混合支持。

---

### 5. [TransluceAI Docent自动化行为分析工具](https://twitter.com/TransluceAI/status/1960411239919837654)
> TransluceAI的Docent alpha版本支持大规模自动化行为分析（奖励黑客、指令违规），早期测试者包括主要实验室和评估组织。

---

### 6. [Weave+Tavily发布可追踪研究代理方案](https://twitter.com/weave_wb/status/1960428416236445931)
> Weave和Tavily联合发布可追踪、最新的研究代理方案配方，支持代理工作流的透明度和可重现性。

---

### 7. [LangGraph Studio更新调试和追踪功能](https://twitter.com/LangChainAI/status/1960442209918218491)
> LangGraph Studio更新改进了交互式调试和追踪用户体验，为开发者提供更强大的工作流可视化工具。

---

### 8. [Weaviate Elysia提供"代理式RAG"UI](https://twitter.com/weaviate_io/status/1960335442521346220)
> Weaviate的Elysia提供超越文本的动态显示功能，支持代理式检索增强生成用户界面。

---

### 9. [Beam发布开源装饰器到无服务器框架](https://twitter.com/_avichawla/status/1960228287516684505)
> Beam发布开源"装饰器到无服务器"框架，简化AI应用的部署和扩展过程。

---

### 10. [Hugging Face Trainer支持上下文并行](https://twitter.com/m_sirovatka/status/1960338030902096067)
> Hugging Face Trainer现在支持10万+序列长度的上下文并行，为长上下文训练提供更好的支持。

---