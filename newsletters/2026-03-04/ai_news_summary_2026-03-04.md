## AINews - 2026-03-04

> [原文链接](https://news.smol.ai/issues/26-03-02-not-much/)

## 📰 十大AI新闻要点

### 1. [阿里发布Qwen 3.5小型模型系列，主打边缘与多模态](https://x.com/Alibaba_Qwen/status/2028460046510965160)
> 阿里巴巴发布了Qwen 3.5小型模型系列，包括0.8B、2B、4B和9B参数版本，提供Base和Instruct模型。该系列定位为“更高智能，更低算力”，具备原生多模态能力和规模化强化学习，明确针对边缘计算和轻量级智能体部署。模型支持高达262K的原生上下文长度（可扩展至1M），并已在Ollama、LM Studio等平台快速集成。

---

### 2. [苹果神经引擎（ANE）被逆向工程，可用于模型训练](https://x.com/AmbsdOP/status/2028457255968874940)
> 研究人员成功逆向工程了苹果的神经引擎（ANE），利用未公开的API绕过了CoreML，构建了Transformer训练循环。该研究展示了ANE极高的能效比（M4 ANE达6.6 TFLOPS/W，而A100为0.08 TFLOPS/W），并指出其实际FP16算力约为19 TFLOPS，而非宣传的38 TOPS。这为在苹果设备上进行本地训练/微调打开了可能性。

---

### 3. [OpenAI与美国国防部合同引发用户强烈反弹](https://x.com/sama/status/2028640354912923739)
> 在OpenAI宣布与美国国防部（DoW）达成协议后，ChatGPT移动应用的卸载量在48小时内激增295%。Sam Altman随后公布了合同修正案语言，明确禁止对美国人员进行“故意”的国内监视，并指出情报机构（如NSA）的使用需要后续修改。然而，法律界人士指出“故意”一词可能保留了“附带收集”的法律漏洞。

---

### 4. [CUDA Agent：基于强化学习的CUDA内核生成取得突破](https://x.com/BoWang87/status/2028599174992949508)
> 字节跳动发布“CUDA Agent”研究，利用基于真实性能剖析的奖励机制进行智能体强化学习，以生成高性能CUDA内核。该方法超越了“能编译的代码”，致力于生成“运行快速的代码”，据称在KernelBench上达到SOTA，性能大幅超越`torch.compile`，并在最难的内核生成任务上与前沿大模型竞争。

---

### 5. [报告称超80%的部署代码由Claude Code编写，引发可靠性担忧](https://x.com/GergelyOrosz/status/2028465387570884640)
> 一份广为流传的数据点称，在部分组织中“超过80%的所有部署代码由Claude Code编写”。这引发了关于开发速度是否以牺牲代码可靠性为代价的讨论，社区担忧这可能带来回归风险。同时，关于Claude Code在大型公司内部的采用以及“监督编码”取代手动编码的讨论也在进行。

---

### 6. [GitNexus：浏览器内仓库知识图谱与图RAG智能体](https://x.com/MillieMarconnni/status/2028436636841996451)
> 发布了GitNexus工具，它能在浏览器内将代码仓库解析成交互式D3知识图谱，将关系存储在嵌入式KuzuDB中，并通过图遍历查询语言（Cypher）而非传统向量检索来回答问题。该项目完全在浏览器中运行，使用Web Workers，并采用MIT许可证，为代码理解和智能体问答提供了新范式。

---

### 7. [智能体可靠性与“可用性”成为新痛点](https://x.com/ThePrimeagen/status/2028477482865774984)
> 社区讨论指出，当前AI运维的痛点不仅是模型质量，还包括服务“可用性”和因宕机导致的用户体验降级。Claude等服务的多次中断对生产力造成了实际影响，引发了“我们即将达到1个9的可用性（即90%可用）”的调侃，凸显了AI服务可靠性的重要性。

---

### 8. [DeepSeek V4发布在即，传闻参数达万亿级](https://www.reddit.com/r/DeepSeek/comments/1ridmnm/deepseek_v4_all_leaks_and_infos_for_the_release/)
> 据社区传闻，DeepSeek V4预计于2026年3月3日左右发布。传闻其参数规模将达到约1万亿，上下文窗口为100万token，并引入“印迹条件记忆”和“流形约束超连接”等新架构特性。该模型将是多模态的（能处理文本、图像、视频、音频），并针对华为昇腾和寒武纪硬件进行了优化。

---

### 9. [五角大楼将Anthropic列为供应链风险，OpenAI趁势而入](https://xcancel.com/secwar/status/2027507717469049070)
> 美国国防部将Anthropic指定为“供应链风险”，并禁止军事承包商使用其模型，原因是Anthropic拒绝提供无限制的访问权限。与此同时，OpenAI与国防部签署了一项在机密环境中部署先进AI系统的协议，并声称设置了比以往交易更严格的护栏。

---

### 10. [Google发布Static框架，将LLM生成式检索解码加速948倍](https://www.marktechpost.com/2026/03/01/google-ai-introduces-static-a-sparse-matrix-framework-delivering-948x-faster-constrained-decoding-for-llm-based-generative-retrieval/)
> Google AI发布了Static，一个稀疏矩阵框架，专为基于大语言模型的生成式检索设计。该框架通过利用稀疏矩阵运算，实现了高达948倍的约束解码加速，显著提升了检索效率和性能。

---

## 🛠️ 十大工具产品要点

### 1. [Qwen 3.5系列模型已在Ollama上线](https://x.com/ollama/status/2028510184788926567)
> Qwen 3.5全系列小型模型（0.8B, 2B, 4B, 9B）已集成至Ollama，用户可通过`ollama run qwen3.5:[size]b`命令直接运行。该集成支持工具调用、思维链和多模态功能，极大简化了本地部署流程。

---

### 2. [Docker Desktop新增MLX模型运行器](https://x.com/Docker/status/2028470592899354929)
> Docker Desktop的“Model Runner”功能新增对MLX模型的支持，能够以OpenAI兼容的API工作流运行模型。这为Apple Silicon开发者提供了更流畅的本地模型服务体验，简化了开发循环。

---

### 3. [Stripe推出LLM代币计费代理服务](https://x.com/miles_matthias/status/2028515021022548181)
> Stripe推出了面向LLM的计费代理服务，允许开发者选择模型、设置加价，并通过Stripe的LLM代理路由调用，自动记录使用量并计费。这标志着“LLM运维”正被整合进标准的SaaS财务基础设施中。

---

### 4. [llama.cpp计划提供官方Debian/Ubuntu软件包](https://x.com/ggerganov/status/2028505638452531340)
> llama.cpp作者正在征求关于提供官方Debian/Ubuntu软件包的反馈。这一举措将有助于主流Linux发行版用户更便捷地安装和使用这款流行的本地推理工具，推动其进一步普及。

---

### 5. [GitNexus：基于Cypher的浏览器内图RAG工具](https://x.com/MillieMarconnni/status/2028436636841996451)
> GitNexus是一个完全在浏览器内运行的工具，能将代码仓库转换为交互式知识图谱，并使用Cypher查询语言进行图遍历检索（Graph RAG），而非传统的基于嵌入向量的检索，为代码库问答提供了新思路。

---

### 6. [LM Studio支持同时加载多个模型并通过API调用](https://cdn.discordapp.com/attachments/1110598183144399061/1477775728857710622/image.png)
> 用户发现LM Studio能够同时加载多个模型，并通过API为特定任务调用不同的模型。这为构建复杂的本地模型工作流提供了便利，例如让不同模型扮演特定角色或处理专门任务。

---

### 7. [Sakana AI发布“文本生成LoRA”模型](https://huggingface.co/SakanaAI/text-to-lora/tree/main)
> Sakana AI开源了“text-to-lora”模型及其代码，该模型能够根据文本提示直接生成LoRA适配器权重。训练该模型大约需要在一张H100 GPU上连续运行5天，为快速定制化模型微调提供了新工具。

---

### 8. [Anthropic发布《Claude技能构建完全指南》](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)
> Anthropic发布了一份30页的指南，引导开发者从冗长的提示词工程转向构建结构化的“技能”文件。通过将工作流打包成专用文件并进行渐进式披露，可以大幅减少上下文膨胀，提升智能体效率。

---

### 9. [AMD开源rocprof-trace-decoder工具](https://x.com/__tinygrad__/status/2028679089650041069)
> AMD开源了rocprof-trace-decoder，提供了SQTT跟踪定义，支持更深层次的指令级时序跟踪。社区认为这标志着AMD的追踪基础设施在某些方面“优于NVIDIA的”，有助于开发者进行性能分析和优化。

---

### 10. [OpenClaw社区开源其治理政策](https://github.com/openclaw/community)
> OpenClaw社区将其政策与指南在GitHub上开源，以提高透明度。该仓库提供了可访问且最新的社区治理文档，但不包含试用版审核员数据和审核日志。