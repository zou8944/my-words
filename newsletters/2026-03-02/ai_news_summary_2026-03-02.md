## AINews - 2026-03-02

> [原文链接](https://news.smol.ai/issues/2026-02-25-wtf-happened/)

## 📰 十大AI新闻要点

### 1. [Perplexity发布“Computer”：首个以编排为核心的多智能体产品](https://x.com/perplexity_ai/status/2026695550771540489)
> Perplexity推出名为“Computer”的端到端系统，旨在通过一个界面编排文件、工具、记忆和模型，以完成研究、设计、编码、部署和管理项目。其核心突破在于采用并行、异步的子智能体架构，由协调模型将任务分配给研究、编码等领域的专家模型，而非单一循环。这标志着向“系统级智能体用户体验”的迈进，将智能体工作视为分布式工作流。

---

### 2. [Karpathy宣称编程智能体自去年12月发生“质变”](https://x.com/karpathy/status/2026731645169185220)
> AI专家Andrej Karpathy提出，自2024年12月以来，编程智能体已跨越一个质的门槛，从脆弱的演示转变为能够持续、长视野地完成任务，具备连贯性和韧性。他举例说明，智能体在极少人工干预下，即可完成从SSH密钥配置到vLLM部署、模型下载、UI创建、系统服务配置及生成报告的完整本地部署流程。

---

### 3. [OpenAI发布GPT-5.3-Codex，社区评测反响热烈](https://x.com/snsf/status/2026513135075746239)
> OpenAI在API中发布了GPT-5.3-Codex模型。Cline等开发工具宣布支持，并声称其速度比GPT-5.2快约25%，完成任务所需token更少，且在SWE-Bench Pro等编程基准测试中表现强劲。社区评测迅速涌现，但需注意其方法论尚未完全清晰。

---

### 4. [Qwen3.5 Medium系列模型发布，开源生态工具链迅速跟进](https://x.com/Alibaba_Qwen/status/2026502059479179602)
> 阿里巴巴发布Qwen3.5 Medium系列模型（包括27B、35B-A3B、122B-A10B），声称在量化、长上下文等方面有显著提升。发布当天即获得vLLM、GGUF、LM Studio、Ollama、Jan等主流部署工具链的广泛支持，展示了开源模型生态的快速成熟。技术亮点包括宣称的“近无损”4位量化、支持超百万token的上下文长度，并开源了35B-A3B的基础模型。

---

### 5. [Anthropic收购Vercept以增强Claude的“计算机使用”能力](https://x.com/AnthropicAI/status/2026705792033026465)
> Anthropic宣布收购专注于“计算机使用”能力的初创公司Vercept，旨在提升Claude模型代表用户执行操作（尤其是非技术任务）的能力。Vercept创始人表示，其使命是从“告诉用户做什么”转向“为用户行动”。

---

### 6. [Anthropic被曝面临美国政府压力，要求放宽AI军事使用限制](https://www.reddit.com/r/OpenAI/comments/1re686c/exclusive_hegseth_gives_anthropic_until_friday_to/)
> 据Axios等媒体报道，美国国防部长向Anthropic发出最后通牒，要求其移除Claude AI模型中关于禁止用于国内监控和自主武器开发的安全护栏，否则可能动用《国防生产法》或将该公司列为供应链风险。此事引发了关于AI伦理、商业公司与政府关系的广泛讨论。

---

### 7. [Anthropic调整其“负责任扩展政策”，放弃单边训练限制承诺](https://www.reddit.com/r/ClaudeAI/comments/1rdwdld/time_anthropic_drops_flagship_safety_pledge/)
> 据TIME报道，Anthropic放弃了其“负责任扩展政策”中的一个关键承诺，即不再坚持“除非能确保足够安全措施，否则不训练AI系统”。公司首席科学家解释称，鉴于AI发展的快速步伐和竞争对手的行动，单边承诺已不切实际。这被视为在竞争压力下的战略调整。

---

### 8. [Karpathy剖析AI算力核心矛盾：片上SRAM与片外DRAM的协同难题](https://x.com/karpathy/status/2026452488434651264)
> Karpathy发表高参与度讨论，指出LLM工作流（特别是长上下文下的解码和紧密的智能体循环）的核心约束在于协调两种内存池：快速但微小的**片上SRAM**和庞大但缓慢的**片外DRAM**。他认为，如何以最佳吞吐量、延迟和成本来协调内存与计算，是当前“以HBM为主”（英伟达风格）和“以SRAM为主”（Cerebras风格）阵营共同面临的重大难题。

---

### 9. [xAI的Grok-4.20-Beta1登顶Arena搜索榜，文本榜表现亦佳](https://x.com/arena/status/2026566773496230383)
> 根据Arena排行榜数据，xAI的Grok-4.20-Beta1模型在搜索竞技场（Search Arena）中排名第一，在文本竞技场（Text Arena）中排名第四，与谷歌的Gemini 3.1 Pro得分相当。这显示了该模型在搜索和通用文本任务上的竞争力。

---

### 10. [AI可靠性研究指出：智能体失败常源于“可靠性”而非“能力”](https://x.com/omarsar0/status/2026471955319189861)
> 一项关于“智能体失败”的研究总结指出，智能体经常因**微小的、偏离路径的工具调用错误不断累积**而失败，一个错误会增加下一个错误发生的可能性，尤其是在长视野任务中。这强调了在模型能力飞速提升的同时，其可靠性（如一致性、鲁棒性）的进步相对有限，且不能简单地用单一“成功率”来衡量。

---

## 🛠️ 十大工具产品要点

### 1. [Perplexity Computer采用基于用量的计费与子智能体模型选择](https://x.com/perplexity_ai/status/2026695793537855526)
> Perplexity Computer首先面向Max订阅用户开放，采用基于使用量的定价模式。用户可以为不同的子智能体（如研究、编码）选择不同的模型，并设置支出上限。Max用户每月包含10,000点积分，并在发布初期获得限时奖励积分。

---

### 2. [GitHub Copilot CLI正式发布，新增 `/research` 深度研究功能](https://x.com/_Evan_Boyle/status/2026706464375796099)
> GitHub Copilot CLI结束测试，进入正式可用阶段。新增的`/research`命令可以利用GitHub代码搜索和基于MCP的动态抓取，对整个代码库进行深度研究，并可将研究报告导出为Gist分享。

---

### 3. [Claude Code迎来“一周年”，集成Slack插件与LangSmith追踪](https://x.com/_catwu/status/2026485966626763120)
> Claude Code作为成熟的编程智能体产品，近期集成了Slack插件，方便在协作环境中使用。同时，通过LangSmith工具链支持追踪，帮助开发者调试智能体在任务路由或“削弱”行为方面的问题。

---

### 4. [Qwen3.5系列模型获全方位本地部署支持，成智能体编码新宠](https://x.com/victormustar/status/2026624792602808707)
> 开发者实测表明，Qwen3.5-35B-A3B模型在本地运行（如使用llama.cpp）时，在智能体编码任务中表现出色，感觉明显更可靠（工具调用、稳定性）。由于其MoE架构（每token仅激活约30亿参数），它可以在32GB VRAM的消费级GPU上运行，成为Claude Code/Codex之外许多工作流的可行本地替代方案。

---

### 5. [Trace-Free+：通过优化工具描述文本提升智能体成功率](https://x.com/omarsar0/status/2026676835539628465)
> Intuit AI Research的研究提出，智能体的成功高度依赖于工具接口的文本描述。他们引入了一种课程学习方法，教导模型将工具描述重写为智能体更易使用的形式，且无需在推理时依赖执行轨迹。该方法在StableToolBench/RestBench上报告了性能提升，并在工具数量超过100个时仍保持鲁棒性。

---

### 6. [ActionEngine：将GUI智能体重构为图遍历，大幅降低LLM调用成本](https://x.com/dair_ai/status/2026678090815123594)
> ActionEngine将GUI自动化智能体重新定义为**图遍历**问题。通过离线探索生成状态机，运行时只需约1次LLM调用即可生成完整的执行程序，据称相比传统的逐步视觉循环方法，在成功率、成本和延迟方面都有显著改善。

---

### 7. [Liquid AI发布开源稀疏MoE模型LFM2-24B-A2B](https://www.reddit.com/r/LocalLLaMA/comments/1rdi26s/liquid_ai_releases_lfm224ba2b/)
> Liquid AI发布了LFM2-24B-A2B，这是一个稀疏混合专家模型，拥有240亿参数，每token激活20亿参数。它设计为可在32GB内存上运行，支持llama.cpp、vLLM和SGLang推理，并提供多种GGUF量化版本，专注于高效部署。

---

### 8. [Nous Research发布开源Hermes Agent，具备多级记忆与持久机器访问](https://github.com/nousresearch/hermes-agent)
> Nous Research发布了开源的Hermes Agent，这是一个功能强大的智能体，内置多级记忆系统，并具有持久的专用机器访问权限，可直接从命令行运行。早期用户可通过优惠码在Nous门户获取免费试用。

---

### 9. [Aider编码助手新增 `/ok` 命令，一键批准并执行AI生成的代码编辑](https://www.reddit.com/r/LocalLLaMA/comments/1rdi26s/liquid_ai_releases_lfm224ba2b/)
> 来源：文章内容
> 流行的编码助手Aider在其主分支中合并了新的`/ok`命令别名，允许开发者瞬间批准并执行AI生成的代码修改建议，极大简化了人机协作编程的工作流。

---

### 10. [LM Studio推出LM Link功能，通过Tailscale实现本地模型的远程安全访问](https://link.lmstudio.ai)
> LM Studio团队发布了LM Link功能的文档，该功能利用Tailscale技术，为用户提供无缝、端到端加密的远程访问，使其能够从任何地方安全地连接到家中或办公室的本地LLM服务器。