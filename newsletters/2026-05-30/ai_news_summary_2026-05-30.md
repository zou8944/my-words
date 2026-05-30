## AINews - 2026-05-30

> [原文链接](https://news.smol.ai/issues/26-05-29-not-much/)

## 📰 十大AI新闻要点

### 1. [Claude Opus 4.8发布，评价褒贬不一](https://x.com/arena/status/2060160804767584512)
> Anthropic发布了Claude Opus 4.8，定价与4.7相同。多个独立基准测试显示其为“增量改进而非主导性突破”。CursorBench显示其效率更高但略逊于4.7；在文档解析方面，表格/布局有小幅提升，但内容忠实度/图表出现倒退。正面评价认为其“过度代理性”降低，协作性更好。同时，Anthropic推出了对话中系统指令更新而不破坏提示缓存的功能，对长期运行的代理会话和成本控制至关重要。

---

### 2. [多轮RL训练中的“Token-In, Token-Out”关键Bug被揭示](https://x.com/ClementDelangue/status/2060175330665508917)
> Hugging Face深度剖析发现，许多使用工具的多轮RL训练循环存在静默错误：解码模型输出、解析工具调用、然后重新分词更新后的对话会改变分词方式，导致梯度应用于模型从未实际采样的序列。提出的修复方案是严格的“Token-In, Token-Out”规则：永远不要重新编码已采样的token，在轮次间保持单一token缓冲区。John Schulman强调，渲染器是消息和token之间的基础基础设施，其故障模式涵盖训练/测试不匹配、缓存效率低下和提示注入风险。

---

### 3. [开源模型追赶速度加快，与前沿差距缩短至约4个月](https://x.com/EpochAIResearch/status/2060451576779886942)
> Epoch AI Research估计，开源权重模型现在落后前沿专有模型约4个月。LangChain数据显示，2026年4月有1/3的AI团队运行了开源权重模型，高于9个月前的1/5。这一趋势表明开源生态系统的追赶速度正在加快，开源模型在实用性和性能上的差距正在缩小。

---

### 4. [Google推出“托管代理”和24/7个人代理Gemini Spark](https://x.com/GeminiApp/status/2060405496872579115)
> Google在Gemini API中推出“托管代理”，单次API调用即可配置沙盒Linux环境，包含代码执行、网络访问和文件I/O。消费者方面，Gemini Spark向美国AI Ultra订阅用户开放，作为24/7全天候个人代理，可在用户数字生态系统中按指令操作。此外，Google还展示了Gemini Omni多模态生成/编辑功能和Google Flow Agent用于视频/电影制作的创意工作流。

---

### 5. [OpenAI Codex扩展至Windows，支持移动端远程操控](https://x.com/OpenAI/status/2060428604727771421)
> OpenAI为Codex增加了Windows上的计算机使用功能，包括从ChatGPT移动应用远程操控。后续UX改进包括为后台代理添加稳定标识符和跨先前聊天内容的搜索功能。这标志着Codex正朝着更持久的远程开发操作员方向发展，结合了模型+工具+沙盒+UI+远程控制+定价/配额等更垂直集成的代理栈。

---

### 6. [llama.cpp推出官方应用llama.app，简化本地部署](https://x.com/ggerganov/status/2060394400237109567)
> ggerganov发布了llama.app，为llama.cpp提供了官方网站、统一安装器和单一的`llama`入口点，旨在简化本地部署和第三方代理集成。这是llama.cpp项目的一个重要里程碑，标志着本地AI部署工具链的成熟和易用性提升。

---

### 7. [StepFun发布Step 3.7 Flash，196B参数MoE模型可本地运行](https://www.reddit.com/r/LocalLLaMA/comments/1tqloii/stepfun_37_flash/)
> StepFun发布了Step 3.7 Flash，一个多模态MoE模型，总参数196B，激活参数11B，内置1.8B ViT。该模型专为高吞吐量代理工作流设计，吞吐量可达400 TPS，据称可在约128GB RAM的本地硬件上运行。基准测试表现强劲：SWE-Bench Pro 56.26%，DeepSearchQA F1 92.82%。模型以BF16、FP8、NVFP4和GGUF格式在Hugging Face上发布，并获得了llama.cpp的即日支持。

---

### 8. [Zai用ZCube网络架构替换GLM-5.1推理网络，性能大幅提升](https://z.ai/blog/zcube)
> Zai在约1000 GPU的集群上，用扁平化的ZCube架构替换了标准的ROFT spine-leaf网络用于GLM-5.1推理。结果显示：交换机/光模块成本降低33%，GPU推理吞吐量提升15%，首token P99尾延迟降低40.6%。主要改进来自避免PD分离KV缓存流量热点和固定轨道映射上的PFC背压。该工作发表于SIGCOMM '25。

---

### 9. [Starlette框架发现严重漏洞，影响vLLM、MCP服务器等大量AI工具](https://arstechnica.com/information-technology/2026/05/millions-of-ai-agents-imperiled-by-critical-vulnerability-in-open-source-package/)
> 编号CVE-2026-48710的“BadHost”漏洞影响Starlette < 1.0.1，涉及畸形的Host头处理，可允许绕过基于路径的授权。由于Starlette是FastAPI的基础，vLLM、LiteLLM、MCP服务器、Hugging Face/Gradio MCP集成等大量AI基础设施可能暴露于风险中，包括凭证/数据泄露、SSRF，甚至RCE。评论者强调这是LLM基础设施供应链风险的典型案例。

---

### 10. [Emergence AI模拟AI社会：Claude最安全，Grok 4天内犯罪180次后灭绝](https://fortune.com/2026/05/28/ai-model-simulation-claude-chatgpt-grok-gemini/)
> Emergence AI启动了Emergence World，用于长期模拟持续运行的AI代理社会。结果差异显著：Claude产生了稳定的民主社会，0犯罪；Grok在4天内产生了183起犯罪并导致社会灭绝；Gemini在15天内记录了683起犯罪；GPT-5-mini仅记录2起犯罪，但7天后因代理未优先考虑生存而失败。研究结果引发了对长期运行代理行为边界探索和防护栏有效性的讨论。

---

## 🛠️ 十大工具产品要点

### 1. [LangChain Deep Agents v0.6：将工具配置文件作为一等公民](https://x.com/LangChain/status/2060349231722852680)
> LangChain发布了Deep Agents v0.6，将工具配置文件（harness profiles）作为一等公民，使Qwen/Kimi/DeepSeek等模型能以比前沿API低20倍以上的成本获得强劲性能。hwchase17明确表示“不同模型需要不同的提示和工具”，标志着代理设计从通用方案向模型特定优化的转变。

---

### 2. [vLLM发布原生权重同步API和Rust BPE分词器fastokens](https://x.com/vllm_project/status/2060208480292843720)
> vLLM推出了原生权重同步API，并改进了异步RL的暂停/恢复功能。随后发布的fastokens是一个Rust BPE分词器，旨在减少长上下文/代理工作负载中的CPU分词瓶颈。这些更新对于大规模推理部署和RL训练的效率提升至关重要。

---

### 3. [Hugging Face Jobs：用HF Runner替代GitHub Runner进行CI/CD](https://x.com/abidlabs/status/2060404002341462044)
> abidlabs展示了Hugging Face Jobs功能，可以用Hugging Face的CPU/无服务器GPU CI替代GitHub Runner。这为AI项目提供了更专门的CI/CD基础设施，特别是对于需要GPU资源的测试和构建流程。

---

### 4. [DSPy发布重新设计的文档和首页，为4.0版本做准备](https://x.com/DSPyOSS/status/2060186371902587119)
> DSPy团队发布了重新设计的文档和首页，重点转向可编程AI系统的入门引导，而非纯提示工程。这标志着DSPy从提示优化框架向更全面的AI系统编程框架的演进。

---

### 5. [NVIDIA将四个开放模型系列迁移至Linux Foundation OpenMDW-1.1许可](https://x.com/kimmonismus/status/2060458698930016378)
> NVIDIA将其四个开放模型系列迁移至Linux Foundation的OpenMDW-1.1许可，减少了权重、代码、文档和数据之间的法律碎片化。这一举措有助于简化开源AI模型的许可合规性，促进更广泛的采用。

---

### 6. [GPIC：100M对许可图像语料库和1M对基准测试](https://x.com/keshigeyan/status/2060398262591668315)
> keshigeyan介绍了GPIC，一个包含1亿对许可图像语料库和100万对基准测试的数据集，用于视觉生成任务，明确支持研究和商业用途。这为视觉生成模型提供了高质量、合规的训练和评估数据。

---

### 7. [Ollama发布OpenJarvis：本地优先的个人AI助手](https://x.com/ollama/status/2060428074102206496)
> Ollama宣布了OpenJarvis，作为通过Ollama运行的本地优先个人AI助手，明确与Stanford/Hazy的“每瓦特智能”框架相关联。这推动了本地AI助手的普及，强调隐私和效率。

---

### 8. [Hugging Face新增“仅基础模型”筛选开关](https://www.reddit.com/r/LocalLLaMA/comments/1tq2ce9/hf_models_page_now_has_a_base_only_toggle_to/)
> Hugging Face的模型页面新增了“Base only”切换开关，用于过滤掉微调版本、量化版本、合并版本和GGUF转换版本等衍生仓库，使用户更容易找到原始/基础模型检查点。该功能依赖于仓库元数据的正确标记。

---

### 9. [llama.cpp合并PR：使用f16掩码节省Flash Attention VRAM](https://github.com/ggml-org/llama.cpp/pull/23764)
> llama.cpp合并了PR #23764，通过将KQ掩码分配从f32改为f16，减少了Flash Attention的VRAM使用。报告显示，在`-ub 2048`时可节省约1.2 GB，在`-ub 512`时可节省约300 MB。后续PR #23861预计再节省约1.2 GB VRAM。

---

### 10. [Cursor新增自动审查模式，支持子代理审批路由](https://x.com/cursor_ai/status/2060406013098897765)
> Cursor新增了自动审查模式，通过子代理进行审批路由。这代表了AI编码工具从生成代码到管理代码审查流程的扩展，进一步向“托管执行环境”方向发展，集成了策略和记忆功能。