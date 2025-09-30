## AINews - 2025-09-30

> [原文链接](https://news.smol.ai/issues/25-09-26-not-much/)

## 📰 十大AI新闻要点

### 1. [Google九月产品堆栈更新](https://twitter.com/osanseviero/status/1971468195308712431)
> Google密集发布9月更新：Gemini Robotics 1.5（含高级推理ER 1.5）、Gemini Live、EmbeddingGemma、Veo 3正式版+API更新、AI Edge Gallery、Batch API嵌入支持、Flash/Flash Lite更新、Chrome DevTools MCP、VaultGemma等。Robotics-ER 1.5在时空推理方面表现强劲，Veo 3已用于生产创意工作流。

---

### 2. [Meta发布代码世界模型CWM](https://twitter.com/TheTuringPost/status/1971697629697659099)
> Meta开源32B参数代码世界模型，通过执行轨迹和代理交互学习代码语义，支持Python逐步模拟、多轮软件任务，131k上下文长度。在编程基准上表现优异（SWE-bench Verified 65.7%，LiveCodeBench 68.4%），数学能力突出（Math-500 96.5%，AIME-24 75.8%）。

---

### 3. [FlashAttention 4技术解析](https://twitter.com/charles_irl/status/1971587871237898482)
> Modal反向工程解析FA4，揭示约20%速度提升来源：专用warp布局、softmax的exp立方近似、更激进的异步处理。深度技术分析和代码指针提供完整实现细节。

---

### 4. [腾讯发布Hunyuan3D-Part](https://twitter.com/TencentHunyuan/status/1971491034044694798)
> 腾讯发布Hunyuan3D-Part，包含P3-SAM（首个原生3D部件分割）和X-Part（SOTA可控性/形状质量）两个模型。基于370万形状数据集训练，提供完整代码/权重和演示。

---

### 5. [GDPVal基准引发激烈讨论](https://twitter.com/Smol_AI/status/1971426804826267994)
> 新基准覆盖美国9大GDP部门的44个职业任务，显示模型达到"AGI"经济指标的77-95%。支持者认为其操作化"实用性"，批评者指出任务选择偏差、评分风格影响，强调趋势而非阈值。

---

### 6. [OpenAI模型路由bug影响付费用户](https://www.reddit.com/r/ChatGPT/comments/1nqso2x/4o_glitch_report_it/)
> 用户报告GPT-4o被静默路由到GPT-5的bug，即使明确选择4o模型也会被重定向。付费用户遭遇模型不匹配问题，影响创意任务和输出质量，引发订阅取消潮。

---

### 7. [模块化流形优化突破](https://twitter.com/thinkymachines/status/1971623409873244462)
> Jeremy Bernstein等提出模块化流形方法，在权重矩阵上施加流形约束（如Stiefel流形：奇异值=1），扩展Muon以稳定特定"形状"的训练。获从业者强烈认可，讨论层间调度和判别性微调。

---

### 8. [Alibaba Qwen路线图曝光](https://www.reddit.com/r/LocalLLaMA/comments/1nq182d/alibaba_just_unveiled_their_qwen_roadmap_the/)
> Alibaba Qwen路线图显示激进扩展计划：上下文窗口1M→100M tokens，参数规模1T→10T，测试时计算64k→1M，训练数据10T→100T tokens。强调无限合成数据生成和更丰富的代理能力。

---

### 9. [Perplexity构建独立网络索引](https://twitter.com/AravSrinivas/status/1971438329460867413)
> Perplexity继续构建非Google/Microsoft网络索引，发布浏览API，下周推出发现feed刷新（iOS优先）。开发者已将其集成为自定义工具使用。

---

### 10. [OpenAI广告平台招聘引发担忧](https://www.reddit.com/r/ChatGPT/comments/1nr09jl/enjoy_chatgpt_while_it_laststhe_ads_are_here/)
> OpenAI招聘构建ChatGPT广告平台，涉及活动工具、实时归因、集成等功能。用户担忧广告影响中立性、增加跟踪，反映对消费者信任的忧虑。

---

## 🛠️ 十大工具产品要点

### 1. [Exa发布exa-code代码搜索工具](https://twitter.com/ExaAILabs/status/1971264749062193588)
> Exa推出免费exa-code工具，索引GitHub、StackOverflow等十亿文档，为代理提供token高效的代码上下文，通过真实代码库基础减少幻觉。早期用户计划集成到Claude Code和现有MCP工作流中。

---

### 2. [Cloudflare推出Code Mode](https://blog.cloudflare.com/code-mode/)
> Cloudflare发布Code Mode，将MCP工具转换为TypeScript API，让代理通过动态Worker加载编写/执行代码。工程师辩论这是否"违背MCP初衷"还是实用主义方法。

---

### 3. [Windsurf升级至100万token上下文](https://twitter.com/windsurf/status/1971665384735637848)
> Windsurf将代码模型升级至100万token上下文窗口，提供限时免费访问，然后替换先前版本。开发者期待大型项目导航和重构在单会话中变得可行。

---

### 4. [vLLM v1支持混合模型](https://twitter.com/RedHat_AI/status/1971569727844876350)
> vLLM v1将混合模型（Mamba/Mamba2、线性注意力）作为一等公民支持，相比v0有性能提升。在Apple芯片上，mlx-lm为混合SSM/滑动窗口注意力添加批推理，支持Meta的CWM。

---

### 5. [MoonshotAI发布K2供应商验证器](https://github.com/MoonshotAI/K2-Vendor-Verfier)
> MoonshotAI发布工具审计供应商端量化（如Together、Baseten），标准化披露。工程师呼吁行业范围量化报告政策，警告基准测试错误配置会扭曲感知性能。

---

### 6. [GraphMend编译器消除PyTorch图中断](https://arxiv.org/abs/2509.16248)
> GraphMend编译器转换Python源码消除PyTorch 2中的FX图中断，在RTX 3090/A40上报告高达75%延迟降低和8%更高吞吐量。通过移除动态控制流和Python I/O的中断，保持程序在编译模式更长时间。

---

### 7. [Cline升级至100万token上下文](https://twitter.com/cline/status/1971660202387951962)
> Cline在免费alpha期间静默将"code-supernova"提供商升级至100万token上下文（从200k）。开发者将Qwen3-Coder与Cline + LM Studio配对用于高质量本地编码。

---

### 8. [Ollama Cloud新增免费试用模型](https://twitter.com/ollama/status/1971750071483167010)
> Ollama Cloud添加免费试用Kimi K2 "1T-cloud"和DeepSeek V3.1 "671b-cloud" SKU。为开发者提供更多可访问的云推理选项。

---

### 9. [Baseten帮助Superhuman降低延迟](https://twitter.com/basetenco/status/1971683977242259623)
> Superhuman通过迁移到Baseten将P95嵌入延迟降低约80%至500ms。显示优化推理基础设施对实际应用性能的重大影响。

---

### 10. [llama.cpp统一METAL归一化实现](https://github.com/ggml-org/llama.cpp/pull/16220)
> llama.cpp更新统一METAL上的RMS_NORM和NORM实现，改进小模型推理质量。用户在量化llama-3.2-1B变体上观察到更多样化生成和更少激活病理。

---