## AINews - 2025-09-13

> [原文链接](https://news.smol.ai/issues/25-09-11-qwen3-next/)

## 📰 十大AI新闻要点

### 1. [Qwen3-Next发布超稀疏MoE架构](https://qwen.ai/blog?id=4074cca80393150c248e508aa62983f9cb7d27cd&from=research.latest-advancements-list)
> 阿里巴巴发布Qwen3-Next-80B-A3B模型，采用超稀疏MoE设计，总参数量80B但每推理步骤仅激活约3B参数（3.75%激活率），相比GPT-OSS的4.3%和Qwen3的10%显著降低。采用512个专家（10个路由专家+1个共享专家）的混合架构，结合Gated DeltaNet和Gated Attention机制，训练成本降低10倍，长上下文推理速度提升10倍。

---

### 2. [混合架构技术突破：Gated Attention与DeltaNet结合](https://twitter.com/teortaxesTex/status/1966201258404204568)
> Qwen3-Next引入混合Gated DeltaNet + Gated Attention架构，注意力输出门控机制消除Attention Sink和Massive Activation问题，确保数值稳定性。同时采用Zero-Centered RMSNorm新层归一化方法，并对归一化权重应用权重衰减防止无界增长。

---

### 3. [ByteDance Seedream 4.0登顶图像生成与编辑排行榜](https://twitter.com/ArtificialAnlys/status/1966167814512980210)
> Seedream 4.0在Artificial Analysis的文本到图像和图像编辑竞技场中均排名第一，超越Google Gemini 2.5 Flash（Nano-Banana）。该模型合并了Seedream 3和SeedEdit 3，改进文本渲染能力，生成成本为30美元/千次，已在FAL、Replicate和BytePlus平台上线。

---

### 4. [OCR技术栈重大更新：PP-OCRv5与Points-Reader发布](https://twitter.com/PaddlePaddle/status/1965957482716832193)
> 百度发布PP-OCRv5模块化OCR管道（70M参数，Apache-2.0许可），专为密集文档和边缘设备优化；腾讯发布Points-Reader（4B参数），基于Qwen2.5-VL标注训练，在多个基准测试中超越Qwen2.5-VL和MistralOCR。Florence-2 VLM正式集成到transformers库。

---

### 5. [VS Code v1.104集成Copilot Chat与Hugging Face模型](https://twitter.com/code/status/1966145747566375215)
> VS Code新版本大幅升级Copilot Chat功能，包括更好的代理集成、自动模式选择、终端自动批准改进和UI优化。新增BYOK扩展API支持直接提供商密钥，并集成Hugging Face推理提供商，使GLM-4.5、Qwen3 Coder等前沿开源LLM一键可用。

---

### 6. [AgentGym-RL：无需SFT的多轮智能体训练框架](https://twitter.com/arankomatsuzaki/status/1965979980971782414)
> ByteDance Seed发布AgentGym-RL统一强化学习框架，支持网页导航、搜索、游戏等多轮智能体训练，无需监督微调（SFT）。在网页导航任务中达到26%成功率（GPT-4o为16%），深度搜索达到38%（GPT-4o为26%），在BabyAI和SciWorld任务中分别达到96.7%和57%的新记录。

---

### 7. [OpenAI Evals支持原生音频输入与评估](https://twitter.com/OpenAIDevs/status/1965923707085533368)
> OpenAI Evals现在支持原生音频输入和音频评分器，无需转录即可评估语音响应。GPT-Realtime在Big Bench Audio竞技场以82.8%准确率领先（原生语音到语音），接近92%的管道方法（Whisper→文本LLM→TTS），同时保持延迟优势。

---

### 8. [HierMoE提升MoE训练效率](https://twitter.com/gm8xx8/status/1965926377279902022)
> HierMoE通过层次感知All-to-All、令牌去重和专家交换减少节点间流量并平衡负载。在32 GPU A6000集群上，相比Megatron-LM/Tutel-2DH/SmartMoE，All-to-All速度快1.55-3.32倍，端到端训练快1.18-1.27倍，增益随top-k值和跨节点增加而提升。

---

### 9. [Trillion Labs发布Apache-2.0许可的70B中间检查点](https://huggingface.co/trillionlabs/Tri-70B-Intermediate-Checkpoints)
> Trillion Labs发布全球首个70B中间训练检查点（含7B、1.9B和0.5B变体），Apache-2.0许可，包含基础和中间检查点及"首个韩语70B模型"。支持透明训练动态研究，如缩放/优化分析、课程消融和微调起点。

---

### 10. [Kyutai DSM实现延迟流序列到序列建模](https://twitter.com/arankomatsuzaki/status/1965984606764818702)
> Kyutai DSM采用仅解码器LM加预对齐流构建"延迟流"流序列到序列模型，支持ASR↔TTS，延迟几百毫秒，与离线基线竞争，支持无限序列和批处理。

---

## 🛠️ 十大工具产品要点

### 1. [Qwen3-Next模型部署与工具链支持](https://twitter.com/Yuchenj_UW/status/1966199037973200955)
> Qwen3-Next在Hugging Face Hyperbolic上以BF16格式提供服务，提供低延迟端点；vLLM提供原生支持（混合模型的加速内核和内存管理）；Baseten在4×H100上提供专用部署。模型可在Hugging Face、ModelScope、Kaggle获取，并在Qwen聊天应用中试用。

---

### 2. [vLLM组建团队推进开源推理](https://twitter.com/woosuk_k/status/1966245455815487703)
> Thinking Machines正在组建vLLM团队，以推进开源推理技术并服务前沿模型，邀请感兴趣者联系加入。

---

### 3. [LangChain人机回环中间件发布](https://twitter.com/sydneyrunkle/status/1966184060360757340)
> LangChain发布基于LangGraph图形原生中断构建的人机回环中间件，支持工具调用批准（批准/编辑/拒绝/忽略），提供生产就绪的HITL功能与简单API。

---

### 4. [Set Block Decoding大幅减少生成步骤](https://arxiv.org/pdf/2509.07367v1)
> Set Block Decoding（SBD）集成下一令牌预测（NTP）和掩码令牌预测（MATP），在Llama-3.1 8B和Qwen-3 8B上减少生成前向传递3-5倍，保持准确性，无需架构更改且完全兼容KV缓存。

---

### 5. [InstantX Qwen图像修复ControlNet](https://twitter.com/multimodalart/status/1966190381340692748)
> InstantX发布Qwen图像修复ControlNet（Hugging Face模型+演示），支持定向高质量编辑，提升图像修复精度。

---

### 6. [Hugging Face transformers性能深度优化](https://twitter.com/reach_vb/status/1966134598682767507)
> GPT-OSS发布带来transformers深度性能升级，包括MXFP4量化、预构建内核、张量/专家并行、连续批处理，提供基准测试和可重现脚本。

---

### 7. [Cursor Tab模型通过在线RL提升建议接受率](https://twitter.com/cursor_ai/status/1966264815175049526)
> Cursor新Tab模型使用在线强化学习减少21%的建议数量，同时提高28%的接受率，优化代码建议效率。

---

### 8. [ROCm性能分析工具链更新](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/amd-mainline/how-to/using-thread-trace.html)
> 针对MI300X的VALU问题，推荐使用rocprofiler线程跟踪和rocprof计算查看器进行诊断，通过限制每SIMD一个波并线程跟踪来验证调度行为。

---

### 9. [SkyPilot自动化分布式训练配置](https://twitter.com/skypilot_org/status/1966208445339807816)
> SkyPilot等工具自动化调整网络（RDMA/结构）和存储配置，在相同GPU和代码上实现分布式训练后10倍速度提升。

---

### 10. [NCCL算法与协议详解发布](https://twitter.com/StasBekman/status/1966194963194257759)
> 发布关于NCCL算法与协议的清晰详解，为优化集体通信提供宝贵资源，帮助开发者优化分布式训练通信效率。

---