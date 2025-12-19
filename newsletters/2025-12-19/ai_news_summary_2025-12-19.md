## AINews - 2025-12-19

> [原文链接](https://news.smol.ai/issues/25-12-17-gemini-3-flash/)

## 📰 十大AI新闻要点

### 1. [谷歌发布Gemini 3 Flash，宣称重夺帕累托前沿优势](https://x.com/sundarpichai/status/2001326061787942957)
> 谷歌正式发布Gemini 3 Flash模型，定位为“专业级推理，闪电级速度”。该模型在多个竞技场和学术基准测试中表现出色，被认为在性能与成本/延迟的权衡上重新定义了帕累托前沿，对GPT-5等模型构成有力挑战。

---

### 2. [Gemini 3 Flash在多项关键基准测试中表现亮眼，甚至超越Pro版本](https://x.com/fchollet/status/2001330643423449409)
> 早期基准测试结果显示，Gemini 3 Flash在ARC-AGI-2和SWE-bench Verified等推理与编码任务中，性能可匹敌甚至超越更大的Gemini 3 Pro模型，并在某些配置下与GPT-5.2竞争。其成本效益显著，输入定价为每百万token 0.5美元。

---

### 3. [xAI发布Grok语音代理API，支持工具调用与多语言](https://twitter.com/xai/status/2001385958147752255)
> xAI推出新的语音到语音代理API，支持工具调用、网络/RAG搜索、SIP电话和100多种语言。该模型在Big Bench Audio基准测试中达到92.3%的推理准确率，首字节时间约0.78秒，定价为每分钟0.05美元。

---

### 4. [腾讯混元HY World 1.5开源，实现实时交互式3D世界建模](https://twitter.com/TencentHunyuan/status/2001170499133653006)
> 腾讯混元团队开源HY World 1.5（WorldPlay），这是一个流式视频扩散框架，能以24 FPS实现实时、交互式的3D世界建模，并保持长期几何一致性。它引入了“重构上下文记忆”和“双重动作表征”技术，支持第一/第三人称视角和无限世界扩展。

---

### 5. [微软开源TRELLIS 2-4B图像转3D模型](https://huggingface.co/microsoft/TRELLIS.2-4B)
> 微软发布开源模型TRELLIS 2-4B，旨在将单张图像转换为3D资产。该模型结合了流匹配变换器和稀疏体素3D VAE架构，参数量为40亿。模型已在Hugging Face上提供，并附有演示空间。

---

### 6. [苹果发布SHARP模型，秒级从单图生成逼真3D高斯表征](https://github.com/apple/ml-sharp)
> 苹果推出SHARP模型，能够从单张图像在数秒内生成逼真的3D高斯表征。该模型依赖CUDA GPU进行渲染加速，代表了3D图像处理领域的显著进步，相关代码和论文已公开。

---

### 7. [Noumena发布“nmoe”，展示面向B200的FP4 MoE训练方案](https://twitter.com/_xjdr/status/2001434891087671779)
> Noumena发布了“nmoe”，一个面向DeepSeek风格超稀疏混合专家模型的生产级参考训练方案，专注于B200 GPU。方案采用RDEP并行策略、通过NVSHMEM直接调度，并支持专家混合精度（BF16/FP8/NVFP4），宣称已“解决”MoE的NVFP4训练问题。

---

### 8. [OpenAI发布FrontierScience基准，揭示科学QA模型短板](https://twitter.com/jungofthewon/status/2001302379527114798)
> OpenAI推出FrontierScience基准测试，旨在揭示当前AI模型在科学问答上的差距，包括推理、小众概念理解和计算错误。此举旨在推动更透明的进展追踪，并促进模型在专业领域的可靠性提升。

---

### 9. [QwenLong-L1.5发布，支持400万token上下文](https://huggingface.co/Tongyi-Zhiwen/QwenLong-L1.5-30B-A3B)
> 通义千问团队推出QwenLong-L1.5模型，在长上下文推理上达到新的SOTA水平，能够处理高达400万token的上下文。该模型通过创新的数据合成、稳定的强化学习和先进的内存管理技术实现。

---

### 10. [vLLM报告与PyTorch深度集成，Blackwell吞吐量一个月内提升33%](https://twitter.com/vllm_project/status/2001449658984632699)
> vLLM项目报告，通过与PyTorch进行深度集成优化，在一个月内将Blackwell GPU上的推理吞吐量提升了高达33%，从而降低了每token成本并提升了峰值速度。

---

## 🛠️ 十大工具产品要点

### 1. [Gemini 3 Flash集成至主流开发环境](https://twitter.com/cursor_ai/status/2001326908030804293)
> Gemini 3 Flash发布后迅速集成到多个主流开发工具中，包括Cursor、VS Code/Code、Ollama Cloud、Yupp、Perplexity以及LlamaIndex FS Agent等，为开发者提供近实时的编码/编辑和多模态分析能力。

---

### 2. [Argmax SDK 2.0发布实时转录功能，速度快于实时且功耗低](https://twitter.com/argmax/status/2001296557556040028)
> Argmax SDK 2.0推出了“带说话人识别的实时转录”功能，在Mac/iPhone上速度快于实时，功耗低于3W，并在准确性上实现了“阶跃式改变”，为生产级语音代理栈提供了强大基础设施。

---

### 3. [Unsloth与PyTorch合作，支持微调模型导出至iOS/Android](https://twitter.com/UnslothAI/status/2001305185206091917)
> Unsloth与PyTorch宣布了一条将微调后的模型导出到iOS和Android设备的路径。例如，Qwen3模型可在Pixel 8或iPhone 15 Pro上以约40 token/秒的速度完全本地运行。

---

### 4. [LangSmith展示规模化Agent部署与评估工具链](https://twitter.com/LangChainAI/status/2001321491703443877)
> LangSmith展示了在Vodafone/Fastweb等企业的规模化Agent部署案例（如“Super TOBi”客服助手），并提供了包括OpenTelemetry追踪、成对偏好队列、自动化评估以及从追踪记录中挖掘技能的工具链，支持持续学习。

---

### 5. [LM-SYS发布“mini-SGLang”，用于教学现代LLM推理内部原理](https://twitter.com/lmsysorg/status/2001356624855023669)
> LM-SYS发布了“mini-SGLang”，将SGLang引擎的核心代码精简至约5000行，旨在用于教学现代大语言模型推理的内部工作原理，同时保持接近原版的性能。

---

### 6. [Qdrant展示“Snappy”开源多模态PDF搜索管道](https://twitter.com/qdrant_engine/status/2001170495987966132)
> 向量数据库Qdrant展示了“Snappy”，一个使用ColPali补丁级嵌入和多向量搜索技术的开源多模态PDF搜索管道。同时配发了一篇关于在生产中部署ColBERT/ColPali的实用文章。

---

### 7. [Runway Gen-4.5强调物理真实的运动生成](https://twitter.com/runwayml/status/2001352437186334875)
> Runway为其Gen-4.5视频生成模型强调了物理真实的运动生成能力。同期，Kling 2.6增加了运动控制和语音控制功能，并举办创作者比赛。

---

### 8. [Warp推出终端驱动型Agent](https://news.smol.ai/issues/25-12-17-gemini-3-flash/#discord-recap)
> Warp终端推出了新的Agent功能，能够驱动终端工作流（例如运行SQLite/Postgres REPL），用户可通过`cmd+i`调用，其`/plan`功能尤其受到团队好评，标志着IDE/终端正加速融合Agent化用户体验。
> 来源：文章内容

---

### 9. [OpenRouter推动“OpenCompletions RFC”以标准化API行为](https://news.smol.ai/issues/25-12-17-gemini-3-flash/#discord-recap)
> OpenRouter社区正在推动一项“OpenCompletions RFC”，旨在标准化不同模型提供商之间的补全API行为，特别是定义当模型收到不支持的参数时应如何处理。此举得到了LiteLLM、Pydantic AI等项目的支持，旨在减少生产中的边缘情况。
> 来源：文章内容

---

### 10. [NeoCloudX推出廉价GPU租赁服务，聚合过剩数据中心算力](https://neocloudx.com/)
> 新服务NeoCloudX通过聚合过剩的数据中心容量，提供廉价的GPU租赁服务，例如A100约0.4美元/小时，V100约0.15美元/小时，旨在降低AI训练与推理的算力门槛。

---