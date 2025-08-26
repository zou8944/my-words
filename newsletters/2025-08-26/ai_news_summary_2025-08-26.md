## AINews - 2025-08-26

> [原文链接](https://news.smol.ai/issues/25-08-22-not-much/)

## 📰 十大AI新闻要点

### 1. [DeepMind发布Genie 3世界模拟器](https://twitter.com/demishassabis/status/1958696882105995312)
> DeepMind的Genie 3是一个多模态交互式世界模拟器，可通过文本、照片或视频提示生成持久化虚拟环境。关键特性包括高级空间记忆（状态在镜头外持续存在）和实时avatar控制，为具身智能训练提供全新平台。

---

### 2. [阿里巴巴Qwen-Image-Edit登顶图像编辑竞技场](https://twitter.com/ArtificialAnlys/status/1958712568731902241)
> 阿里巴巴开源的Qwen-Image-Edit在Image Editing Arena获得ELO 1098分（排名第2），性能与GPT-4o相当但成本大幅降低。该Apache-2.0许可模型支持局部精确编辑和风格保真，社区演示显示其在建筑改造等复杂任务中的卓越表现。

---

### 3. [DeepSeek V3.1全面发布，专注智能体应用](https://twitter.com/basetenco/status/1958716181256577347)
> DeepSeek V3.1在多个平台上线，重点优化软件工程智能体（SWE agents）和搜索智能体（Search agents）能力。技术社区报告其在Apple Silicon上的本地推理性能：M3 Ultra单节点达21 tok/s，多节点通过MLX Distributed实现线性扩展。

---

### 4. [Intern-S1科学多模态MoE模型突破](https://twitter.com/iScienceLuvr/status/1958894938248384542)
> 上海AI实验室推出Intern-S1科学多模态混合专家模型，总参数量241B（激活28B），在5T token（2.5T科学数据）上持续预训练。采用创新性的InternBootCamp训练框架，通过混合奖励（MoR）机制在1000+任务上进行离线到在线强化学习。

---

### 5. [OpenAI与RetroBio合作突破细胞重编程效率](https://twitter.com/BorisMPower/status/1958915868693602475)
> OpenAI定制开发的"gpt-4b micro"模型设计出新型Yamanaka因子变体，在体外实验中实现比传统OSKM方法50倍以上的iPSC重编程效率，并显示改善的DNA修复能力早期证据。技术文档已公开分享。

---

### 6. [混合模型路由系统实现成本效益突破](https://twitter.com/omarsar0/status/1958897458408563069)
> 新型k-means路由系统（k=60，使用Qwen3-embedding-8B）通过动态α参数在准确性和成本间权衡，在特定配置中相比GPT-5-medium实现约7%准确率提升的同时降低27%成本，支持从廉价模型到高端推理模型的智能切换。

---

### 7. [ByteDance发布512K上下文Seed-OSS-36B模型](https://www.reddit.com/r/LocalLLaMA/comments/1mxf2sz/seedoss36b_is_ridiculously_good/)
> ByteDance开源的Seed-OSS-36B-Instruct模型具备原生512K上下文窗口，在RULER基准128K上下文测试中获得94分。独特的内置"思考预算"机制可通过<seed:think>标签自监控token使用，实现可控的思维链推理。

---

### 8. [Google DeepMind公布Gemini碳足迹数据](https://twitter.com/GoogleDeepMind/status/1958855573790765273)
> Google DeepMind发布Gemini模型的环境影响方法论，显示中位数文本提示消耗<9秒电视能源、约5滴水、0.03克二氧化碳当量。相比去年，每提示的能源消耗减少33倍，碳排放减少44倍。

---

### 9. [xAI宣布Colossus 2千兆瓦级AI超算](https://twitter.com/elonmusk/status/1958846872157921546)
> Elon Musk宣布xAI正在建设世界首个千兆瓦级AI训练超级计算机"Colossus 2"，同时推出"Macrohard"纯AI软件公司概念，旨在用AI端到端模拟现代软件组织运作。

---

### 10. [Kling 2.1视频生成实现帧级精确控制](https://twitter.com/Kling_ai/status/1958835762369372269)
> Kling 2.1推出"Start & End Frames"功能，声称相比1.6版本有235%的质量提升，支持精确的中间帧合成。与Lovart平台集成，为用户提供更精细的视频生成控制能力。

---

## 🛠️ 十大工具产品要点

### 1. [Qwen-Image-Edit微调工具链成熟](https://twitter.com/ostrisai/status/1958932936620900666)
> AI Toolkit现已支持使用3-bit ARA对Qwen-Image-Edit进行微调，单张RTX 5090即可训练1024分辨率LoRA。文本嵌入缓存技术使24GB显存目标接近实现，虽尚未完全稳定，但为开源图像编辑模型定制化开辟新途径。

---

### 2. [Snowglobe模拟器新增只读分享链接](https://twitter.com/zaydsimjee/status/1958938033811869735)
> Snowglobe模拟器平台新增只读分享链接功能，SDK即将发布。建设者社区报告模拟器在数据生成、评估引导、预发布安全测试和轨迹分析等多个应用场景的价值。

---

### 3. [EXO实现Apple Silicon多节点线性扩展](https://twitter.com/MattBeton/status/1958946396062851484)
> EXO演示通过MLX Distributed over TB5在多个Mac Studio间实现线性扩展：2×M3 Ultra达14 tok/s，4×节点支持两个模型同时运行达28 tok/s。EXO 1.0即将开源，为分布式推理提供新解决方案。

---

### 4. [Daft集成Hugging Face Xet存储](https://twitter.com/lhoestq/status/1958904406004449452)
> Daft数据框架现在支持通过Xet（基于去重的存储系统）读写Hugging Face数据集，实现快速多模态数据集操作，为大规模AI数据处理提供高效解决方案。

---

### 5. [Gemini Batch API降低成本50%](https://twitter.com/_philschmid/status/1958910444799726014)
> Gemini API推出Batch API服务，针对大型作业（最多2GB JSONL）提供50%成本优惠，集成Google Search等工具，为企业级批量处理提供经济高效的选择。

---

### 6. [DINOv3 WebGPU浏览器语义追踪](https://huggingface.co/spaces/webml-community/DINOv3-video-tracking)
> 基于WebGPU的DINOv3语义视频追踪演示，支持完全在浏览器中进行的点提示实例掩码传播和追踪。适用于浏览器端视频编辑，无需服务器支持，代码和实时空间已公开。

---

### 7. [MLX支持DeepSeek V3.1 4-bit推理](https://twitter.com/Prince_Canuma/status/1958791001301987628)
> MLX现在支持DeepSeek V3.1的4-bit量化推理，达到两位数tok/s速度。通过Thunderbolt 5实现多设备分布式计算，显示线性扩展能力，为Apple Silicon生态提供强大推理支持。

---

### 8. [Web-curl MCP工具连接智能体与Web API](https://github.com/rayss868/MCP-Web-Curl)
> Web-curl（Node/TypeScript）MCP工具使智能能够获取并与Web API交互，MCP Boss提供集中式密钥管理，AI路由网关自动选择合适工具端点，为智能体Web集成提供完整解决方案。

---

### 9. [WildChat-4M英语提示数据集发布](https://huggingface.co/datasets/MasonMac/WildChat-4M-English-Semantic-Deduplicated)
> WildChat-4M-English语义去重数据集在Hugging Face发布，包含使用Qwen-4B-Embedding + HNSW等方法去重的英语提示，当前版本支持≤2000 token提示，为提示调优和指令微调管道提供高质量数据源。

---

### 10. [a16z创始人版工作站配置公开](https://twitter.com/Mascobot/status/1958925710988582998)
> a16z的Founders Edition工作站配备4×RTX 6000 Blackwell Max-Q（384GB VRAM）、8TB NVMe、Threadripper PRO 7975WX（32c/64t）、256GB ECC内存，在标准15A/120V电路上峰值功耗1650W，提供完整构建指南。

---