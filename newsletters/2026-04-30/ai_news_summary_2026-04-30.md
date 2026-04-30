## AINews - 2026-04-30

> [原文链接](https://news.smol.ai/issues/26-04-28-not-much/)

## 📰 十大AI新闻要点

### 1. [vLLM v0.20.0 发布：聚焦内存与MoE服务效率](https://x.com/TeksEdge/status/2048983564801450315)
> vLLM v0.20.0 正式发布，核心亮点包括：**TurboQuant 2-bit KV缓存**实现**4倍KV容量**；为SM90+架构重新启用FA4 MLA预填充；引入新的**vLLM IR**基础架构；融合RMSNorm带来**2.1%端到端延迟改进**。此外，该版本还支持DeepSeek V4 MegaMoE在Blackwell、Jetson Thor、ROCm、Intel XPU等平台上的运行，并简化了GB200/Grace-Blackwell的部署。SemiAnalysis 同时指出，在B200/B300/H200/GB200分离式部署中，**B300处理DeepSeek V4 Pro的速度可达H200的8倍**。

---

### 2. [Poolside 发布首个公开模型 Laguna XS.2：33B/3B活跃参数的MoE编码器](https://x.com/poolsideai/status/2049144111626670282)
> Poolside 宣布推出其首个公开模型 Laguna XS.2，这是一个**33B总参数量/3B活跃参数**的MoE编码模型，完全内部训练，采用**Apache 2.0**许可，并宣称可在**单张GPU**上运行。同时发布的还有**Laguna M.1**和一个Agent框架。该模型采用**混合注意力机制**和**FP8 KV缓存**，性能接近**Qwen-3.5**。Ollama 已立即支持该模型。

---

### 3. [NVIDIA 发布 Nemotron 3 Nano Omni：30B/A3B 多模态MoE模型](https://x.com/NVIDIAAI/status/2049159441870717428)
> NVIDIA 发布了 Nemotron 3 Nano Omni，这是一个开源的**30B / A3B 多模态MoE**模型，拥有**256K上下文**，专为处理**文本、图像、视频、音频和文档**的Agent工作负载而设计。该模型发布后迅速获得全栈支持，包括OpenRouter、LM Studio、Ollama、Unsloth、fal、Fireworks、DeepInfra、Together、Baseten等平台均宣布同日可用。其**5.95%的词错误率（WER）** 在Open ASR排行榜上表现突出，多个主机声称其吞吐量是同类开源全模态模型的**约9倍**。

---

### 4. [Mistral 推出 Workflows 公开预览版：企业级AI编排层](https://x.com/MistralAI/status/2049128071874179091)
> Mistral 发布了 Workflows 公开预览版，这是一个旨在将企业AI流程转变为**持久、可观测、容错的生产系统**的编排层。这标志着Agent构建者正从演示阶段转向生产原语。相关讨论也强调了**持久执行**对于长时间运行的Agent至关重要，以及子Agent/Agent即工具（具备持久化、流式传输和恢复能力）的发展方向。

---

### 5. [本地/离线Agent取得可信进展：从愿景到可行工作流](https://x.com/Teknium/status/2048975223853350976)
> Teknium 断言“完全离线的Agent是可能的”，Niels Rogge 演示了Pi与本地模型结合用于桌面清理，Google Gemma 分享了本地编码Agent教程。Hugging Face 的本地化推动也体现在数据上：Clement Delangue 表示已有**30万用户**在Hub上添加了硬件规格以探索本地可运行的模型。此外，Ammaar 开源了一个在设备上通过MLX运行Gemma 4的vibe-coding应用。

---

### 6. [GPT-5.5 Pro 在 Epoch 能力指数上达到159，并在FrontierMath上取得新高](https://x.com/EpochAIResearch/status/2049186851844771888)
> Epoch AI Research 报告称，GPT-5.5 Pro 在**Epoch能力指数（ECI）** 上达到**159分**，并在**FrontierMath**基准测试中创下新高：**Tier 1-3达到52%**，**Tier 4达到40%**。其中，有两个Tier 4问题此前从未被任何模型解决。同时，Greg Kamradt 表示GPT-5.5和Opus 4.7的ARC-AGI-3测试已完成，失败模式正在分析中。

---

### 7. [ChatGPT 5.4 解决了一个60多年未解的Erdős数学难题](https://www.reddit.com/r/singularity/comments/1sxixck/chat_gpt_54_solved_a_60_years_unsolved_erdos/)
> 据报道，ChatGPT 5.4 Pro 在**1小时20分钟**内解决了一个长达60多年的Erdős数学难题（Erdős #1196）。该解决方案由一位23岁的用户引导，通过应用一个已知公式的新颖方式实现。著名数学家**陶哲轩**已评论并确认该证明的合法性。这一成就挑战了LLM仅能预测下一个token而缺乏真正推理能力的观点。

---

### 8. [Google 与五角大楼的机密AI协议引发内部强烈反弹](https://x.com/kimmonismus/status/2049081961222955403)
> 据报道，Google签署了一项协议，允许其AI用于机密工作和“任何合法的政府目的”，合同语言可能允许政府请求修改安全过滤器，而对监控或自主武器的限制仅为非约束性的“非预期用途”。这引发了来自Google/DeepMind内部的罕见公开批评，有员工称其“可耻”，并指出事先没有内部公告或讨论。该事件凸显了**安全政策、部署控制和合同语言正日益成为前沿AI提供商产品表面的一部分**。

---

### 9. [Anthropic 悄然为 Claude Code Pro 用户设置 Opus 模型额外付费墙](https://www.reddit.com/r/ClaudeAI/comments/1sxi9mo/anthropic_just_quietly_locked_opus_behind_a/)
> Anthropic 被曝为 Claude Code 用户引入了新的定价结构，即使是Pro计划（$20/月）的用户，也需要额外付费才能访问**Opus模型**。默认模型为Sonnet 4.5，而Opus 4.5被锁定在额外付费墙之后。此举引发了用户对透明度和成本影响的强烈不满，并被视为向计量模式转变的信号。

---

### 10. [GitHub Copilot 对 Claude 模型实施9倍价格上调](https://www.reddit.com/r/ClaudeAI/comments/1sxcxge/github_copilot_9x_price_increase_for_claude_models/)
> GitHub Copilot 宣布从6月开始，对Claude模型实施**900%的价格上调**，从固定计划转向基于使用量的计费模式。这一变化是向API计费转变的一部分，可能会严重依赖Claude Agent进行生产的企业客户产生重大影响，因为推理成本的增加将显著改变单位经济效益。评论者指出，缺乏对Agent操作和Token使用情况的可见性会加剧财务影响。

---

## 🛠️ 十大工具产品要点

### 1. [vLLM v0.20.0：TurboQuant 2-bit KV缓存与DeepSeek V4 MegaMoE支持](https://x.com/TeksEdge/status/2048983564801450315)
> 核心特性：**TurboQuant 2-bit KV缓存**（4倍KV容量）、**FA4 MLA预填充**（SM90+）、**vLLM IR**新基础架构、**融合RMSNorm**（2.1%端到端延迟改进）。支持**DeepSeek V4 MegaMoE on Blackwell**、Jetson Thor、ROCm、Intel XPU，并简化GB200/Grace-Blackwell部署。

---

### 2. [Poolside Laguna XS.2：33B/3B活跃参数MoE编码模型，单GPU可运行](https://x.com/poolsideai/status/2049144111626670282)
> 特性：Apache 2.0许可，**33B总参/3B活跃参数**MoE，**混合注意力**，**FP8 KV缓存**，性能接近Qwen-3.5。Ollama立即支持。同时发布Laguna M.1和Agent框架。

---

### 3. [NVIDIA Nemotron 3 Nano Omni：30B/A3B多模态MoE，256K上下文](https://x.com/NVIDIAAI/status/2049159441870717428)
> 特性：开源，**30B/A3B**多模态MoE，**256K上下文**，支持文本/图像/视频/音频/文档。**Parakeet编码器**实现5.95% WER。全栈同日可用（OpenRouter, LM Studio, Ollama, Unsloth, fal, Fireworks等），吞吐量是同类模型的**9倍**。

---

### 4. [Microsoft TRELLIS.2：4B参数开源图像转3D模型](https://github.com/microsoft/TRELLIS.2)
> 特性：**4B参数**，图像转3D，输出**1536³ PBR纹理资产**。采用**原生3D VAE**实现**16倍空间压缩**。基于“无场”稀疏体素结构O-Voxel，可重建复杂3D拓扑。开源，提供Hugging Face演示。

---

### 5. [Mistral Workflows：企业级AI编排层（公开预览）](https://x.com/MistralAI/status/2049128071874179091)
> 特性：将AI流程转化为**持久、可观测、容错**的生产系统。支持**子Agent/Agent即工具**，具备持久化、流式传输和恢复能力。面向企业级长时运行Agent的编排需求。

---

### 6. [Luce DFlash：Qwen3.6-27B在单张RTX 3090上实现2倍吞吐量](https://www.reddit.com/r/LocalLLaMA/comments/1sx8uok/luce_dflash_qwen3627b_at_up_to_2x_throughput_on_a/)
> 特性：基于`ggml`的独立C++/CUDA栈，实现**DDTree树验证推测解码**、**KV缓存压缩**、**滑动窗口Flash Attention**。在HumanEval、GSM8K、Math500上达到**1.98倍吞吐量**，支持**256K上下文**，无需重新训练。

---

### 7. [Hermes Agent：在指令遵循和实际工作流中超越OpenClaw](https://x.com/SecretArjun/status/2049006382763110639)
> 特性：多个报告显示Hermes在指令遵循和实际工作流中表现优于OpenClaw。已通过Telegram部署，并用于医学文献提取等场景。强调**Harness选择**对模型性能的关键影响。

---

### 8. [LlamaIndex ParseBench：文档智能基准测试，超越OCR](https://x.com/llama_index/status/2049139409316946011)
> 特性：强调OCR基准测试忽略了**语义格式**（如删除线和上标），这些格式会实质性地改变Agent对文档的理解。ParseBench旨在更真实地评估文档智能能力。

---

### 9. [Modded-NanoGPT Optimizer Benchmark：轻量级优化器比较框架](https://x.com/kellerjordan0/status/2049193527440187494)
> 特性：Keller Jordan发布的轻量级优化器基准测试，用于在可复现的速通式任务上比较**Muon**和**AdamW**等优化方法。旨在为优化器研究提供标准化、可复现的评估环境。

---

### 10. [DeepSeek V4 Pro 激进定价与缓存折扣](https://x.com/ZhihuFrontier/status/2049027925920637077)
> 特性：DeepSeek 推出激进的V4 Pro定价策略和缓存折扣，并**延长至5月底**。此举强化了开源模型的经济性优势，促使许多Haiku/Flash工作负载被重新评估是否转向DeepSeek、Minimax、GLM、Nemotron等开源模型家族。