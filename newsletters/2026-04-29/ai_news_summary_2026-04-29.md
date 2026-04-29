## AINews - 2026-04-29

> [原文链接](https://news.smol.ai/issues/26-04-27-not-much/)

## 📰 十大AI新闻要点

### 1. [OpenAI 打破 Azure 独家协议，模型将登陆 AWS Bedrock](https://x.com/sama/status/2048755148361707946)
> OpenAI 更新了与微软的合作伙伴关系，微软仍为主要云服务商，但 OpenAI 现在可以跨所有云平台提供产品。产品/模型承诺延长至 2032 年，收入分成至 2030 年。AWS CEO [@ajassy](https://x.com/ajassy/status/2048806022253609115) 确认 OpenAI 模型将在未来几周内登陆 AWS Bedrock。这标志着 OpenAI 分销策略的重大转变，旧版 AGI 条款实际上已失效。

---

### 2. [GPT-5.5 性能全面升级但非绝对领先](https://x.com/htihle/status/2048717753394090274)
> 社区评测显示，GPT-5.5 无思考模式在 WeirdML 上达到 67.1%（GPT-5.4 为 57.4%），但仍落后于 Opus 4.7 的 76.4%。LMSYS Arena 排名显示 GPT-5.5 在代码领域第 9、数学第 3、搜索第 2。开发者反馈在 GPU 内核等硬编码任务上表现积极，但无思考模式存在“压缩 CoT 泄漏”问题。

---

### 3. [GitHub Copilot 将于 6 月 1 日转向按用量计费](https://x.com/github/status/2048794729274278258)
> GitHub 宣布 Copilot 将从 6 月 1 日起采用基于使用量的计费模式，这是对代理工作流消耗更多运行时的直接回应。同时，Codex 使用乘数被记录：GPT-5.4 fast 为 2x，GPT-5.5 fast 为 2.5x，而 5.4-mini 和 GPT-5.3-Codex 则便宜得多。

---

### 4. [小米开源 MiMo-V2.5 系列模型，MIT 许可+1M 上下文](https://x.com/XiaomiMiMo/status/2048821516079661561)
> 小米开源了 MiMo-V2.5-Pro 和 MiMo-V2.5，均采用 MIT 许可，支持 1M token 上下文。Pro 版约 1T 总参数/42B 活跃参数，训练于 27T tokens；标准版约 310B 总/15B 活跃，训练于 48T tokens。小米还宣布为开发者提供 100T token 的赠款。vLLM 和 SGLang 已迅速提供 Day-0 推理支持。

---

### 5. [Kimi K2.6 登顶 OpenRouter 周榜，支持 300 个并发子代理](https://x.com/Kimi_Moonshot/status/2048693682329776223)
> Kimi K2.6 成为 OpenRouter 周榜第一，专为编码和长周期代理任务设计。它能扩展到 300 个并发子代理，协调 4,000 个步骤。实践者发现它在 Hermes 中比 DeepSeek V4 慢得多，但有时能修复 V4 无法修复的 bug。

---

### 6. [Sakana 发布 7B Conductor：用 RL 训练模型来编排其他 AI 模型](https://x.com/SakanaAILabs/status/2048777689763639741)
> Sakana AI 推出 7B Conductor，通过强化学习训练，用自然语言编排前沿模型池。它动态决定调用哪个代理、分配什么子任务以及暴露哪些上下文。在 LiveCodeBench 上达到 83.9%，在 GPQA-Diamond 上达到 87.5%，击败了池中任何单个工作模型。这代表了“AI 管理 AI”和递归自选择作为测试时扩展的新方向。

---

### 7. [Google TPU v8 拆分为训练和推理专用芯片](https://x.com/kimmonismus/status/2048745304007299230)
> Google Cloud Next 宣布 TPU v8 拆分为 8t（训练）和 8i（推理），训练速度提升约 2.8 倍，推理性能/美元提升 80%。这是 Google 首次按工作负载拆分定制芯片。据报道，OpenAI、Anthropic 和 Meta 正在购买 TPU 容量。

---

### 8. [vLLM 0.20.0 发布，支持 DeepSeek V4 和 2-bit KV 缓存](https://x.com/vllm_project/status/2048918629144805619)
> vLLM 0.20.0 版本亮点包括：DeepSeek V4 基础模型支持（需要 expert_dtype 配置字段区分 FP4 指令版和 FP8 基础版）、FA4 作为默认 MLA 预填充、TurboQuant 2-bit KV 缓存，以及 Blackwell 上的 DeepSeek 专用 MegaMoE 路径。

---

### 9. [FP8 KV 缓存修复将 128k 大海捞针准确率从 13% 提升至 89%](https://x.com/vllm_project/status/2048796304508330462)
> vLLM 与 Red Hat/AWS 联合发布 FP8 KV 缓存深度分析，修复了 FA3 两级累积问题，将 128k 上下文的大海捞针测试准确率从 13% 提升至 89%，同时保留了 FP8 解码的速度优势。这凸显了 KV 缓存优化在长上下文场景中的关键作用。

---

### 10. [代理编码消耗 token 可达聊天模式的 1000 倍，成本意识评估成为焦点](https://x.com/dair_ai/status/2048784506635878644)
> 一项关于 SWE-bench Verified 上编码代理支出的新研究显示：代理编码可消耗约 1000 倍于聊天/代码推理的 token，相同任务的不同运行间使用量可变化 30 倍，且更多支出并不单调地提高准确率。这与 Copilot 定价模式变化和对不受控代理运行时经济的担忧相呼应。

---

## 🛠️ 十大工具产品要点

### 1. [OpenAI 开源 Symphony：连接问题追踪器与 Codex 代理的编排层](https://x.com/OpenAIDevs/status/2048825010371039648)
> OpenAI 开源 Symphony，这是一个编排层，将问题追踪器连接到 Codex 代理，实现“开放问题 → 代理 → PR → 人工审查”的完整工作流。这是 OpenAI 在开发者工具生态中的重要开源举措。

---

### 2. [Cognition 发布 Devin for Terminal：本地 Shell 代理](https://x.com/cognition/status/2048821234281181302)
> Cognition 推出 Devin for Terminal，一个本地 shell 代理，可以稍后“移交”到云端。这扩展了 Devin 的使用场景，使其能在本地环境中工作，同时保留云端的扩展能力。

---

### 3. [Google 展示基于 Gemma 4 + WebGPU 的完全本地浏览器代理](https://x.com/googlegemma/status/2048805789788413984)
> Google Gemma 团队演示了一个 100% 本地运行的浏览器代理，使用 Gemma 4 和 WebGPU，支持原生工具调用，包括浏览历史管理、标签页管理和页面摘要。这标志着本地 AI 代理的重要进展。

---

### 4. [Hermes Agent 仓库超越 Claude Code，原生视觉成为默认模式](https://x.com/Teknium/status/2048710115885523444)
> Hermes Agent 的 GitHub 仓库星数已超越 Claude Code。同时，当支持时，原生视觉已成为默认模式。Hermes 生态系统在代理框架领域持续获得关注。

---

### 5. [Cline Kanban 支持每个任务卡使用不同的代理/模型](https://x.com/cline/status/2048814649513275448)
> Cline 的看板功能现在支持为每个任务卡分配不同的代理或模型。这为复杂工作流提供了更大的灵活性，允许用户根据任务特性选择最合适的模型。

---

### 6. [微软开源 TRELLIS.2：4B 参数图像转 3D 模型](https://github.com/microsoft/TRELLIS.2)
> 微软发布 TRELLIS.2，一个 4B 参数的开源模型，可从图像生成高达 1536³ 分辨率的高保真 3D 资产，支持完整 PBR 材质。采用创新的“O-Voxel”结构，实现 16 倍空间压缩。代码和演示均已开源。

---

### 7. [AMD Hipfire：专为 AMD GPU 优化的新推理引擎](https://www.localmaxxing.com/)
> AMD Hipfire 是一个非官方的推理引擎，专为 AMD GPU 优化，使用独特的 mq4 量化方法。在 RX 7900 XTX 上相比基线实现 2.86 倍加速。在 AR 解码方面表现优异，但在预填充方面落后于 llama.cpp，特别适合结构化/代码生成任务。

---

### 8. [Luce DFlash：Qwen3.6-27B 在单张 RTX 3090 上实现 2 倍吞吐量](https://www.reddit.com/r/LocalLLaMA/comments/1sx8uok/luce_dflash_qwen3627b_at_up_to_2x_throughput_on_a/)
> Luce DFlash 是 Qwen3.6-27B 模型的新推测解码实现，在单张 RTX 3090 上使用独立的 C++/CUDA 栈（基于 ggml），在 HumanEval、GSM8K 和 Math500 等基准上实现高达 1.98 倍的吞吐量提升，无需重新训练。

---

### 9. [DeepSeek 再次降价：缓存命中输入 token 降至原价的 1/10](https://www.reddit.com/r/DeepSeek/comments/1sw6y3c/deepseek_reduces_prices_again_the_price_for_input/)
> DeepSeek 宣布永久性降价，缓存命中输入 token 价格从 $0.145 降至 $0.0145，仅为原价的 1/10。这对需要 1M 上下文长度的应用尤其有利，显著增强了 DeepSeek 的市场竞争力。

---

### 10. [LlamaIndex 发布 ParseBench：2000 页企业文档解析基准](https://x.com/osanseviero/status/2048777802015535189)
> LlamaIndex 推出 ParseBench，包含 2000 页经过验证的企业文档，用于评估解析代理的性能。这填补了企业级文档解析评估的空白，为开发者提供了更贴近实际应用场景的测试标准。