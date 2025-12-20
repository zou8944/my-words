## AINews - 2025-12-20

> [原文链接](https://news.smol.ai/issues/25-12-18-claude-skills-grows/)

## 📰 十大AI新闻要点

### 1. [Claude Skills 增长迅猛，成为事实上的可移植性标准](https://x.com/swyx/status/1998786773477110049)
> Anthropic 的 Claude Skills 概念持续发展，其相关演讲视频在一天内获得超过10万次观看，成为AI领域历史上最快达到此里程碑的视频。Skills 作为一种可互操作的包装格式（指令/脚本/资源），正获得强大的工具链支持，包括 VS Code 已支持其开放标准，社区评论将其比作 MCP 的标准化进程。

---

### 2. [OpenAI 发布 GPT-5.2-Codex，专注智能体编码与网络安全](https://twitter.com/OpenAIDevs/status/2001723687373017313)
> OpenAI 发布了 GPT-5.2-Codex，定位为其最佳的“智能体编码”模型，改进了原生压缩、长上下文可靠性和工具调用能力。该模型已向付费 ChatGPT 用户推出，API“即将推出”。Sam Altman 强调了其在现实世界安全方面的影响（如 React 漏洞披露），并提及正在探索用于防御性网络能力的“可信访问”。

---

### 3. [Google 发布 FunctionGemma 与 T5Gemma 2，推动设备端AI](https://twitter.com/osanseviero/status/2001704034667769978)
> Google/DeepMind 发布了 FunctionGemma（270M参数）和 T5Gemma 2。FunctionGemma 是一个纯文本函数调用基础模型，需要领域微调，旨在实现设备端/浏览器部署。T5Gemma 2 则是一个罕见的多模态、多语言编码器-解码器模型系列（270M/1B/4B）。生态系统迅速跟进，Ollama、Unsloth、MLX 均已提供支持。

---

### 4. [METR 修正时间范围评估套件，Claude 性能被低估](https://twitter.com/METR_Evals/status/2001473506442375645)
> 评估机构 METR 报告其时间范围任务中存在两个问题，其中一个问题“差异性地降低了 Claude 的性能”。在发布修正后的仪表板数据后，评论指出 Claude Sonnet 4.5 的性能被低估，修正后其表现提升了约20分钟。这揭示了基准测试的工程细节可能对跨模型比较产生重大偏差。

---

### 5. [OpenAI 发布链式思维（CoT）可监控性评估框架](https://twitter.com/OpenAI/status/2001791131353542788)
> OpenAI 发布了一个旨在衡量模型何时表达其内部推理特定方面的评估套件（涵盖24个环境的13项评估）。该研究认为，可监控性取决于监控强度和测试时计算量，后续提问可以引出先前未说出的想法。Neel Nanda 将其与解释激活的“元模型”联系起来。

---

### 6. [MLX 通过 JACCL 实现 Mac 多节点分布式计算](https://twitter.com/awnihannun/status/2001667839539978580)
> Apple 的 MLX 框架新增了一个名为 JACCL 的分布式后端，利用 Thunderbolt 5 上的 RDMA 技术实现多台 Mac 之间的低延迟通信。后续更新还包括 CUDA 后端改进、更快的预填充/训练速度，以及利用 JACCL 的 mlx-lm 张量并行推理。

---

### 7. [vLLM 在多节点 H200 上实现宽专家并行 MoE 的高吞吐量](https://twitter.com/vllm_project/status/2001695354983723361)
> 新的基准测试结果显示，通过宽专家并行、负载均衡和分解方法，vLLM 在 H200 GPU 上实现了约 2.2k tokens/s 的持续吞吐量（此前约为 1.5k）。该推文强调了通信/KV缓存瓶颈，以及通过 DeepEP all-to-all 和重叠策略进行的缓解。

---

### 8. [Mistral 发布 OCR 3，号称文档智能前沿模型](https://twitter.com/MistralAI/status/2001669581275033741)
> Mistral AI 发布了 OCR 3，称其为新的“前沿”文档智能模型，在准确性和效率方面有显著提升。Guillaume Lample 指出其在手写体、低质量扫描件和复杂表格/表单识别方面的改进。这对于依赖高质量文档处理的 RAG/文档智能体来说是一个重要的瓶颈突破。

---

### 9. [Kling 2.6 推出运动控制功能，实现高度可控视频生成](https://twitter.com/seiiiiiiiiiiru/status/2001502678116110430)
> 多个高参与度的帖子声称，Kling 的新“运动控制”功能能够实现高度可控的全身运动、表情和唇形同步。一些帖子称其“在所有指标上击败了竞争对手”，但缺乏共享的评估协议。这标志着视频生成在可控性方面取得了显著进展。

---

### 10. [AI 在医疗诊断中的实际应用案例引发关注](https://www.reddit.com/r/singularity/comments/1ppp0p4/2_weeks_ago_i_had_a_latenight_conversation_with/)
> Reddit 用户分享亲身经历，称 AI 模型 Grok 在深夜对话中促使其要求进行 CT 扫描，最终诊断出阑尾破裂，拯救了其生命。另一案例中，ChatGPT 准确建议用户可能患有带状疱疹，促使其及时就医并获得确诊。这些案例凸显了 AI 在辅助医疗决策和初步评估中的潜在效用，同时也引发了关于责任与信任的讨论。

---

## 🛠️ 十大工具产品要点

### 1. [Claude Skills 新增组织管理、目录和开放标准](https://claude.com/blog/organization-skills-and-directory)
> Anthropic 为 Claude Skills 推出多项更新：支持跨组织的管理员管理；发布新的 Skills 目录（似乎与 MCP 重叠）；并成为一个名为“Agent Skills”的供应商中立“开放标准”。这些更新旨在推动 Skills 在企业中的采用和标准化。

---

### 2. [Gemini 3 Flash 因速度改变工作流程，被集成至 Gemini 应用](https://twitter.com/Google/status/2001746491275083925)
> 多位从业者认为，Gemini 3 Flash 因其速度优势改变了日常工作流程，速度不仅影响基准测试，更改变了迭代循环和用户行为（留存/参与度）。Google 将 Flash 集成到 Gemini 应用中，作为“通过语音构建应用”的基础功能进行推广。

---

### 3. [Arena-Rank：开源的、基于 JAX 的模型对战排名包](https://github.com/lmarena/arena-ai)
> LMArena 团队发布了 Arena-Rank，这是一个开源的 Python 包，为其配对比较排行榜提供支持。该包采用基于 JAX 的优化，并将预处理与建模清晰分离，可通过 `pip install arena-rank` 安装，为前沿模型比较提供了生产级基础设施。

---

### 4. [OpenRouter 推出 JSON 修复层，大幅减少缺陷](https://openrouter.ai/announcements/response-healing-reduce-json-defects-by-80percent)
> OpenRouter 推出了一个积极的 JSON 修复层，可自动修复格式错误的工具/JSON 响应。据称，这在 Gemini 2.0 Flash 上减少了 80% 的缺陷，在 Qwen3 235B 上减少了 99.8% 的缺陷。该平台还推出了针对长上下文（100k–1M tokens）工作负载的排行榜过滤器。

---

### 5. [SonicMoE：针对 NVIDIA Hopper GPU 优化的 MoE 实现](https://arxiv.org/abs/2512.14080)
> 研究人员推出了 SonicMoE，这是一个针对 NVIDIA Hopper GPU 优化的混合专家模型实现。据称，与之前的 SOTA 相比，其在 H100 上减少了 45% 的激活内存，速度提升了 1.86 倍。代码已在 GitHub 上开源。

---

### 6. [Exa AI Labs 推出基于 10 亿个体的语义人物搜索](https://x.com/exaailabs/status/2001373897154007390)
> Exa AI Labs 推出了“人物搜索”，这是一个基于微调 Exa 嵌入的混合检索语义引擎，覆盖超过 10 亿个体。这展示了利用 LLM 在大规模人物图谱上进行搜索和发现的潜力，同时也引发了关于隐私和滥用的隐忧。

---

### 7. [Strawberry：基于 Gemini 1.5 Flash 的 Android 语音助手](https://www.strawberry.li/)
> 一位工程师在 HuggingFace 社区展示了一款名为 Strawberry 的 Android 语音助手，其推理部分由 Gemini 1.5 Flash 驱动，语音合成使用 VoxCPM 1.5，并针对 Apple Neural Engine 进行了优化以降低 iOS 设备延迟。

---

### 8. [Unsloth 更新实现 3 倍训练加速和 30% VRAM 节省](https://docs.unsloth.ai/new/3x-faster-training-packing)
> Unsloth 的最新更新通过新内核和无填充实现，实现了 3 倍训练加速和 30% VRAM 使用减少，使得在单张 80GB GPU 上进行 500K 上下文训练成为可能。该更新还支持 Google 的 FunctionGemma、NVIDIA 的 Nemotron 3 以及新的视觉模型 GLM-4.6V。

---

### 9. [dLLM 库：可将任何自回归语言模型转化为扩散语言模型](https://twitter.com/akshay_pachaar/status/2001562985043783908)
> dLLM 库声称可以“将任何自回归语言模型转化为扩散语言模型”，并提供统一的训练和评估流程。这反映了社区正趋向于“从预训练的自回归模型适配”，而非从头训练扩散语言模型。

---

### 10. [Rust 版 vLLM Router：为 vLLM 集群设计的控制平面](https://d1hr2uv.github.io/api-agents.html)
> 社区讨论了一个基于 Rust 的 vLLM Router，它为 KV 缓存局部性提供一致性哈希、2的幂次负载均衡、重试/退避、熔断器、Kubernetes 服务发现和 Prometheus 指标。这是一个专为 vLLM 集群构建的控制平面，针对 P/D 分解和尾部延迟控制进行了调优。

---