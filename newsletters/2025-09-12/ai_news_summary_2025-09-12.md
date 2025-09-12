## AINews - 2025-09-12

> [原文链接](https://news.smol.ai/issues/25-09-11-qwen3-next/)

## 📰 十大AI新闻要点

### 1. [Qwen3-Next发布超稀疏MoE架构](https://qwen.ai/blog?id=4074cca80393150c248e508aa62983f9cb7d27cd&from=research.latest-advancements-list)
> 阿里巴巴发布Qwen3-Next-80B-A3B模型，采用超稀疏MoE设计，总参数量80B但每token仅激活约3B参数（3.75%激活率），创下行业新低。模型使用512个专家（10个路由专家+1个共享专家），结合门控DeltaNet和门控注意力机制，训练成本比Qwen3-32B降低10倍，长上下文推理速度提升10倍。

---

### 2. [混合架构实现严格帕累托优势](https://twitter.com/teortaxesTex/status/1966201258404204568)
> Qwen3-Next在预训练中实现严格帕累托改进，关键架构创新包括：混合门控DeltaNet+门控注意力机制消除注意力沉没和大规模激活问题；采用零中心RMSNorm防止层归一化权重异常增长；改进MoE路由器初始化确保专家无偏选择。

---

### 3. [Seedream 4.0登顶图像生成与编辑排行榜](https://twitter.com/ArtificialAnlys/status/1966167814512980210)
> 字节跳动Seedream 4.0在Artificial Analysis的文本到图像和图像编辑竞技场中均排名第一，超越谷歌Gemini 2.5 Flash（Nano-Banana）。该模型合并了Seedream 3和SeedEdit 3，改进文本渲染能力，生成成本为30美元/千次。

---

### 4. [OCR技术栈重大更新](https://twitter.com/mervenoyann/status/1966176133894098944)
> 多项OCR技术发布：PP-OCRv5（70M参数模块化管道，专为密集文档和边缘设备优化）；腾讯Points-Reader（4B参数，基于Qwen2.5-VL标注训练，多项基准测试超越Qwen2.5-VL和MistralOCR）；Florence-2正式接入transformers库。

---

### 5. [VS Code v1.104集成Copilot重大升级](https://twitter.com/code/status/1966145747566375215)
> VS Code新版本带来Copilot Chat多项增强：更好的智能体集成、自动模式选择模型、终端自动批准改进、UI优化，并正式支持AGENTS.md文件管理规则和指令。新增BYOK扩展API支持直接使用提供商密钥。

---

### 6. [Hugging Face推理提供商集成VS Code](https://twitter.com/reach_vb/status/1966185427582497171)
> Hugging Face推理提供商现直接集成到VS Code中，使前沿开源LLM（GLM-4.5、Qwen3 Coder、DeepSeek 3.1、Kimi K2、GPT-OSS等）一键可用，极大提升开发者访问开放模型的便利性。

---

### 7. [AgentGym-RL统一强化学习框架发布](https://twitter.com/arankomatsuzaki/status/1965979980971782414)
> 字节跳动Seed团队推出AgentGym-RL，统一的多轮智能体训练框架，覆盖网页导航、搜索、游戏、具身和科学任务。无需监督微调，在网页导航任务达到26%（GPT-4o为16%），深度搜索38%（GPT-4o为26%），BabyAI任务96.7%，SciWorld创57%新纪录。

---

### 8. [OpenAI Evals支持原生音频输入](https://twitter.com/OpenAIDevs/status/1965923707085533368)
> OpenAI Evals现在支持原生音频输入和音频评分器，无需转录即可评估语音响应。GPT-Realtime在Big Bench Audio竞技场以82.8%准确率领先（原生语音到语音），接近92%的流水线方法（Whisper→文本LLM→TTS），同时保持延迟优势。

---

### 9. [HierMoE提升MoE训练效率](https://twitter.com/gm8xx8/status/1965926377279902022)
> 分层感知All-to-All通过令牌去重和专家交换减少节点间流量并平衡负载。在32GPU A6000集群上，相比Megatron-LM/Tutel-2DH/SmartMoE，All-to-All快1.55-3.32倍，端到端训练快1.18-1.27倍，增益随top-k值和跨节点增加而提升。

---

### 10. [Set Block Decoding大幅减少生成步骤](https://arxiv.org/pdf/2509.07367v1)
> Set Block Decoding（SBD）集成下一令牌预测（NTP）和掩码令牌预测（MATP），在Llama-3.1 8B和Qwen-3 8B上减少生成前向传递3-5倍，同时保持准确性，无需架构更改且完全兼容KV缓存。

---

## 🛠️ 十大工具产品要点

### 1. [Qwen3-Next生态系统部署支持](https://twitter.com/Yuchenj_UW/status/1966199037973200955)
> Qwen3-Next获全方位部署支持：Hyperbolic在Hugging Face提供BF16服务和低延迟端点；vLLM提供原生支持（混合模型加速内核和内存管理）；Baseten在4×H100上提供专用部署；可在Hugging Face、ModelScope、Kaggle获取，Qwen聊天应用提供试用。

---

### 2. [vLLM组建前沿模型推理团队](https://twitter.com/woosuk_k/status/1966245455815487703)
> Thinking Machines正在组建vLLM团队，推进开源推理技术并服务前沿模型，邀请感兴趣者加入，重点优化大规模模型推理性能和效率。

---

### 3. [LangChain人机回圈中间件发布](https://twitter.com/sydneyrunkle/status/1966184060360757340)
> LangChain推出基于LangGraph图形原生中断的人机回圈中间件，支持工具调用批准（批准/编辑/拒绝/忽略），提供简单API实现生产就绪的HITL功能。

---

### 4. [InstantX精准修复ControlNet](https://twitter.com/multimodalart/status/1966190381340692748)
> InstantX发布Qwen图像修复ControlNet，支持针对性高质量编辑，提供Hugging Face模型和演示，专注于精确控制和高保真度输出。

---

### 5. [Transformers性能深度优化](https://twitter.com/ariG23498/status/1966111451481043402)
> GPT-OSS发布带来transformers深度性能升级：MXFP4量化、预构建内核、张量/专家并行、连续批处理，提供基准测试和可复现脚本，显著提升推理效率。

---

### 6. [Kyutai延迟流序列到序列模型](https://twitter.com/arankomatsuzaki/status/1965984604558700751)
> Kyutai DSM采用仅解码器LM加预对齐流，支持ASR↔TTS转换，延迟仅几百毫秒，竞争离线基线，支持无限序列和批处理，提供论文和代码库。

---

### 7. [OCR模块化管道PP-OCRv5](https://twitter.com/PaddlePaddle/status/1965957482716832193)
> PP-OCRv5为70M参数模块化OCR管道（Apache-2.0许可），专为密集文档布局/文本定位和边缘设备优化，现可在Hugging Face获取。

---

### 8. [Tri-70B中间检查点开源](https://huggingface.co/trillionlabs/Tri-70B-Intermediate-Checkpoints)
> Trillion Labs发布Apache-2.0许可的70B transformer中间训练检查点，包含7B、1.9B和0.5B变体，提供完整训练历程而非最终权重，支持训练动力学研究和透明分析。

---

### 9. [1GIRL QWEN v2.0 LoRA发布](https://civitai.com/models/1923241?modelVersionId=2203783)
> 针对Qwen-Image/Qwen2-Image文本到图像模型的LoRA微调，专注于逼真单主题（女性）肖像，在Civitai发布，但未提供训练细节和基准测试。

---

### 10. [rocprofiler线程追踪工具](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/amd-mainline/how-to/using-thread-trace.html)
> 工程师推荐使用rocprofiler线程追踪和rocprof compute viewer诊断MI300X VALU问题，提供可重复方法在SIMD粒度隔离调度器行为，优化GPU性能分析。

---