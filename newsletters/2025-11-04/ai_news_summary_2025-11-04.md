## AINews - 2025-11-04

> [原文链接](https://news.smol.ai/issues/25-10-30-not-much/)

## 📰 十大AI新闻要点

### 1. [Kimi Linear (KDA)发布，实现长上下文高效处理](https://twitter.com/Kimi_Moonshot/status/1983937694360322136)
> Moonshot AI发布Kimi Linear技术报告和检查点，采用混合架构交织Kimi Delta Attention与MLA，开源优化KDA CUDA内核并在vLLM中集成。报告显示KV缓存减少75%，解码吞吐量提升6倍，在长上下文和RL长形式推理任务中质量优于全注意力机制。

---

### 2. [OpenAI Aardvark (GPT-5)进入私有测试阶段](https://twitter.com/OpenAI/status/1983956431360659467)
> Aardvark定位为"代理安全研究员"，能够读取/分析代码、编写运行测试并提出补丁，早期用户认为这是可扩展漏洞发现和修复的预览。

---

### 3. [Hugging Face发布200+页Smol训练手册](https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook)
> Hugging Face科学团队发布全面的训练指南，涵盖预训练数据管理、架构选择、后训练和基础设施调试，强调消融实验和论文中常被忽略的实际问题。

---

### 4. [Anthropic发现LLM中的"真正内省意识"证据](https://www.anthropic.com/research/introspection)
> Anthropic研究表明大型语言模型可能通过检测自身激活状态的变化表现出"真正内省意识"，这种内省体现在模型识别和响应其神经激活变化的能力上。

---

### 5. [ScaleAI远程劳动指数显示自动化率仅2.5%](https://scale.com/leaderboard/rli)
> ScaleAI新基准测试显示，当前代理在需要人类平均30小时的任务中表现不佳，顶级代理Manus仅实现2.5%自动化率，主要失败原因是质量和完整性。

---

### 6. [Cognition SWE-1.5达到950 tok/s速度记录](https://x.com/cognition/status/1983662836896448756)
> Cognition发布Windsurf代理编码模型，使用Cerebras硬件、推测解码和自定义优先级队列，比Haiku快6倍，比Sonnet快13倍，同时保持接近SOTA质量。

---

### 7. [Voyage-3-large嵌入模型在HF RTEB排行榜登顶](https://twitter.com/_avichawla/status/1983783708047093838)
> Voyage的量化感知训练嵌入模型在33个数据集上排名第一，在金融/法律/医疗检索任务中超越OpenAI/Cohere，INT8/二进制下保持准确。

---

### 8. [Epoch AI显示开源与闭源差距缩小至3.5个月](https://twitter.com/EpochAIResearch/status/1983987212183335097)
> Epoch AI的ECI指标表明开源权重与闭源SOTA的平均差距约为3.5个月（约7个ECI点），显示追赶速度快于预期。

---

### 9. [Cartesia Sonic-3 TTS使用状态空间模型架构](https://twitter.com/ArtificialAnlys/status/1983879759194157194)
> Cartesia新旗舰TTS采用SSM架构提供低延迟流式语音，支持韵律元素（笑声、惊讶），覆盖42种语言包括9种印度语言。

---

### 10. [NVIDIA ChronoEdit-14B开源图像编辑工具](https://twitter.com/_akhaliq/status/1983953896415604836)
> NVIDIA开源图像编辑工具通过"视频推理"阶段和轨迹令牌的上下文编辑，在约8个扩散步骤（H100上约4秒/图像）完成图像编辑。

---

## 🛠️ 十大工具产品要点

### 1. [vLLM集成Kimi Linear支持](https://twitter.com/vllm_project/status/1983941708233765149)
> vLLM在发布首日集成Kimi Linear优化内核，显示RULER 128k基准测试中84.3分，速度比基线提升约4倍，确认内存/吞吐量优势。

---

### 2. [Cursor推出更快更可靠的云代理](https://twitter.com/cursor_ai/status/1983954528933421419)
> Cursor推出更快更可靠的云代理并分享内部使用模式，同时用户注意到Composer-1偶尔"用中文思考"，引发基础模型来源透明度问题。

---

### 3. [Cognition发布"计算机使用"公测版](https://twitter.com/cognition/status/1983983151157563762)
> Devin现在可以操作桌面/移动工具，分享屏幕录制并构建GUI应用程序，扩展了代理的实际操作能力。

---

### 4. [LangGraph添加Overwrite功能](https://twitter.com/caspar_br/status/1983949095837519901)
> LangGraph新增Overwrite功能，绕过reducers进行直接状态替换，简化状态管理流程。

---

### 5. [Perplexity推出专利研究代理](https://twitter.com/perplexity_ai/status/1983875975877423277)
> Perplexity推出"Patents"功能，作为引用优先的专利研究代理，免费公测，同时推出"Discover"和政客持股跟踪等金融功能。

---

### 6. [VS Code集成OpenAI Codex和Plan功能](https://twitter.com/code/status/1983942033879257195)
> VS Code Insiders添加"Plan"任务分析和实施计划功能，为Copilot Pro+账户集成OpenAI Codex，同时推出Codex信用突破计划限制。

---

### 7. [OpenRouter独家推出Perplexity Sonar Pro搜索](https://openrouter.ai/perplexity/sonar-pro-search)
> OpenRouter与Perplexity合作推出独家Sonar Pro搜索模式，支持多步代理推理、动态工具执行、实时思维流和自适应研究策略。

---

### 8. [LightOn Fast-Plaid 1.2.5提升检索效率](https://twitter.com/raphaelsrty/status/1983906400725024931)
> LightOn Fast-Plaid 1.2.5为ColPali/ColQwen/PyLate风格检索带来速度和GPU内存优化，提升后期交互检索基础设施性能。

---

### 9. [Baseten Training正式发布](https://twitter.com/basetenco/status/1983958807353934180)
> Baseten Training GA提供按需多节点训练，具有缓存感知调度功能，简化大规模模型训练部署。

---

### 10. [Locally AI推出基于MLX的Mac原生应用](https://twitter.com/LocallyAIApp/status/1983957683737915405)
> Locally AI发布基于MLX构建的原生Mac应用程序，优化苹果芯片上的AI模型运行体验。

---