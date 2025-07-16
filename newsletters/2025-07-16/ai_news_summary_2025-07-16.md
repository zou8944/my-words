## AINews - 2025-07-16

> [原文链接](https://news.smol.ai/issues/25-07-15-thinky/)

## 📰 十大AI新闻要点

### 1. [Mistral发布开源语音转录模型Voxtral](https://x.com/GuillaumeLample/status/1945161150900924490)
> Mistral AI推出Voxtral系列开源语音模型，包含3B和24B两个版本，支持32k token上下文长度，可处理30-40分钟音频，具备多语言转录、内置问答和摘要功能，并可直接从语音触发API调用。

### 2. [Kimi K2模型挑战西方AI巨头](https://twitter.com/teortaxesTex/status/1944856509734961596)
> Moonshot AI发布的Kimi K2非推理型MoE模型以200人团队和有限GPU预算开发，在Groq硬件上达到185 tokens/秒推理速度，1T参数模型可运行于M4 Max 128GB Mac。

### 3. [xAI推出Grok虚拟伴侣功能](https://twitter.com/chaitualuru/status/1945053158071255257)
> xAI的Grok新增AI虚拟伴侣功能，包含动漫角色"Ani"等个性化形象，在日本市场引发热潮，用户可通过互动解锁更高级别内容。

### 4. [Meta将建成首个1GW超级计算集群](https://twitter.com/AIatMeta/status/1945182467088113920)
> Meta宣布正在建设多个GW级超级计算集群(包括Prometheus和Hyperion)，目标成为首个拥有1GW计算能力的实验室，推动个人超级智能发展。

### 5. [LG发布EXAONE 4.0 32B模型](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-32B)
> LG的32B参数多语言模型支持131k token上下文窗口，具备可切换推理模式，在多项基准测试中超越Qwen 3 32B，但采用严格非商业许可。

### 6. [Runway推出新一代动作捕捉模型Act-Two](https://twitter.com/c_valenzuelab/status/1945190630449172587)
> RunwayML的Act-Two模型在手部动作生成和质量上有显著提升，支持创作文艺复兴风格人声打击乐等创新内容。

### 7. [Google Gemini嵌入模型登顶MTEB榜单](https://twitter.com/demishassabis/status/1944870402251219338)
> Google DeepMind宣布Gemini Embedding模型正式发布并在MTEB排行榜位列第一，同时新增照片转有声视频功能。

### 8. [AI行业推动"思维链监控"标准化](https://twitter.com/OpenAI/status/1945156362859589955)
> OpenAI、Anthropic等机构联合倡议保留AI推理过程的可监控性，认为思维链(CoT)是监管智能体系统的关键安全机制。

### 9. [Meta取消Llama 4 Behemoth开源计划](https://analyticsindiamag.com/global-tech/meta-plans-to-abandon-llama-4-behemoth-but-why/)
> Meta因技术问题放弃开源2T参数的Llama 4 Behemoth，问题包括分块注意力导致长上下文推理能力下降和MoE路由不稳定。

### 10. [Chroma报告揭示"上下文腐烂"现象](https://twitter.com/swyx/status/1944848537092809177)
> 研究显示随着输入token增加，LLM性能会下降，113k token的对话历史可能导致30%准确率下降，质疑百万token上下文窗口的实际效用。

---

## 🛠️ 十大工具产品要点

### 1. [Voxtral语音转录API](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507)
> Mistral的Voxtral提供API和Hugging Face集成，支持英语、西班牙语等8种主要语言，转录30分钟音频仅需9.5GB GPU内存(bf16/fp16)。

### 2. [Kimi K2开发者工具集成](https://huggingface.co/moonshotai/Kimi-K2-Instruct)
> Kimi K2已集成到LangChain、Cline等开发工具，DeepInfra提供$0.55/$2.20每百万token的API服务，支持Anthropic兼容接口。

### 3. [Qdrant Cloud推理服务](https://twitter.com/qdrant_engine/status/1945090285039464518)
> Qdrant推出云端嵌入生成和索引服务，支持CLIP等多模态模型，可直接在集群中处理密集/稀疏向量。

### 4. [Unsloth量化工具支持Kimi K2](https://docs.unsloth.ai/basics/datasets-guide#synthetic-data-generation)
> Unsloth提供Kimi K2模型的1.8-bit量化版本，显著降低内存需求，使大模型能在消费级硬件运行。

### 5. [MLX框架扩展至tvOS](https://twitter.com/awnihannun/status/1944893455202967921)
> Apple的MLX机器学习框架新增tvOS支持和C++版本(mlx-lm.cpp)，持续扩大跨平台部署能力。

### 6. [LEAP移动端LLM平台](https://twitter.com/maximelabonne/status/1945110321938514335)
> 新推出的LEAP平台支持在iOS/Android设备本地运行LLM，为移动端AI应用开发提供解决方案。

### 7. [Perplexity Comet浏览器新增语音模式](https://twitter.com/AravSrinivas/status/1944861476692615333)
> Perplexity的AI浏览器Comet增加语音交互和邮箱整理功能，目标是创建无缝的多工具融合体验。

### 8. [N8N无代码AI代理平台](https://n8n.io/)
> 可视化工作流平台N8N支持构建定制AI代理，解决预约管理等商业问题，高级解决方案价值5k-8k美元。

### 9. [Torchtune宽松许可框架](https://github.com/pytorch/torchtune/issues/2883)
> Torchtune采用BSD 3许可，允许开发者自由提取组件用于其他项目，社区持续维护Discord和GitHub支持。

### 10. [LMArena模型竞技场](https://lmarena.ai/leaderboard/text)
> 开源模型评测平台新增ernie-x1-turbo-32k等中文模型，但用户报告界面存在连续聊天中模型切换混乱的问题。