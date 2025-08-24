## AINews - 2025-08-24

> [原文链接](https://news.smol.ai/issues/25-08-22-not-much/)

## 📰 十大AI新闻要点

### 1. [DeepMind发布Genie 3多模态世界模拟器](https://twitter.com/demishassabis/status/1958696882105995312)
> Genie 3是交互式世界模拟器，支持文本、照片或视频提示，具有高级空间记忆（状态在镜头外持续存在）和实时头像控制功能。DeepMind还发布了关于Genie 3潜力的播客。

---

### 2. [阿里巴巴Qwen-Image-Edit开源图像编辑器达到顶级性能](https://twitter.com/ArtificialAnlys/status/1958712568731902241)
> 阿里巴巴新开源图像编辑器在图像编辑竞技场中获得ELO 1098（排名第2），与GPT-4o性能相当但成本大幅降低。社区示例显示强大的局部编辑和风格保真度。

---

### 3. [DeepSeek V3.1正式发布，专注智能体应用](https://twitter.com/basetenco/status/1958716181256577347)
> DeepSeek v3.1在多个平台上线，重点强调软件工程智能体和搜索智能体用例，向完整DeepResearch系统发展。支持Apple Silicon本地推理和集群服务。

---

### 4. [Intern-S1科学多模态MoE模型突破](https://twitter.com/iScienceLuvr/status/1958894938248384542)
> 上海AI实验室推出241B总参数/28B激活参数的科学多模态MoE，在5T token（2.5T科学数据）上持续预训练，使用混合奖励（MoR）在1000+任务上进行离线→在线RL训练。

---

### 5. [混合模型路由系统实现成本效益优化](https://twitter.com/omarsar0/status/1958897458408563069)
> k-means路由系统（k=60）通过α参数在准确性和成本间权衡，报告显示在某一配置下比GPT-5-medium准确率高约7%，成本低约27%。

---

### 6. [OpenAI与RetroBio合作开发高效重编程因子](https://twitter.com/BorisMPower/status/1958915868693602475)
> 定制"gpt-4b micro"模型设计出新型Yamanaka因子变体，在体外实现比OSKM高50倍以上的iPSC重编程效率，并有早期DNA修复改善证据。

---

### 7. [ByteDance发布Seed-OSS-36B长上下文模型](https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct)
> 36B参数模型支持原生512k上下文，在RULER基准测试中128k上下文得分94，内置"思考预算"机制，通过特殊标记自跟踪token使用。

---

### 8. [xAI宣布Colossus 2千兆瓦级AI训练超算](https://twitter.com/elonmusk/status/1958846872157921546)
> Elon Musk宣布xAI的Colossus 2成为"世界首个千兆瓦+AI训练超级计算机"，同时公布"Macrohard"纯AI软件公司招聘计划。

---

### 9. [Google DeepMind公布Gemini可持续性指标](https://twitter.com/GoogleDeepMind/status/1958855573790765273)
> 发布每提示的中位数文本提示能耗指标：<9秒电视能量，约5滴水，0.03 gCO2e，报告显示过去一年每提示能耗降低33倍，碳排放减少44倍。

---

### 10. [Kling 2.1视频模型实现精确帧控制](https://twitter.com/Kling_ai/status/1958835762369372269)
> Kling 2.1发布"开始和结束帧"功能，声称比1.6版本质量提升235%，支持精确中间帧合成，与Lovart平台集成。

---

## 🛠️ 十大工具产品要点

### 1. [Genie 3世界模拟器工具](https://twitter.com/demishassabis/status/1958696898488840414)
> DeepMind的交互式世界模拟器，支持多模态输入和实时控制，具有持久状态记忆功能，为 embodied AI 训练提供环境。

---

### 2. [Qwen-Image-Edit图像编辑工具](https://twitter.com/Alibaba_Qwen/status/1958725835818770748)
> Apache-2.0开源图像编辑器，支持3-bit ARA微调，在单张5090显卡上训练1024分辨率LoRA，成本效益极高。

---

### 3. [DeepSeek V3.1智能体开发工具](https://twitter.com/teortaxesTex/status/1958750497965302118)
> 专为软件工程和搜索智能体优化的模型，支持本地推理和集群部署，在Apple Silicon上实现线性扩展。

---

### 4. [Snowglobe模拟器可分享只读链接](https://twitter.com/zaydsimjee/status/1958938033811869735)
> 模拟器工具新增可分享只读链接功能，SDK即将发布，用于数据生成、评估引导和安全测试。

---

### 5. [MLX分布式推理框架](https://twitter.com/MattBeton/status/1958946396062851484)
> 支持在Mac Studio集群上通过TB5实现线性扩展，EXO 1.0即将开源，实现多设备分布式推理。

---

### 6. [DINOv3浏览器语义视频跟踪](https://huggingface.co/spaces/webml-community/DINOv3-video-tracking)
> WebGPU实现的浏览器内语义对象跟踪，支持点提示实例掩码传播，完全客户端运行，无需服务器。

---

### 7. [Gemini批量API降低成本50%](https://twitter.com/_philschmid/status/1958910444799726014)
> Gemini API提供批量处理功能，大型作业成本降低50%，支持最多2GB JSONL文件和Google搜索等工具。

---

### 8. [DeepConf推理时分支剪枝方法](https://twitter.com/jiawzhao/status/1958982524333678877)
> 插件式推理时方法，在并行CoT中剪枝低置信度分支，节省最多85%的token，约50行代码即可集成到vLLM。

---

### 9. [a16z创始人版工作站配置](https://twitter.com/Mascobot/status/1958925710988582998)
> 搭载4×RTX 6000 Blackwell Max-Q（384GB VRAM）、8TB NVMe、Threadripper PRO 7975WX，峰值功耗1650W，提供完整构建指南。

---

### 10. [MCP Web-curl网络工具集成](https://github.com/rayss868/MCP-Web-Curl)
> Node/TypeScript工具，让智能体能够获取和与Web API交互，支持MCP协议，实现智能体与网络服务的无缝连接。

---