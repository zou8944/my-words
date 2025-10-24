## AINews - 2025-10-24

> [原文链接](https://news.smol.ai/issues/25-10-22-not-much/)

## 📰 十大AI新闻要点

### 1. [LangChain & LangGraph 1.0发布](https://twitter.com/hwchase17/status/1981030005229670438)
> LangChain和LangGraph 1.0进行了重大重写，专注于可靠、可控的智能体。新特性包括：新的`create_agent`模板、提供商无关的"标准内容块"、用于可控性和上下文工程的中间件，以及通过LangGraph运行时实现持久化的人机协同执行。

---

### 2. [PyTorch发布Monarch和TorchForge](https://twitter.com/PyTorch/status/1981020264474231030)
> Meta推出两个大规模智能体系统构建模块：Monarch（用于编排集群、调试和预训练的分布式编程框架）和TorchForge（具有高性能组件和示例的PyTorch原生强化学习库），为智能体工作负载提供从研究到生产的端到端路径。

---

### 3. [OpenAI ChatGPT Atlas浏览器集成](https://twitter.com/OpenAI/status/1981098271901962439)
> ChatGPT浏览器集成智能体可以在页面上执行操作，引入"Ask ChatGPT"（上下文页面问答）功能，并配备深度防御安全措施：无凭证操作模式、敏感网站的"监视模式"，以及对提示注入攻击的快速响应。

---

### 4. [Google量子计算突破](https://twitter.com/sundarpichai/status/1981013746698100811)
> Google使用Willow芯片上的"Quantum Echoes"测量报告了首个可验证的量子优势——比顶级超级计算机上的最佳经典算法快13,000倍，在基于NMR的分子建模方面具有潜在应用价值，已在Nature上发表并经过同行评审。

---

### 5. [DeepSeek v3.2发布](https://twitter.com/DeepLearningAI/status/1980846573681520824)
> DeepSeek v3.2（685B MoE）专注于长上下文成本/速度优化，关注"最相关的token"，相比v3.1提供2-3倍更快的长上下文推理和6-7倍更低的处理成本，MIT许可权重，API定价为每100万输入/缓存/输出token $0.28/$0.028/$0.42。

---

### 6. [vLLM推理基础设施改进](https://twitter.com/vllm_project/status/1981017184769061153)
> vLLM的OpenAI兼容端点现在可以直接返回token ID，防止字符串→token不匹配破坏强化学习稳定性，同时引入批量不变推理标志，显著简化服务堆栈的调试和可重现性。

---

### 7. [腾讯开源Hunyuan World 1.1](https://twitter.com/TencentHunyuan/status/1980930623536837013)
> 腾讯开源了Hunyuan World 1.1（WorldMirror），这是一个单通道前馈视频/多视角到3D重建模型，在单个GPU上几秒钟内输出点云、深度、法线、相机参数和3D高斯，具有灵活几何先验以保持一致性。

---

### 8. [AI2发布olmOCR 2](https://twitter.com/allen_ai/status/1981029159267659821)
> AI2发布Apache-2.0许可的olmOCR 2，包含新数据集、单元测试的合成训练，声称达到SOTA水平——每100万页成本约$178，提供模型+FP8和公开演示。

---

### 9. [IBM发布150万任务场景数据集](https://twitter.com/IBMResearch/status/1981066891062817274)
> IBM与华盛顿大学在Hugging Face上发布了150万个任务场景数据集，推动智能体评估和"完成任务"工作流程，同时斯坦福大学新开设CME295（Transformers & LLMs）课程。

---

### 10. [持续学习"记忆层"研究](https://twitter.com/giffmana/status/1980869216149619009)
> 研究人员提出具有输入无关KV记忆的层，仅在高TF-IDF槽上进行微调，为可扩展持续学习生成重要兴趣，后续讨论包括包含"接收"槽以允许"不使用记忆"选择，并注意内循环中随机内存访问的性能/吞吐量影响。

---

## 🛠️ 十大工具产品要点

### 1. [OpenRouter推出:exacto端点](https://openrouter.ai/announcements/provider-variance-introducing-exacto)
> OpenRouter推出:exacto端点以提高工具调用准确性，将请求路由到具有优越结构化输出性能的提供商，初始基准显示在qwen/qwen3-coder:exacto等模型上工具调用成功率显著提升。

---

### 2. [MCP生态系统主流化](https://twitter.com/code/status/1981076900471562579)
> Microsoft Learn MCP服务器使官方文档在Claude Code和VS Code等工具中可即时查询——无需认证，OpenAI兼容——加速基于基础的智能体工作流程，LangChain文档现在内置MCP。

---

### 3. [Cursor IDE安全漏洞](https://www.bleepingcomputer.com/news/security/cursor-windsurf-ides-riddled-with-94-plus-n-day-chromium-vulnerabilities/)
> Cursor和Windsurf IDE因过时的Chromium和V8引擎而存在漏洞，导致超过94个n-day安全问题，可能引发拒绝服务甚至远程代码执行，同时用户报告"apply"功能被禁用。

---

### 4. [Fenic集成Hugging Face数据集](https://github.com/typedef-ai/fenic)
> Fenic开源项目现在直接与Hugging Face数据集集成，允许用户直接从Hub水合版本上下文并安全地将其工具化用于智能体，支持数据快照、智能体上下文创建，并通过类似pandas的dataframe API暴露MCP工具。

---

### 5. [Awesome LLM Systems仓库发布](https://github.com/romitjain/awesome-llm-systems)
> 新仓库Awesome LLM Systems发布，包含精选论文、博客和资源，专注于大语言模型的系统方面，为对LLM部署和优化的工程挑战和解决方案感兴趣的人提供全面指南。

---

### 6. [Lovable推出Shopify集成](https://lovable.dev/merch)
> Lovable宣布Shopify集成，允许用户通过简单提示启动完整的在线商店，演示了通过启动自己的商品商店的流程，该功能对所有用户可用，附带30天Shopify试用。

---

### 7. [Next.js Evals开源评估](https://xcancel.com/rauchg/status/1981037270624076092)
> Guillermo Rauch宣布Next.js Evals，开源"考试"让任何LLM/智能体证明它可以正确使用Next.js和其他支持的框架构建，目前GPT-5-codex和Claude Sonnet 4.5等模型得分在40%左右。

---

### 8. [Amazon Vibe Code IDE发布](https://kiro.dev/blog/waitlist-is-over/)
> Amazon的Vibe Code IDE退出仅限邀请的测试版，为用户提供500积分开始使用，设计为"基于规范"，围绕功能和实现的规范工作，而不是仅基于提示。

---

### 9. [Unsloth与PyTorch量化合作](https://x.com/UnslothAI/status/1981021761782317368)
> Unsloth AI和PyTorch正在合作新的量化感知训练（QAT）计划，工程师们对其实现提出技术问题，特别是是否会保持视觉编码器不变。

---

### 10. [DSPy与ElevenLabs语音合成集成](https://github.com/Gielinor-Speaks/voiceover-mage)
> 成员开发了游戏NPC语音生成系统，利用DSPy解析维基内容，并与ElevenLabs集成进行语音合成，旨在通过自动化评判循环自动化语音策划，使用手动选择作为训练信号来提高生成语音质量。

---