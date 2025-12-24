## AINews - 2025-12-24

> [原文链接](https://news.smol.ai/issues/25-12-22-not-much/)

## 📰 十大AI新闻要点

### 1. 智谱AI发布GLM-4.7，在多项基准测试中表现优异
> 智谱AI发布了GLM-4.7模型，在编码、复杂推理和工具使用方面相比GLM-4.6有显著提升。该模型在LM Arena的WebDev排行榜上以1449分位列开源模型第一，总榜第六。在SWE-bench验证集上达到73.8%的准确率，接近Claude Sonnet 4.5（77.2%）。模型引入了“交错思考”、“保留思考”和“轮次级思考”等新认知模式，并首次在推理/规划中使用了图表。
来源：https://z.ai/blog/glm-4.7

---

### 2. 小米发布MiMo-V2-Flash，强调部署成本与效率
> 小米发布了MiMo-V2-Flash模型，这是一个专注于成本、速度和可部署性的混合专家模型，而非追求排行榜分数。据称，它以更少的参数匹敌强大的开源模型，输入token价格低至每百万0.1美元。vLLM项目为其发布了官方服务配置方案。
来源：https://twitter.com/omarsar0/status/2002768840556728714

---

### 3. 百度ERNIE 5.0预览版在文本排行榜上取得领先
> 百度ERNIE-5.0-Preview-1203在LM Arena的文本排行榜上以1451分位列第一，相比其1103预览版提升了23分，展示了中国在文本模型领域的进展。
来源：https://twitter.com/arena/status/2003151045946376482

---

### 4. 开源文生图模型竞争加剧，Z-Image Turbo登顶
> 根据Artificial Analysis的报告，Z-Image Turbo成为其Image Arena中排名第一的开源权重文生图模型。该模型拥有60亿参数，采用Apache-2.0许可，在阿里云上的定价为每千张图像5美元。
来源：https://twitter.com/ArtificialAnlys/status/2002839525609865575

---

### 5. 谷歌发布A2UI协议，推动智能体生成交互式UI
> 谷歌开源了A2UI协议，旨在让智能体能够生成交互式用户界面。这标志着智能体从“仅聊天”向“UI生成器”的范式转变，提供了一个标准化的接口层。
来源：https://twitter.com/osanseviero/status/2002747011230269893

---

### 6. 研究显示生产级智能体项目普遍混合使用多个框架
> 一项针对1,575个智能体项目的实证研究显示，96%的高星项目混合使用了多个框架（如LangChain+LlamaIndex），GitHub星数并不能预测实际采用率。主要痛点集中在逻辑失败、终止检测、智能体-工具交互和版本兼容性上。
来源：https://twitter.com/dair_ai/status/2003178236696776814

---

### 7. 强化学习安全应用：OpenAI利用RL加固浏览器智能体
> OpenAI描述了如何通过自动化红队测试、强化学习和快速缓解循环来加固其浏览器智能体（ChatGPT Atlas），以抵御提示注入攻击。这展示了RL作为一种持续的安全维护循环，而不仅仅是能力加速器。
来源：https://twitter.com/cryps1s/status/2003182649662140620

---

### 8. 机器人学习新趋势：视频-动作模型与仿真到现实的挑战
> 研究界引入了“视频-动作模型”用于机器人学习，旨在更紧密地耦合感知主干网络和动作策略。同时，John Carmack指出，即使在理论上相同的3D打印机器人之间转移策略也会导致性能损失，凸显了仿真到现实以及机器人间策略转移的困难。
来源：https://twitter.com/elvisnavah/status/2003088362119512560

---

### 9. Vercel AI SDK 6发布，全面支持智能体与MCP
> Vercel发布了AI SDK 6，新增了对本地智能体的支持、工具执行审批、完整的模型上下文协议集成、增强的开发者工具以及标准化的JSON模式工具。这为前端团队提供了一个开箱即用的多模型、工具调用应用开发栈。
来源：https://twitter.com/aisdk/status/2003156089177792827

---

### 10. 关于AI“通用性”与“幻觉”的业界辩论升温
> DeepMind CEO Demis Hassabis反驳了Yann LeCun关于通用智能是“幻觉”的观点，认为他混淆了通用智能与万能智能。与此同时，社区内关于LLM“幻觉”或“精神病”的讨论激增，尤其是在数学证明领域，突显了流畅输出带来的验证危机。
来源：https://twitter.com/Yuchenj_UW/status/2002803245354459588

---

## 🛠️ 十大工具产品要点

### 1. GLM-4.7模型权重与量化版本发布
> GLM-4.7模型权重已在Hugging Face上发布。社区迅速推出了多种量化版本，包括适用于苹果芯片的MLX 3比特和4比特量化版本，方便开发者在不同硬件上部署。
来源：https://huggingface.co/zai-org/GLM-4.7

---

### 2. 超快TTS模型Soprano-80M发布
> Soprano-80M是一个开源的文本转语音模型，声称能以低于15毫秒的延迟流式传输音频，生成10小时的有声书仅需不到20秒（约2000倍实时速度）。它采用32kHz采样率和新颖的神经音频编解码器，但尚不支持语音克隆和多语言。
来源：https://github.com/ekwek1/soprano

---

### 3. vLLM为MiMo-V2-Flash提供官方服务配置
> vLLM项目为小米的MiMo-V2-Flash模型发布了官方的服务配置方案，提供了针对上下文长度、延迟、KV缓存以及数据/张量/流水线并行的具体优化参数。
来源：https://twitter.com/vllm_project/status/2002938138549682366

---

### 4. 运动控制与长视频生成模型取得进展
> Kling 2.6的运动控制功能受到关注，用户展示了其用于舞蹈/动作控制的能力。研究方面，MemFlow提出了用于生成长篇叙事视频的自适应记忆检索方法。
来源：https://twitter.com/fal/status/2003103565309415665

---

### 5. LangChain推出支持持久化存储的智能体中心
> LangChain与Oracle合作推出了一个智能体中心，提供持久化存储并总结了“六种记忆模式”，反映了生产级智能体对状态、回忆和可审计性的需求日益增长。
来源：https://twitter.com/LangChainAI/status/2002771047234613550

---

### 6. 开源RL框架OpenTinker旨在降低使用门槛
> OpenTinker被定位为一个解耦的客户端/服务器RL框架，允许用户在GPU集群上配置一次后端，在本地定义环境并进行远程训练，旨在将RL流程设置时间减少约10倍。
来源：https://twitter.com/youjiaxuan/status/2002838551319253281

---

### 7. 高性能注意力推理库QSInference发布
> QSInference是一个用于长上下文LLM的量化稀疏注意力Triton实现，声称在128k上下文长度下比FlashAttention-2快8倍，比块稀疏注意力快3倍，专注于解决注意力计算占主导的长序列推理问题。
来源：https://github.com/yogeshsinghrbt/QSInference

---

### 8. Hugging Face `smolagents`框架新增代码执行沙盒
> Hugging Face的`smolagents`框架通过PR #1912新增了CustomCodeAgent，支持通过本地Docker或远程工作空间对代码执行智能体进行沙盒隔离，增强了安全性。
来源：https://github.com/huggingface/smolagents/pull/1912

---

### 9. OpenRouter SDK支持基于复杂度的模型选择
> OpenRouter的SDK新增了上下文/工作流管理功能，并支持“基于复杂度的模型选择”，允许SDK根据工具输出在流程中动态切换模型ID，以实现成本与性能的优化。
来源：https://openrouter.ai/docs/sdks/call-model/next-turn-params#complexity-based-model-selection

---

### 10. Reachy Mini机器人平台获开发者青睐
> Reachy Mini机器人因其快速设置、精美的用户体验（手册+应用+SDK）而受到开发者社区欢迎，被用作构建本地助理的“假日机器人平台”，其代码仓库趋势走高。
来源：https://twitter.com/Prince_Canuma/status/2002695729442402496

---