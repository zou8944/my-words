## AINews - 2026-03-26

> [原文链接](https://news.smol.ai/issues/26-03-24-not-much/)

## 📰 十大AI新闻要点

### 1. [Anthropic发布多智能体工作流工程实践](https://x.com/AnthropicAI/status/2036481033621623056)
> Anthropic发布了一篇关于如何利用**多智能体框架**进行前端设计和长期软件任务的工程文章。文章强调，智能体能力的核心正从基础模型转向**编排框架**本身，并指出在生产环境中部署智能体时，重试、回滚、结构化日志和恢复路径等非技术性瓶颈至关重要。

---

### 2. [Figma推出MCP服务器，实现AI原生设计编辑](https://x.com/figma/status/2036434766661296602)
> Figma的**MCP服务器**和直接在画布上进行AI编辑的功能已进入公开测试阶段。GitHub和Cursor等工具迅速跟进，通过MCP协议或直接集成，使AI能够基于团队的设计系统生成组件和前端。这标志着**工具调用正从聊天界面原生转向产品界面原生**。

---

### 3. [NousResearch发布Hermes Agent v0.4.0重大更新](https://x.com/NousResearch/status/2036492872044745180)
> NousResearch发布了**Hermes Agent v0.4.0**，一周内合并了约300个PR。更新包括**OpenAI兼容的Responses API后端**、后台自我改进循环、更广泛的消息集成、改进的上下文压缩以及一个关键的**响应后审查智能体**，该智能体可决定将哪些信息保留为可重用的记忆或技能。

---

### 4. [AI2发布开源浏览器智能体MolmoWeb](https://x.com/allen_ai/status/2036460260936814915)
> AI2发布了基于Molmo 2的**开源浏览器智能体MolmoWeb**，提供4B和8B两种规模。该模型声称在四个网页智能体基准测试中达到了开源权重模型的SOTA水平，甚至超越了一些专有智能体，展示了开源智能体生态的竞争力。

---

### 5. [LiteLLM库遭PyPI供应链攻击](https://x.com/karpathy/status/2036487306585268612)
> **LiteLLM 1.82.8**版本在PyPI上被恶意代码注入，攻击者利用`.pth`文件漏洞在解释器启动时执行代码，试图窃取云凭证、SSH密钥、Kubernetes配置等敏感信息。该事件引发了关于AI时代**整个文件系统都成为攻击面**的广泛讨论，凸显了软件供应链的脆弱性。

---

### 6. [vLLM与Transformers均报告显著推理性能提升](https://x.com/vllm_project/status/2036389182579642544)
> vLLM在GTC上展示了多项系统升级，包括GPU原生的Triton内核、混合内存分配器、编码器预填充解耦（为多模态工作负载带来高达**2.5倍的P99吞吐量提升**）以及模块化MoE内核。同时，Hugging Face方面的工作表明，通过连续批处理和`torch.compile`调优，Transformers在8K生成长度下达到了**vLLM 95%的吞吐量**。

---

### 7. [Hugging Face发布hf-mount，连接本地工具与云端数据](https://x.com/julien_c/status/2036436553082286342)
> Hugging Face发布了**hf-mount**工具，允许用户将Hub上的数据集、模型和存储桶挂载为本地文件系统。这不仅是便利性工具，更被视为一个关键的**智能体/数据基元**，为智能体记忆、草稿、团队工件存储以及大型语料库的惰性访问提供了自然的底层支持。

---

### 8. [微软挖角AI2领导团队，人才向大厂集中趋势明显](https://x.com/eliebakouch/status/2036251901985988800)
> 微软挖走了**AI2（艾伦人工智能研究所）** 的部分领导团队成员，包括Ali Farhadi、Hanna Hajishirzi和Ranjay Krishna，他们将加入微软的超级智能团队。这一事件引发了业界对开源研究机构能否继续与超大规模公司在顶尖人才和前沿研究上竞争的担忧。

---

### 9. [OpenAI宣布基金会投入10亿美元，并调整产品重心](https://x.com/sama/status/2036488680769241223)
> OpenAI宣布其基金会将在未来一年投入至少**10亿美元**，Wojciech Zaremba将转岗领导**AI韧性**相关工作。同时，有报道称OpenAI已完成下一代主要LLM（代号“Spud”）的初步开发，并正在缩减Sora的应用/产品规模以释放算力。这表明OpenAI正**将产品重心收窄到核心通用模型和基础设施**上。

---

### 10. [谷歌发布TurboQuant，KV缓存压缩实现6-8倍效率提升](https://x.com/GoogleResearch/status/2036533564158910740)
> 谷歌研究院发布了**TurboQuant**，这是一种KV缓存压缩算法，据称能在不损失精度的情况下实现至少**6倍的内存减少**和高达**8倍的加速**。这再次印证了当前AI性能提升的重点正从更大的模型检查点转向**运行时、内存和系统层**的优化。

---

## 🛠️ 十大工具产品要点

### 1. [Figma MCP服务器与AI画布编辑](https://x.com/figma/status/2036434766661296602)
> Figma推出MCP服务器，允许AI通过标准协议（如Copilot CLI）直接读取和编辑设计文件。这实现了**设计到代码/动作的无缝工作流**，是工具调用深度集成到生产环境中的典范。

---

### 2. [Hermes Agent v0.4.0个人智能体运行时](https://x.com/Teknium/status/2036473305025356023)
> Hermes Agent v0.4.0更新使其成为一个功能完整的个人智能体运行时，提供OpenAI兼容的API，可被Open WebUI、LobeChat等任何兼容客户端调用，并具备后台自我改进和记忆管理能力。

---

### 3. [GenReasoning推出OpenReward RL环境平台](https://x.com/GenReasoning/status/2036412836742590950)
> OpenReward平台提供了**330多个强化学习环境**、自动扩展的环境计算能力以及**超过450万个独特的RL任务**，旨在解决智能体强化学习中常被忽视的“环境计算”层问题。

---

### 4. [Zhipu发布ZClawBench真实世界智能体基准](https://x.com/HuggingPapers/status/2036424833144139891)
> ZClawBench是一个包含**116个真实世界智能体任务**的基准测试套件，涵盖办公自动化、编码和分析等领域，旨在推动智能体评估从演示走向标准化和可复现。

---

### 5. [hf-mount：远程存储本地挂载工具](https://x.com/julien_c/status/2036436553082286342)
> Hugging Face的`hf-mount`工具允许将远程数据集、模型等挂载为本地文件系统。它降低了智能体访问大规模云端数据的摩擦，为构建基于文件系统的智能体记忆和协作工具提供了基础设施。

---

### 6. [Fox：高性能Rust本地LLM推理引擎](https://www.reddit.com/r/LocalLLM/comments/1s2753y/i_built_fox_a_rust_llm_inference_engine_with_2x/)
> **Fox**是一个用Rust编写的本地LLM推理引擎，作为Ollama的替代品，它实现了`PagedAttention`、连续批处理和前缀缓存，在RTX 4060上测试Llama-3.2-3B模型时，实现了**72%的更低保真时间（TTFT）**和**111%的更高吞吐量**。

---

### 7. [Claude Code新增“Auto Dream”记忆管理功能](https://www.reddit.com/r/ClaudeCode/comments/1s2ci4f/claude_code_can_now_dream/)
> Claude Code引入**Auto Dream**功能，模仿人类REM睡眠过程，定期审查、整理和压缩会话记忆，以解决长期使用导致的“记忆膨胀”问题，旨在智能管理记忆而非单纯扩展上下文窗口。

---

### 8. [Claude推出“计算机使用”功能](https://www.reddit.com/r/ClaudeAI/comments/1s1ujv6/claude_can_now_use_your_computer/)
> Anthropic为Claude（Pro和Max用户）推出了“计算机使用”功能（研究预览版），允许Claude在获得权限后直接操作macOS上的应用程序、浏览器和电子表格，实现任务自动化。

---

### 9. [Optimal Intellect推出GPU原生求解器Moreau](https://x.com/opt_intellect/status/2036485190646735291)
> 来自CVXPY团队的**Moreau**是一个**GPU原生求解器**，声称相比现有工具能带来数量级的速度提升，展示了在模型层之下进行数学优化的重要性。

---

### 10. [SillyTavern扩展实现游戏NPC智能化](https://www.reddit.com/r/LocalLLaMA/comments/1s2ci9r/created_a_sillytavern_extension_that_brings_npcs/)
> 一款新的SillyTavern扩展利用本地运行的**Cydonia（角色扮演模型）**和**Qwen 3.5 0.8B（游戏主持模型）**，通过读取游戏Wiki并集成语音克隆和游戏状态信息，为任何游戏中的NPC注入动态、符合背景的交互能力。

---