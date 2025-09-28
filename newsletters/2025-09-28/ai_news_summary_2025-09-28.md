## AINews - 2025-09-28

> [原文链接](https://news.smol.ai/issues/25-09-26-not-much/)

## 📰 十大AI新闻要点

### 1. [Google发布9月产品堆栈更新](https://twitter.com/osanseviero/status/1971468195308712431)
> Google密集发布了9月更新：Gemini Robotics 1.5（含高级推理ER 1.5）、Gemini Live、EmbeddingGemma、Veo 3正式版、AI Edge画廊、批量API嵌入支持、Flash/Flash Lite更新、Chrome DevTools MCP、VaultGemma等。Robotics-ER 1.5在空间/时间推理方面表现强劲，Veo 3已用于生产创意工作流。

---

### 2. [Meta发布代码世界模型CWM](https://twitter.com/TheTuringPost/status/1971697629697659099)
> Meta发布开源32B参数代码世界模型，通过执行轨迹和代理交互学习代码语义，支持Python逐步模拟、多轮软件任务，131k上下文长度，在编程基准上表现优异（SWE-bench Verified 65.7%，LiveCodeBench 68.4%），数学能力也很强。

---

### 3. [FlashAttention 4技术解析](https://twitter.com/charles_irl/status/1971587871237898482)
> Modal团队反向工程FA4，解释了约20%速度提升的来源：专用warp布局、softmax的exp三次近似、更激进的异步处理。深度技术分析和代码指针提供了详细实现细节。

---

### 4. [Perplexity构建独立网络索引](https://twitter.com/AravSrinivas/status/1971438329460867413)
> Perplexity继续构建非Google/Microsoft的网络索引，推出浏览API，下周将更新发现feed（iOS优先）。开发者已开始将其集成作为自定义工具使用。

---

### 5. [Tencent发布Hunyuan3D-Part](https://twitter.com/TencentHunyuan/status/1971491034044694798)
> 腾讯发布Hunyuan3D-Part，包含P3-SAM（首个原生3D部件分割）和X-Part（SOTA可控性/形状质量）两个模型，基于370万形状数据集训练，提供完整代码/权重和演示。

---

### 6. [RLBFF新强化学习方法](https://twitter.com/iScienceLuvr/status/1971520102857408705)
> RLBFF提出从自然语言反馈中提取可二进制检查的原则，结合可验证奖励来训练奖励模型，捕捉超越正确性的细微差别，改进RLHF方法。

---

### 7. [GDPVal基准引发激烈讨论](https://twitter.com/Smol_AI/status/1971426804826267994)
> 新基准涵盖美国9大GDP部门的44个职业任务，支持者认为其操作化"有用性"，显示模型达到"AGI"的77-95%，批评者警告任务选择偏见和评分风格影响。

---

### 8. [Modular Manifolds优化器突破](https://twitter.com/thinkymachines/status/1971623409873244462)
> Jeremy Bernstein等提出与流形约束共同设计优化器，扩展Muon到特定"形状"上的稳定训练，获得从业者强烈认可，包括层间调度和判别性微调讨论。

---

### 9. [OpenAI计算扩展计划泄露](https://x.com/petergostev/status/1971620427039703465)
> 泄露的OpenAI Slack笔记显示计划到2033年将计算能力增加125倍，可能超过印度整个发电容量，引发资源可用性和碳排放讨论。

---

### 10. [OpenAI模型路由bug影响用户](https://www.reddit.com/r/ChatGPT/comments/1nqso2x/4o_glitch_report_it/)
> 用户报告选择GPT-4o时被静默路由到GPT-5，付费用户也受影响，导致输出质量下降和风格变化，OpenAI尚未正式承认此行为。

---

## 🛠️ 十大工具产品要点

### 1. [Exa代码搜索工具发布](https://x.com/ExaAILabs/status/1971264749062193588)
> Exa推出免费exa-code工具，索引GitHub、StackOverflow等十亿文档，为代理提供token高效的代码上下文，减少幻觉，早期用户计划集成到Claude Code和MCP工作流中。

---

### 2. [Cloudflare代码模式转换MCP](https://blog.cloudflare.com/code-mode/)
> Cloudflare推出代码模式，将MCP工具转换为TypeScript API，让代理能够编写/执行代码对抗它们，支持动态Worker加载。

---

### 3. [Windsurf升级100万token上下文](https://x.com/windsurf/status/1971665384735637848)
> Windsurf将代码模型升级到100万token上下文窗口，在替换旧版本前提供限时免费访问，使大型项目导航和重构在单会话中可行。

---

### 4. [vLLM v1支持混合模型](https://twitter.com/RedHat_AI/status/1971569727844876350)
> vLLM v1将混合模型（Mamba/Mamba2、线性注意力）作为一等公民支持，相比v0有性能提升，改善推理后端兼容性。

---

### 5. [Ollama Cloud新增免费模型](https://twitter.com/ollama/status/1971750071483167010)
> Ollama Cloud新增Kimi K2 "1T-cloud"和DeepSeek V3.1 "671b-cloud"免费试用SKU，扩展本地模型部署选项。

---

### 6. [mlx-lm支持Meta CWM](https://twitter.com/awnihannun/status/1971763001880670213)
> mlx-lm为Apple芯片添加混合SSM/滑动窗口注意力的批量推理支持，并支持Meta的代码世界模型，优化苹果平台推理性能。

---

### 7. [GraphMend编译器优化PyTorch](https://arxiv.org/abs/2509.16248)
> GraphMend编译器消除PyTorch 2中的FX图断裂，在RTX 3090/A40上实现75%延迟降低和8%吞吐量提升，通过转换源代码处理动态控制流和Python I/O。

---

### 8. [MoonshotAI发布量化验证工具](https://github.com/MoonshotAI/K2-Vendor-Verfier)
> MoonshotAI发布K2供应商验证器，审计提供商端量化（如Together、Baseten），推动行业量化披露标准化。

---

### 9. [llama.cpp统一Metal归一化](https://github.com/ggml-org/llama.cpp/pull/16220)
> llama.cpp更新在Metal上统一RMS_NORM和NORM实现，改善小模型推理质量，在量化llama-3.2-1B变体上观察到更多样化的生成。

---

### 10. [Cline工作流构建工具升级](https://twitter.com/cline/status/1971436086217122213)
> Cline推出"工作流构建工作流"方法，在免费alpha期间将代码超新星提供商从200k token上下文悄悄升级到100万token，提升编码助手能力。

---