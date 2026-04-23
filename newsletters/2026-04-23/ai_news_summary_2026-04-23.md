## AINews - 2026-04-23

> [原文链接](https://news.smol.ai/issues/26-04-21-image-2/)

## 📰 十大AI新闻要点

### 1. [OpenAI 发布 GPT-Image-2 和 ChatGPT Images 2.0](https://x.com/OpenAI/status/2046670977145372771)
> OpenAI 正式推出 GPT-Image-2 模型及 ChatGPT Images 2.0 产品，强调在文本渲染、布局保真度、编辑、多语言支持和图像“思考”能力上的显著提升。该模型支持联网搜索、生成多个候选方案、自我检查输出，并能创建幻灯片、信息图、图表、UI 线框图和二维码等实用视觉内容。模型已通过 API 开放，并迅速被 Figma、Canva、Adobe Firefly 等下游工具集成。

---

### 2. [GPT-Image-2 在 Arena 基准测试中取得压倒性领先](https://x.com/arena/status/2046670703311884548)
> 根据 Arena 基准测试报告，GPT-Image-2 在文本到图像、单图编辑和多图编辑等所有图像竞技场排行榜上均位列第一，Elo 分数分别为 1512、1513 和 1464。尤其在文本到图像任务上，其领先优势高达 +242 Elo，显示出在实用图像任务（如 UI 设计、文档制作和生产力视觉内容）上的巨大飞跃。

---

### 3. [Hugging Face 发布开源研究循环智能体 ml-intern](https://x.com/akseljoonas/status/2046543093856412100)
> Hugging Face 推出开源智能体 `ml-intern`，旨在自动化后训练研究循环。该智能体能够阅读论文、追踪引用图谱、收集/重组数据集、启动训练任务、评估运行结果并从失败中迭代。社区测试显示，它可以在 10 小时内将 Qwen3-1.7B 在 GPQA 科学推理基准上的表现从 10% 提升至 32%，并能自主微调模型并将成果发布回 Hugging Face Hub。

---

### 4. [Moonshot 发布 Kimi K2.6 模型并展示长程编码能力](https://x.com/Kimi_Moonshot/status/2046531052957569211)
> Moonshot 发布了 Kimi K2.6 模型，这是一个拥有 1 万亿参数的混合专家模型，专注于长程编码和自主任务编排。演示显示，该模型能通过超过 4000 次工具调用，在 12 小时以上时间内下载并用 Zig 语言优化 Qwen3.5-0.8B 的推理代码，将吞吐量从 ~15 tok/s 提升至 ~193 tok/s，最终性能比 LM Studio 快约 20%。

---

### 5. [Moonshot 开源高性能注意力内核 FlashKDA](https://x.com/Kimi_Moonshot/status/2046607915424034839)
> Moonshot 开源了 FlashKDA，这是一个基于 CUTLASS 的 Kimi Delta Attention 内核实现。据称，在 H20 GPU 上，其预填充速度比 flash-linear-attention 基线快 1.72 倍至 2.22 倍，可作为后者的即插即用后端。外部测试显示，K2.6 结合 DFlash 在 8x MI300X 上实现了 508 tok/s 的吞吐量，比基线自回归设置提升了 5.6 倍。

---

### 6. [Google 推出升级版 Deep Research 和 Deep Research Max API](https://x.com/Google/status/2046627647208259835)
> Google/DeepMind 通过 Gemini API 发布了升级版的 Deep Research 和 Deep Research Max，由 Gemini 3.1 Pro 驱动。新版本支持协作规划、任意 MCP 工具连接、多模态输入（PDF/CSV/图像/音频/视频）、代码执行、原生图表/信息图生成以及实时进度流。Deep Research Max 在 DeepSearchQA、BrowseComp 和 HLE 等基准测试中取得了高分，旨在产品化“隔夜尽职调查/分析师报告生成”工作流。

---

### 7. [LightOn 发布高效开源检索模型 LateOn 和 DenseOn](https://x.com/raphaelsrty/status/2046609364929187845)
> LightOn 发布了 LateOn 和 DenseOn 两款 1.49 亿参数的检索模型，采用 Apache 2.0 许可证。LateOn（多向量/ColBERT 风格）在 BEIR 基准测试上的 NDCG@10 达到 57.22，DenseOn（密集单向量）达到 56.20，性能超过了参数规模达其 4 倍的模型。同时，他们还发布了包含 14 亿查询-文档对的整合数据集。

---

### 8. [Anthropic 将 Claude Code 功能从 Pro 订阅计划中移除](https://claude.com/pricing)
> Anthropic 在未发布正式公告的情况下，从其 Claude Pro 订阅计划的定价页面和功能列表中移除了 Claude Code。根据更新的支持文章，Claude Code 现在仅包含在 Max 计划中。这一变动引发了 Pro 计划用户的困惑和不满，可能导致部分用户转向其他替代方案。

---

### 9. [DeepSeek 宣布支持 100 万上下文并发布 mHC 架构论文](https://www.reddit.com/r/DeepSeek/comments/1sqw6dq/deepseeks_3_underrated_advantages_1m_context/)
> DeepSeek 宣布其模型已支持 100 万令牌的上下文窗口，无需分块即可处理大量数据输入。同时，他们发布了关于流形约束超连接架构的新论文，旨在提高训练稳定性和效率。此外，DeepSeek 的 API 定价保持竞争力，为每百万令牌 0.28 美元，显著低于 GPT-4o 等竞争对手。

---

### 10. [vLLM 推出交互式部署知识库 recipes.vllm.ai](https://x.com/vllm_project/status/2046592125740142903)
> vLLM 项目重新设计了 recipes.vllm.ai 网站，将其打造为一个实用的部署知识层。该网站将模型页面映射到可运行的部署方案，包含交互式命令构建器，支持 NVIDIA 和 AMD 硬件，涵盖张量/专家/数据并行变体，并暴露了供智能体使用的 JSON API。这种基础设施文档层旨在降低部署新开源模型的操作摩擦。

---

## 🛠️ 十大工具产品要点

### 1. [GPT-Image-2 API 现已可用](https://x.com/OpenAIDevs/status/2046671238534496259)
> OpenAI 开发者账号宣布 GPT-Image-2 模型现已通过 API 提供。开发者可以调用该 API 来利用其强大的图像生成和编辑能力，集成到自己的应用程序和工作流中。

---

### 2. [Figma、Canva 等工具宣布集成 GPT-Image-2](https://x.com/figma/status/2046673364496875977)
> 在 GPT-Image-2 发布后，包括 Figma、Canva、Adobe Firefly、fal.ai 和 Hermes Agent 在内的多个下游设计和创意工具迅速宣布了集成计划，表明该模型将很快成为这些平台内部工作流的一部分。

---

### 3. [Hermes 智能体平台功能持续增强](https://x.com/Teknium/status/2046709250114957624)
> Hermes 智能体平台正在演变为一个更丰富的本地/开源智能体堆栈。最新更新显示，其子智能体现在支持更大的生成宽度和递归生成深度，实现了更深层次的层次化任务分解，标志着从“单一聊天循环”智能体向具有内存、工具、权限和可复用技能的多进程编排系统转变。

---

### 4. [DSPy 3.2 发布 RLM 改进与优化器链](https://x.com/isaacbmiller1/status/2046643827247546441)
> DSPy 框架发布 3.2 版本，带来了检索语言模型改进、优化器链功能以及与 LiteLLM 的解耦。这些更新旨在提升构建和优化基于检索的 LM 系统的灵活性和效率。

---

### 5. [开源医疗推理模型 Chaperone-Thinking-LQ-1.0 发布](https://huggingface.co/empirischtech/DeepSeek-R1-Distill-Qwen-32B-gptq-4bit)
> 基于 DeepSeek-R1-Distill-Qwen-32B 微调的开源推理模型 Chaperone-Thinking-LQ-1.0 发布。该模型采用 4 位 GPTQ 量化，大小从约 60GB 压缩至约 20GB，在 MedQA 上达到 84% 的准确率，接近 GPT-4o 的 88%，推理速度比基础模型快 1.6 倍，适用于本地企业级医疗应用。

---

### 6. [LangChain 为 deepagents 部署添加自定义认证](https://x.com/sydneyrunkle/status/2046643201738449076)
> LangChain 宣布为其 deepagents 部署功能添加了自定义认证支持，这增强了在部署复杂智能体系统时的安全性和访问控制能力。

---

### 7. [Skillkit 增加对 Hermes 的原生支持](https://x.com/ghumare64/status/2046542176142733712)
> Skillkit 工具宣布增加对 Hermes 智能体平台的原生支持，使得开发者能够更便捷地在 Skillkit 环境中利用 Hermes 的能力来构建和编排智能体任务。

---

### 8. [为 Kimi K2.6 推出的 macOS GUI 应用 Scarf](https://x.com/QingQ77/status/2046592289540346020)
> 一款名为 Scarf 的新 macOS 图形用户界面应用被推出，旨在为 Kimi K2.6 模型提供更友好的本地交互体验，显示了开源模型在本地工作流中应用的增长趋势。

---

### 9. [LlamaIndex 推出图表理解基准 ParseBench](https://x.com/llama_index/status/2046586730879283227)
> LlamaIndex 推出了 ParseBench，这是一个专门用于评估 AI 模型在真实企业文档内部理解图表能力的基准测试，反映了业界对智能体在具体、复杂场景下盲点探测的重视。

---

### 10. [Google Research 提出 ReasoningBank 框架](https://x.com/GoogleResearch/status/2046631948437921801)
> Google Research 提出了 ReasoningBank 框架，该框架将记忆视为从成功和失败的轨迹中学习，旨在提升智能体的推理和学习能力，是智能体系统向更复杂、更健壮方向发展的一个研究信号。