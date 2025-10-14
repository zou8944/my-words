## AINews - 2025-10-14

> [原文链接](https://news.smol.ai/issues/25-10-10-not-much/)

## 📰 十大AI新闻要点

### 1. [GPT-5 Pro在FrontierMath Tier 4测试中创下新纪录](https://twitter.com/EpochAIResearch/status/1976685685349441826)
> GPT-5 Pro在计算密集型设置中达到13%准确率，以单一问题优势领先Gemini 2.5 Deep Think（统计上不显著）。Epoch澄清泄漏问题：OpenAI可访问28/48个问题，GPT-5 Pro解决的8个问题中有5个来自保留集。

---

### 2. [Markovian Thinking方法显著提升推理效率](https://twitter.com/jiqizhixin/status/1976466786565656986)
> Mila和微软提出在固定边界"写状态"的训练方法，将推理长度与上下文大小解耦，使推理变为线性计算。R1-Distill 1.5B模型仅用8K上下文推理24K token，以约4倍更低计算量击败在完整24K上训练的LongCoT-RL。

---

### 3. [推理训练本质研究：基础模型已包含推理机制](https://twitter.com/cvenhoff00/status/1976633766811734461)
> 新研究认为基础模型已包含推理机制，"思考模型"学习何时调用它们。在正确时间调用技能可恢复基础模型与推理模型之间高达91%的差距。

---

### 4. [NVIDIA Blackwell与vLLM在InferenceMAX中获胜](https://twitter.com/mgoin_/status/1976452383258648972)
> vLLM通过与NVIDIA深度合作实现强大帕累托改进：100+ PRs跨堆栈、FP4/FP8内核、异步调度、图融合和FlashInfer集成。通过推测解码和数据+专家并行，预计吞吐量再提升2-3倍。

---

### 5. [Together AI推出自适应推测解码系统ATLAS](https://twitter.com/togethercompute/status/1976655646474031362)
> ATLAS从实时流量中学习，报告比基线快4倍（DeepSeek-V3.1上500 TPS），并随使用改进。早期报告显示通过自适应推测器可减少60%以上RL训练时间。

---

### 6. [微软推出首个规模化NVIDIA GB300 NVL72集群](http://blogs.nvidia.com/blog/microsoft-azure-worlds-first-gb300-nvl72-supercomputing-cluster-openai/)
> 微软/Azure为OpenAI部署首个生产级NVIDIA GB300 NVL72集群，涵盖>4,600个Blackwell Ultra GPU。每个NVL72 VM通过NVLink Switch fabric融合72个GPU，提供37TB统一加速器，每VM提供1.44 exaflops FP4性能。

---

### 7. [月度token处理量数据公布](https://twitter.com/sundeep/status/1976475987962626062)
> Google每月处理约1.3 quadrillion tokens，OpenAI约260T，Groq约50T。Google的Demis Hassabis重申1.3 quadrillion tokens/月的处理量。

---

### 8. [OpenAI计算支出估算](https://twitter.com/EpochAIResearch/status/1976714284349767990)
> Epoch估计OpenAI去年在计算上花费约70亿美元，大部分用于研发（实验/失败运行），最终训练运行花费不到10亿美元。

---

### 9. [GPT-5训练规格外部估算](https://twitter.com/teortaxesTex/status/1976441366969532888)
> 粗略外部估算显示约1000亿活跃参数，30-100T tokens，RL占预训练的10-100%，总计约6e25 FLOPs。MoE稀疏性讨论暗示总参数非常高但活跃子集很小。

---

### 10. [机器人硬件实现重定向杂技动作](https://twitter.com/zhenkirito123/status/1976663920552427619)
> 使用OmniRetarget + BeyondMimic最小RL跟踪，人形机器人执行墙翻动作，成功率5/5。训练仅需轻微调整（如放宽终止条件、调整奖励）。Unitree G1复制跆拳道旋转踢，通过调优解决模拟到现实的IMU陀螺仪饱和问题。

---

## 🛠️ 十大工具产品要点

### 1. [Qwen3-VL Cookbooks发布](https://twitter.com/Alibaba_Qwen/status/1976479304814145877)
> 为多模态任务提供精炼的notebook集合，涵盖计算机使用、全方位识别、文档解析/OCR、3D定位、视频理解、移动代理、长文档理解、空间推理等，支持本地/API使用。

---

### 2. [GPT Realtime Mini语音到语音模型](https://twitter.com/ArtificialAnlys/status/1976696262083985636)
> 比旗舰Realtime便宜约7倍，将TTFA降至0.81秒（从1.27秒），上下文加倍至32K，增加图像输入，定位用于WebRTC/WebSocket/SIP上的可扩展代理。

---

### 3. [Moondream 3小型快速开源视觉模型](https://twitter.com/moondreamai/status/1976624914070401142)
> 90亿参数，64专家MoE，约20亿活跃参数，增加原生指向、改进OCR和32K上下文，针对UI理解和代理工作流优化。

---

### 4. [KAT-Dev-72B-Exp代理编码模型](https://twitter.com/TheAhmadOsman/status/1976606921756205531)
> 在SWE-Bench Verified排名第2，通过中期训练→SFT+RFT→代理RL调优，可在4×RTX 3090 @ 4位量化上运行。

---

### 5. [Tora统一RL后训练框架](https://twitter.com/gm8xx8/status/1976443792850092464)
> 基于torchtune构建，统一GRPO、FSDP、编译支持，支持稳定的4位RL（QLoRA/QDoRA），通过DoRA-Cache将rollouts速度提升2-4倍。

---

### 6. [ComfyUI集成NVIDIA GPUDirect Storage](https://github.com/maifeeulasad/ComfyUI)
> 通过cuFile DMA直接从NVMe流式传输模型权重到GPU VRAM，使重模型可在仅6GB VRAM的GPU上运行，无需自定义卸载器或量化。

---

### 7. [AniSora V3.2动漫图像到视频模型](https://github.com/bilibili/Index-anisora)
> 基于Wan2.2 I2V的动漫专注图像到视频模型，直接插入ComfyUI Wan2.2工作流，提供开箱即用的"360°角色旋转"功能。

---

### 8. [LangSmith支持JS代码评估](https://twitter.com/LangChainAI/status/1976700402105233603)
> 除Python外新增JavaScript代码评估支持，实现更快、堆栈原生评估。LangChain v1发布可定制的create_agent和模型/工具调用前后中间件钩子。

---

### 9. [LlamaIndex增加可解释文档分类](https://twitter.com/llama_index/status/1976686683468026337)
> 添加具有自定义规则的可解释文档分类功能，增强文档处理和分析能力。

---

### 10. [Glass Health推出生产级开发者API](https://twitter.com/GlassHealthHQ/status/1976713436773138599)
> 推出具有HIPAA合规性和引用元数据的生产级开发者API，为医疗AI应用提供企业级支持。

---