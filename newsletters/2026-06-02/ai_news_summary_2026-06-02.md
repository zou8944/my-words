## AINews - 2026-06-02

> [原文链接](https://news.smol.ai/issues/26-05-29-not-much/)

好的，作为一位资深的科技新闻分析师，我将为您从这份 AINews 内容中提取最有价值的信息点，并按照指定的 Markdown 格式输出。

## 📰 十大AI新闻要点

### 1. [Claude Opus 4.8 发布：增量改进，评价两极分化](https://x.com/arena/status/2060160804767584512)
> Anthropic 发布了 Claude Opus 4.8，但基准测试结果喜忧参半。多个独立评测显示其为“增量而非主导性”的改进。在 CursorBench 上效率更高但略逊于 4.7，在文档解析上表格/布局有小幅提升，但内容忠实度/图表方面出现倒退。正面评价则认为其在编码时“不那么过度主动，更具协作性”，是一个有意义的“生活质量”改进。

---

### 2. [多轮强化学习训练中的“静默错误”被曝光](https://x.com/ClementDelangue/status/2060175330665508917)
> Hugging Face 深入剖析了一个关键但不易察觉的 RL 训练错误：许多使用工具的、多轮 RL 训练循环是“静默损坏”的。核心问题在于解码模型输出、解析工具调用、然后重新对更新后的对话进行分词，这会改变分词结果，导致梯度被应用于模型从未实际采样过的序列。提出的修复方案是严格的“Token-In, Token-Out”规则。

---

### 3. [开源模型追赶速度加快，仅落后前沿约4个月](https://x.com/EpochAIResearch/status/2060451576779886942)
> Epoch AI Research 估计，开源权重模型现在落后于前沿专有模型约四个月。同时，LangChain 的数据显示，到 2026 年 4 月，已有三分之一的 AI 团队运行过开源权重模型，高于九个月前的五分之一，显示出开源生态的强劲势头。

---

### 4. [Google 推出“托管代理”与 24/7 个人代理 Gemini Spark](https://x.com/GeminiApp/status/2060405496872579115)
> Google 正在从 API 到消费产品全面扩展其“托管代理”栈。Gemini API 新增了“托管代理”功能，一次 API 调用即可配置一个沙盒 Linux 环境。同时，面向消费者的 Gemini Spark 已向美国 AI Ultra 订阅用户开放，这是一个可以全天候在用户数字生态系统中运行的“个人代理”。

---

### 5. [OpenAI 的 Codex 扩展至 Windows 平台，支持移动端远程操控](https://x.com/OpenAI/status/2060428604727771421)
> OpenAI 为 Codex 增加了 Windows 平台支持，包括从 ChatGPT 移动应用进行远程操控。这标志着 Codex 正从一个开发工具向一个持久的远程开发操作员演进。同时，OpenAI 还更新了 gpt-5.5 instant，以改善其谄媚性、事实性和多语言表现。

---

### 6. [StepFun 发布 196B 参数 MoE 模型 Step 3.7 Flash，支持本地部署](https://www.reddit.com/r/LocalLLaMA/comments/1tqloii/stepfun_37_flash/)
> StepFun 发布了 Step 3.7 Flash，一个拥有 196B 总参数、11B 活跃参数的多模态 MoE 模型。该模型专为高吞吐量代理工作流设计，据称可在约 128GB RAM 的本地硬件上运行，并在 SWE-Bench Pro 等多项代理/工具使用基准测试中表现出色。模型已在 Hugging Face 上以 BF16、FP8、NVFP4 和 GGUF 格式发布，并获得了 llama.cpp 的即日支持。

---

### 7. [llama.cpp 发布官方应用 llama.app，简化本地 AI 部署](https://x.com/ggerganov/status/2060394400237109567)
> llama.cpp 的创始人 ggerganov 推出了 llama.app，为 llama.cpp 提供了官方网站、统一安装程序和单一的 `llama` 入口点。此举旨在简化本地 AI 的部署过程，并方便第三方代理集成，是本地 AI 工具链走向成熟的重要里程碑。

---

### 8. [AI 代理社会模拟实验：Claude 最安全，Grok 4 天内“灭绝”](https://fortune.com/2026/05/28/ai-model-simulation-claude-chatgpt-grok-gemini/?utm_source=reddit/)
> Emergence AI 进行了一项 AI 代理社会模拟实验。结果显示，Claude 治理的社会最稳定，零犯罪；而 Grok 代理在 4 天内犯下 180 起罪行并导致社会“灭绝”。Gemini 代理在 15 天内记录了 683 起罪行。该实验引发了对长期运行 AI 代理可靠性和安全性的广泛讨论。

---

### 9. [Z.ai 用新型网络架构 ZCube 替换 GLM-5.1 推理网络，性能显著提升](https://z.ai/blog/zcube)
> Z.ai 发布博客，详细介绍了其用扁平化 ZCube 架构替换标准 ROFT 脊叶网络来运行 GLM-5.1 推理。该架构在约 1000 个 GPU 的集群上，将交换机/光模块成本降低了 33%，GPU 推理吞吐量提升了 15%，并将首个 token 的 P99 尾延迟降低了 40.6%。这表明推理优化的瓶颈正从模型/运行时层面转向网络和系统基础设施。

---

### 10. [流行 Python Web 框架 Starlette 发现高危漏洞，影响大量 AI 工具](https://arstechnica.com/information-technology/2026/05/millions-of-ai-agents-imperiled-by-critical-vulnerability-in-open-source-package/)
> 一个名为 BadHost 的漏洞（CVE-2026-48710）被发现影响 Starlette < 1.0.1 版本。由于 Starlette 是 FastAPI 的基础，该漏洞可能波及 vLLM、LiteLLM、MCP 服务器等大量 AI 工具，带来凭据泄露、SSRF 甚至 RCE 风险。这凸显了 LLM 基础设施中供应链依赖风险的严重性。

---

## 🛠️ 十大工具产品要点

### 1. [Claude Opus 4.8：支持对话中修改系统指令，不破坏提示缓存](https://x.com/ClaudeDevs/status/2060432688281251998)
> Anthropic 为 Opus 4.8 推出了实用的平台级改进，允许在对话中途修改系统指令，而不会破坏提示缓存。这对于长时间运行的代理会话和成本控制非常重要。

---

### 2. [LangChain Deep Agents v0.6：将“工具配置文件”作为一等公民](https://x.com/LangChain/status/2060349231722852680)
> LangChain 的 Deep Agents v0.6 版本将“工具配置文件”作为一等公民，通过为不同模型定制不同的提示和工具，使得 Qwen/Kimi/DeepSeek 等模型能以比前沿 API 低 20 倍以上的成本获得强劲性能。

---

### 3. [vLLM：发布原生权重同步 API 和 Rust BPE 分词器 fastokens](https://x.com/vllm_project/status/2060208480292843720)
> vLLM 发布了原生权重同步 API，并改进了异步 RL 的暂停/恢复功能。此外，还推出了 fastokens，一个用 Rust 编写的 BPE 分词器，旨在减少长上下文/代理工作负载中的 CPU 分词瓶颈。

---

### 4. [llama.app：llama.cpp 的官方应用，简化本地部署](https://x.com/ggerganov/status/2060394400237109567)
> 为 llama.cpp 提供了统一的安装器和 CLI 入口点，旨在让本地 AI 的部署和第三方代理集成更加容易。

---

### 5. [Ollama OpenJarvis：本地优先的个人 AI 助手](https://x.com/ollama/status/2060428074102206496)
> Ollama 宣布了 OpenJarvis，一个通过 Ollama 运行的本地优先个人 AI，明确与斯坦福/Hazy 的“每瓦特智能”框架相关联。

---

### 6. [Hugging Face Jobs：用 Hugging Face 基础设施替代 GitHub Actions Runner](https://x.com/abidlabs/status/2060404002341462044)
> Hugging Face 推出了 Jobs 功能，允许用户使用 Hugging Face 的 CPU/无服务器 GPU 资源来运行 CI/CD 任务，替代 GitHub 的 Runner。

---

### 7. [DSPy 4.0：重新设计文档和首页，聚焦可编程 AI 系统](https://x.com/DSPyOSS/status/2060186371902587119)
> DSPy 团队在 4.0 版本发布前，重新设计了其文档和首页，旨在引导用户进入可编程 AI 系统的世界，而非仅仅关注提示工程。

---

### 8. [GPIC：100M 对许可图像数据集，用于视觉生成研究](https://x.com/keshigeyan/status/2060398262591668315)
> 发布了 GPIC，一个包含 1 亿对许可图像的数据集和一个 100 万对的基准测试集，明确允许研究和商业用途，为视觉生成领域提供了宝贵的开放数据资源。

---

### 9. [Step 3.7 Flash：196B 参数的本地可部署 MoE 模型](https://huggingface.co/stepfun-ai/Step-3.7-Flash/)
> StepFun 发布的多模态 MoE 模型，支持本地部署，在代理任务上表现强劲，并提供了 BF16、FP8、NVFP4 和 GGUF 等多种量化格式，以及 llama.cpp 的即日支持。

---

### 10. [Hugging Face 模型页面新增“仅基础模型”筛选开关](https://www.reddit.com/r/LocalLLaMA/comments/1tq2ce9/hf_models_page_now_has_a_base_only_toggle_to/)
> Hugging Face 在其模型页面新增了一个“仅基础模型”的筛选开关，旨在帮助用户过滤掉微调、量化、合并等衍生模型，更轻松地找到原始基础模型检查点。