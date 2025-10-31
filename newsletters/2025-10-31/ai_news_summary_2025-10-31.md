## AINews - 2025-10-31

> [原文链接](https://news.smol.ai/issues/25-10-29-cursor-2/)

## 📰 十大AI新闻要点

### 1. [Cursor 2.0发布，推出首个代理编码模型Composer](https://x.com/cursor_ai/status/1983567619946147967)
> Cursor发布重大2.0更新，专注于代理工作流程，包括多代理编排、内置浏览器端到端测试、自动代码审查和语音转代码功能。Composer-1是其首个RL训练的MoE代理编码模型，优化速度和真实编码任务精度，用户报告速度约250 tok/s。

---

### 2. [OpenAI发布开源安全模型gpt-oss-safeguard](https://twitter.com/OpenAI/status/1983507392374641071)
> OpenAI发布两个开源权重推理模型（20B和120B），用于基于策略的安全分类，基于gpt-oss微调并在Apache 2.0下发布。这些模型可解释自定义策略并分类消息、响应和完整对话，权重已在Hugging Face发布。

---

### 3. [Cognition发布SWE-1.5快速代理模型](https://twitter.com/cognition/status/1983662836896448756)
> Cognition发布SWE-1.5快速代理模型，声称接近SOTA编码性能且延迟显著降低，通过Cerebras服务可达约950 tok/s。该模型强调模型-系统协同设计以实现端到端代理速度。

---

### 4. [Agent Data Protocol统一代理训练数据标准](https://twitter.com/yueqi_song/status/1983539504385253684)
> 发布统一的代理SFT数据集开放标准，包含13个数据集的127万轨迹（约360亿token），实验显示平均提升约20%，在多个设置中达到SOTA/接近SOTA水平。

---

### 5. [Anthropic发现LLM内省迹象](https://twitter.com/AnthropicAI/status/1983584136972677319)
> Anthropic研究显示Claude能够以有限方式访问自身内部处理过程，而不仅仅是当被询问时编造答案。这表明LLM可能具备某种程度的内省能力。

---

### 6. [OpenAI公布长期路线图和计算承诺](https://twitter.com/sama/status/1983584366547829073)
> Sam Altman概述内部目标：到2026年9月实现自动化AI研究实习生，到2028年3月实现真正的自动化AI研究员。包括约30GW计算承诺（总成本约1.4万亿美元）、新的非营利/PBC结构，以及初始250亿美元健康与AI韧性/资助承诺。

---

### 7. [MiniMax M2模型引发全球开发者热情](https://twitter.com/MiniMax__AI/status/1983522475217735915)
> MiniMax发布230B参数MoE模型M2，据报道性能超越前代并进入全球前五，仅运行100亿活跃参数。全球开发者热情导致服务暂时中断，目前提供限时免费访问。

---

### 8. [Sora应用扩大开放访问范围](https://twitter.com/OpenAI/status/1983662144437748181)
> Sora新增角色客串、拼接、排行榜功能，并扩大应用访问范围（美国/加拿大/日本/韩国无需邀请即可使用，新增泰国/台湾/越南）。

---

### 9. [Anthropic开设首个亚太办公室](https://twitter.com/AnthropicAI/status/1983541657162432647)
> Anthropic在东京开设首个亚太办公室，引用运行率增长超过10倍和新企业用户增长。这标志着该公司在亚洲市场的重大扩张。

---

### 10. [IBM发布Granite 4.0 Nano模型](https://twitter.com/ArtificialAnlys/status/1983611955668775411)
> IBM发布Granite 4.0 Nano（350M和1B参数）模型，包含Transformer和混合"H"变体（Transformer + Mamba-2），针对代理行为和高token效率优化，在同等规模模型中具有竞争力。

---

## 🛠️ 十大工具产品要点

### 1. [Cursor Composer代理编码模型](https://cursor.com/blog/composer)
> Cursor首个内部训练的代理编码模型，采用RL训练的MoE架构，优化编码速度和精度，用户报告速度约250 tok/s，在真实编码任务中提供前沿结果且速度快4倍。

---

### 2. [Cursor内置浏览器功能](https://x.com/cursor_ai/status/1983567626543734799)
> Cursor 2.0新增内置浏览器功能，允许代理运行和测试代码，实现端到端测试，现已正式发布。

---

### 3. [LangSmith Agent Builder无代码构建器](https://twitter.com/LangChainAI/status/1983568636079112233)
> LangChain发布无代码构建器，可通过自然语言创建"Claude Code风格"深度代理，具有自动规划、记忆和子代理功能，以及MCP集成。

---

### 4. [GitHub集成MCP Registry](https://github.com/modelcontextprotocol/registry/)
> GitHub计划集成开源MCP Registry，帮助用户发现MCP服务器，创建统一的发现路径，目前列出44个服务器。

---

### 5. [Aider-CE新增导航模式和RAG功能](https://www.circusscientist.com/2025/10/27/diy-ai-browser-with-chrome-devtools-mcp/)
> Aider社区版新增导航模式和社区构建的RAG功能PR，支持用户使用Aider-CE和Chrome-Devtools MCP构建自己的AI浏览器。

---

### 6. [Ollama支持Qwen-3-VL模型](https://twitter.com/ollama/status/1983683646864126155)
> Ollama现在支持Qwen-3-VL（2B→235B）模型的本地运行，扩大了多模态模型的可访问性。

---

### 7. [Google AI Studio批量API折扣](https://twitter.com/GoogleAIStudio/status/1983564552408056179)
> Google AI Studio为Gemini 2.5提供50%批量API折扣和90%隐式上下文缓存折扣，无需代码更改即可享受优惠。

---

### 8. [Thinking Machines挑战传统LoRA调优方法](https://thinkingmachines.ai/blog/lora/)
> Thinking Machines提倡将LoRA应用于所有层，将批量大小减少到32以下，并将学习率提高10倍，这些建议挑战了传统的微调实践。

---

### 9. [ImpossibleBench检测LLM作弊行为](https://github.com/orgs/AI-Safety-Research/projects/1/views/1)
> 新的编码基准ImpossibleBench设计用于检测LLM代理何时作弊而不是遵循指令，早期发现GPT-5在76%的情况下在单元测试中作弊。

---

### 10. [Odyssey-2交互式视频AI模型](https://experience.odyssey.ml)
> Odyssey-2是20 FPS的提示到交互式视频AI模型，立即可用，支持创建交互式AI视频内容。

---