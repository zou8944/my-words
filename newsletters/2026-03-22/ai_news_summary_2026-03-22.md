## AINews - 2026-03-22

> [原文链接](https://news.smol.ai/issues/26-03-20-not-much/)

## 📰 十大AI新闻要点

### 1. [Cursor Composer 2 模型基于 Kimi K2.5 引发行业讨论](https://x.com/Kimi_Moonshot/status/2035074972943831491)
> Cursor 发布的新编码模型 Composer 2 被证实基于 Kimi K2.5 模型，并进行了持续的预训练和高算力强化学习。Kimi 官方确认了与 Cursor 及 Fireworks 的商业合作关系。此事引发了关于开源模型衍生品在商业产品中的归属、许可合规性以及行业规范的广泛讨论，凸显了产品差异化正转向领域特定的持续预训练/强化学习、评估和用户体验。

---

### 2. [NVIDIA 发布高性能开源模型 Nemotron-Cascade 2](https://x.com/_weiping/status/2034877099908243746)
> NVIDIA 发布了 Nemotron-Cascade 2，这是一个拥有 300 亿参数、30 亿活跃参数的混合专家模型。该模型声称在 IMO 2025、IOI 2025 和 ICPC 世界总决赛 2025 中达到金牌水平，在数学、代码、对齐和指令遵循方面表现卓越，超越了 Qwen3.5 的某些变体。其发布标志着紧凑、高激活效率的推理模型成为开源领域的一流选择。

---

### 3. [Meta FAIR 发布视觉自监督学习模型 V-JEPA 2.1](https://x.com/TheTuringPost/status/2034795966931640533)
> Meta 的 FAIR 团队发布了 V-JEPA 2.1，这是一个重要的视觉自监督学习更新。新版本从仅掩码监督转向同时学习掩码和可见标记，增加了跨中间层的深度自监督，并使用共享编码器下的模态特定分词器。据报道，它在零样本机器人抓取任务上比 V-JEPA 2 的成功率提高了 20%，并在 Ego4D 和 EPIC-KITCHENS 密集预测任务上取得了新的 SOTA 成绩。

---

### 4. [研究显示针对性的数据预训练比微调更有效](https://x.com/konwookim/status/2035029597491011984)
> 来自斯坦福/Marin 生态系统的研究指出，通过合成“超级文档”进行数据高效的预训练，可以获得约 1.8 倍的数据效率提升。研究表明，在预训练阶段混合小型领域数据集比重复微调或重放更能抵抗过拟合。这强调了“模型适应”正成为一项关键的应用能力。

---

### 5. [开源编码工具生态快速发展，Claude Code 扩展至第三方](https://x.com/theo/status/2034831968463200359)
> Theo 宣布 T3 Code 集成 Claude Code，允许用户在 T3 Code 内部使用本地 Claude Code CLI。同时，Anthropic 似乎正将 Claude Code 从终端扩展到 Telegram 和 Discord 等渠道。开源维护者也报告了 Claude 支持计划在集成、性能分析和硬件感知管道优化等任务上带来的显著生产力提升。

---

### 6. [本地/离线深度研究代理栈日趋成熟](https://x.com/ihtesham2005/status/2035009684386771306)
> 多个帖子强调了“Local Deep Researcher”，这是一个 MIT 许可的本地研究循环工具，可以自行编写搜索查询、抓取信息、识别差距并迭代生成带引用的 Markdown 报告。社区演示还展示了在 Apple Silicon 和旧款 GPU 上使用 Hermes/OpenClaw、Qwen、Nemotron、Ollama 和混合运行器组合的完全本地代理栈。

---

### 7. [强化学习应用扩展到代码搜索和预测领域](https://x.com/gneubig/status/2035037624105410926)
> CMU/Meta 的研究人员引入了一种用于代码搜索模型的强化学习方案，仅使用 bash 终端作为探索界面，无需特殊工具即可获得强大结果。同时，Tinker 和 Mantic 报告称，在 gpt-oss-120b 上针对判断性预测进行的强化学习，在事件预测方面超越了前沿模型，推动了“自动化超级预测”的发展。

---

### 8. [文档解析正成为智能体基础能力并走向标准化](https://x.com/jerryjliu0/status/2034790590572060848)
> LlamaIndex 发布了 LiteParse，这是一个免费的本地解析器，可通过一行命令安装并接入 40-46+ 个智能体。它既可作为任务解决工具，也可作为向编码智能体提供文档上下文的方式。LlamaParse 还发布了官方智能体技能，用于跨格式、表格、图表和图像的更复杂文档理解。

---

### 9. [AI 助力个性化 mRNA 疫苗开发取得突破](https://www.the-scientist.com/chatgpt-and-alphafold-help-design-personalized-vaccine-for-dog-with-cancer-74227)
> 一位澳大利亚机器学习研究员利用 ChatGPT 和 AlphaFold，在两个月内为其患有致命性肥大细胞瘤的宠物狗开发出个性化 mRNA 疫苗，使肿瘤缩小了 75%。该案例通过测序肿瘤 DNA、使用 ChatGPT 识别新抗原、利用 AlphaFold 预测蛋白质结构完成，展示了 AI 在快速、个性化医疗中的巨大潜力。

---

### 10. [复古计算项目成功在 2002 年 PowerBook G4 上运行 TinyLlama](https://www.reddit.com/r/LocalLLaMA/comments/1ryu7rr/running_tinyllama_11b_locally_on_a_powerbook_g4/)
> 一个项目成功在运行 Mac OS 9 的 2002 年款 PowerBook G4 上本地运行了 TinyLlama 1.1B 模型。该项目采用了专门为经典 Macintosh 硬件设计的自定义 C89 推理引擎，通过 AltiVec SIMD 优化实现了 7.3 倍加速，并利用磁盘分页技术处理超出可用 RAM 的模型层，展示了在极端受限的复古硬件上运行现代 AI 模型的可能性。

---

## 🛠️ 十大工具产品要点

### 1. [Cursor Composer 2：基于 Kimi K2.5 的高性价比编码模型](https://x.com/leerob/status/2035035355364081694)
> Cursor 推出的 Composer 2 编码模型，在 Terminal-Bench 2.0 上以 61.7% 的得分超越 Claude Opus 4.6，且价格仅为后者的十分之一（$0.50/百万 tokens）。该模型专注于代码训练，并具备“自我总结”功能以压缩长会话上下文。

---

### 2. [T3 Code 集成 Claude Code](https://x.com/theo/status/2034831968463200359)
> T3 Code 编辑器现已集成 Claude Code，允许已安装本地 Claude Code CLI 的用户在编辑器内直接使用其功能，为开发者提供了新的编码辅助工作流。

---

### 3. [HermesWorkspace v0.2.0 发布，增强本地智能体体验](https://x.com/outsource_/status/2034788187944431914)
> HermesWorkspace 更新至 v0.2.0，新增一键启动、基于 UI 的提供商/模型配置、实时模型目录以及新的配置/模型端点，简化了本地智能体的设置和使用流程。

---

### 4. [LangChain 推出 Deep Agents/Open SWE 及 LangSmith Fleet](https://x.com/KSimback/status/2034793268886601986)
> LangChain 生态正在扩展，推出了作为 Claude Code 开源替代品的 Deep Agents/Open SWE，以及作为多智能体/劳动力风格产品层的 LangSmith Fleet，标志着其从编排框架向智能体产品演进。

---

### 5. [LlamaIndex LiteParse：轻量级本地文档解析器](https://x.com/jerryjliu0/status/2034790590572060848)
> LlamaIndex 发布的 LiteParse 是一个免费、本地的文档解析器，可通过 `npx skills add ... --skill liteparse` 快速集成到数十个智能体中，旨在将文档解析能力普及化。

---

### 6. [Prompt-Master：为特定 AI 工具优化提示的 Claude 技能](https://www.reddit.com/r/ClaudeAI/comments/1rxyarx/i_built_a_claude_skill_that_writes_accurate/)
> 一个名为 `prompt-master` 的 Claude 技能在 GitHub 上获得超过 600 星。它能智能检测目标 AI 工具（如 Midjourney, Claude Code），提取用户输入的多个维度，识别常见提示问题，并应用特定策略生成优化提示，以提高准确性和效率。

---

### 7. [OpenTabs：通过单一 MCP 服务器连接 Claude 与上百个网页应用](https://github.com/opentabs-dev/opentabs)
> OpenTabs 提供了一个开源解决方案，通过一个 MCP 服务器和 Chrome 扩展，让 Claude 能够利用现有的浏览器会话（如 Slack, Linear, Google Sheets）调用工具，无需管理多个 API 密钥，从而自动化跨应用的“粘合工作”。

---

### 8. [Perplexity Computer 集成 Pitchbook、Statista 和 CB Insights 数据](https://x.com/AravSrinivas/status/2035043246376984663)
> Perplexity 的 Computer 功能新增了对 Pitchbook、Statista 和 CB Insights 专业数据库的访问，进一步深入分析师和风险投资工作流，增强了其作为研究工具的能力。

---

### 9. [Devin 新增自调度周期性任务功能](https://x.com/cognition/status/2035041799245279498)
> AI 编码智能体 Devin 新增了自我调度周期性任务的能力，可以将一次性的任务会话转变为定期执行的工作流，提升了自动化程度。

---

### 10. [vLLM 成为文本推理端点的实际标准](https://x.com/vllm_project/status/2034828731983044971)
> 根据 RunPod 的生产数据，大约一半的纯文本推理端点运行着 vLLM 或其变体，这确立了 vLLM 在高性能模型服务领域的领先地位。