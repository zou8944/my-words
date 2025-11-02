## AINews - 2025-11-02

> [原文链接](https://news.smol.ai/issues/25-10-30-not-much/)

## 📰 十大AI新闻要点

### 1. [Kimi Linear (KDA)发布线性注意力架构](https://twitter.com/Kimi_Moonshot/status/1983937694360322136)
> Moonshot AI发布Kimi Linear技术报告和检查点，采用Kimi Delta Attention (KDA)与MLA混合架构，开源优化CUDA内核并在vLLM中集成。报告显示KV缓存减少75%，解码吞吐量提升6倍，在长上下文任务中质量与全注意力相当或更好。

---

### 2. [OpenAI Aardvark (GPT-5)进入私有测试](https://twitter.com/OpenAI/status/1983956431360659467)
> Aardvark定位为"智能安全研究员"，能够读取分析代码、编写运行测试并提出补丁，早期用户认为这是可扩展漏洞发现和修复的预览。

---

### 3. [Hugging Face发布200+页Smol训练手册](https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook)
> Hugging Face科学团队发布全面的训练指南，涵盖预训练数据整理、架构选择、后训练(SFT/RL)和基础设施调试，强调消融实验和论文中常被忽略的实际问题。

---

### 4. [MiniMax M2转向全注意力架构](https://twitter.com/omarsar0/status/1983915573215162873)
> MiniMax公开反思早期混合/滑动窗口变体在多跳推理中的挑战，将M2转向全注意力架构，但仍保持强大的智能编码性能，200k上下文，约100 TPS，现可限时免费试用。

---

### 5. [HKUST推出Toolathlon工具使用基准](https://twitter.com/junxian_he/status/1983834164727312391)
> Toolathlon引入基于执行的基准测试，涵盖32个应用/600+工具，显示当前SOTA性能较低(Claude Sonnet 4.5成功率38.6%)，开源与专有模型差距持续存在。

---

### 6. [Cartesia发布SSM架构语音模型Sonic-3](https://twitter.com/ArtificialAnlys/status/1983879759194157194)
> Cartesia的新旗舰TTS模型Sonic-3使用状态空间模型架构，提供低延迟流式语音，支持韵律元素(笑声、惊讶)，涵盖42种语言(包括9种印度语言)。

---

### 7. [Anthropic发现LLM内省意识证据](https://www.anthropic.com/research/introspection)
> Anthropic研究表明大型语言模型可能表现出"真正内省意识"，能够检测自身激活状态的修改，这属于内部处理而非输入输出文本。

---

### 8. [Perplexity推出专利研究代理](https://twitter.com/perplexity_ai/status/1983875975877423277)
> Perplexity发布"Patents"功能，这是引用优先的专利研究代理，免费测试版，同时推出"Discover"和新的金融功能如政客持股追踪。

---

### 9. [VS Code集成OpenAI Codex和Plan功能](https://twitter.com/code/status/1983942033879257195)
> VS Code Insiders添加"Plan"功能(任务分析和实施计划)，并为Copilot Pro+账户集成OpenAI Codex，OpenAI还引入Codex信用以突破计划限制。

---

### 10. [Epoch AI显示开源与闭源差距缩小](https://twitter.com/EpochAIResearch/status/1983987212183335097)
> Epoch AI的ECI指标显示开源权重与闭源SOTA的平均滞后约3.5个月(约7 ECI点)，表明追赶速度比预期更快。

---

## 🛠️ 十大工具产品要点

### 1. [vLLM集成Kimi Linear支持](https://twitter.com/vllm_project/status/1983941708233765149)
> vLLM在发布首日集成Kimi Linear优化内核，显示RULER 128k基准测试中84.3分，速度比基线提升约4倍，确认内存/吞吐量优势。

---

### 2. [Cursor推出更快更可靠的云代理](https://twitter.com/cursor_ai/status/1983954528933421419)
> Cursor推出更快更可靠的云代理并分享内部使用模式，同时用户注意到Composer-1偶尔"用中文思考"，引发基础模型来源透明度问题。

---

### 3. [Cognition发布"Computer Use"公开测试版](https://twitter.com/cognition/status/1983983151157563762)
> Devin现在可以操作桌面/移动工具，分享屏幕录制并构建GUI应用，标志着智能代理能力的重大扩展。

---

### 4. [Voyage-3-large嵌入模型登顶HF RTEB排行榜](https://twitter.com/_avichawla/status/1983783708047093838)
> Voyage的量化感知训练嵌入模型voyage-3-large在HF RTEB排行榜33个数据集中排名第一，在应用中心(金融/法律/医疗)检索任务中优于OpenAI/Cohere。

---

### 5. [NVIDIA ChronoEdit-14B开源图像编辑工具](https://twitter.com/_akhaliq/status/1983953896415604836)
> NVIDIA开源ChronoEdit-14B代码、模型和演示，通过"视频推理"阶段+轨迹令牌上下文编辑，在约8个扩散步骤(~4秒/图像在H100上)执行图像编辑。

---

### 6. [Google Veo 3.1图像到视频质量显著提升](https://twitter.com/ArtificialAnlys/status/1983938159839998249)
> Google Veo 3.1在图像到视频方面显著改进(Veo 3.1 Fast在AA的I2V竞技场排名第2)，虽然文本到视频质量未超过Veo 3，定价保持$0.2/秒不含音频。

---

### 7. [LangGraph添加Overwrite功能](https://twitter.com/caspar_br/status/1983949095837519901)
> LangGraph添加Overwrite功能，绕过reducer进行直接状态替换，为智能代理状态管理提供更灵活的控制。

---

### 8. [LightOn Fast-Plaid 1.2.5检索基础设施](https://twitter.com/raphaelsrty/status/1983906400725024931)
> LightOn的Fast-Plaid 1.2.5为ColPali/ColQwen/PyLate风格检索带来速度和更低GPU内存，优化后期交互检索性能。

---

### 9. [Baseten Training正式发布](https://twitter.com/basetenco/status/1983958807353934180)
> Baseten Training GA带来按需多节点训练，具有缓存感知调度，为企业级模型训练提供可扩展基础设施。

---

### 10. [SGLang-JAX现在支持TPU](https://twitter.com/skypilot_org/status/1983957542863851899)
> SGLang-JAX现在支持TPU与SkyPilot单行命令，为大规模语言模型推理提供更广泛硬件支持选择。

---