## AINews - 2026-04-02

> [原文链接](https://news.smol.ai/issues/26-03-30-not-much/)

## 📰 十大AI新闻要点

### 1. Anthropic发布Claude Code“计算机使用”功能，实现闭环应用开发验证
> Anthropic为Claude Code增加了“计算机使用”功能，使其能够在CLI中直接打开应用、点击UI并测试其构建的代码。这项研究预览功能面向Pro/Max用户，实现了“代码→运行→检查UI→修复→重新测试”的闭环验证流程，被多位工程师认为是实现可靠应用迭代的关键缺失环节。
来源：https://x.com/claudeai/status/2038663014098899416

---

### 2. OpenAI推出Claude Code的Codex插件，标志编码堆栈向可组合“工具链”演进
> OpenAI发布了一个用于Claude Code的Codex插件，可直接在Anthropic的工具链内触发代码审查、对抗性审查和“救援”流程，无需自定义粘合代码。这不仅是插件创新，更标志着编码堆栈正从单一产品演变为可组合的“工具链”。
来源：https://x.com/dkundel/status/2038670330257109461

---

### 3. Nous Research发布重大Hermes Agent更新，推动向“代理操作系统”演进
> Nous Research发布了Hermes Agent的重大更新，推动了从OpenClaw等设置的迁移潮。新版本强调更好的压缩、更少的臃肿、更强的适应性和更快的发布节奏。新增的“多代理配置文件”功能为每个机器人提供独立的内存、技能、历史和网关连接，使Hermes从“个人助手”向可重用的“代理操作系统”抽象迈进。
来源：https://x.com/NousResearch/status/2038688578201346513

---

### 4. 阿里巴巴发布Qwen3.5-Omni，实现原生多模态理解与“视听氛围编码”
> 阿里巴巴推出Qwen3.5-Omni模型，具备原生文本/图像/音频/视频理解能力，支持脚本级字幕生成、内置网络搜索和函数调用。其突出的“音频-视觉氛围编码”演示展示了模型根据口语视觉指令构建网站/游戏的能力。该模型支持10小时音频/400秒720p视频、113种语音识别语言和36种口语。
来源：https://x.com/Alibaba_Qwen/status/2038636335272194241

---

### 5. llama.cpp达到10万GitHub星标，本地代理工作流迎来里程碑
> 本地AI运行时项目llama.cpp在GitHub上达到10万星标，被视为本地代理工作流发展的一个象征性里程碑。项目创始人认为，2026年可能是本地代理工作流的爆发年，有用的自动化并不需要前沿规模的托管模型，而合适的便携式运行时堆栈比绝对规模更重要。
来源：https://x.com/ggerganov/status/2038632534414680223

---

### 6. 清华/深圳团队研究自然语言代理工具链，让LLM执行SOP编排逻辑
> 来自清华大学和深圳的研究人员发表了一篇关于自然语言代理工具链的论文，提出让LLM根据标准操作程序（SOP）执行编排逻辑，而非依赖硬编码的工具链规则。随着上下文预算的增加，这一方向被多位从业者认为具有颠覆性潜力。
来源：https://x.com/rronak_/status/2038401494177694074

---

### 7. CMU提出CAID框架，异步多代理软件工程设计获实证支持
> 卡内基梅隆大学的CAID论文提出了“集中式异步隔离委托”框架，利用管理器代理、依赖图、隔离的git工作树、自我验证和合并。报告显示，与单代理基线相比，该框架在PaperBench上实现了+26.7的绝对增益，在Commit0上实现了+14.3的增益，表明并发性和隔离性优于单纯增加单个代理的迭代次数。
来源：https://x.com/omarsar0/status/2038627572108743001

---

### 8. Anthropic意外泄露并确认正在测试代号“Mythos”的新顶级模型
> 由于CMS配置错误导致资料泄露，Anthropic确认正在测试一款代号为“Claude Mythos”的新AI模型，并称其为“有史以来最强大的AI模型”。该模型属于名为“Capybara”的新层级，超越了现有的Opus系列，在推理、编码和网络安全任务上均有显著提升。公司因潜在的滥用风险而对发布持谨慎态度。
来源：文章内容

---

### 9. OpenAI面临战略挑战，取消多个项目并聚焦企业解决方案
> 媒体报道指出，OpenAI近期取消了Sora视频生成器和Stargate等项目，并延迟了承诺的硬件发布，这些举措被解读为面临困境的信号。评论认为，在算力短缺和竞争加剧的背景下，OpenAI的战略正从消费级项目转向更有利可图的企业解决方案。
来源：文章内容

---

### 10. Shopify利用DSPy优化AI应用，年成本从550万美元大幅降至7.3万美元
> Shopify分享了一个DSPy应用案例研究，展示了显著的经济效益：通过解构业务逻辑、使用DSPy对意图进行建模，并转向更小、优化的模型，同时保持性能，成功将年成本从550万美元大幅降低至7.3万美元。
来源：https://x.com/dbreunig/status/2038650860843245814

---

## 🛠️ 十大工具产品要点

### 1. Claude Code的计算机使用功能
> Anthropic为Claude Code添加了计算机使用能力，允许AI代理直接与操作系统和应用UI交互，实现从编码到测试的端到端闭环，极大提升了应用开发的迭代效率和可靠性。
来源：https://x.com/claudeai/status/2038663014098899416

---

### 2. OpenAI的Claude Code Codex插件
> 该插件实现了OpenAI Codex与Anthropic Claude Code工具链的无缝集成，用户可以使用ChatGPT订阅来触发代码审查等流程，无需编写中间代码，体现了工具链的可组合性趋势。
来源：https://x.com/dkundel/status/2038670330257109461

---

### 3. Hermes Agent及其多代理配置文件系统
> Nous Research的Hermes Agent更新引入了多代理配置文件，每个代理拥有独立的内存、技能和历史，将框架从个人助手提升为可管理多个专用代理的“代理操作系统”。
来源：https://x.com/NousResearch/status/2038688578201346513

---

### 4. opentraces.ai：代理轨迹分析平台
> 该项目提供了一个CLI/模式/审查流程，用于清理代理执行轨迹并将其发布到Hugging Face，以进行分析、评估、监督微调和强化学习，助力代理的自我改进和社区研究。
来源：https://x.com/jayfarei/status/2038385591818023278

---

### 5. Qwen3.5-Omni多模态模型
> 阿里巴巴发布的Qwen3.5-Omni是一个全能理解模型，支持长音频/视频输入、多语言语音识别与合成，并内置网络搜索和函数调用能力，其“视听氛围编码”演示展示了强大的多模态指令跟随潜力。
来源：https://x.com/Alibaba_Qwen/status/2038636335272194241

---

### 6. Z AI的AutoClaw本地运行时
> Z AI推出了AutoClaw，这是一个本地的OpenClaw风格运行时，无需API密钥即可运行，并可选配GLM-5-Turbo模型，专注于为代理工作负载提供本地化、隐私安全的解决方案。
来源：https://x.com/Zai_org/status/2038632251551023250

---

### 7. CODEC：本地全功能计算机控制框架
> CODEC是一个开源框架，集成了Qwen 3.5 35B（推理）、Whisper（语音识别）和Kokoro（语音合成）等模型，在单台Mac Studio上实现了通过语音和文本对计算机进行全面控制，无需外部API调用，强调隐私和自主性。
来源：https://github.com/AVADSA25/codec

---

### 8. SentrySearch：基于Qwen3-VL的本地语义视频搜索工具
> 这是一个CLI工具，利用本地的Qwen3-VL-Embedding模型将原始视频直接嵌入向量空间，实现无需转录或帧字幕的自然语言视频搜索，支持在Apple Silicon和CUDA上运行。
来源：https://github.com/ssrajadh/sentrysearch

---

### 9. Transformers.js v4 with WebGPU后端
> Transformers.js v4增加了跨浏览器/Node/Bun/Deno的WebGPU后端，带来了显著的性能提升，并支持200多种模型架构，极大增强了AI模型在Web环境中的推理能力。
来源：https://x.com/xenovacom/status/2038610331417608691

---

### 10. vLLM-Omni v0.18.0生产级服务框架
> vLLM-Omni新版本包含324次提交，提供了生产级的TTS/全能模型服务、统一的量化方案、扩散运行时重构，并支持十多个新模型，是一个功能强大的模型服务与推理框架。
来源：https://x.com/vllm_project/status/2038415516772299011

---