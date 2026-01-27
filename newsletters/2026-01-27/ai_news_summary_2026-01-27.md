## AINews - 2026-01-27

> [原文链接](https://news.smol.ai/issues/26-01-21-openevidence/)

## 📰 十大AI新闻要点

### 1. [OpenEvidence完成120亿美元融资，估值一年内增长12倍](https://www.cnbc.com/2026/01/21/openevidence-chatgpt-for-doctors-doubles-valuation-to-12-billion.html)
> 医疗AI公司OpenEvidence完成新一轮融资，估值达到120亿美元，是去年估值的12倍。公司CEO称其产品已被美国40%的医生使用，去年年收入超过1亿美元，这意味着其估值达到了收入的120倍。

---

### 2. [Anthropic发布Claude“宪法”并采用CC0许可](https://twitter.com/AnthropicAI/status/2014005798691877083)
> Anthropic发布了用于直接训练Claude模型的“宪法”，详细描述了期望的行为和价值观。该宪法被定位为一份“活文件”，并采用CC0 1.0许可发布，以鼓励社区重用和改编，旨在促进AI对齐的透明度和协作。

---

### 3. [Podium宣布AI代理业务年经常性收入超1亿美元](https://twitter.com/ericwilliamrea/status/2013980401635582277)
> 商业软件公司Podium宣布其AI代理业务（代号“Jerry”）的年经常性收入（ARR）已超过1亿美元，部署了超过1万个代理。其商业模式是将AI代理定位为“AI员工”，为中小企业提供端到端的自动化运营服务，以解决人力短缺问题。

---

### 4. [Runway发布Gen-4.5图像转视频模型，强调叙事连贯性](https://twitter.com/runwayml/status/2014090404769976744)
> Runway发布了新一代图像转视频模型Gen-4.5，重点提升了视频的叙事连贯性和镜头控制能力。早期用户反馈认为，评估视频模型的最佳方法是看其“故事构建”能力，而不仅仅是单帧质量。

---

### 5. [Cognition推出Devin Review代码审查工具](https://twitter.com/cognition/status/2014079905755955592)
> AI编程公司Cognition推出了Devin Review，这是一个新的PR代码审查界面。它可以通过替换GitHub URL或使用CLI工具访问，旨在通过重新排序重要变更、识别重复代码、添加聊天层等功能来减少“代码审查噪音”。

---

### 6. [谷歌与可汗学院合作推出Gemini写作教练](https://twitter.com/Google/status/2014082428957045007)
> 谷歌宣布与可汗学院建立合作伙伴关系，推出基于Gemini的“写作教练”。该工具旨在指导学生完成写作的起草和修改过程，而不是直接生成最终答案，标志着AI在教育领域向引导式辅导的转变。

---

### 7. [Runpod年经常性收入达1.2亿美元，验证GPU云服务市场](https://techcrunch.com/2026/01/16/ai-cloud-startup-runpod-hits-120m-in-arr-and-it-started-with-a-reddit-post/)
> AI云基础设施初创公司Runpod宣布其年经常性收入达到1.2亿美元。该公司四年前从一个Reddit帖子起步，其快速增长验证了面向开发者的“GPU云”是一个持久且规模化的市场利基。

---

### 8. [xAI联合创始人Greg Yang因健康问题转为顾问角色](https://xcancel.com/TheGregYang/status/2013652609455006006)
> xAI联合创始人Greg Yang宣布，因被诊断出莱姆病并受慢性疲劳等症状困扰，他将从全职角色转为公司顾问，以专注于健康恢复。这一消息引发了AI社区对其健康的广泛关注和支持。

---

### 9. [Lightning AI与Voltage Park合并，整合AI云与基础设施](https://lightning.ai/blog/lightning-ai-voltage-park-merger-ai-cloud)
> AI开发平台Lightning AI与GPU云提供商Voltage Park宣布合并。合并后的实体将由Lightning AI的CEO William Falcon和Voltage Park的前CEO Ozan Kaya领导，旨在提供从开发到部署的一体化AI云解决方案，被视为Runpod的潜在竞争对手。

---

### 10. [社区主导的LMArena文本竞技场投票数突破500万](https://cdn.discordapp.com/attachments/1343296395620126911/1463271605697511485/5M_votes_social_post_3.mp4)
> 开源评估平台LMArena宣布，其文本竞技场（Text Arena）的社区投票总数已超过500万次。这标志着大规模、实时的A/B测试正在成为影响模型评价和社区认知的重要力量，补充了传统基准测试。

---

## 🛠️ 十大工具产品要点

### 1. [AirLLM：通过分层流式加载实现极低VRAM推理](https://twitter.com/LiorOnAI/status/2014005554948047122)
> AirLLM提出了一种顺序加载模型层的推理方法（加载→计算→释放），可选压缩，提供类似Hugging Face的API。它声称可以在极低的VRAM（如8GB）上运行超大规模模型（如405B参数），但需要权衡吞吐量和延迟。

---

### 2. [Prefect Horizon：定位为AI代理的“上下文层”平台](https://twitter.com/jlowin/status/2014023606380957754)
> Prefect推出Horizon平台，旨在解决企业部署和管理MCP（模型上下文协议）服务器的挑战。它提供托管部署、工具注册/目录、带RBAC和审计日志的网关，以及面向业务用户的“代理化界面”，将MCP从协议提升为企业级平台。

---

### 3. [LangChain发布Agent Builder GA及合作伙伴模板库](https://twitter.com/LangChain/status/2014034320256880768)
> LangChain宣布其Agent Builder功能正式发布（GA），并推出了一个与Tavily、PagerDuty、Box等域合作伙伴共同构建的模板库。此举旨在降低从提示词到可部署代理的构建门槛，加速代理应用的开发。

---

### 4. [Agent Cognitive Compressor：提出压缩认知状态以提升长程可靠性](https://twitter.com/dair_ai/status/2014000799245107339)
> 针对长程任务中代理的幻觉和漂移问题，Agent Cognitive Compressor提出维护一个有界的“压缩认知状态”，并通过模式约束提交来更新。它批评了简单的转录回放和检索方法，声称能显著降低长期运行中的错误。

---

### 5. [APEX-Agents：评估Google Workspace中的长程专业服务任务](https://twitter.com/BrendanFoody/status/2014028956752568356)
> APEX-Agents是一个新的基准测试，专注于评估AI代理在Google Workspace环境中执行“专业服务”类长程任务的能力。早期结果显示，即使顶级模型（如Gemini 3 Flash High）的首次通过率也仅约24%，凸显了当前代理自主性的脆弱性。

---

### 6. [GitHub Copilot CLI新增交互式提问工具](https://twitter.com/_Evan_Boyle/status/2014012076881064173)
> GitHub Copilot CLI引入了一个名为`askUserQuestionTool`的新工具，允许代理在遇到模糊指令时（例如处理混乱的代码变基）向用户提出澄清性问题。这标志着CLI代理从纯自动补全向交互式、工具使用型助手演进。

---

### 7. [Coderrr：开源的Claude Code替代品](https://coderrr.aksn.lol/)
> 开发者Akash构建并开源了Coderrr，一个旨在替代Claude Code的代码生成工具。项目在GitHub上公开，正在寻求社区的反馈和贡献，为开发者提供了一个新的、可定制的AI编码助手选择。

---

### 8. [Inforno：基于OpenRouter和Ollama的开源桌面聊天应用](https://github.com/alexkh/inforno)
> Inforno是一款开源桌面应用程序，允许用户通过OpenRouter API和本地Ollama同时与多个LLM进行侧边栏聊天，并将聊天历史保存为.rno文件。它内置了俄语支持，提供了灵活的多模型对话界面。

---

### 9. [Video Arena上线：社区投票驱动的视频模型竞技场](https://twitter.com/arena/status/2014035528979747135)
> LMArena的视频竞技场（Video Arena）全面上线，允许用户在约15个前沿视频生成模型之间进行头对头的生成比较，并通过社区投票驱动排行榜。目前采用“对战模式”并限制每日生成次数，以收集高质量的偏好数据。

---

### 10. [Mixedbread.ai展示ColBERT风格检索的规模化优势](https://twitter.com/mixedbreadai/status/2014062123358548017)
> Mixedbread.ai声称，其开源的1700万参数ColBERT模型在LongEmbed基准上击败了80亿参数的嵌入模型。他们已在生产环境中为超过10亿份文档提供检索服务，p50延迟低于50毫秒，证明了细粒度多向量检索系统在大规模应用中的可行性和效率。