## AINews - 2026-03-03

> [原文链接](https://news.smol.ai/issues/2026-02-25-wtf-happened/)

## 📰 十大AI新闻要点

### 1. Perplexity发布“Computer”端到端AI代理系统
> Perplexity推出名为“Computer”的新产品，定位为一个端到端系统，能够通过在一个界面中编排文件、工具、记忆和模型，来“研究、设计、编码、部署和管理”项目。其核心突破在于采用并行、异步的子代理架构，由协调模型将任务分配给不同的专家模型（如研究、编码、媒体），而非单一的单体代理循环。这标志着向系统级代理用户体验的迈进。
> 来源：[Perplexity官方发布推文](https://x.com/perplexity_ai/status/2026695550771540489)

---

### 2. 编码代理能力发生“质变”，进入实用阶段
> Andrej Karpathy声称，自去年12月以来，编码代理已跨越了一个质变的门槛——从脆弱的演示转变为能够持续、长视野地完成任务，具备连贯性和韧性。他举例说明，现在可以委托代理完成从SSH密钥配置到vLLM部署、模型下载/基准测试、服务器端点设置、UI创建、systemd服务配置再到生成报告的完整本地部署流程，且只需极少的人工干预。
> 来源：[Andrej Karpathy推文](https://x.com/karpathy/status/2026731645169185220)

---

### 3. OpenAI发布GPT-5.3-Codex，社区关注其性能
> OpenAI在API中发布了GPT-5.3-Codex。Cline等工具宣布支持，并声称其速度比GPT-5.2快约25%，完成任务所需token更少，且在SWE-Bench Pro上表现强劲。社区对其早期基准测试结果反应热烈，但提醒在方法论明确前应谨慎对待。
> 来源：[snsf推文](https://x.com/snsf/status/2026513135075746239)

---

### 4. 阿里发布Qwen3.5 Medium系列模型，推动本地代理发展
> 阿里巴巴发布了Qwen3.5 Medium系列模型（包括35B-A3B、27B、122B-A10B），并迅速获得vLLM、GGUF、LM Studio、Ollama、Jan等工具的支持。技术亮点包括：声称在4位权重+KV缓存量化下近乎无损；支持超长上下文（如35B-A3B在32GB显存消费级GPU上支持超过100万token）；开源了35B-A3B-Base模型和FP8权重。有实践者认为Qwen3.5-35B-A3B使本地代理循环的可靠性显著提升，激活参数仅约30亿/令牌，标志着本地代理的可行转折点。
> 来源：[Alibaba_Qwen推文](https://x.com/Alibaba_Qwen/status/2026502059479179602)

---

### 5. Anthropic收购Vercept并调整安全政策，面临军事应用压力
> Anthropic收购了专注于“计算机使用”能力的公司Vercept，以增强Claude的代理行动能力。同时，Anthropic对其“负责任扩展政策”（RSP）进行了调整，从僵化的“达到阈值即停止训练”转向更频繁地发布透明度报告和更新威胁模型。此外，有报道称美国国防部向Anthropic发出最后通牒，要求其移除Claude的安全护栏以供军事用途（包括国内监控和自主武器），否则可能动用《国防生产法》或将其列为供应链风险。
> 来源：[AnthropicAI收购公告推文](https://x.com/AnthropicAI/status/2026705792033026465) 及 [Axios新闻报道](https://www.axios.com)（文章内容）

---

### 6. AI代理可靠性问题凸显，研究聚焦失败模式与工具优化
> 有研究指出，尽管模型能力快速进步，但代理的可靠性提升有限。代理失败往往源于“可靠性”问题而非“能力”不足，例如微小的偏离路径的工具调用错误会不断累积，尤其在长视野任务中。此外，研究强调工具描述的文本质量对代理成功至关重要，并提出通过课程学习让模型重写工具描述以提升性能的方法（Trace-Free+）。
> 来源：[omarsar0推文总结代理失败论文](https://x.com/omarsar0/status/2026471955319189861) 及 [omarsar0推文介绍Trace-Free+](https://x.com/omarsar0/status/2026676835539628465)

---

### 7. 计算与内存架构成为AI扩展的关键瓶颈
> Andrej Karpathy指出，AI工作流的核心约束在于协调两种不同的内存池：快速但微小的片上SRAM与庞大但缓慢的片外DRAM。最大的难题是如何为LLM工作流（预填充/解码/训练）组织内存和计算，以实现最佳的吞吐量、延迟和成本效益，尤其是在长上下文和紧密的代理循环下的解码任务，这对“HBM优先”（英伟达风格）和“SRAM优先”（Cerebras风格）的阵营都是挑战。
> 来源：[Andrej Karpathy推文](https://x.com/karpathy/status/2026452488434651264)

---

### 8. 扩散模型LLM作为提升推理速度的替代架构受关注
> Andrew Ng等人强调了Inception Labs的扩散LLM在推理速度上的令人印象深刻的表现。有讨论称扩散方法可以通过架构创新（而非芯片）实现约1000 token/秒的速度，可能改变推理速度的游戏规则。相关研究也在探索用于均匀扩散LLM的推理时缩放采样器。
> 来源：[Andrew Ng推文](https://x.com/AndrewYNg/status/2026478474681262576)

---

### 9. AI能源需求激增，成为基础设施与政策约束
> 有报告称，由于AI和数据中心需求给电网带来压力，美国政治领导层正在推动主要的AI/数据中心公司自行提供电力，以避免引起纳税人的反弹。这表明AI的扩展正日益成为基础设施和政策问题，与算法问题同等重要。
> 来源：[kimmonismus推文](https://x.com/kimmonismus/status/2026720759163298282)

---

### 10. xAI的Grok 4.20 Beta在竞技场排名中表现突出
> 根据Arena报告，Grok-4.20-Beta1在搜索竞技场（Search Arena）排名第一，在文本竞技场（Text Arena）排名第四，与Google的Gemini 3.1 Pro得分相当。这显示了模型在特定评估中的竞争力，但排名可能随采样策略和模型变体而变化。
> 来源：[arena推文](https://x.com/arena/status/2026566773496230383)

---

## 🛠️ 十大工具产品要点

### 1. Perplexity Computer：基于使用的多模型代理编排平台
> Perplexity Computer是一个集研究、设计、编码、部署和管理于一体的端到端系统。采用基于使用量的定价，允许用户为子代理选择不同模型，并设有消费上限。首先面向Max订阅用户开放，随后将面向Pro/企业用户。其架构核心是并行异步的子代理与协调器模型。
> 来源：[Perplexity定价详情推文](https://x.com/perplexity_ai/status/2026695793537855526)

---

### 2. GitHub Copilot CLI正式发布，新增 `/research` 深度研究功能
> GitHub Copilot CLI已达到正式发布（GA）阶段。新增的`/research`命令可利用GitHub代码搜索和基于MCP的动态获取功能，进行全仓库范围的深度研究，并可将报告导出到Gist进行分享。终端中的Copilot CLI还能实时更新标题。
> 来源：[Evan Boyle功能介绍推文](https://x.com/_Evan_Boyle/status/2026458533320077689)

---

### 3. Claude Code生态系统扩展，集成Slack与可观测性工具
> Claude Code迎来“一周年”，被定位为基础性编码代理产品。其实用生态扩展包括：推出了Slack插件集成；以及通过LangSmith追踪功能来调试Claude Code的“削弱”/路由问题，提升可观测性。
> 来源：[catwu推文介绍Slack插件](https://x.com/_catwu/status/2026485966626763120)

---

### 4. Qwen3.5系列获广泛本地推理工具支持
> Qwen3.5 Medium系列模型在发布当天即获得了vLLM、GGUF、LM Studio、Ollama和Jan等主流本地部署和推理工具的支持，展示了当前开源模型部署生态的极高速度。
> 来源：[Alibaba_Qwen感谢vLLM支持推文](https://x.com/Alibaba_Qwen/status/2026496673179181292)

---

### 5. Liquid AI发布稀疏MoE模型LFM2-24B-A2B
> Liquid AI发布了LFM2-24B-A2B，这是一个稀疏混合专家模型，拥有240亿参数，每令牌激活20亿参数。设计可在32GB内存上运行，支持通过llama.cpp、vLLM和SGLang进行推理，并提供多种GGUF量化版本。
> 来源：文章内容（Reddit讨论）

---

### 6. ActionEngine：将GUI代理重构为图遍历，大幅提升效率
> ActionEngine将GUI代理重新定义为图遍历问题，通过离线探索生成状态机；在运行时生成完整程序，仅需约1次LLM调用。据称相比逐步视觉循环的方法，在成功率、成本和延迟方面有巨大改进。
> 来源：[dair_ai推文](https://x.com/dair_ai/status/2026678090815123594)

---

### 7. Nous Research发布开源Hermes Agent，具备系统级访问能力
> Nous Research发布了开源Hermes Agent仓库。这是一个强大的工具，内置多级记忆系统和持久的专用机器访问权限，可直接从CLI运行，允许AI控制浏览器并自主管理子代理。
> 来源：[Hermes Agent GitHub仓库](https://github.com/nousresearch/hermes-agent)

---

### 8. Aider编码助手新增 `/ok` 快捷批准命令
> Aider编码助手在其主分支中合并了新的`/ok`别名，允许开发者一键批准并执行AI生成的代码编辑。这进一步优化了开发者的AI辅助工作流程。
> 来源：文章内容（Discord总结）

---

### 9. LM Studio推出LM Link功能，实现本地模型的远程安全访问
> LM Studio团队发布了LM Link文档，该功能利用Tailscale为用户提供无缝、端到端加密的远程访问，使其能够从任何地方安全地查询本地LLM服务器。
> 来源：[LM Link文档](https://link.lmstudio.ai)

---

### 10. 开发者分享高效模型路由组合：Kimi用于规划，Mimo用于执行
> 开发者发现一种高效的模型路由堆栈：使用强大的moonshotai/kimi-k2.5进行高级架构规划，然后将实际的文件编辑工作交给超快、超便宜的Xiaomi/mimo-v2-flash模型执行，以实现成本与性能的平衡。
> 来源：文章内容（Discord总结）