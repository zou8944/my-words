## AINews - 2025-09-29

> [原文链接](https://news.smol.ai/issues/25-09-26-not-much/)

## 📰 十大AI新闻要点

### 1. [Google九月产品堆栈更新：Gemini Robotics 1.5、Live、Veo 3 GA](https://twitter.com/osanseviero/status/1971468195308712431)
> Google在9月发布了密集的产品更新，包括Gemini Robotics 1.5（含高级推理"ER 1.5"）、最新Gemini Live、EmbeddingGemma、Veo 3正式版及API更新等。Robotics-ER 1.5在空间/时间推理方面表现强劲，Veo 3已在创意工作流中投入生产使用。

---

### 2. [Meta发布Code World Model (CWM) 32B开源模型](https://twitter.com/TheTuringPost/status/1971697629697659099)
> Meta发布32B参数的开源代码世界模型，通过执行轨迹和代理交互学习代码语义，支持Python逐步模拟、多轮软件任务，在SWE-bench Verified上达到65.7%，在数学推理上表现优异（96.5% Math-500）。

---

### 3. [FlashAttention 4技术解析](https://twitter.com/charles_irl/status/1971587871237898482)
> Modal团队对FA4进行逆向工程，揭示了约20%速度提升的来源：专用warp布局、softmax的exp立方近似、更激进的异步处理。详细技术分析和代码指针已发布。

---

### 4. [腾讯发布Hunyuan3D-Part部件级3D生成](https://twitter.com/TencentHunyuan/status/1971491034044694798)
> 腾讯发布Hunyuan3D-Part，包含P3-SAM（首个原生3D部件分割）和X-Part（SOTA可控性/形状质量）两个模型，基于370万形状数据集训练，提供完整代码/权重和演示。

---

### 5. [GDPVal基准引发激烈讨论](https://twitter.com/Smol_AI/status/1971426804826267994)
> 新基准GDPVal涵盖美国前9大GDP部门的44个职业任务，支持者认为其将"实用性"操作化，显示模型在经济指标上达到AGI的77-95%。批评者警告存在任务选择偏见和评分风格影响。

---

### 6. [Modular Manifolds优化器突破](https://twitter.com/thinkymachines/status/1971623409873244462)
> Jeremy Bernstein等人提出在权重矩阵上施加流形约束（如Stiefel流形：奇异值=1）的优化器设计，扩展Muon以稳定特定"形状"的训练，获得从业者强烈认可。

---

### 7. [OpenAI计算扩展计划泄露](https://x.com/petergostev/status/1971620427039703465)
> 泄露的OpenAI Slack笔记显示计划到2033年将计算能力提高125倍，可能超过印度整个发电容量，引发关于资源可用性、碳排放和负载平衡策略的讨论。

---

### 8. [Alibaba Qwen路线图公布](https://www.reddit.com/r/LocalLLaMA/comments/1nq182d/alibaba_just_unveiled_their_qwen_roadmap_the/)
> 阿里巴巴公布激进的Qwen路线图，目标统一多模态堆栈，包括上下文窗口从1M→100M tokens，参数从约1T→10T，训练数据从10T→100T tokens，强调无限合成数据生成管道。

---

### 9. [OpenAI模型路由bug影响付费用户](https://www.reddit.com/r/ChatGPT/comments/1nqso2x/4o_glitch_report_it/)
> 用户报告ChatGPT存在路由/别名bug，选择4o时响应来自"5/5-auto"，即使使用模型范围URL或显式选择，重新生成也会切换到5，影响付费用户体验。

---

### 10. [Perplexity构建非Google/Microsoft网络索引](https://twitter.com/AravSrinivas/status/1971438329460867413)
> Perplexity继续构建独立的网络索引，正在发布浏览API，发现feed刷新将于下周推出（iOS优先），开发者已开始将其集成为自定义工具。

---

## 🛠️ 十大工具产品要点

### 1. [Exa发布exa-code代码搜索工具](https://x.com/ExaAILabs/status/1971264749062193588)
> Exa推出免费工具exa-code，索引GitHub、StackOverflow等数十亿文档，为代理提供token高效的代码上下文，通过真实代码库基础减少幻觉，早期用户计划集成到Claude Code和MCP工作流中。

---

### 2. [Cloudflare推出Code Mode for MCP](https://blog.cloudflare.com/code-mode/)
> Cloudflare发布Code Mode，将MCP工具转换为TypeScript API，让代理通过动态Worker加载编写/执行代码，引发关于这是否"违背MCP目的"或实用利用模型编码能力的讨论。

---

### 3. [Windsurf升级至100万token上下文](https://x.com/windsurf/status/1971665384735637848)
> Windsurf将其代码模型升级到100万token上下文窗口，在替换前版本前提供限时免费访问，开发者期待大型项目导航和重构在单会话中变得可行。

---

### 4. [vLLM v1支持混合模型](https://twitter.com/RedHat_AI/status/1971569727844876350)
> vLLM v1将混合模型（如Mamba/Mamba2、线性注意力）作为一等公民支持，相比v0版本有性能提升，为新型架构提供更好的推理支持。

---

### 5. [Ollama Cloud新增免费试用SKU](https://twitter.com/ollama/status/1971750071483167010)
> Ollama Cloud添加Kimi K2 "1T-cloud"和DeepSeek V3.1 "671b-cloud" SKU供免费试用，扩展了云端模型部署选项。

---

### 6. [GraphMend编译器消除PyTorch图中断](https://arxiv.org/abs/2509.16248)
> GraphMend编译器通过转换Python源代码消除PyTorch 2中的FX图中断，在RTX 3090/A40上报告高达75%延迟降低和8%吞吐量提升，针对动态控制流和Python I/O函数引起的中断。

---

### 7. [MoonshotAI发布K2供应商验证器](https://github.com/MoonshotAI/K2-Vendor-Verfier)
> MoonshotAI发布工具审计供应商端量化（如Together、Baseten）并标准化披露，工程师呼吁行业范围的量化报告政策，警告基准测试配置错误可能扭曲感知性能。

---

### 8. [Cline升级至100万token上下文](https://twitter.com/cline/status/1971660202387951962)
> Cline在免费alpha期间将其"code-supernova"提供商从200k token上下文悄悄提升到100万token，同时发布了"构建工作流的工作流"和提示配方。

---

### 9. [mlx-lm添加混合SSM支持](https://twitter.com/awnihannun/status/1971763001880670213)
> 在Apple芯片上，mlx-lm为混合SSM/滑动窗口注意力添加了批量推理支持，并支持Meta的CWM模型，扩展了Apple平台上的模型推理能力。

---

### 10. [Superhuman通过Baseten优化嵌入延迟](https://twitter.com/basetenco/status/1971683977242259623)
> Superhuman通过迁移到Baseten将P95嵌入延迟降低约80%至500ms，展示了推理基础设施优化对实际应用性能的显著影响。

---