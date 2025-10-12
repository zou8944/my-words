## AINews - 2025-10-12

> [原文链接](https://news.smol.ai/issues/25-10-10-not-much/)

## 📰 十大AI新闻要点

### 1. [GPT-5 Pro在FrontierMath Tier 4创下新纪录](https://twitter.com/EpochAIResearch/status/1976685685349441826)
> GPT-5 Pro在计算密集型设置中达到13%准确率，以单一问题优势领先Gemini 2.5 Deep Think（统计不显著）。Epoch澄清泄漏问题：OpenAI可访问28/48个问题，GPT-5 Pro的8个解答中有5个来自保留集。

---

### 2. [Markovian Thinking实现推理长度与上下文大小解耦](https://twitter.com/jiqizhixin/status/1976466786565656986)
> Mila+微软提出在固定边界"写入状态"的训练方法，R1-Distill 1.5B模型仅用8K上下文推理24K token，以4倍低计算量击败LongCoT-RL（7 vs 27 H100-月）。

---

### 3. [NVIDIA Blackwell与vLLM在InferenceMAX中获胜](https://twitter.com/mgoin_/status/1976452383258648972)
> vLLM通过深度联合优化实现显著帕累托改进：100+ PRs、FP4/FP8内核、异步调度、图融合和FlashInfer集成，预计通过推测解码和DEP实现额外2-3倍吞吐量提升。

---

### 4. [ATLAS自适应推测解码系统实现4倍加速](https://twitter.com/togethercompute/status/1976655646474031362)
> Together AI的ATLAS系统从实时流量中学习，在DeepSeek-V3.1上达到500 TPS，比基线快4倍，且性能随使用提升。早期报告显示自适应推测器可减少60% RL训练时间。

---

### 5. [微软部署首个大规模NVIDIA GB300 NVL72集群](http://blogs.nvidia.com/blog/microsoft-azure-worlds-first-gb300-nvl72-supercomputing-cluster-openai/?linkId=100000386364404)
> Azure为OpenAI部署4,600+ Blackwell Ultra GPU集群，每个NVL72 VM通过NVLink Switch提供1.44 exaflops FP4算力，目标是在数天而非数周内训练万亿参数模型。

---

### 6. [Google月处理1.3万亿token领先行业](https://twitter.com/demishassabis/status/1976712484657475691)
> Google每月处理约1.3万亿token，远超OpenAI的260万亿和Groq的50万亿。Demis Hassabis确认该数据，同时指出不同模型/词汇表/任务中token信息密度存在差异。

---

### 7. [Epoch估计OpenAI去年计算支出约70亿美元](https://twitter.com/EpochAIResearch/status/1976714284349767990)
> 大部分支出用于研发（实验/失败运行），最终训练运行成本低于10亿美元。这反映了前沿AI研发的巨大计算成本。

---

### 8. [SparseServe为动态稀疏注意力引入KV分层](https://twitter.com/ZhihuFrontier/status/1976544233700929614)
> 通过HBM↔DRAM KV分层、工作集感知动态批处理和层分段预填充，在vLLM测试中实现9.26倍更低TTFT和3.14倍更高吞吐量。

---

### 9. [机器人实现硬件重定向杂技动作](https://twitter.com/zhenkirito123/status/1976663920552427619)
> 使用OmniRetarget + BeyondMimic最小RL跟踪，人形机器人执行墙面翻转动作，成功率5/5。训练仅需轻微调整（如放松终止条件、调整奖励）。

---

### 10. [Benchmarking改革提案PeerBench](https://twitter.com/iScienceLuvr/status/1976586775603851344)
> "Benchmarking is Broken"提案社区治理、监考的评估蓝图：密封执行、滚动题库、延迟透明度，旨在解决AI自我评估的问题。

---

## 🛠️ 十大工具产品要点

### 1. [Qwen3-VL Cookbooks发布多模态任务笔记本](https://twitter.com/Alibaba_Qwen/status/1976479304814145877)
> 阿里巴巴发布完善的笔记本集合，涵盖计算机使用、全向识别、文档解析/OCR、3D定位、视频理解、移动代理、长文档理解、空间推理等多模态任务。

---

### 2. [GPT Realtime Mini语音到语音模型成本大幅降低](https://twitter.com/ArtificialAnlys/status/1976696262083985636)
> 比旗舰Realtime便宜约7倍，TTFA降至0.81秒（从1.27秒），上下文加倍至32K，增加图像输入，定位为WebRTC/WebSocket/SIP上的可扩展代理。

---

### 3. [Moondream 3小型快速开源视觉模型发布](https://twitter.com/moondreamai/status/1976624914070401142)
> 9B参数、64专家MoE、约2B激活参数，增加原生指向、改进OCR和32K上下文，针对UI理解和代理工作流优化。

---

### 4. [KAT-Dev-72B-Exp在SWE-Bench Verified排名第二](https://twitter.com/TheAhmadOsman/status/1976606921756205531)
> Kwaipilot的代理编码模型通过中期训练→SFT+RFT→代理RL调优，可在4×RTX 3090 @ 4位量化下运行。

---

### 5. [Tora统一RL后训练工具发布](https://twitter.com/gm8xx8/status/1976443792850092464)
> 基于torchtune构建，统一GRPO、FSDP、编译支持，实现稳定的4位RL（QLoRA/QDoRA），通过DoRA-Cache将rollout速度提升2-4倍。

---

### 6. [ComfyUI集成NVIDIA GPUDirect Storage](https://github.com/maifeeulasad/ComfyUI)
> 通过cuFile DMA直接从NVMe流式传输模型权重到GPU VRAM，使6GB VRAM GPU能够运行重型模型，无需自定义卸载器或量化。

---

### 7. [AniSora V3.2基于Wan2.2的动漫I2V模型](https://github.com/bilibili/Index-anisora)
> 动漫专注的图像到视频模型，支持360°角色旋转，保持线条细节和平坦插图保真度，可直接集成到ComfyUI Wan2.2工作流。

---

### 8. [LangSmith支持JS代码评估](https://twitter.com/LangChainAI/status/1976700402105233603)
> 除Python外新增JavaScript代码评估支持，实现更快、堆栈原生评估。LangChain v1发布可定制的create_agent和中间件钩子。

---

### 9. [Glass Health推出生产级开发者API](https://twitter.com/GlassHealthHQ/status/1976713436773138599)
> 提供HIPAA合规性和引用元数据的生产开发者API，增强医疗AI应用的可信度和可追溯性。

---

### 10. [Predicted Outputs为vLLM提供预填充加速](https://cascadetech.ai/blog/vllm-predicted-outputs/)
> Cascade Tech将可能完成转换为预填充，对部分匹配进行加速生成，无需改变API即可显著降低延迟，提供实时演示和应用集成。

---