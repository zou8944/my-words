## AINews - 2026-01-23

> [原文链接](https://news.smol.ai/issues/26-01-21-openevidence/)

## 📰 十大AI新闻要点

### 1. [OpenEvidence 融资120亿美元，估值达120倍PS](https://www.cnbc.com/2026/01/21/openevidence-chatgpt-for-doctors-doubles-valuation-to-12-billion.html)
> AI医疗公司OpenEvidence完成新一轮融资，估值达到120亿美元，是去年估值的12倍。公司CEO称其产品已被美国40%的医生使用，去年年收入超过1亿美元，这意味着其估值达到了惊人的120倍市销率。

---

### 2. [Anthropic发布Claude“宪法”并采用CC0许可](https://twitter.com/AnthropicAI/status/2014005798691877083)
> Anthropic公开发布了用于直接训练Claude模型的“宪法”，详细描述了期望的行为和价值观。该宪法以CC0 1.0许可发布，鼓励社区重用和改编，Anthropic将其定位为一个由内外部专家共同塑造的“活文件”。

---

### 3. [Podium宣布AI智能体年经常性收入超1亿美元](https://twitter.com/ericwilliamrea/status/2013980401635582277)
> 商业软件公司Podium宣布其AI智能体业务年经常性收入（ARR）已超过1亿美元，部署了超过1万个名为“Jerry”的AI智能体。该公司将智能体定位为“AI员工”，用于解决中小企业的人力资源限制问题，如处理非工作时间线索和错过的电话。

---

### 4. [Runway发布Gen-4.5图像转视频模型](https://twitter.com/runwayml/status/2014090404769976744)
> Runway发布了新一代图像转视频模型Gen-4.5，重点强调其在叙事一致性、相机控制和故事连贯性方面的提升。早期使用者认为“故事构建”能力是评估视频模型的最佳方法。

---

### 5. [Cognition推出Devin Review代码审查工具](https://twitter.com/cognition/status/2014079905755955592)
> AI编程公司Cognition推出了Devin Review，这是一个新的PR阅读界面，旨在通过重新按重要性排序差异、识别重复/复制代码、添加聊天层以及与GitHub评论集成来减少代码审查中的“马虎”。用户可以通过替换URL或使用`npx` CLI来访问。

---

### 6. [Google与可汗学院合作推出Gemini写作教练](https://twitter.com/Google/status/2014082428957045007)
> Google宣布与可汗学院建立合作伙伴关系，首先推出“写作教练”功能。该工具旨在指导学生进行草稿撰写和修改，而不是直接生成最终答案，标志着AI在教育领域向引导式辅助的转变。

---

### 7. [Runpod年经常性收入达到1.2亿美元](https://techcrunch.com/2026/01/16/ai-cloud-startup-runpod-hits-120m-in-arr-and-it-started-with-a-reddit-post/)
> AI云基础设施初创公司Runpod在成立四年后，年经常性收入（ARR）达到1.2亿美元。该公司最初从一个Reddit帖子起步，其快速增长验证了“面向开发者的GPU云”是一个持久的市场利基。

---

### 8. [Lightning AI与Voltage Park合并](https://lightning.ai/blog/lightning-ai-voltage-park-merger-ai-cloud)
> Lightning AI（由William Falcon领导）与GPU云提供商Voltage Park（由Ozan Kaya领导）宣布合并。此举被视为在快速整合的“托管GPU基础设施”领域，与Runpod等公司展开竞争的重要一步。

---

### 9. [xAI联合创始人Greg Yang因健康问题转为顾问](https://xcancel.com/TheGregYang/status/2013652609455006006)
> xAI联合创始人Greg Yang宣布，因被诊断出莱姆病并出现慢性疲劳和免疫系统问题，他将转为公司的顾问角色，以专注于个人健康恢复。这一消息引发了AI社区的广泛关注和支持。

---

### 10. [Video Arena视频模型对战平台上线](https://twitter.com/arena/status/2014035528979747135)
> 视频生成模型评估平台Video Arena现已上线网页版，允许用户在约15个前沿视频模型之间进行头对头生成比较，并通过社区投票驱动排行榜。不过，平台目前限制每24小时只能生成3次。

---

## 🛠️ 十大工具产品要点

### 1. [AirLLM：极低VRAM推理引擎](https://twitter.com/LiorOnAI/status/2014005554948047122)
> AirLLM的核心创新是顺序层加载（加载→计算→释放）技术，可选压缩，提供类似Hugging Face的API，支持CPU/GPU和Linux/macOS。开发者声称其可以在极低的VRAM（如8GB）上运行超大规模模型（如405B参数），但需要注意吞吐量和延迟方面的工程限制。

---

### 2. [Prefect Horizon：企业级智能体“上下文层”平台](https://twitter.com/jlowin/status/2014023606380957754)
> Prefect推出Horizon平台，定位为连接智能体与企业工具/数据的“上下文层”接口。它解决了MCP协议在组织级部署、治理方面的不足，提供托管部署、注册表/目录、带RBAC和审计日志的网关，以及面向业务用户的“智能体界面”。

---

### 3. [LangChain Deep Agents与Agent Builder GA](https://twitter.com/LangChain/status/2014034320256880768)
> LangChain发布了Deep Agents框架和Agent Builder的正式版（GA）。Deep Agents采用“智能体即文件夹”的理念，强调可移植性和快速部署。Agent Builder则提供了一个模板库，与Tavily、PagerDuty等合作伙伴集成，旨在减少从提示词到可运行智能体的摩擦。

---

### 4. [CopilotKit构建全栈Deep Agent应用教程](https://twitter.com/CopilotKit/status/2013997128683856159)
> CopilotKit发布了一个教程，演示如何构建一个全栈的Deep Agent应用，流程包括简历摄取→技能提取→集成网络搜索的子智能体→流式UI。该教程旨在解决智能体开发中“缺失的UI/应用层”问题。

---

### 5. [Agent Cognitive Compressor (ACC)：压缩智能体状态](https://twitter.com/dair_ai/status/2014000799245107339)
> ACC（Agent Cognitive Compressor）提出了一种新的智能体记忆管理方法，认为“更多上下文 ≠ 更好的智能体”。它通过模式约束的提交来维护一个有界的“压缩认知状态”，声称可以在长程任务中降低漂移和幻觉。

---

### 6. [APEX-Agents：专业服务长程任务基准](https://twitter.com/BrendanFoody/status/2014028956752568356)
> APEX-Agents是一个新的基准测试，用于评估智能体在Google Workspace环境中执行长程“专业服务”任务的能力。早期Pass@1分数普遍较低（如Gemini 3 Flash High为24.0%），凸显了当前“智能体自主性”仍然脆弱。

---

### 7. [prinzbench：法律研究与搜索私有基准](https://twitter.com/deredleritt3r/status/2013979845378580684)
> prinzbench引入了一个用于法律研究和搜索的私有基准（33个问题，手动评分，运行3次）。结果显示，搜索是主要的失败模式，GPT-5.2 Thinking的准确率勉强超过50%，而Claude Sonnet/Opus 4.5在搜索任务上得分为0/24。

---

### 8. [GitHub Copilot CLI新增交互式提问工具](https://twitter.com/_Evan_Boyle/status/2014012076881064173)
> GitHub Copilot CLI增加了一个`askUserQuestionTool`工具，允许AI在遇到模糊指令（例如混乱的代码变基）时向用户提出澄清性问题。这标志着CLI智能体从纯自动补全向交互式工具使用的演变。

---

### 9. [Coderrr：开源Claude Code替代品](https://github.com/Akash-nath29/Coderrr)
> 开发者Akash构建了Coderrr，一个免费开源的Claude Code替代品，旨在提供一种新颖的代码生成方法。该项目正在GitHub上寻求反馈和贡献。

---

### 10. [Inforno：支持多模型并排聊天的开源桌面应用](https://github.com/alexkh/inforno)
> Inforno是一个开源桌面应用程序，利用OpenRouter和Ollama，允许用户与多个LLM进行并排聊天，并将聊天历史保存为.rno文件。该应用内置俄语支持，提供了一个集中管理多模型对话的界面。