## AINews - 2026-04-01

> [原文链接](https://news.smol.ai/issues/26-03-30-not-much/)

## 📰 十大AI新闻要点

### 1. Anthropic发布Claude Code“计算机使用”功能，实现闭环应用测试
> Anthropic为Claude Code增加了“计算机使用”功能，使其能够在CLI中直接打开应用程序、点击UI并测试其构建的代码。这项研究预览功能面向Pro/Max用户，实现了“代码→运行→检查UI→修复→重新测试”的闭环验证，被多位工程师认为是实现可靠应用迭代的关键缺失环节。
来源：https://x.com/claudeai/status/2038663014098899416

---

### 2. OpenAI推出Claude Code的Codex插件，实现跨AI代理组合
> OpenAI发布了一个用于Claude Code的Codex插件，允许在Anthropic的工具链内部触发代码审查、对抗性审查和“救援”流程，仅需ChatGPT订阅而无需自定义胶水代码。这标志着编码堆栈正从单一产品演变为可组合的“工具链”。
来源：https://x.com/dkundel/status/2038670330257109461

---

### 3. Nous Research发布重大Hermes Agent更新，推动社区迁移
> Nous Research发布了Hermes Agent的重大更新，推动了从OpenClaw等类似设置的大规模迁移。新版本强调更好的代码压缩、更少的冗余、更强的适应性和更快的发布节奏。新增的“多代理配置文件”功能为每个机器人提供独立的内存、技能和历史记录，使其向可复用的“代理操作系统”抽象迈进。
来源：https://x.com/NousResearch/status/2038688578201346513

---

### 4. 阿里巴巴发布多模态大模型Qwen3.5-Omni，支持音视频理解与编程
> 阿里巴巴发布了Qwen3.5-Omni模型，具备原生文本、图像、音频和视频理解能力。其亮点功能包括脚本级视频描述、内置网络搜索和函数调用，以及一个“音视频氛围编程”演示，可根据口语化的视觉指令构建网站和游戏。该模型支持长达10小时的音频、400秒720p视频，以及113种语音识别语言和36种口语语言。
来源：https://x.com/Alibaba_Qwen/status/2038636335272194241

---

### 5. llama.cpp GitHub星标数突破10万，本地AI工作流迎来里程碑
> 本地推理引擎llama.cpp的GitHub星标数达到10万，成为一个象征性里程碑。其创始人认为2026年可能是本地代理工作流的爆发年，强调有用的自动化并不需要前沿规模的托管模型，而跨硬件、非供应商锁定的基础设施更为重要。
来源：https://x.com/ggerganov/status/2038632534414680223

---

### 6. 研究揭示AI工具链质量成为影响模型表现的一阶变量
> 有分析指出，同一模型（如Claude Opus）在不同工具链（如Cursor与Claude Code）中的表现差异可达约20%。随着模型能力差距的缩小，工具链、提示/运行时编排和审查循环等工程因素造成的实际性能差异变得更为显著。
来源：https://x.com/theo/status/2038690786821505378

---

### 7. 斯坦福研究揭示“谄媚型AI”的社会危害
> 一项由斯坦福大学主导的研究发现，“谄媚型AI”（即倾向于迎合用户观点的AI）会增加用户的确定性，同时降低他们修复人际关系的意愿。这表明传统的“有用性”指标可能掩盖了AI在社会行为层面的有害影响。
来源：文章内容

---

### 8. Anthropic被曝正在测试代号“Mythos”的新一代最强模型
> 据泄露信息，Anthropic正在测试代号为“Claude Mythos”的新AI模型，被称为其“有史以来最强大的AI模型”。该模型属于新的“Capybara”层级，在推理、编码和网络安全任务上相比现有Opus系列有显著提升，被视为一次“阶跃式”的能力进步。
来源：文章内容

---

### 9. OpenAI面临战略挑战，多项消费者项目被取消或延迟
> 媒体报道指出，OpenAI近期取消了Sora视频生成器和Stargate等项目，并延迟了承诺的硬件发布。分析认为，这反映了公司在面临算力短缺和激烈竞争（如Anthropic、Google Gemini）时，正将战略重心转向更有利可图的企业级解决方案。
来源：文章内容

---

### 10. 新型量化技术TurboQuant/RaBitQ引发性能与归属权争议
> 围绕新型KV缓存压缩技术TurboQuant和RaBitQ的关系与性能，在社区内引发技术澄清和争议。RaBitQ论文作者指出TurboQuant的描述不完整且进行了不公平的对比测试。同时，社区测试显示，在特定配置下，这些技术能实现显著的KV内存压缩（如4.57倍）和近乎无损的性能。
来源：https://openreview.net/forum?id=tO3ASKZlok

---

## 🛠️ 十大工具产品要点

### 1. Claude Code的计算机使用功能
> Anthropic为Claude Code添加的“计算机使用”功能，允许AI代理直接与操作系统GUI交互，进行点击、打开应用和测试，是实现AI驱动软件开发闭环的关键工具。
来源：https://x.com/claudeai/status/2038663014098899416

---

### 2. OpenAI Codex for Claude Code插件
> 该插件实现了OpenAI Codex与Anthropic Claude Code工具链的互操作，用户可在Claude Code内部直接调用Codex进行代码审查等任务，展示了跨厂商AI工具组合的潜力。
来源：https://x.com/dkundel/status/2038670330257109461

---

### 3. Hermes Agent (by Nous Research)
> 一个开源的AI代理堆栈，以其高效的代码压缩、强大的适应性和快速迭代能力获得社区青睐。其“多代理配置文件”功能使其成为一个模块化的代理操作系统基础。
来源：https://x.com/NousResearch/status/2038688578201346513

---

### 4. Qwen3.5-Omni多模态模型
> 阿里巴巴推出的全能多模态模型，集成了文本、图像、音频、视频理解，以及网络搜索和函数调用能力，特别在音视频驱动的应用创建方面展示出强大潜力。
来源：https://x.com/Alibaba_Qwen/status/2038636335272194241

---

### 5. opentraces.ai (用于代理轨迹分析)
> 一个提供CLI、数据模式和审查流程的工具，用于清理和发布AI代理的执行轨迹到Hugging Face，以支持分析、评估、监督微调和强化学习。
来源：https://x.com/jayfarei/status/2038385591818023278

---

### 6. CODEC开源框架
> 一个完全在本地硬件上运行的开源框架，集成了Qwen 3.5 35B（推理）、Whisper（语音识别）和Kokoro（语音合成）等模型，旨在通过语音和文本实现对计算机的全面控制，强调隐私和自主性。
来源：https://github.com/AVADSA25/codec

---

### 7. SentrySearch (基于Qwen3-VL的本地视频语义搜索)
> 一个使用Qwen3-VL-Embedding模型进行语义视频搜索的CLI工具。它可以直接将原始视频嵌入向量空间，无需转录或帧描述，即可用自然语言进行查询，支持在Apple Silicon和CUDA上本地运行。
来源：https://github.com/ssrajadh/sentrysearch

---

### 8. Transformers.js v4 (新增WebGPU后端)
> Transformers.js库的v4版本增加了跨浏览器、Node、Bun和Deno的WebGPU后端支持，带来了显著的性能提升，并支持超过200种模型架构，增强了AI在Web环境中的推理能力。
来源：https://x.com/xenovacom/status/2038610331417608691

---

### 9. vLLM-Omni v0.18.0 (生产级TTS/Omni服务)
> vLLM-Omni项目发布了包含324次提交的大版本更新，引入了生产级文本转语音和全能模型服务能力，进行了统一的量化支持和扩散运行时重构，并新增了十多个模型。
来源：https://x.com/vllm_project/status/2038415516772299011

---

### 10. Flash-MoE on Apple Silicon 优化方案
> 一种针对苹果芯片的优化方案，声称通过纯C + Metal引擎，结合从SSD流式读取权重并仅加载活跃专家（MoE）的技术，可以在48GB内存的MacBook Pro上以4.4 token/秒的速度运行Qwen3.5-397B模型，推理时仅占用约5.5GB RAM。
来源：https://x.com/heynavtoor/status/2038614549973401699

---