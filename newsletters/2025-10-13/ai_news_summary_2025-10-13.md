## AINews - 2025-10-13

> [原文链接](https://news.smol.ai/issues/25-10-10-not-much/)

## 📰 十大AI新闻要点

### 1. [GPT-5 Pro在FrontierMath Tier 4测试中创下新纪录](https://twitter.com/EpochAIResearch/status/1976685685349441826)
> GPT-5 Pro在计算密集型设置下达到13%准确率，以单一问题优势领先Gemini 2.5 Deep Think（无统计学显著性）。Epoch澄清泄露问题：OpenAI可访问28/48个问题，GPT-5 Pro的8个解答中有5个来自保留测试集。

---

### 2. [Markovian Thinking技术实现推理长度与上下文大小解耦](https://twitter.com/jiqizhixin/status/1976466786565656986)
> Mila和微软提出在固定边界"写入状态"的训练方法，R1-Distill 1.5B模型仅用8K上下文推理24K token，以4倍低计算量击败在完整24K上训练的LongCoT-RL（7 vs 27 H100-月）。

---

### 3. [NVIDIA Blackwell与vLLM在InferenceMAX中展现显著性能提升](https://twitter.com/mgoin_/status/1976452383258648972)
> vLLM通过深度联合优化实现强大帕累托改进：100+ PRs跨栈优化、FP4/FP8内核、异步调度、图融合和FlashInfer集成，预计通过推测解码和数据+专家并行实现额外2-3倍吞吐量提升。

---

### 4. [Together AI发布自适应推测解码系统ATLAS](https://twitter.com/togethercompute/status/1976655646474031362)
> ATLAS从实时流量中学习，报告比基线快4倍（DeepSeek-V3.1上500 TPS），并随使用改进。早期报告显示通过自适应推测器减少60%以上RL训练时间。

---

### 5. [Google月处理约1.3万亿token，OpenAI约2600亿](https://twitter.com/sundeep/status/1976475987962626062)
> Google的Demis Hassabis确认月处理约1.3万亿token，OpenAI约2600亿，Groq约500亿。不同模型/词汇/任务中token的信息密度和有用性存在差异。

---

### 6. [Epoch估计OpenAI去年计算支出约70亿美元](https://twitter.com/EpochAIResearch/status/1976714284349767990)
> 大部分支出用于研发（实验/失败运行），最终训练运行不到10亿美元。GPT-5训练外部估计：约1000亿活跃参数，30-100万亿token，RL占预训练的10-100%，总计约6e25 FLOPs。

---

### 7. [微软发布首个规模化NVIDIA GB300 NVL72集群](http://blogs.nvidia.com/blog/microsoft-azure-worlds-first-gb300-nvl72-supercomputing-cluster-openai/)
> 为OpenAI部署超过4600个Blackwell Ultra GPU，每个NVL72 VM融合72个GPU，提供1.44 exaflops FP4计算能力，使OpenAI能在数天而非数周内训练数万亿参数模型。

---

### 8. [OmniRetarget + BeyondMimic实现人形机器人后空翻](https://twitter.com/zhenkirito123/status/1976663920552427619)
> 使用最小化RL跟踪，人形机器人执行墙面后空翻达到5/5成功率，训练仅需轻微调整（如放宽终止条件、调整奖励）。Unitree G1也重现跆拳道旋转踢。

---

### 9. [Sora 2视频生成质量引发真实性担忧](https://openai.com/sora)
> Sora生成的"耶稣基督"水上运动视频因逼真度引发关注，评论指出这些视频开始欺骗非技术观众，凸显检测问题和深度伪造风险，需要更强大的取证线索和来源工具。

---

### 10. [PeerBench提出社区治理的基准测试改革方案](https://twitter.com/iScienceLuvr/status/1976586775603851344)
> "基准测试已坏-不要让AI成为自己的法官"提出PeerBench蓝图：密封执行、滚动题库、延迟透明度，旨在解决当前基准测试的局限性。

---

## 🛠️ 十大工具产品要点

### 1. [Qwen3-VL Cookbooks发布多模态任务笔记本集](https://twitter.com/Alibaba_Qwen/status/1976479304814145877)
> 为本地/API使用提供精炼的笔记本集，涵盖计算机使用、全方位识别、文档解析/OCR、3D定位、视频理解、移动代理、长文档理解、空间推理等多模态任务。

---

### 2. [GPT Realtime Mini语音到语音模型成本大幅降低](https://twitter.com/ArtificialAnlys/status/1976696262083985636)
> 比旗舰Realtime便宜约7倍，TTFA降至0.81秒（从1.27秒），上下文加倍至32K，增加图像输入，定位用于WebRTC/WebSocket/SIP上的可扩展代理。

---

### 3. [Moondream 3发布小型快速开源视觉模型](https://twitter.com/moondreamai/status/1976624914070401142)
> 90亿参数，64专家MoE，约20亿活跃参数，增加原生指向、改进OCR和32K上下文，针对UI理解和代理工作流程优化。

---

### 4. [KAT-Dev-72B-Exp在SWE-Bench Verified排名第二](https://twitter.com/TheAhmadOsman/status/1976606921756205531)
> 通过中期训练→SFT+RFT→代理RL调优，可在4×RTX 3090 @ 4位量化上运行，展示代理编码能力。

---

### 5. [Tora统一RL后训练与LoRA/QLoRA/DoRA支持](https://twitter.com/gm8xx8/status/1976443792850092464)
> 基于torchtune构建，统一GRPO、FSDP、编译支持，实现稳定的4位RL（QLoRA/QDoRA），通过DoRA-Cache将rollout速度提高2-4倍。

---

### 6. [ComfyUI集成GPUDirect Storage支持](https://github.com/maifeeulasad/ComfyUI)
> 通过cuFile DMA直接从NVMe流式传输模型权重到GPU VRAM，使重模型可在仅6GB VRAM的GPU上运行，无需自定义卸载器或量化。

---

### 7. [AniSora V3.2基于Wan2.2实现360°动漫旋转](https://github.com/bilibili/Index-anisora)
> 动漫专注的图像到视频模型，插入ComfyUI Wan2.2工作流程，提供开箱即用的360°角色转盘，保持线条细节和平滑旋转。

---

### 8. [LangChain v1发布可定制create_agent和中间件钩子](https://twitter.com/sydneyrunkle/status/1976751776620593564)
> 支持模型/工具调用前后的预/后处理钩子，LangSmith现在支持JS代码评估，LlamaIndex增加可解释文档分类。

---

### 9. [Glass Health推出生产级开发者API](https://twitter.com/GlassHealthHQ/status/1976713436773138599)
> 提供HIPAA合规性和引用元数据，为医疗AI应用提供生产就绪的API解决方案。

---

### 10. [Hyperparameters优化实现扩散模型步骤大幅减少](https://arxiv.org/abs/2510.02390)
> 8步实现与20步相当的FID性能，计算减少约60%，速度提高2.5倍，无需训练或蒸馏，跨模型工作。

---