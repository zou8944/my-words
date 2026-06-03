## AINews - 2026-06-03

> [原文链接](https://news.smol.ai/issues/26-06-01-not-much/)

## 📰 十大AI新闻要点

### 1. [NVIDIA发布Cosmos 3开源世界模型与Nemotron 3 Ultra](https://x.com/NVIDIAAI/status/2061498958283968735)
> NVIDIA本周主导了开源模型话题，发布了**Cosmos 3**——一个面向物理AI的全模态世界模型家族，以及**Nemotron 3 Ultra**——一个550B参数的开源权重模型，被多位评论者称为迄今为止最强的美国开源模型。Cosmos 3采用**混合Transformer**架构，将语言、图像、视频、音频和动作统一在一个模型中，结合自回归推理器和扩散生成器，在Artificial Analysis的文本到图像和图像到视频排行榜上均达到**#1**。

---

### 2. [MiniMax M3发布：开源多模态Agent模型](https://x.com/MiniMax_AI/status/2061425142795034794)
> MiniMax M3作为开源权重的多模态Agent/编码模型发布，拥有**1M上下文**、原生多模态能力，在SWE-Bench Pro上达到**59.0%**，Terminal Bench 2.1达到**66.0%**，MCP Atlas达到**74.2%**。多个基础设施供应商（Novita、Vercel AI Gateway、Cloudflare AI Gateway等）在发布首日即提供支持，显示出异常快速的生态系统采用。但评测者也报告了**高Token消耗**和冗长的自我检查循环问题。

---

### 3. [Anthropic秘密提交IPO申请](https://x.com/AnthropicAI/status/2061478052257841495)
> Anthropic宣布已向SEC**秘密提交S-1草案**，开启了IPO之路，目前正在等待审查。这是AI领域最受关注的IPO动态之一，标志着Anthropic从私营公司向上市公司的战略转变。

---

### 4. [Perplexity推出“Search as Code”架构](https://x.com/perplexity_ai/status/2061506359326384319)
> Perplexity发布了“Search as Code”方案，模型不再进行迭代搜索工具调用，而是编写**Python代码**调用搜索SDK，实现自定义排序管道、Map-Reduce索引、批处理和聚合，显著降低Token开销。Perplexity报告其内部WANDR基准测试从**0.152跃升至0.386**，这是Agent架构创新的重要案例。

---

### 5. [Google推出Gemini API托管Agent](https://x.com/_philschmid/status/2061457703210197273)
> Google详细介绍了**Gemini API中的托管Agent**功能，单个API调用即可启动一个能推理、编写/运行代码、管理文件并在托管**Linux沙箱**内操作的Agent。这标志着Agent运行时正成为主要工程杠杆点，而非模型调用本身。

---

### 6. [OpenAI Codex登陆AWS Bedrock](https://x.com/OpenAI/status/2061564502160892138)
> OpenAI宣布前沿模型和**Codex**现已在**AWS / Amazon Bedrock**上全面可用，面向希望在现有AWS安全/合规工作流中使用OpenAI能力的企业。同时发布了**Codex Python SDK**，支持线程、轮次、流式、恢复、图像和沙箱控制。

---

### 7. [Claude Code出现Ops事故：并行子Agent导致配额耗尽](https://x.com/ClaudeDevs/status/2061501787769893055)
> Anthropic重置了Pro和Max用户的**5小时和周速率限制**，原因是修复了一个bug——某些**Opus 4.8**会话生成了过多**并行子Agent/工具调用**，意外消耗了用户配额。有用户报告Max计划会话限制被消耗两次，周使用量达到**70%以上**，这凸显了编码Agent的产品质量越来越取决于编排行为而非原始模型智商。

---

### 8. [NVIDIA推出RTX Spark个人AI计算机](https://x.com/kimmonismus/status/2061484174088007739)
> NVIDIA与微软合作推出了**RTX Spark**“个人AI计算机”，基于**Grace + Blackwell**架构，最高**128GB统一内存**，声称达到**1 PFLOP FP4**。战略意义在于NVIDIA不再仅销售加速器，而是提供端到端的本地AI系统，与Apple Silicon、x86 PC和Qualcomm同时竞争。

---

### 9. [Qwen3.7-Plus发布：多模态交互式混合Agent](https://x.com/Alibaba_Qwen/status/2061506641120641494)
> 阿里巴巴发布了**Qwen3.7-Plus**，一个统一**GUI和CLI操作**、视觉推理、编码和搜索增强QA的多模态交互式混合Agent。通过阿里云Model Studio提供API，并迅速被集成到Cline等工具中。这强化了亚洲实验室不再发布“仅聊天模型”，而是发布完整**Agent能力多模态系统**的趋势。

---

### 10. [JetBrains Mellum2：面向开发者工作流的小型快速模型](https://x.com/jetbrains/status/2061444430884675791)
> JetBrains发布了**Mellum2**，一个**12B MoE**模型（**2.5B活跃参数**），训练约**11T Token**，采用**RLVR**后训练，提供base/SFT/RL检查点。其定位是**超低延迟推理**，用于**路由、RAG、子Agent和IDE使用**，并立即登陆vLLM。这看起来是一个严肃的“面向开发者工作流的小型快速开源模型”策略。

---

## 🛠️ 十大工具产品要点

### 1. [NVIDIA Cosmos 3：开源全模态世界模型](https://x.com/NVIDIAAI/status/2061498958283968735)
> 开源发布，包含**权重、代码、数据集和微调配方**。采用混合Transformer架构，统一语言、图像、视频、音频和动作。生成器使用**结构化JSON提示**，可由外部提示放大或自身推理器分支驱动。在Artificial Analysis的Text-to-Image和Image-to-Video排行榜上均排名**#1**。

---

### 2. [NVIDIA Nemotron 3 Ultra：550B开源权重模型](https://x.com/NVIDIA/status/2061379856433107135)
> **550B-A55 MoE**架构，约55B活跃参数。社区反应异常强烈，声称在某些设置下可达**300+ tok/s**，远快于DeepSeek/Kimi类大型模型。Artificial Analysis评分**48**，接近前沿水平，被认为是迄今为止最强的美国开源模型。

---

### 3. [MiniMax M3：开源多模态Agent模型](https://www.minimax.io/models/text/m3)
> 开源权重，**1M上下文**（保证512K），原生多模态。采用**MiniMax Sparse Attention**技术。在SWE-Bench Pro（59.0%）、Terminal Bench 2.1（66.0%）、MCP Atlas（74.2%）上表现突出。支持12小时ICLR论文复现和Hopper FP8 GEMM CUDA/Triton优化（**9.4×加速**）。

---

### 4. [Perplexity “Search as Code”](https://x.com/perplexity_ai/status/2061506359326384319)
> 模型编写**Python代码**调用搜索SDK，而非迭代搜索工具调用。支持自定义排序管道、Map-Reduce索引、批处理和聚合。内部WANDR基准测试从**0.152提升至0.386**，显著降低Token开销。

---

### 5. [Google Gemini API托管Agent](https://x.com/GoogleAIStudio/status/2061452967530701090)
> 单个API调用即可启动一个能推理、编写/运行代码、管理文件并在托管**Linux沙箱**内操作的Agent。这是Agent即服务的重要进展，降低了构建复杂Agent系统的门槛。

---

### 6. [OpenAI Codex Python SDK](https://x.com/reach_vb/status/2061569472792572163)
> 支持**线程、轮次、流式、恢复、图像和沙箱控制**。同时Codex和前沿模型现已在**AWS Bedrock**上可用，面向企业级安全/合规工作流。

---

### 7. [MLX-VLM v0.6.0：本地Agent工具](https://x.com/Prince_Canuma/status/2061541992790683726)
> 新增**推测解码**、Anthropic风格和响应风格API、工具调用、多模态模型支持、图像/音频功能。明确目标是将Apple设备转变为“真正的本地Agent机器”。

---

### 8. [JetBrains Mellum2：12B MoE开发者模型](https://x.com/jetbrains/status/2061444430884675791)
> **12B总参数，2.5B活跃参数**，训练约11T Token，采用RLVR后训练。定位为**超低延迟推理**，用于路由、RAG、子Agent和IDE使用。提供base/SFT/RL检查点，立即登陆**vLLM**。

---

### 9. [Qwen3.7-Plus：多模态交互式混合Agent](https://x.com/Alibaba_Qwen/status/2061506641120641494)
> 统一**GUI和CLI操作**、视觉推理、编码和搜索增强QA。通过阿里云Model Studio提供API，已集成到Cline等工具中。代表亚洲实验室发布完整Agent能力多模态系统的趋势。

---

### 10. [NVIDIA RTX Spark：个人AI计算机](https://x.com/swyx/status/2061567877879369953)
> 基于**Grace + Blackwell**架构，最高**128GB统一内存**，声称**1 PFLOP FP4**。NVIDIA首次提供端到端本地AI系统，与Apple Silicon、x86 PC和Qualcomm竞争。Dell已确认将推出基于NVIDIA N1X的XPS笔记本。