## AINews - 2026-01-16

> [原文链接](https://news.smol.ai/issues/26-01-14-not-much/)

## 📰 十大AI新闻要点

### 1. OpenAI发布GPT-5.2-Codex API，定位为最强长时任务编码模型
> OpenAI通过Responses API正式发布了GPT-5.2-Codex，将其定位为处理功能开发、重构和漏洞查找等长时运行任务的最强编码模型。官方明确指出这是迄今为止“最具网络能力”的模型，能够理解代码库中的安全漏洞。该模型已迅速被Cursor和GitHub Copilot集成。
> 来源：[OpenAIDevs推文](https://twitter.com/OpenAIDevs/status/2011499597169115219)

---

### 2. 团队利用GPT-5.2-Codex在Cursor中运行一周，生成300万行Rust代码构建浏览器
> 有报告称，一个团队使用Cursor集成的GPT-5.2-Codex模型，让其不间断地自主运行了一周，生成了超过300万行Rust代码，构建了一个包含HTML解析、CSS层叠布局、绘制和自定义JS虚拟机等模块的浏览器，并声称该浏览器对简单网站“基本可用”。这成为衡量“连续智能体运行时间”和自主代码生成实际前沿的参考点。
> 来源：[mntruell推文](https://twitter.com/mntruell/status/2011562190286045552)

---

### 3. OpenAI与Cerebras宣布建立战略计算合作伙伴关系
> OpenAI宣布与AI芯片公司Cerebras建立合作伙伴关系，旨在扩展AI计算规模。业界解读此举是为了应对与其他硬件厂商（如Groq）的合作竞争，并认为在ChatGPT式体验中，延迟和每秒处理令牌数正日益成为用户可见的产品差异化因素。
> 来源：[cerebras推文](https://twitter.com/cerebras/status/2011531740804964855)

---

### 4. 谷歌Gemini推出“个性化智能”功能，连接用户历史数据
> 谷歌宣布为Gemini推出个性化功能，通过连接用户的Gmail、照片、搜索和YouTube历史记录来提供个性化体验，并强调用户需选择加入且拥有隐私控制权。该功能由谷歌及其Gemini领导层账号高调宣布。
> 来源：[Google推文](https://twitter.com/Google/status/2011473056921706852)

---

### 5. Meta Llama项目负责人Ahmad Al-Dahle加入Airbnb担任CTO
> Meta Llama项目的负责人Ahmad Al-Dahle宣布将加入Airbnb担任首席技术官。他在声明中肯定了Meta开源Llama模型的战略（下载量超12亿，衍生模型超6万），并将Airbnb视为应用先进模型能力的产品前沿。多位行业领袖对此表示认可。
> 来源：[Ahmad_Al_Dahle推文](https://twitter.com/Ahmad_Al_Dahle/status/2011440460821320056)

---

### 6. 谷歌开源通用商务协议，旨在让AI智能体自主管理电商任务
> 谷歌开源了通用商务协议，该协议允许AI智能体自主执行产品发现、购物车管理和支付处理等电子商务任务。其关键集成包括用于多步骤工作流的Agent2Agent、用于安全支付的Agents Payment Protocol，以及与vLLM、Ollama等现有LLM栈集成的Model Context Protocol。
> 来源：文章内容（提及GitHub仓库：[Universal-Commerce-Protocol/ucp](https://github.com/Universal-Commerce-Protocol/ucp)）

---

### 7. 数学专用版Gemini模型证明了一个新的数学定理
> 据报道，一个“数学专用”版本的Gemini AI模型证明了一个新的数学定理，相关细节在一篇arXiv论文中阐述。该模型的架构和训练针对数学推理进行了优化，利用了符号计算和定理证明的先进技术，展示了AI在推动数学研究方面的潜力。
> 来源：文章内容（提及arXiv论文链接：[https://arxiv.org/abs/2601.07222](https://arxiv.org/abs/2601.07222)）

---

### 8. GPT-5.2 Pro在数十年未解的数学问题上取得进展
> 用户“Archivara”利用GPT-5.2 Pro模型，通过重新优化椭圆轨迹构造参数，将Moser蠕虫问题的通用覆盖面积上限降低至0.260069597，超越了201年创下的0.26007纪录。这一进展在法国国家信息与自动化研究所数学家的验证下，展示了AI在获得恰当工具和引导后解决复杂数学问题的潜力。
> 来源：文章内容

---

### 9. Thinking Machines Lab与OpenAI出现高层人事变动
> Thinking Machines Lab的Mira Murati宣布Barret Zoph已离职，Soumith Chintala成为新任CTO。随后不久，OpenAI宣布Barret Zoph、Luke Metz和Sam Schoenholz回归OpenAI。
> 来源：[miramurati推文](https://twitter.com/miramurati/status/2011577319295692801) 及 [fidjissimo推文](https://twitter.com/fidjissimo/status/2011592010881446116)

---

### 10. 中文模型ERNIE-5.0首次进入Text Arena排行榜前十
> 百度ERNIE-5.0-0110模型在LM Arena的Text Arena排行榜上位列第8（得分1460），在Arena Expert中位列第12，成为首个进入总榜前十的中文模型。该模型在数学和职业类别中表现优异。
> 来源：文章内容（提及排行榜链接：[https://lmarena.ai/leaderboard/text](https://lmarena.ai/leaderboard/text)）

---

## 🛠️ 十大工具产品要点

### 1. Cursor IDE立即集成GPT-5.2-Codex，支持长时任务
> Cursor在OpenAI发布后立即集成了GPT-5.2-Codex API，并将其定位为“用于长时运行任务的前沿模型”。用户报告了使用该模型进行大规模自主编码的案例。
> 来源：[cursor_ai推文](https://twitter.com/cursor_ai/status/2011500027945033904)

---

### 2. LangChain发布LangSmith智能体构建器，支持技能/MCP/子智能体
> LangChain发布了LangSmith Agent Builder，提出了“智能体即文件系统”的概念，内置记忆功能、环境智能体触发器，并支持技能、模型上下文协议和子智能体。
> 来源：[LangChain推文](https://twitter.com/LangChain/status/2011501888735494184)

---

### 3. GitHub Copilot (@code) 集成GPT-5.2-Codex并调整预览/正式版标签
> GitHub将GPT-5.2-Codex集成到GitHub Copilot中，并宣布正在改变预览版和正式版的标签方式，以减少企业采用的摩擦。
> 来源：[code推文](https://twitter.com/code/status/2011503658815668623)

---

### 4. Phil Schmid发布“Agent Skills”技能便携层
> Phil Schmid为`antigravity`项目发布了“Agent Skills”，提供了标准化的文件夹结构，旨在实现跨Gemini CLI、Claude Code和OpenCode风格生态系统的技能兼容性。
> 来源：[_philschmid推文](https://twitter.com/_philschmid/status/2011345054343053370)

---

### 5. CopilotKit添加中间件，将LangChain智能体转化为面向UI的应用
> CopilotKit添加了中间件，可以将LangChain的预构建智能体（包括“深度智能体”）转化为面向用户界面的应用程序。
> 来源：[CopilotKit推文](https://twitter.com/CopilotKit/status/2011453920321929237)

---

### 6. 开源混合图像模型GLM-Image发布，专注文本渲染和高保真细节
> Zai发布了开源的GLM-Image模型，这是一个结合了自回归和扩散的混合图像模型，专注于高保真细节和强大的文本渲染能力，并提供了丰富的图生图工具。
> 来源：文章内容（提及GitHub仓库：[zai-org/GLM-Image](https://github.com/zai-org/GLM-Image)）

---

### 7. 谷歌Veo 3.1视频模型升级，支持4K超高清和肖像模式
> 谷歌的Veo 3.1视频模型新增了原生肖像模式、用户照片生成视频功能，并在Gemini、YouTube和Google AI Studio中提供了先进的1080p/4K超高清升级能力。
> 来源：文章内容（提及推文链接：[https://x.com/tulseedoshi/status/2011174465720430612](https://x.com/tulseedoshi/status/2011174465720430612)）

---

### 8. 开源视频模型LTX-2可生成带音频的20秒4K视频片段
> LTX-2作为一个开源视频模型出现，能够生成带音频、时长最长20秒的4K视频片段，被创作者视为进行电影样本制作和实验的社区友好基线。
> 来源：文章内容（提及推文链接：[https://x.com/venturetwins/status/2010878914273697956](https://x.com/venturetwins/status/2010878914273697956)）

---

### 9. SprocketLab发布SlopCodeBench，评估智能体在大型编程任务中的表现
> SprocketLab发布了SlopCodeBench基准测试，显示智能体在拆分为检查点的大型编程任务上常常做出糟糕的早期设计选择，并且在简化后往往无法泛化。
> 来源：文章内容（提及GitHub仓库：[SprocketLab/slop-code-bench](https://github.com/SprocketLab/slop-code-bench)）

---

### 10. 小型AI计算机TiinyAI宣称可本地运行120B参数模型
> TiinyAI开发了一款紧凑型AI设备，宣称配备80GB RAM，功耗30W，能够本地运行1200亿参数模型，作为DGX Spark等大型系统在便携性和隐私优先场景下的替代方案。
> 来源：文章内容