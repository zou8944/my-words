## AINews - 2026-04-10

> [原文链接](https://news.smol.ai/issues/26-04-08-not-much/)

## 📰 十大AI新闻要点

### 1. Meta正式发布首款超级智能模型Muse Spark
> Meta Superintelligence Labs正式推出其首款模型Muse Spark，定位为原生多模态推理模型，具备工具使用、视觉思维链和多智能体编排（“沉思模式”）能力。该模型已在meta.ai和Meta AI应用中上线，并向部分合作伙伴提供私有API预览。Meta表示未来版本将开源，但首版不会。
来源：[@AIatMeta](https://x.com/AIatMeta/status/2041910285653737975)

---

### 2. Muse Spark在第三方基准测试中表现强劲，跻身前沿模型行列
> 第三方评估显示Muse Spark是真正的前沿竞争者。Artificial Analysis的“智能指数”给其打分为52，仅次于Gemini 3.1 Pro Preview、GPT-5.4和Claude Opus 4.6。该模型在MMMU-Pro（80.5%）和HLE（39.9%）上表现强劲，且推理令牌使用效率极高（仅5800万输出令牌）。Vals将其列为综合指数第3名，在TaxEval、金融和终端任务上表现出色。
来源：[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2041913043379220801)

---

### 3. Meta宣称其训练栈效率实现巨大飞跃
> Meta声称其重建的预训练栈，在达到与Llama 4 Maverick同等能力时，所需计算量减少了超过10倍。强化学习训练显示出平滑的扩展性，并存在一个“思维压缩”机制，即在响应长度压力下模型会变得更令牌高效。
来源：[@AIatMeta](https://x.com/AIatMeta/status/2041926291142930899)

---

### 4. GLM-5.1成为领先的开源权重模型
> 智谱AI的GLM-5.1被多个技术账号称为当前旗舰级开源权重模型。它采用类似DeepSeek-V3.2的架构（MLA和DeepSeek稀疏注意力），但层数更多，基准测试成绩更强。该模型采用MIT许可证，在SWE-Bench Pro上取得了开源SOTA成绩。
来源：[@rasbt](https://x.com/rasbt/status/2041864806534086881)

---

### 5. 通义千问Qwen3.6 Plus发布，性能显著提升但仍为闭源
> 阿里巴巴发布Qwen3.6-Plus，宣布其已完全可用于生产。Artificial Analysis评估其智能指数得分为50，比Qwen3.5 397B提升了5分，与MiniMax-M2.7大致相当，略低于GLM-5.1（51分）。其幻觉行为显著改善，AA-Omniscience指数从-30提升至+3，并保持100万令牌上下文窗口和相对低廉的价格。但阿里巴巴未发布可自托管权重。
来源：[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2041970925873320203)

---

### 6. Anthropic推出“托管智能体”，标志产品层向系统化服务转变
> Anthropic发布关于“托管智能体”的工程文章，将其描述为长期运行智能体的托管运行时。这标志着从“销售令牌”向“销售智能体成果”的战略转变，运行时、基础设施和工具编排正越来越多地与模型捆绑。
来源：[@AnthropicAI](https://x.com/AnthropicAI/status/2041929199976640948)

---

### 7. 新基准APEX-Agents-AA发布，揭示长视野专业任务挑战巨大
> Artificial Analysis发布了APEX-Agents-AA基准，这是对Mercor投资银行、咨询和法律领域专业工作任务基准的实现，包含452项任务。顶级模型表现接近：GPT-5.4为33.3%，Claude Opus 4.6为33.0%，Gemini 3.1 Pro Preview为32%。这表明即使在顶级模型中，这些现实、工具密集的长视野任务的一次通过率也仅约三分之一，可靠性仍有巨大提升空间。
来源：[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2041896261826310598)

---

### 8. Meta FAIR发布“交错推理的强化学习”研究，提出中训练阶段
> Meta FAIR发布关于“交错推理的强化学习”的研究，主张在预训练和后训练之间增加一个“中训练SFT+RL”阶段。在Llama-3-8B上，他们报告称相比直接的后训练RL，在推理基准上实现了3.2倍的改进。
来源：[@jaseweston](https://x.com/jaseweston/status/2041864833214095484)

---

### 9. 技术社区对Claude Mythos的炒作提出基于可复现性的反驳
> 针对Anthropic的Claude Mythos模型在网络安全能力上的炒作，技术社区提出了基于可复现性的反驳。Stanislav Fort报告称，使用开源模型复现了Anthropic展示的漏洞分析，包括8/8的模型恢复了标志性的FreeBSD零日漏洞，甚至在限定场景下，一个30亿参数级别的模型也能做到。这表明AI网络安全能力可能是“超级参差不齐的”，而非由单一闭源模型垄断。
来源：[@stanislavfort](https://x.com/stanislavfort/status/2041922370206654879)

---

### 10. 本地文档解析与检索技术取得进展
> 一系列进展聚焦于本地PDF/文档解析和检索。LlamaIndex发布了基于本地解析器LiteParse的Claude技能`/research-docs`，具备精确引用、页面级边界框和可审计HTML报告功能。Muna和Nomic发布了用于本地/设备端PDF布局解析的`nomic-layout-v1`。Weaviate的IRPAPERS基准发现，纯文本检索和图像检索在不同PDF搜索任务子集上失败，最佳结果来自多模态混合搜索。
来源：[@ErickSky](https://x.com/ErickSky/status/2041691680076681669)

---

## 🛠️ 十大工具产品要点

### 1. Cursor发布远程智能体执行与实时学习代码审查智能体
> Cursor发布多项产品级智能体改进：支持从任何机器远程执行智能体；以及一个代码审查智能体，能够实时从PR活动中学习，并声称在合并前解决了78%被发现的问题。
来源：[@cursor_ai](https://x.com/cursor_ai/status/2041912812637966552)

---

### 2. LangChain发布“Harness Hill-Climbing”研究，强调智能体自改进是系统工程
> LangChain发布关于“Harness Hill-Climbing”的研究，认为自改进智能体是一个系统工程问题，涉及评估集管理、过拟合控制、验收门控和更新算法，而非单一巧妙提示。
来源：[@Vtrivedy10](https://x.com/Vtrivedy10/status/2041927895434588401)

---

### 3. PyTorch Monarch框架大幅更新，增强分布式训练与智能体编排能力
> PyTorch的Monarch框架获得重大更新，增加了Kubernetes支持、AWS EFA和AMD ROCm上的RDMA、SQL遥测、实时仪表盘和TUI，明确旨在让超级计算机对人类和智能体都更易于操作。
来源：[@PyTorch](https://x.com/PyTorch/status/2041773098324603208)

---

### 4. Weights & Biases推出“自动化”功能，连接训练/评估事件与工作流
> Weights & Biases推出“自动化”功能，允许将训练/评估事件触发器连接到GitHub Actions、部署工作流和基础设施关闭流程中。
来源：[@wandb](https://x.com/wandb/status/2041948335863689338)

---

### 5. Meta FAIR开源并行推理方法ThreadWeaver
> Meta FAIR开源了并行推理方法ThreadWeaver，声称在保留顺序长思维链性能的同时，在六项任务上实现了高达3倍的加速。
来源：[@LongTonyLian](https://x.com/LongTonyLian/status/2041912704584331616)

---

### 6. LangChain在LangSmith Deployments中增加A2A支持
> LangChain在LangSmith Deployments中增加了A2A（智能体到智能体）支持，以促进多智能体通信。
来源：[@LangChain](https://x.com/LangChain/status/2041908977642967322)

---

### 7. 开源应用AgentHandover利用Gemma 4自动创建智能体技能
> AgentHandover是一款开源Mac应用，利用Gemma 4观察用户工作流程，并将其转换为结构化技能文件供智能体执行。它完全在设备上运行，通过MCP与Claude Code、OpenClaw等工具集成。
来源：[GitHub](https://github.com/sandroandric/AgentHandover)

---

### 8. Unsloth支持在8GB VRAM上本地微调Gemma 4
> Unsloth发布更新，支持在仅8GB VRAM的情况下本地微调Gemma 4模型，声称比FA2设置快约1.5倍，且VRAM占用减少约60%，并修复了多项错误。
来源：文章内容（Reddit讨论）

---

### 9. Cline智能体工具新增看板支持和Droid智能体支持
> Cline智能体工具新增了看板支持，改进了终端持久性，并增加了对Droid智能体的支持。
来源：[@cline](https://x.com/cline/status/2041940975208268196)

---

### 10. 研究实验室分享本地部署GPT-OSS-120B服务超10亿令牌/天的架构
> 一个大学医院的研究实验室分享了使用两个H200 GPU本地部署GPT-OSS-120B模型，每天处理超过10亿令牌的架构。该架构使用Docker、vLLM和LiteLLM，采用mxfp4量化，并利用PostgreSQL、Prometheus和Grafana进行监控。
来源：文章内容（Reddit讨论）