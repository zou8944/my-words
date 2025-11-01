## AINews - 2025-11-01

> [原文链接](https://news.smol.ai/issues/25-10-30-not-much/)

## 📰 十大AI新闻要点

### 1. [Kimi Linear (KDA)技术突破](https://twitter.com/Kimi_Moonshot/status/1983937694360322136)
> Moonshot AI发布Kimi Linear技术报告，采用混合架构交织Kimi Delta Attention与MLA，开源优化CUDA内核并集成到vLLM。报告显示：高达75% KV缓存减少，高达6倍解码吞吐量，在长上下文和RL长形式推理任务中质量优于全注意力机制。

---

### 2. [OpenAI Aardvark进入私有测试](https://twitter.com/OpenAI/status/1983956431360659467)
> OpenAI的GPT-5驱动代理Aardvark作为"代理安全研究员"进入私有测试，能够读取/分析代码、编写和运行测试、提出补丁，被视为可扩展漏洞发现和修复的预览。

---

### 3. [Hugging Face发布Smol训练手册](https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook)
> Hugging Face科学团队发布200+页的"Smol训练手册"，涵盖预训练数据管理、架构选择、后训练(SFT/RL)和基础设施调试，强调消融实验和论文中常被忽略的实际细节。

---

### 4. [Anthropic发现LLM内省意识证据](https://www.anthropic.com/research/introspection)
> Anthropic研究表明大型语言模型可能表现出"真正内省意识"，通过检测自身激活状态的变化来识别和响应神经激活的修改，暗示处理过程中的某种自我意识形式。

---

### 5. [Cognition发布"计算机使用"公测版](https://twitter.com/cognition/status/1983983151157563762)
> Cognition的Devin现在可以操作桌面/移动工具，分享屏幕录制并构建GUI应用程序，标志着代理能力的重大扩展。

---

### 6. [HKUST推出Toolathlon基准测试](https://twitter.com/junxian_he/status/1983834164727312391)
> 香港科技大学的Tool Decathlon引入基于执行的基准测试，涵盖32个应用/600+工具，显示当前SOTA性能较低(Claude Sonnet 4.5成功率38.6%)，开源与专有模型差距持续存在。

---

### 7. [Voyage嵌入模型在HF RTEB排行榜领先](https://twitter.com/_avichawla/status/1983783708047093838)
> Voyage的量化感知训练嵌入模型voyage-3-large在新的HF RTEB排行榜上排名第一，在33个数据集中表现优异，在金融/法律/医疗检索任务中超越OpenAI/Cohere。

---

### 8. [Epoch AI显示开源与闭源差距缩小](https://twitter.com/EpochAIResearch/status/1983987212183335097)
> Epoch AI的ECI指标显示开源权重与闭源SOTA的平均滞后约为3.5个月(约7个ECI点)，表明追赶速度快于预期假设。

---

### 9. [NVIDIA发布ChronoEdit-14B开源编辑工具](https://twitter.com/_akhaliq/status/1983953896415604836)
> NVIDIA的ChronoEdit-14B通过"视频推理"阶段和轨迹令牌的上下文编辑，在约8个扩散步骤(~4秒/图像在H100上)执行图像编辑，还可用于可视化编辑"思考过程"。

---

### 10. [ScaleAI远程劳动指数揭示自动化率低](https://scale.com/leaderboard/rli)
> ScaleAI的新基准测试显示当前代理在需要人类平均30小时的任务中表现不佳，顶级代理(Manus)仅实现2.5%自动化率，主要因质量和完整性问题失败。

---

## 🛠️ 十大工具产品要点

### 1. [Cursor推出更快云代理](https://twitter.com/cursor_ai/status/1983954528933421419)
> Cursor推出更快、更可靠的云代理并分享内部使用模式，同时用户注意到Composer-1偶尔"用中文思考"，引发关于基础模型来源透明度的讨论。

---

### 2. [LangGraph添加Overwrite功能](https://twitter.com/caspar_br/status/1983949095837519901)
> LangGraph添加Overwrite功能以绕过reducers进行直接状态替换，增强代理状态管理能力。

---

### 3. [Confluent + Weaviate/Qdrant实时上下文管道](https://twitter.com/weaviate_io/status/1983921589163835398)
> 事件驱动的"流式代理"通过Confluent + Weaviate示例和Confluent + Qdrant合作伙伴关系接近生产就绪，实现实时数据+向量搜索，支持超越陈旧RAG快照的上下文感知代理。

---

### 4. [Cartesia Sonic-3 TTS系统](https://twitter.com/ArtificialAnlys/status/1983879759194157194)
> Cartesia的新旗舰TTS Sonic-3使用状态空间模型架构提供低延迟流式语音，支持韵律元素(笑声、惊讶)，覆盖42种语言(包括9种印度语言)。

---

### 5. [Perplexity推出专利研究代理](https://twitter.com/perplexity_ai/status/1983875975877423277)
> Perplexity推出"Patents" - 引用优先的专利研究代理，免费测试版，同时推出"Discover"和新的金融功能如政客持股跟踪。

---

### 6. [VS Code集成OpenAI Codex](https://twitter.com/code/status/1983942033879257195)
> VS Code Insiders添加"Plan"(任务分析和实施计划)功能，并为Copilot Pro+账户集成OpenAI Codex，OpenAI还引入Codex积分以突破计划限制。

---

### 7. [Baseten Training正式发布](https://twitter.com/basetenco/status/1983958807353934180)
> Baseten Training GA带来按需多节点训练，具有缓存感知调度功能，提升训练基础设施能力。

---

### 8. [SGLang-JAX支持TPU](https://twitter.com/skypilot_org/status/1983957542863851899)
> SGLang-JAX现在支持TPU，通过SkyPilot一行命令简化部署，扩展硬件支持范围。

---

### 9. [Locally AI推出原生Mac应用](https://twitter.com/LocallyAIApp/status/1983957683737915405)
> Locally AI推出基于MLX构建的原生Mac应用程序，优化苹果芯片上的AI应用体验。

---

### 10. [OpenRouter推出Sonar Pro搜索](https://openrouter.ai/perplexity/sonar-pro-search)
> OpenRouter与Perplexity合作推出OpenRouter专属的Sonar Pro with Pro Search模式，具有多步代理推理、动态工具执行、实时思维流和自适应研究策略功能。

---