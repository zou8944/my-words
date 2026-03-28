## AINews - 2026-03-28

> [原文链接](https://news.smol.ai/issues/26-03-24-not-much/)

## 📰 十大AI新闻要点

### 1. [Anthropic发布多智能体工作流工程实践](https://x.com/AnthropicAI/status/2036481033621623056)
> Anthropic发布了一篇关于如何利用**多智能体框架**进行前端设计和长期软件任务的工程文章。文章强调，智能体能力的核心正从基础模型转向**编排与框架**，而非单次提示。这反映了生产级智能体部署中，重试、回滚、结构化日志和恢复路径等非技术性瓶颈的重要性。

---

### 2. [Figma推出MCP服务器，实现AI原生设计编辑](https://x.com/figma/status/2036434766661296602)
> Figma的**MCP服务器**和直接AI画布编辑功能进入公开测试阶段。GitHub和Cursor迅速跟进，展示了通过Copilot CLI和MCP协议，AI可以直接在Figma等生产工具中生成组件和前端。这标志着**工具调用正变得产品原生**，而非局限于聊天机器人包装。

---

### 3. [Nous发布Hermes Agent v0.4.0，成为个人智能体运行时](https://x.com/Teknium/status/2036473305025356023)
> Nous Research发布了Hermes Agent v0.4.0重大更新，一周内合并了约300个PR。新增功能包括**OpenAI兼容的Responses API后端**、后台自我改进循环、更广泛的消息集成以及改进的上下文压缩。最有趣的技术特性是**响应后审查智能体**，它能决定将哪些信息保留为可重用的记忆或技能。

---

### 4. [AI2发布开源浏览器智能体MolmoWeb，声称多项基准SOTA](https://x.com/allen_ai/status/2036460260936814915)
> AI2发布了基于Molmo 2的**开源浏览器智能体MolmoWeb**，提供4B和8B两种规模。该模型声称在四个网页智能体基准测试中达到开源权重SOTA，甚至超越了一些专有智能体。这标志着开放智能体生态系统在标准化环境服务和可复现评估方面日趋成熟。

---

### 5. [LiteLLM PyPI包遭供应链攻击，引发安全担忧](https://x.com/karpathy/status/2036487306585268612)
> LiteLLM库的PyPI包（版本1.82.7和1.82.8）被恶意代码入侵，攻击者利用`.pth`文件漏洞在解释器启动时执行代码，试图窃取云凭证、SSH密钥、Kubernetes配置等敏感信息。该事件引发了关于AI时代**整个文件系统都成为攻击面**的广泛讨论，凸显了软件供应链的脆弱性。

---

### 6. [vLLM与Transformers均报告显著推理性能提升](https://x.com/vllm_project/status/2036389182579642544)
> vLLM在GTC回顾中展示了多项系统升级，包括GPU原生Triton内核的Model Runner V2、混合内存分配器、编码器预填充解耦（为多模态工作负载带来高达2.5倍的P99吞吐量提升）以及模块化MoE内核。同时，Hugging Face方面的工作表明，通过连续批处理和`torch.compile`调优，Transformers在8K生成长度下能达到vLLM 95%的吞吐量。

---

### 7. [Hugging Face发布hf-mount，连接本地工具与云端数据](https://x.com/julien_c/status/2036436553082286342)
> Hugging Face发布了**hf-mount**工具，允许用户将Hub上的数据集、模型和存储桶挂载为本地文件系统。这不仅是便利性提升，更是一个重要的智能体/数据原语，为智能体记忆、草稿、团队工件存储以及大型语料库的惰性访问提供了自然的底层支持。

---

### 8. [微软挖角AI2领导团队，引发人才竞争担忧](https://x.com/eliebakouch/status/2036251901985988800)
> 微软挖走了**AI2（艾伦人工智能研究所）** 的部分领导团队成员，包括Ali Farhadi、Hanna Hajishirzi和Ranjay Krishna，他们将加入微软超级智能团队。这一事件引发了技术圈对开放研究机构能否继续与超大规模企业在顶尖人才和前沿研究上竞争的担忧。

---

### 9. [OpenAI宣布基金会投入10亿美元，并调整产品重心](https://x.com/sama/status/2036488680769241223)
> OpenAI宣布其基金会将在未来一年投入至少**10亿美元**，Wojciech Zaremba将转任领导**AI韧性**团队。同时，有报道称OpenAI已完成下一代主要LLM（代号“Spud”）的初期开发，并正在缩减Sora的应用/产品足迹以释放算力。这表明OpenAI正**将产品重心收窄到核心通用模型和基础设施**。

---

### 10. [Google发布TurboQuant，实现KV缓存6-8倍压缩](https://x.com/GoogleResearch/status/2036533564158910740)
> Google Research发布了**TurboQuant**，一种KV缓存压缩算法，声称能在不损失精度的情况下实现至少**6倍的内存减少**和高达**8倍的速度提升**。这反映了高价值性能增益正越来越多地来自**运行时、内存和系统层**的优化，而不仅仅是更大的模型检查点。

---

## 🛠️ 十大工具产品要点

### 1. [Figma MCP服务器与AI画布编辑](https://x.com/figma/status/2036434766661296602)
> Figma推出MCP服务器，允许AI通过模型上下文协议直接在设计画布上进行编辑和生成组件。这实现了设计到代码的无缝AI驱动工作流，是工具调用深度集成到专业产品中的典范。

---

### 2. [Hermes Agent v0.4.0运行时](https://x.com/Teknium/status/2036473305025356023)
> Hermes Agent v0.4.0作为一个功能完整的个人智能体运行时，提供了OpenAI兼容的API、自我改进循环和记忆管理功能。其“响应后审查代理”能自动提炼可重用技能，使其易于通过Open WebUI等标准客户端集成和使用。

---

### 3. [hf-mount远程存储挂载工具](https://x.com/julien_c/status/2036436553082286342)
> Hugging Face的hf-mount工具将远程Hub资源（如5TB的FineWeb数据集切片）挂载为本地文件系统。这极大地降低了智能体访问和处理大规模云端数据的摩擦，为智能体记忆和团队协作提供了基础设施。

---

### 4. [Fox：高性能Rust本地LLM推理引擎](https://github.com/ferrumox/fox)
> Fox是一个用Rust编写的本地LLM推理引擎，作为Ollama的替代品，具备PagedAttention、连续批处理和前缀缓存功能。在RTX 4060上测试Llama-3.2-3B-Instruct-Q4_K_M模型时，实现了72%的TTFT降低和111%的吞吐量提升。

---

### 5. [MolmoWeb开源浏览器智能体](https://x.com/allen_ai/status/2036460260936814915)
> AI2发布的MolmoWeb是一个开源的、基于浏览器的智能体，在多项网页任务基准测试中表现优异。其4B和8B的紧凑尺寸使其在开源智能体生态中成为一个高性能、可复现的基准选项。

---

### 6. [OpenReward RL环境服务平台](https://x.com/GenReasoning/status/2036412836742590950)
> GenReasoning推出的OpenReward平台提供了**330多个强化学习环境**、自动扩展的环境计算能力以及**超过450万个独特的RL任务**。它明确针对智能体RL中常被忽视的“环境计算”层，为可复现的智能体训练和评估提供基础设施。

---

### 7. [Claude Code的Auto Dream记忆管理功能](https://www.reddit.com/r/ClaudeCode/comments/1s2ci4f/claude_code_can_now_dream/)
> Claude Code引入的“Auto Dream”功能，模仿人类REM睡眠过程，定期审查、整理和压缩项目记忆文件，以解决长期使用导致的记忆膨胀和性能下降问题。这是一种创新的AI记忆管理方法。

---

### 8. [vLLM Model Runner V2与系统优化](https://x.com/vllm_project/status/2036389182579642544)
> vLLM的Model Runner V2引入了GPU原生Triton内核、混合内存分配器和编码器预填充解耦等优化，显著提升了多模态工作负载的吞吐量。这些系统级优化是提升推理效率的关键。

---

### 9. [FlashAttention-4实现1613 TFLOPS/s峰值性能](https://www.reddit.com/r/LocalLLaMA/comments/1s1yw23/flashattention4_1613_tflopss_27x_faster_than/)
> FlashAttention-4在Blackwell B200 GPU上实现了1613 TFLOPS/s的算力，达到其理论峰值的71%，比Triton快2.1-2.7倍。其完全使用Python（通过CuTeDSL）编写，编译速度快，并已集成到vLLM 0.17.0中。

---

### 10. [Cursor集成Figma MCP，实现设计系统驱动的前端生成](https://x.com/cursor_ai/status/2036468982560202773)
> Cursor AI迅速将Figma的MCP模式扩展到自身产品中，能够利用团队的**设计系统**在Figma中直接生成组件和前端。这展示了AI工具链的快速整合能力，将设计规范直接转化为可操作的代码生成。