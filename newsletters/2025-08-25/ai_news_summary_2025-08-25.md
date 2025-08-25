## AINews - 2025-08-25

> [原文链接](https://news.smol.ai/issues/25-08-22-not-much/)

## 📰 十大AI新闻要点

### 1. [DeepMind发布Genie 3世界模拟器](https://twitter.com/demishassabis/status/1958696882105995312)
> DeepMind的Genie 3是一个多模态交互式世界模拟器，可通过文本、照片或视频提示生成持久化虚拟环境，具备高级空间记忆功能（状态在镜头外持续存在）和实时avatar控制能力，为具身智能训练提供全新平台。

---

### 2. [阿里开源Qwen-Image-Edit登顶图像编辑榜](https://twitter.com/Alibaba_Qwen/status/1958725835818770748)
> 阿里开源的Qwen-Image-Edit在Image Editing Arena获得ELO 1098分（排名第2），性能与GPT-4o相当但成本大幅降低，支持局部精确编辑和风格保真，采用Apache-2.0许可证，社区已展示建筑改造等高质量案例。

---

### 3. [Kling 2.1实现帧级精确视频控制](https://twitter.com/Kling_ai/status/1958835762369372269)
> Kling 2.1推出"Start & End Frames"功能，声称相比1.6版本有235%的质量提升，支持精确的中间帧合成，并与Lovart平台集成，实现端到端的视频生成控制。

---

### 4. [DeepSeek V3.1专注智能体与本地推理](https://twitter.com/basetenco/status/1958716181256577347)
> DeepSeek V3.1正式发布，重点优化软件工程智能体和搜索智能体能力，支持在Apple Silicon设备上运行，M3 Ultra单节点可达21 tok/s，多节点通过MLX Distributed实现线性扩展。

---

### 5. [Intern-S1科学多模态MoE模型突破](https://twitter.com/iScienceLuvr/status/1958894938248384542)
> 上海AI实验室推出Intern-S1科学多模态MoE模型，总参数量241B（激活28B），在5T token（2.5T科学数据）上持续预训练，采用混合奖励（MoR）机制在1000+任务上进行强化学习。

---

### 6. [OpenAI与RetroBio合作突破细胞重编程](https://twitter.com/BorisMPower/status/1958915868693602475)
> OpenAI定制"gpt-4b micro"模型设计出新型Yamanaka因子变体，在体外实验中实现比传统OSKM方法50倍以上的iPSC重编程效率，并显示改善的DNA修复能力。

---

### 7. [ByteDance发布512K上下文Seed-OSS-36B](https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct)
> ByteDance开源Seed-OSS-36B模型，支持原生512K上下文窗口，内置"thinking budget"机制可自监控token使用，在RULER基准128K上下文测试中获得94分，表现优于同类长上下文模型。

---

### 8. [Google DeepMind公布Gemini碳足迹数据](https://twitter.com/GoogleDeepMind/status/1958855573790765273)
> Google DeepMind发布Gemini模型每提示的碳排放指标：中位文本提示消耗<9秒电视能源、约5滴水、0.03克CO2e，相比一年前实现33倍能效提升和44倍碳减排。

---

### 9. [混合模型路由实现成本效益突破](https://twitter.com/omarsar0/status/1958897458408563069)
> 新型k-means路由系统（k=60）通过动态模型选择，在复杂推理任务中相比GPT-5-medium实现约7%准确率提升的同时降低27%成本，支持从廉价模型到高端模型的智能切换。

---

### 10. [xAI宣布建造吉瓦级AI超算Colossus 2](https://twitter.com/elonmusk/status/1958846872157921546)
> xAI宣布正在建造世界首个吉瓦级以上AI训练超级计算机Colossus 2，同时启动"Macrohard"纯AI软件公司项目，模拟端到端现代软件组织运作。

---

## 🛠️ 十大工具产品要点

### 1. [Genie 3世界模拟器工具链](https://twitter.com/demishassabis/status/1958696898488840414)
> DeepMind Genie 3提供完整的世界模拟工具链，支持文本、图像、视频多种输入方式，具备持久化状态管理和实时控制API，为具身智能训练提供完整解决方案。

---

### 2. [Qwen-Image-Edit低成本图像编辑](https://twitter.com/ostrisai/status/1958932936620900666)
> Qwen-Image-Edit支持3-bit ARA微调，单张RTX 5090即可训练1024分辨率LoRA，提供媲美商业模型的编辑质量但成本大幅降低，社区已展示建筑改造、风格迁移等应用案例。

---

### 3. [Snowglobe可分享只读链接功能](https://twitter.com/zaydsimjee/status/1958938033811869735)
> Snowglobe模拟器平台新增可分享只读链接功能，SDK即将发布，支持数据生成、评估引导、安全测试和轨迹分析等应用场景。

---

### 4. [DeepSeek本地推理优化方案](https://twitter.com/ivanfioravanti/status/1958778366229655971)
> DeepSeek V3.1提供优化的本地推理方案，4-bit量化版本在M3 Ultra+512GB RAM设备上达到21 tok/s，支持多节点分布式部署，EXO框架即将开源。

---

### 5. [DINOv3浏览器端视频追踪](https://huggingface.co/spaces/webml-community/DINOv3-video-tracking)
> 基于WebGPU的DINOv3语义视频追踪工具，完全在浏览器端运行，支持点提示实例掩码传播和跨帧追踪，无需服务器支持，适合在线视频编辑应用。

---

### 6. [MLX分布式推理框架](https://twitter.com/MattBeton/status/1958946396062851484)
> MLX支持DeepSeek V3.1 4-bit推理，通过Thunderbolt 5实现多设备线性扩展，2×M3 Ultra达14 tok/s，4×设备可同时运行两个模型达28 tok/s。

---

### 7. [Gemini批量API降低成本50%](https://twitter.com/_philschmid/status/1958910444799726014)
> Gemini API推出批量处理功能，大作业（最大2GB JSONL）成本降低50%，集成Google搜索等工具，支持异步处理大规模任务。

---

### 8. [MCP Web-curl网络工具集成](https://github.com/rayss868/MCP-Web-Curl)
> MCP Web-curl工具允许智能体通过Node/TypeScript与Web API交互，MCP Boss提供集中式密钥管理和AI路由网关，实现自动化工具端点选择。

---

### 9. [WildChat-4M英语提示数据集](https://huggingface.co/datasets/MasonMac/WildChat-4M-English-Semantic-Deduplicated)
> 经过语义去重的WildChat-4M英语提示数据集，使用Qwen-4B-Embedding+HNSW技术，包含≤2000 token的提示，适合指令微调和提示工程 pipeline。

---

### 10. [llama.cpp支持Seed-OSS长上下文](https://github.com/ggml-org/llama.cpp/pull/15490)
> llama.cpp通过PR#15490添加对Seed-OSS-36B长上下文模型的支持，提供patched版本和GGUF权重转换，支持512K上下文本地推理。

---