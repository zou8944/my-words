## AINews - 2026-05-01

> [原文链接](https://news.smol.ai/issues/26-04-29-not-much/)

## 📰 十大AI新闻要点

### 1. [OpenAI将Codex从编码工具转变为通用工作平台](https://x.com/OpenAI/status/2049583167406064115)
> OpenAI正在将Codex扩展为通用工作平台，支持研究合成、电子表格和决策跟踪等知识工作。同时推出Codex专属席位（至6月底免费），并新增Supabase集成和Figma插件（可将实施计划转为FigJam看板）。这标志着AI编码工具向通用工作自动化平台的战略转型。

---

### 2. [Cursor发布SDK，从IDE产品转向可编程代理基础设施](https://x.com/cursor_ai/status/2049499866217185492)
> Cursor推出SDK，将其运行时、框架和模型开放给CI/CD、自动化及嵌入式代理使用。这标志着Cursor从基于座位的IDE产品转向可编程代理基础设施，与Codex应用服务器和VS Code框架工作一起，推动行业向“无头代理运行时+可编程框架+使用量计费”模式收敛。

---

### 3. [Mistral Medium 3.5发布：128B密集模型引发激烈讨论](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)
> Mistral发布Medium 3.5，为128B密集参数模型，支持256K上下文窗口、可配置推理深度和多模态输入。评论两极分化：有人批评其128K上下文和定价策略，也有人认为这是Mistral在“企业可靠性和指令遵循”上的战略押注。模型采用修改版MIT许可，商用需付费。

---

### 4. [IBM发布Granite 4.1系列：开源Apache 2.0模型](https://x.com/ArtificialAnlys/status/2049505499377193156)
> IBM发布Granite 4.1系列，包括30B、8B和3B三个开源Apache 2.0非推理模型。亮点：Granite 4.1 8B在AA智能指数上仅用4M输出token（Qwen3.5 9B需78M），AA开放指数得分61。虽智能水平不及领先模型，但瞄准企业/边缘部署中对成本和透明度的需求。

---

### 5. [Agent框架工程成为独立优化层：Terminal-Bench 2提升至77.0%](https://x.com/omarsar0/status/2049492169887748365)
> 研究表明，模型质量本身不足以决定生产性能，框架优化成为关键。Agentic Harness Engineering通过可回滚组件、压缩执行证据和可证伪预测，在10次迭代中将Terminal-Bench 2 pass@1从69.7%提升至77.0%，超越人类设计的Codex-CLI基线（71.9%），并在SWE-bench Verified上减少12% token使用。

---

### 6. [Qwen发布FlashQLA：高性能线性注意力内核](https://github.com/QwenLM/FlashQLA)
> 阿里巴巴发布FlashQLA，基于TileLang的高性能线性注意力内核，报告2-3倍前向和2倍反向加速，特别适用于小模型、长上下文和tensor-parallel场景。设计围绕门控驱动的自动intra-card CP、代数重构和融合warp专用内核，定位为“个人设备上的代理AI”解决方案。

---

### 7. [vLLM与Blackwell协同设计：DeepSeek V3.2达230 tok/s](https://x.com/vllm_project/status/2049503979898274163)
> vLLM在Artificial Analysis上实现DeepSeek V3.2输出速度第一（230 tok/s，TTFT 0.96s），并在DigitalOcean的NVIDIA HGX B300上优化Qwen 3.5 397B。优化包括NVFP4量化、EAGLE3+MTP推测解码和per-model内核融合，是硬件/软件/模型协同设计的典型案例。

---

### 8. [Talkie：仅用1931年前数据训练的13B语言模型](https://talkie-lm.com/introducing-talkie)
> 由Nick Levine、David Duvenaud和Alec Radford开发的Talkie，使用260B token的1931年前文本训练（书籍、报纸、科学期刊），旨在研究LLM如何在没有现代数据的情况下泛化知识。令人惊讶的是，该模型能通过上下文示例生成Python代码（利用19世纪数学），并展示了早期语言和算术能力。模型采用Apache 2.0许可。

---

### 9. [Anthropic发布Blender MCP连接器](https://www.blender.org/press/anthropic-joins-the-blender-development-fund-as-corporate-patron/)
> Anthropic发布Blender MCP连接器，使Claude能通过Python API控制Blender，支持自然语言创建和修改3D场景、调试节点设置、批量更改等。Anthropic同时加入Blender开发基金（最低$280k赞助），这被视为对入门级创意自由职业者的重大冲击。

---

### 10. [Google Cloud同比增长63%，Gemini势头强劲](https://x.com/sundarpichai/status/2049581838260461916)
> Sundar Pichai报告Google Cloud同比增长63%，Gemini势头强劲，搜索查询量创历史新高。同时，Gemini现可直接从聊天生成可下载的Docs、Sheets、Slides、PDF等文件。这是“AI货币化”论题的重要数据点。

---

## 🛠️ 十大工具产品要点

### 1. [Cursor SDK：可编程代理运行时](https://x.com/cursor_ai/status/2049499866217185492)
> Cursor SDK将Cursor的运行时、框架和模型开放给CI/CD、自动化和嵌入式产品使用。提供starter projects和客户示例，标志着Cursor从IDE产品向可编程代理基础设施的战略转型。

---

### 2. [Codex专属席位免费至6月底](https://x.com/OpenAIDevs/status/2049505143218217048)
> OpenAI为符合条件的Business/Enterprise客户推出Codex专属席位，至6月底免席位费。同时Codex新增Supabase集成和Figma插件（将实施计划转为FigJam看板）。

---

### 3. [VS Code框架升级：语义索引、跨仓库搜索、聊天会话洞察](https://x.com/pierceboggan/status/2049504445424423133)
> VS Code发布并行框架改进：跨工作区语义索引、跨仓库搜索、聊天会话洞察、技能上下文、Copilot CLI远程控制，以及提示/代理评估扩展，用于优化提示、技能和指令。

---

### 4. [WebSocket模式加速Codex工作流40%](https://x.com/OpenAIDevs/status/2049595890395152728)
> OpenAI表示，将Codex工作流迁移到Responses API的WebSocket模式可保持状态跨工具调用热启动，减少重复工作，实现高达40%的代理工作流加速。

---

### 5. [LangChain Deep Agents：Harness Profiles和低代码部署](https://x.com/LangChain_OSS/status/2049539590990557381)
> LangChain推出Harness Profiles，支持团队按模型版本化提示、工具和中间件，内置OpenAI、Anthropic和Google模型配置。同时推出DeepAgents Deploy，通过少量markdown/config文件和LangSmith追踪实现低代码部署。

---

### 6. [Cloudflare：让代理成为Cloudflare客户](https://x.com/Cloudflare/status/2049545195914498139)
> Cloudflare扩展“代理即软件”栈，使代理能够创建账户、注册域名、启动付费计划、获取部署token。这标志着供应商开始将业务工作流直接暴露给代理，而非将其视为被动副驾驶。

---

### 7. [Tencent Hunyuan Hy-MT1.5-1.8B：440MB离线翻译模型](https://x.com/TencentHunyuan/status/2049487799850840334)
> 腾讯开源Hy-MT1.5-1.8B-1.25bit，仅440MB的完全离线手机翻译模型，覆盖33种语言、1056个翻译方向，通过激进的1.25-bit量化声称在标准MT基准上与商业API/235B级模型持平。

---

### 8. [Anthropic BioMysteryBench：生物数据分析基准](https://x.com/AnthropicAI/status/2049624600741560340)
> Anthropic发布BioMysteryBench，报告近期Claude模型能解决约30%的专家级生物数据分析难题。同时Hugging Face推出Hugging Science，汇集78GB基因组学、11TB PDE模拟、100M细胞图谱、9T DNA碱基对等开放科学数据。

---

### 9. [Sakana KAME：边说话边思考的语音架构](https://x.com/SakanaAILabs/status/2049544945233764755)
> Sakana提出KAME架构，通过结合低延迟前端模型和异步后端LLM oracle信号，实现“边说话边思考”的语音到语音系统，为实时语音交互提供新范式。

---

### 10. [Odysseys基准：200个长时实时互联网任务](https://x.com/rsalakhu/status/2049521211353301198)
> 新基准Odysseys引入200个长时实时互联网任务、基于评分的评估（非二元成功/失败）和轨迹效率指标。最佳模型成功率仅44.5%，效率低至1.15%，反映了行业向更真实的多步浏览和编排工作评估的推进。