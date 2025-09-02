## AINews - 2025-09-02

> [原文链接](https://news.smol.ai/issues/25-08-29-not-much/)

## 📰 十大AI新闻要点

### 1. [Apple发布FastVLM和MobileCLIP2实时视觉语言模型](https://twitter.com/reach_vb/status/1961471154197053769)
> Apple在Hugging Face上发布了三个实时视觉语言模型（0.5B、1.5B、7B），支持WebGPU/transformers.js演示和MLX/Core ML。声称比之前工作快85倍、小3.4倍，通过减少视觉token和精简编码器实现7.9倍更快的首token时间。实时视频字幕可在浏览器中100%本地运行。

---

### 2. [xAI的grok-code-fast-1在Cline中表现卓越](https://twitter.com/cline/status/1961488289803939915)
> Cline用户报告grok-code-fast-1在差异编辑和复杂重构上感觉比Claude快10倍且更好，早期数据显示约87 TPS，经过三天迭代后在差异编辑失败率上与Sonnet-4持平。xAI通过Cline的重型跟踪频繁发布检查点。

---

### 3. [OpenAI将GPT-5集成到Xcode 26中](https://twitter.com/OpenAIDevs/status/1961557515331862853)
> OpenAI宣布GPT-5内置到Xcode 26中，通过登录ChatGPT可获得更高限制。同时推出了VS Code的Codex插件，被评价为"已经非常不错"。

---

### 4. [单向量嵌入遇到瓶颈，ColBERT式后期交互成为解决方案](https://twitter.com/orionweller/status/1961436569409331579)
> 理论和实证表明单向量无法满足现代检索任务需求。ColBERT风格的后期交互避免了基本权衡，开源后期交互栈pylate提供了技术支持。

---

### 5. [Claude Opus 4.1在多步软件工程任务上实现1小时45分钟时间跨度](https://twitter.com/METR_Evals/status/1961527692072993272)
> METR评估显示Claude Opus 4.1在多步软件工程任务上达到50%成功率的约1小时45分钟时间跨度，比Opus 4长约30%，具有统计显著性。

---

### 6. [Step-Audio 2 Mini开源8B语音到语音模型](https://twitter.com/reach_vb/status/1961414067668558319)
> StepFun AI发布Apache-2.0许可的8B参数语音到语音模型，声称在内部评估中击败GPT-4o-Audio，支持5万+声音，基于Qwen2-Audio + CosyVoice构建。

---

### 7. [Alibaba开发国产AI推理芯片替代Nvidia](https://www.wsj.com/tech/ai/alibaba-ai-chip-nvidia-f5dc96e3)
> 华尔街日报报道阿里巴巴正在测试国产AI推理芯片，旨在填补中国市场的Nvidia空缺，保持与Nvidia生态系统的兼容性，采用国内代工厂制造。

---

### 8. [Meta取消Behemoth大语言模型的公开发布计划](https://www.ft.com/content/feccb649-ce95-43d2-b30a-057d64b38cdf)
> 金融时报报道Meta已放弃公开发布旗舰Behemoth LLM的计划，转而专注于构建新模型，并考虑从初创公司许可AI技术来缩小与竞争对手的性能差距。

---

### 9. [Anthropic澄清数据保留政策](https://twitter.com/michael_nielsen/status/1961439837791367501)
> Anthropic澄清如果用户选择退出训练，数据保留期仍为30天；否则适用更长的保留期。多位开发者呼吁在产品中提供更清晰的披露。

---

### 10. [Unitree G1人形机器人在乒乓球对打中实现100+回合](https://v.redd.it/eaof7erhyvlf1)
> Unitree G1人形机器人在与人类的乒乓球对打中持续100+回合，展示了高频率感知到控制的可靠性，虽然是在高度受控的环境中进行的演示。

---

## 🛠️ 十大工具产品要点

### 1. [Apple MLX添加MXFP4支持](https://twitter.com/awnihannun/status/1961484829037330612)
> Apple MLX添加了对GPT-OSS使用的MXFP4支持，可通过pip install -U mlx升级。LM Studio确认在MLX中对openai/gpt-oss提供MXFP4支持。

---

### 2. [SemTools提供无需向量数据库的语义搜索](https://twitter.com/LoganMarkewich/status/1961448960184520945)
> run-llama的SemTools提供shell语义搜索，无需向量数据库，通过parse和search功能实现400倍更快的静态嵌入。

---

### 3. [MLX推出"ollama风格"本地运行器](https://twitter.com/tom_doerr/status/1961309536406392877)
> 为Apple Silicon推出的MLX "ollama风格"本地运行器，支持本地模型运行和推理。

---

### 4. [FastMCP一键式MCP服务器+聊天客户端](https://twitter.com/fastmcp/status/1961436552057278512)
> FastMCP提供一键推送的MCP服务器和聊天客户端，简化模型上下文协议的使用。

---

### 5. [llama.vim推荐Qwen 3 Coder 30B A3B](https://twitter.com/ggerganov/status/1961471397428883882)
> llama.vim现在推荐在Mac上使用Qwen 3 Coder 30B A3B，通过llama.cpp在本地编码中表现优于Qwen 2.5 Coder 7B。

---

### 6. [Weaviate推出8位旋转量化](https://twitter.com/dl_weekly/status/1961413948877553899)
> Weaviate详细介绍了8位旋转量化，通过随机旋转+标量量化实现4倍压缩，更快的向量搜索和质量提升。

---

### 7. [UC Berkeley的XQuant/XQuant-CL内存优化技术](https://twitter.com/TheTuringPost/status/1961475078753063322)
> XQuant/XQuant-CL从量化激活中重新生成K/V，实现2×到12.5×的内存削减，精度损失最小，通过SVD处理GQA。

---

### 8. [MCP-Bench工具使用LLM基准测试发布](https://twitter.com/_akhaliq/status/1961456699564294651)
> 多个新的MCP-Bench版本正在出现，用于工具使用LLM的基准测试，标准化工具调用评估需求激增。

---

### 9. [DeepScholar-Bench生成研究合成基准](https://twitter.com/lianapatel_/status/1961487232331911651)
> 斯坦福/伯克利的实时DeepScholar-Bench针对生成研究合成，提供排行榜、代码和论文链接。

---

### 10. [环境中心作为开放AGI堆栈的一部分](https://twitter.com/vincentweisser/status/1961594111733158141)
> 环境中心作为更广泛开放AGI堆栈（计算、沙盒、RFT、评估）的一部分宣布，提供开放基础设施支持代理开发。

---