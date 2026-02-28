## AINews - 2026-02-28

> [原文链接](https://news.smol.ai/issues/2026-02-25-wtf-happened/)

## 📰 十大AI新闻要点

### 1. Perplexity发布“Computer”端到端AI代理系统
> Perplexity推出名为“Computer”的新产品，定位为一个能够“研究、设计、编码、部署和管理”项目的端到端系统。其核心突破在于采用并行、异步的子代理架构，由协调模型将任务分配给专门的研究、编码或媒体模型，而非单一的主代理循环。这代表了向系统级代理用户体验的推进，将“代理工作”视为分布式工作流。
> 来源：[Perplexity官方发布推文](https://x.com/perplexity_ai/status/2026695550771540489)

---

### 2. 编码代理能力发生“质变”，GPT-5.3-Codex等新模型发布
> Andrej Karpathy声称，自去年12月以来，编码代理已跨越了一个质变门槛，从脆弱的演示转变为能够持续、长视野地完成任务，具备连贯性和韧性。与此同时，OpenAI发布了GPT-5.3-Codex API，据称速度比5.2快约25%。Claude Code庆祝“一周年”，并集成了Slack插件等生态工具。GitHub Copilot CLI进入正式发布阶段，并新增了用于代码库深度研究的 `/research` 功能。
> 来源：[Andrej Karpathy关于编码代理质变的推文](https://x.com/karpathy/status/2026731645169185220)

---

### 3. Qwen3.5 Medium系列模型发布，推动本地代理临界点
> 阿里巴巴发布了Qwen3.5 Medium系列模型（包括35B-A3B、27B、122B-A10B），并获得了vLLM、GGUF、Ollama等工具的即时支持。该系列模型技术亮点包括：支持超长上下文（如35B-A3B在32GB显存上支持超过100万token）、宣称在4位量化下近乎无损的精度，以及开源了FP8权重。社区反馈认为，Qwen3.5-35B-A3B等模型使本地代理循环的可靠性显著提升，达到了本地代理的“临界点”。
> 来源：[Alibaba Qwen关于模型技术细节的推文](https://x.com/Alibaba_Qwen/status/2026502059479179602)

---

### 4. 代理可靠性问题凸显，研究聚焦工具接口优化与失败模式
> 有研究指出，尽管模型能力快速进步，但代理的**可靠性提升有限**。代理失败往往源于**可靠性问题而非能力不足**，例如微小的工具调用错误会在长视野任务中不断累积。Intuit AI Research的工作表明，工具描述的文本质量对代理成功至关重要，并提出了一种无需推理时追踪的课程学习方法（Trace-Free+）来优化工具接口，显著提升了代理在复杂工具环境下的表现。
> 来源：[关于代理可靠性研究的推文](https://x.com/IEthics/status/2026435186704134617)

---

### 5. 计算与内存架构成为AI扩展的核心约束
> Andrej Karpathy指出，LLM工作流（特别是长上下文下的解码和紧密的代理循环）的核心约束在于协调两种内存池：快速但微小的**片上SRAM**与大而慢的**片外DRAM**。如何为LLM工作流（预填充/解码/训练）组织内存和计算，以实现最佳吞吐量、延迟和成本效益，是当前最大的难题。同时，扩散LLM等替代架构因声称能达到约1000 tok/s的推理速度而受到关注。
> 来源：[Andrej Karpathy关于计算与内存的推文](https://x.com/karpathy/status/2026452488434651264)

---

### 6. Anthropic收购Vercept并调整其负责任扩展政策
> Anthropic宣布收购专注于“计算机使用”能力的公司Vercept，以增强Claude代表用户执行操作（尤其是非技术任务）的能力。同时，Anthropic对其“负责任扩展政策”进行了重大调整，从僵化的“达到阈值即停止训练”模式，转向更频繁地发布透明度报告和路线图，并更新威胁模型和外部审查承诺，这被解读为应对竞争压力和风险科学不确定性的举措。
> 来源：[Anthropic关于收购Vercept的公告](https://x.com/AnthropicAI/status/2026705792033026465)

---

### 7. AI军事化与安全政策引发激烈争议
> 据报道，美国国防部向Anthropic发出最后通牒，要求其移除Claude AI中关于禁止用于大规模监控和自主武器的安全护栏，否则可能动用《国防生产法》或将其列为供应链风险。与此同时，xAI（Grok）据称已与五角大楼达成协议，将其模型用于机密系统。这些事件引发了关于AI军事化、企业伦理与政府监管之间紧张关系的广泛讨论。
> 来源：文章内容（综合多个Reddit讨论）

---

### 8. 能源成为AI规模扩张的硬性约束
> 有报告指出，由于AI和数据中心需求对电网造成巨大压力，美国政治领导层正在推动主要AI公司**自行供应电力**，以避免引起纳税人的反弹。这表明AI的规模扩张正日益成为基础设施和政策问题，而不仅仅是算法问题。
> 来源：[关于能源约束的推文](https://x.com/kimmonismus/status/2026720759163298282)

---

### 9. 大规模可解释性基础设施取得进展
> Goodfire AI展示了能够以最小推理开销实现**万亿参数规模可解释性**的基础设施工作。该技术可以捕获**数十亿激活**，并已实现至少一个案例研究中对思维链的实时引导，为理解和控制超大模型提供了新工具。
> 来源：[Goodfire AI关于可解释性基础设施的推文](https://x.com/GoodfireAI/status/2026748839303246238)

---

### 10. 开发者工作流深度集成AI，引发行为模式改变
> 评估机构METR发现，软件开发者越来越拒绝在“无AI”的控制组中工作，认为传统手动编码过程效率低下，即使提供高额报酬（如50美元/小时）也无法吸引合格的工程参与者。这反映了AI工具（如Aider新增的 `/ok` 一键批准功能）已深度融入开发者工作流，并从根本上改变了开发行为。
> 来源：[METR关于测试协议更新的推文](https://x.com/METR_Evals/status/2026355544668385373)

---

## 🛠️ 十大工具产品要点

### 1. Perplexity Computer：基于使用的多模型代理编排平台
> Perplexity Computer是一个集文件、工具、内存和模型于一体的界面，采用基于使用量的定价模式。它首先面向Max订阅用户开放，提供消费上限和每月积分（Max用户含1万积分）。其核心是并行异步的子代理架构，用户可为不同子任务选择不同模型。
> 来源：[Perplexity关于定价详情的推文](https://x.com/perplexity_ai/status/2026695793537855526)

---

### 2. GitHub Copilot CLI GA版及 `/research` 功能
> GitHub Copilot CLI已达到正式发布（GA）状态。新增的 `/research` 命令可利用GitHub代码搜索和MCP进行动态抓取，对整个代码库进行深度研究，并将报告导出到Gist以便分享。
> 来源：[关于Copilot CLI `/research` 功能的推文](https://x.com/_Evan_Boyle/status/2026458533320077689)

---

### 3. Claude Code生态扩展：Slack插件与可观察性工具
> Claude Code推出了Slack插件集成，允许在Slack环境中直接使用编码代理。同时，社区通过LangSmith为Claude Code添加追踪功能，以调试其“削弱”/路由问题，提升可观察性。
> 来源：[关于Claude Code Slack插件的推文](https://x.com/_catwu/status/2026485966626763120)

---

### 4. ActionEngine：将GUI代理重构为图遍历的离线探索框架
> ActionEngine将GUI代理任务重新定义为**图遍历**问题。它通过离线探索生成一个状态机，在运行时仅需约1次LLM调用即可生成完整执行程序，据称相比逐步视觉循环方法，在成功率、成本和延迟方面有巨大改进。
> 来源：[dair_ai关于ActionEngine的推文](https://x.com/dair_ai/status/2026678090815123594)

---

### 5. 开源代理框架Hermes Agent发布
> Nous Research发布了开源Hermes Agent，这是一个具有多级记忆系统和持久专用机器访问权限的强大工具，可直接从CLI运行。早期采用者可在Nous门户使用优惠码获得免费体验。
> 来源：[Hermes Agent GitHub仓库](https://github.com/nousresearch/hermes-agent)

---

### 6. LM Link：通过Tailscale实现本地模型的远程加密访问
> LM Studio团队推出了LM Link功能，该功能利用Tailscale为用户提供无缝、端到端加密的远程访问，使其能够从任何地方安全地连接到本地LLM服务器。
> 来源：[LM Link文档](https://link.lmstudio.ai)

---

### 7. Aider编码助手新增 `/ok` 别名快速批准代码
> Aider编码助手在其主分支中合并了新的 `/ok` 别名，允许开发者一键批准并执行AI生成的代码编辑，极大简化了人机协作流程。
> 来源：文章内容

---

### 8. 低成本云GPU服务Packet.ai推出Blackwell GPU
> Packet.ai开始提供Blackwell GPU用于AI工作负载，价格低至**0.66美元/小时**或**199美元/月**（用于训练），为开发者提供了负担得起的GPU云解决方案。
> 来源：[Packet.ai Blackwell定价页面](https://packet.ai/blackwell)

---

### 9. 分布式微调系统Zagora
> Zagora团队正在构建一个分布式微调系统，旨在通过标准互联网连接训练70B+的模型（如Qwen 2.5、Mistral），将分散的消费级GPU集群整合成一台巨型超级计算机。
> 来源：文章内容

---

### 10. PyTorch集成Flash Attention 3内核
> 用户可通过在PyTorch中调用 `activate_flash_attention_impl(“FA3”)`，安全地将默认的Flash Attention 2内核替换为FA3，这通过简单的字典交换实现，有望提升注意力计算效率。
> 来源：[PyTorch中FA3的相关代码](https://github.com/pytorch/pytorch/blob/580a6e2c814db93aa8df0a80e3e85c330621b9cb/torch/nn/attention/_fa3.py#L54)