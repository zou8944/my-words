## AINews - 2025-07-17

> [原文链接](https://news.smol.ai/issues/25-07-15-thinky/)

## 📰 十大AI新闻要点

### 1. [Mistral发布开源语音转录模型Voxtral](https://x.com/GuillaumeLample/status/1945161150900924490)
> Mistral AI推出Voxtral系列开源语音转录模型，包含3B和24B两个版本，支持32k token上下文长度，可处理30-40分钟音频，具备多语言转录、内置问答和摘要功能，性能超越Whisper large-v3和GPT-4o mini Transcribe。

---

### 2. [Kimi K2模型挑战西方AI巨头](https://twitter.com/teortaxesTex/status/1944856509734961596)
> Moonshot AI发布的Kimi K2非推理型MoE模型以200人团队和有限GPU预算开发，在Groq硬件上实现185 tokens/秒推理速度，1T参数模型可运行于M4 Max 128GB Mac，被社区誉为"领先的开源非推理模型"。

---

### 3. [xAI推出Grok虚拟伴侣功能](https://twitter.com/chaitualuru/status/1945053158071255257)
> xAI发布Grok虚拟伴侣和头像功能，包含动漫角色"Ani"等个性化AI形象，在日本市场迅速走红，展示AI社交互动的新方向。

---

### 4. [Meta计划建设1GW超级计算集群](https://twitter.com/AIatMeta/status/1945182467088113920)
> Meta宣布将建立首个1GW规模的AI超级计算集群，包括Prometheus和Hyperion项目，旨在为全球用户提供"个人超级智能"，引发对开源AI未来的担忧。

---

### 5. [LG发布EXAONE 4.0 32B多语言模型](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-32B)
> LG AI Research推出EXAONE 4.0-32B模型，支持英语、韩语和西班牙语，具备131k token上下文窗口和可切换推理模式，性能超越Qwen 3 32B，但采用严格非商业许可。

---

### 6. [Google Gemini嵌入模型登顶MTEB榜单](https://twitter.com/demishassabis/status/1944870402251219338)
> Google DeepMind宣布Gemini Embedding模型正式发布并在MTEB排行榜位列第一，同时展示将照片转换为带声音视频的新功能。

---

### 7. [Runway推出新一代动作捕捉模型Act-Two](https://twitter.com/c_valenzuelab/status/1945190630449172587)
> RunwayML发布Act-Two动作捕捉模型，在手部生成和质量上有显著提升，并展示文艺复兴风格人声打击乐创意演示。

---

### 8. [行业呼吁保持AI推理过程可监控性](https://twitter.com/OpenAI/status/1945156362859589955)
> OpenAI、Anthropic等机构联合论文主张保留AI的思维链(CoT)监控能力，认为这是确保AI安全的关键技术，获得Yoshua Bengio等专家支持。

---

### 9. [研究揭示"上下文衰减"现象](https://twitter.com/swyx/status/1944848537092809177)
> Chroma技术报告显示随着输入token增加，LLM性能会下降，113k token的对话历史可能导致30%准确率下降，质疑百万token上下文窗口的实际价值。

---

### 10. [Meta取消Llama 4 Behemoth开源计划](https://analyticsindiamag.com/global-tech/meta-plans-to-abandon-llama-4-behemoth-but-why/)
> Meta因技术问题放弃开源2T参数的Llama 4 Behemoth计划，问题包括分块注意力导致长上下文推理能力下降、MoE路由不稳定等，转向闭源超级智能实验室。

---

## 🛠️ 十大工具产品要点

### 1. [Voxtral语音转录API](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507)
> Mistral Voxtral提供直接语音触发函数调用功能，无需中间解析步骤即可将语音交互转化为系统命令，支持多语言自动检测和结构化摘要生成。

---

### 2. [Kimi K2 API接入方案](https://openrouter.ai/moonshotai/kimi-k2)
> Kimi K2在DeepInfra提供$0.55/$2.20每百万token的API服务，Groq提供250 tokens/秒高速推理，支持Anthropic兼容API端点重定向。

---

### 3. [Qdrant Cloud推理服务](https://twitter.com/qdrant_engine/status/1945090285039464518)
> Qdrant推出云端嵌入生成、存储和索引一体化服务，支持CLIP等多模态模型，简化向量数据库工作流程。

---

### 4. [Unsloth量化工具](https://docs.unsloth.ai/basics/datasets-guide#synthetic-data-generation)
> Unsloth提供1.8-bit量化技术，使1T参数的Kimi K2 MoE模型能在有限硬件运行，社区期待更极致的0.11-bit版本。

---

### 5. [N8N无代码AI代理平台](https://n8n.io/)
> 可视化平台支持构建定制AI代理解决商业问题，如预约管理和客户支持，结合工作流和业务逻辑可创造5k-8k+美元价值。

---

### 6. [MLX框架扩展至tvOS](https://twitter.com/awnihannun/status/1944893455202967921)
> Apple的MLX机器学习框架正在移植到纯C++(mlx-lm.cpp)并支持tvOS，推动设备端AI发展。

---

### 7. [LEAP移动端LLM平台](https://twitter.com/maximelabonne/status/1945110321938514335)
> 支持在iOS和Android设备本地运行LLM的开发平台，降低移动端AI应用门槛。

---

### 8. [Perplexity Comet浏览器语音模式](https://twitter.com/AravSrinivas/status/1944861476692615333)
> Perplexity为Comet浏览器添加语音交互和邮箱清理功能，目标是创建无缝融合的工具体验。

---

### 9. [Torchtune BSD 3许可组件](https://github.com/pytorch/torchtune/issues/2883)
> Torchtune的宽松许可允许开发者提取库组件用于其他项目，促进开源AI工具复用。

---

### 10. [LFM2模型微调方案](https://twitter.com/maximelabonne/status/1945018242290082047)
> 支持通过Axolotl对LFM2模型进行微调，配合FineWeb和FineWeb-Edu数据集(包含2025年CommonCrawl快照)。