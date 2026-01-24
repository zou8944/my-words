## AINews - 2026-01-24

> [原文链接](https://news.smol.ai/issues/26-01-21-openevidence/)

## 📰 十大AI新闻要点

### 1. [OpenEvidence完成120亿美元融资，估值一年内增长12倍](https://www.cnbc.com/2026/01/21/openevidence-chatgpt-for-doctors-doubles-valuation-to-12-billion.html)
> 医疗AI公司OpenEvidence完成新一轮融资，估值达到120亿美元，是去年估值的12倍。公司CEO称其产品已被美国40%的医生使用，去年年收入超过1亿美元，这意味着其估值达到了收入的120倍。

---

### 2. [Anthropic发布Claude“宪法”并采用CC0许可](https://twitter.com/AnthropicAI/status/2014005798691877083)
> Anthropic发布了用于直接训练Claude模型的“宪法”文件，详细描述了期望的模型行为和价值观。该文件被定位为一份“活文件”，并采用CC0 1.0许可发布，以鼓励社区重用和改编。

---

### 3. [Podium宣布其AI代理业务ARR超1亿美元，部署超1万个“AI员工”](https://twitter.com/ericwilliamrea/status/2013980401635582277)
> 客户沟通平台Podium宣布其AI代理业务年经常性收入（ARR）已超过1亿美元，在约21个月内从零增长至此。公司已部署超过1万个名为“Jerry”的AI代理，将其定位为解决中小企业人力限制的“AI操作员”。

---

### 4. [Runway发布Gen-4.5图像转视频模型，强调叙事连贯性](https://twitter.com/runwayml/status/2014090404769976744)
> Runway发布了新一代图像转视频模型Gen-4.5，重点提升了视频的连贯性和叙事能力。早期使用者认为“故事构建”能力是评估视频模型的最佳方法。

---

### 5. [Cognition推出Devin Review代码审查工具](https://twitter.com/cognition/status/2014079905755955592)
> AI编程公司Cognition推出了Devin Review工具，旨在优化代码审查体验。它可以通过替换GitHub PR的URL（`github` -> `devinreview`）或使用`npx` CLI来访问，功能包括按重要性重新排序差异、识别重复代码、添加聊天层等。

---

### 6. [GPU云服务商Runpod ARR达1.2亿美元，验证“开发者GPU云”市场](https://techcrunch.com/2026/01/16/ai-cloud-startup-runpod-hits-120m-in-arr-and-it-started-with-a-reddit-post/)
> AI云初创公司Runpod宣布其年经常性收入（ARR）已达到1.2亿美元。该公司四年前从一个Reddit帖子起步，其快速增长验证了“为开发者服务的GPU云”是一个持久且有利可图的市场。

---

### 7. [Google与可汗学院合作推出Gemini写作教练](https://twitter.com/Google/status/2014082428957045007)
> Google宣布与可汗学院建立合作伙伴关系，首先推出“写作教练”功能。该工具旨在指导学生进行写作草稿和修改，而不是直接生成最终答案，体现了AI在教育中向引导式辅助的转变。

---

### 8. [xAI联合创始人Greg Yang因健康问题转为顾问角色](https://xcancel.com/TheGregYang/status/2013652609455006006)
> xAI联合创始人Greg Yang宣布，因被诊断出莱姆病并受慢性疲劳和免疫问题困扰，他将从全职角色转为公司顾问，以专注于健康恢复。这一消息引发了AI社区的广泛关注和支持。

---

### 9. [Lightning AI与Voltage Park合并，加剧GPU基础设施竞争](https://lightning.ai/blog/lightning-ai-voltage-park-merger-ai-cloud)
> 深度学习平台Lightning AI与GPU云提供商Voltage Park宣布合并。由Lightning AI的William Falcon和Voltage Park的Ozan Kaya共同领导新实体。此举被视为对Runpod等竞争对手的直接回应，标志着“托管GPU基础设施”领域的整合加速。

---

### 10. [社区主导的AI模型评估平台LMArena文本对战投票数突破500万](https://cdn.discordapp.com/attachments/1343296395620126911/1463271605697511485/5M_votes_social_post_3.mp4)
> LMArena平台的“文本竞技场”功能累计社区投票数已超过500万次。工程师们认为，这种大规模的真实世界A/B测试正在日益影响人们对模型的认知，即使正式基准测试的差异很小。

---

## 🛠️ 十大工具产品要点

### 1. [AirLLM：实现极低VRAM需求的大模型推理](https://twitter.com/LiorOnAI/status/2014005554948047122)
> AirLLM提出了一种通过逐层顺序加载（加载->计算->释放）来实现大模型在极小VRAM上推理的方法，声称可以在4GB VRAM上运行700亿参数模型，甚至在8GB VRAM上运行4050亿参数的Llama 3.1模型。它提供了类似Hugging Face的API，支持CPU/GPU和Linux/macOS。

---

### 2. [Prefect Horizon：定位为AI代理的“上下文层”平台](https://twitter.com/jlowin/status/2014023606380957754)
> Prefect推出了Horizon平台，将其定位为连接AI代理与企业工具/数据的“上下文层”接口。它解决了MCP协议在组织级部署、治理方面的不足，提供托管部署、工具注册/目录、带RBAC和审计日志的网关，以及面向业务用户的“代理界面”。

---

### 3. [LangChain发布Agent Builder GA及合作伙伴模板库](https://twitter.com/LangChain/status/2014034320256880768)
> LangChain宣布其Agent Builder功能正式发布（GA），并推出了一个与Tavily、PagerDuty、Box等域合作伙伴共同构建的模板库。此举旨在减少从“提示词到代理”的构建摩擦，加速生产级AI代理的落地。

---

### 4. [APEX-Agents：评估长周期专业服务任务的代理基准](https://twitter.com/BrendanFoody/status/2014028956752568356)
> APEX-Agents是一个新的基准测试，用于评估AI代理在Google Workspace环境中执行长周期“专业服务”任务（如项目管理、数据分析）的能力。早期Pass@1得分普遍较低（顶尖模型约24%），凸显了当前“代理自主性”仍然脆弱。

---

### 5. [GitHub Copilot CLI新增交互式提问工具](https://twitter.com/_Evan_Boyle/status/2014012076881064173)
> GitHub Copilot CLI增加了一个`askUserQuestionTool`工具，允许AI在遇到模糊指令时（例如处理混乱的代码变基）主动向用户提问以澄清需求。这标志着CLI智能助手从纯自动补全向交互式工具使用的演进趋势。

---

### 6. [Coderrr：一个开源的Claude Code替代品](https://coderrr.aksn.lol/)
> 开发者Akash构建并开源了Coderrr，这是一个旨在模仿Claude Code功能的免费替代工具。项目正在GitHub上寻求反馈和贡献，为开发者提供了另一种代码生成与交互的选择。

---

### 7. [Inforno：支持多模型并排聊天的开源桌面应用](https://github.com/alexkh/inforno)
> Inforno是一款开源桌面应用程序，它利用OpenRouter和Ollama，允许用户与多个LLM进行并排聊天，并将聊天历史保存为.rno文件。该应用内置了对俄语的支持。

---

### 8. [Video Arena：在线视频模型对战与评估平台上线](https://twitter.com/arena/status/2014035528979747135)
> LMArena推出了网页版的Video Arena，允许用户在约15个前沿视频生成模型之间进行“头对头”生成比较，并通过社区投票驱动排行榜。目前该平台设有每24小时3次生成的限制，且仅支持对战模式。

---

### 9. [Agent Cognitive Compressor (ACC)：旨在解决长程代理记忆与漂移问题](https://twitter.com/dair_ai/status/2014000799245107339)
> ACC（代理认知压缩器）提出了一种新的代理记忆管理方法，批评了简单的转录回放和检索方法。它通过维护一个有界的、受模式约束的“压缩认知状态”来降低长程任务中的幻觉和漂移。

---

### 10. [MCP Inspector存在401错误重认证缺陷](https://github.com/modelcontextprotocol/inspector/issues/576#issuecomment-3766294454)
> 模型上下文协议（MCP）的官方检查工具MCP Inspector目前存在一个缺陷：当遇到401未授权错误时，它无法重新进行身份认证。这是由于SDK在重定向过程中未能持久化`resourceMetadata`所致。当前建议仅使用VS Code进行初始连接。