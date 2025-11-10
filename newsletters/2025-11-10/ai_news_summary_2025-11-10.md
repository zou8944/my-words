## AINews - 2025-11-10

> [原文链接](https://news.smol.ai/issues/25-11-07-tbench2/)

## 📰 十大AI新闻要点

### 1. [Terminal-Bench 2.0发布，修复基准测试问题](https://www.tbench.ai/news/announcement-2.0)
> Terminal-Bench发布2.0版本，解决了原有任务过于简单或不可能完成的问题，并采用新的Harbor框架在云容器中轻松运行。该基准测试已被Claude 4.5和Kimi K2 Thinking等顶级模型引用。

---

### 2. [Moonshot AI发布Kimi K2 Thinking开源推理模型](https://twitter.com/ArtificialAnlys/status/1986911675820446013)
> Kimi K2 Thinking是1T参数的MoE模型，仅激活约32B参数，原生INT4量化，256K上下文窗口，在Artificial Analysis Intelligence Index得分67，成为新的开源权重领导者，在代理任务表现突出。

---

### 3. [Kimi K2 Thinking在代理基准测试中超越GPT-5](https://moonshotai.github.io/Kimi-K2/thinking.html#footnote-3-2)
> 在τ²-Bench Telecom基准测试中，Kimi K2 Thinking以93%的得分领先GPT-5 Codex的87%，成为最强的代理模型，在复杂工具使用和决策任务中表现卓越。

---

### 4. [DreamGym通过"经验模型"革新RL训练](https://twitter.com/jaseweston/status/1986613046047846569)
> DreamGym用基于推理的合成经验替代缓慢的真实环境演练，环境模型从离线轨迹中提炼界面动态，为RL创建新的在线经验，在模拟到真实RL转换中表现优异。

---

### 5. [Cambrian-S推进视频空间认知研究](https://twitter.com/sainingxie/status/1986685042332958925)
> 包含位置论文、VSI-590K数据集、基准测试和开源模型，探索视频中的空间认知，通过内部预测世界模型学习组织和预测感官输入，在空间推理上比基础MLLM提升30%。

---

### 6. [Meta EdgeTAM实现实时分割跟踪](https://twitter.com/mervenoyann/status/1986785795424788812)
> EdgeTAM作为SAM2的替代方案，速度提升22倍，在iPhone 15 Pro Max上达到16 FPS，支持点和边界框提示，Apache-2.0许可，为设备端跟踪工作负载提供实用解决方案。

---

### 7. [长上下文信息聚合仍是技术挑战](https://twitter.com/abertsch72/status/1986842177692180497)
> Oolong测试显示，在128K上下文中，没有模型能在信息密集输入上的简单验证聚合任务中超过50%准确率，表明"精确聚合大量信息"仍是未解决问题。

---

### 8. [vLLM与SGLang竞争定义推理能力边界](https://twitter.com/EdwardSun0909/status/1986603769195602411)
> 业界将vLLM与SGLang的竞争视为"真正的AGI竞争"，反映推理堆栈在实践中如何定义能力边界，腾讯的Hunyuan-image 3.0也采用基于vLLM的官方实现。

---

### 9. [Sam Altman澄清计算基础设施投资意图](https://twitter.com/sama/status/1986917979343495650)
> Altman澄清其诉求不是为OpenAI争取贷款担保，而是推动美国更广泛的再工业化——包括晶圆厂、变压器、钢铁等国内供应链和制造业的国家政策。

---

### 10. [Google重新审视AI意识问题](来源：文章内容)
> 三年前因提出AI具有意识而被解雇的Blake Lemoine事件后，Google现在召集世界顶级意识专家讨论该话题，显示对AI意识问题的态度转变。

---

## 🛠️ 十大工具产品要点

### 1. [Harbor框架支持云容器基准测试](https://harborframework.com/)
> Terminal-Bench 2.0采用Harbor框架重写，支持在云容器中轻松运行大规模沙盒化代理演练，简化AI基准测试部署。

---

### 2. [Kimi K2 Thinking在Apple Silicon原生运行](https://twitter.com/awnihannun/status/1986601104130646266)
> 在2×M3 Ultra上使用MLX流水线并行，K2 Thinking以约15 tok/s速度生成3,500个token，包含具体MLX命令和mlx-lm PR，展示消费级硬件上的高性能推理。

---

### 3. [GitHub Copilot Orchestra多代理模式开源](https://twitter.com/code/status/1986622178146562300)
> 正式化多代理、测试驱动的开发循环（计划→实施→审查→提交），完整提示词开源，为AI辅助编程提供标准化工作流。

---

### 4. [WarpFrac实现精确INT8 GEMM运算](https://github.com/playfularchitect/WarpFrac.git)
> GMP验证的精确INT8×INT8→INT32 GEMM达到300.26 T-ops/s吞吐量，支持在A100上运行，目标是在张量核心速度下实现任意精度计算。

---

### 5. [Parakeet v2实现200倍实时语音转录](https://huggingface.co/spaces/nvidia/parakeet-tdt-0.6b-v2)
> 在单RTX 4090低功耗模式下，Parakeet v2达到约200倍实时STT，3.5小时播客可在10.5秒内转录，多GPU设置预期达到1,200倍。

---

### 6. [OpenRouter推出视频多模态支持](https://openrouter.ai/docs/features/multimodal/videos)
> OpenRouter新增视频支持功能，同时推出TypeScript SDK、Embedding模型和Exacto Variants，提升开发者体验和检索质量。

---

### 7. [Intel llm-scaler优化Intel GPU性能](https://github.com/intel/llm-scaler)
> Intel的llm-scaler通过模型和图级转换提升LLM在Intel GPU上的性能，针对企业级模型和代理工作负载进行优化。

---

### 8. [FastWorkflow在Tau Bench达到SOTA](https://github.com/radiantlogicinc/fastworkflow)
> 在零售和航空工作流中达到最先进水平，证明通过适当的上下文工程，小模型可以匹配或超越大模型，GEPA优化正在进行中。

---

### 9. [Helion GPU内核DSL简化注意力机制开发](https://pytorch.org/blog/helion/)
> PyTorch团队的Helion作为GPU内核领域特定语言，提供注意力内核示例，在延迟、吞吐量和内存方面相比Triton和Flex Attention有优势。

---

### 10. [VoxCPM TTS移植到Apple Neural Engine](https://github.com/0seba/VoxCPMANE)
> OpenBMB VoxCPM文本转语音模型成功移植到CoreML，在Apple Neural Engine上运行，推进真正设备端语音合成流水线在Apple Silicon上的发展。

---