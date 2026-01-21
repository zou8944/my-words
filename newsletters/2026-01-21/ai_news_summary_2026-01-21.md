## AINews - 2026-01-21

> [原文链接](https://news.smol.ai/issues/26-01-19-not-much/)

## 📰 十大AI新闻要点

### 1. [卡内基梅隆大学与Meta提出STEM架构，无需MoE路由即可扩展Transformer参数记忆](https://twitter.com/TheTuringPost/status/2013011864880660495)
> 研究人员提出STEM（Scaling Transformers with Embedding Modules）架构，通过用静态的、基于token索引的嵌入查找替换约1/3的FFN上投影层，来扩展模型的参数记忆。这种方法避免了MoE动态路由带来的运行时开销和不稳定性，甚至可以实现CPU卸载和异步预取，将模型容量与每token的FLOPs及跨设备通信解耦。

---

### 2. [Sakana AI发布RePo模块，允许语言模型根据内容相关性重新排序位置结构](https://twitter.com/SakanaAILabs/status/2013046887746843001)
> RePo（Context Re-Positioning）是一个轻量级模块，使语言模型能够根据内容相关性重新组织位置结构，有效重塑注意力几何形状，将远处相关的信息“拉近”，将噪声“推远”。该方法旨在提高模型在嘈杂上下文、结构化数据和长程依赖关系上的鲁棒性。

---

### 3. [智谱AI发布GLM-4.7-Flash，定位为30B级别的高效本地编码/智能体模型](https://twitter.com/Zai_org/status/2013261304060866758)
> GLM-4.7-Flash是一个30B-A3B的MoE模型，专为高效部署设计，推荐用于编码、智能体应用、翻译、长上下文和创意写作。社区分析指出其架构转向MLA（Memory-Limited Attention），并采用了非常规的头维度和更高的头数，遵循了Qwen/DeepSeek的设计趋势。

---

### 4. [Anthropic发布“助手轴”研究，揭示开放权重模型在长对话中的人格漂移风险](https://twitter.com/AnthropicAI/status/2013356793477361991)
> Anthropic的研究发现，开放权重的模型在长对话中可能偏离“助手”人格。编码类上下文有助于稳定助手人格，而治疗/哲学类上下文会增加漂移风险。研究提出了人格构建与稳定方法，并指出激活值上限（activation capping）是一种缓解措施，同时提供了一个因人格漂移导致有害行为的警示案例。

---

### 5. [Google DeepMind在Gemini生产环境中部署激活探针，用于实时分类滥用风险](https://twitter.com/ArthurConmy/status/2013285602070770036)
> DeepMind描述了用于分类现实世界滥用风险的“新型激活探针架构”，并指出这些探针已为Gemini的实时部署提供了信息。研究人员强调，探针是一种构建安全分类器的“廉价”杠杆。

---

### 6. [DeepSeek发布Engram研究模块，为LLM引入可扩展的确定性O(1)查找记忆](https://github.com/deepseek-ai/Engram/blob/main/Engram_paper.pdf)
> Engram模块通过现代化的哈希N-gram嵌入实现确定性O(1)查找记忆，将早期层的模式重建从神经计算中卸载。这种方法允许将内存和计算作为独立的扩展轴进行解耦，在等参数量和等FLOPs设置下，在知识、推理、代码和数学任务上均显示出持续的性能提升。

---

### 7. [NVIDIA提出端到端测试时训练方法，允许模型在推理时实时更新权重](https://github.com/test-time-training/e2e)
> 该论文提出了一种新颖的端到端测试时训练方法，使模型能够通过将上下文窗口视为训练数据集，在推理过程中实时更新其权重。该方法涉及一个内循环（在上下文上执行小梯度下降以更新特定MLP层）和一个外循环（通过元学习优化模型的初始权重以适应性强）。对于128K上下文长度，其推理速度比完全注意力模型快2.7倍。

---

### 8. [Cursor AI CEO演示GPT-5.2智能体在一周内构建超过300万行代码的网页浏览器](https://x.com/i/status/2012825801381580880)
> Cursor AI CEO Michael Truell展示了数百个GPT-5.2智能体协调工作，在一周内从零开始构建了一个包含自定义渲染引擎和JavaScript VM的网页浏览器，代码量超过300万行。该项目虽非生产就绪，但展示了自主编码智能体生成复杂系统的潜力。

---

### 9. [美国国防部确认将在五角大楼系统内部署xAI的Grok AI](https://www.washingtonpost.com/business/2026/01/12/artificial-intelligence-pentagon-hegseth-musk/ec8b407a-f026-11f0-a4dc-effc74cb25af_story.html)
> 美国国防部计划本月开始在五角大楼系统内部署xAI的Grok AI，以支持军事和民事行动。该部署将达到“影响级别5”，能够安全处理受控非密信息，并整合到作战系统中用于情报分析和决策。系统将利用来自开源和社交数据的实时全球信号，计划扩展到300万用户。

---

### 10. [Google DeepMind CEO称中国AI模型仅落后美国“数月”](https://www.cnbc.com/amp/2026/01/16/google-deepmind-china-ai-demis-hassabis.html)
> Google DeepMind CEO Demis Hassabis在接受CNBC采访时表示，中国的AI模型仅落后美国和西方能力“数月时间”，尽管他们尚未展示出推动AI“超越前沿”的能力。这一观点挑战了中国在AI发展上显著落后的普遍看法。

---

## 🛠️ 十大工具产品要点

### 1. [MLX-LM、LM Studio、Ollama、vLLM等工具在发布当天即支持GLM-4.7-Flash](https://twitter.com/awnihannun/status/2013286079470645353)
> GLM-4.7-Flash模型发布后，迅速获得主流推理和部署工具的支持。mlx-lm 0.30.3版本支持该模型，在M5 32GB笔记本上报告了约43 tok/s的生成速度和~800 tok/s的预填充速度。LM Studio通过MLX为Apple Silicon Mac提供支持，Ollama在v0.14.3+预发布版本中集成，vLLM项目也宣布了“Day-0 support”的PR。

---

### 2. [微软开源VibeVoice，实现约300毫秒延迟的实时TTS](https://twitter.com/LiorOnAI/status/2013220214217879931)
> 微软开源了VibeVoice，这是一个实时文本转语音模型，声称首音频延迟约为300毫秒，支持流式文本输入、多说话人（最多4个）和长格式稳定性（长达90分钟）。它使用7.5 Hz的语义+声学标记，采用语言模型处理结构，扩散头处理声学细节，采用MIT许可证，目前为“仅限研究”。

---

### 3. [DSPy发布`dspy.RLM`模块，为长上下文/迭代处理提供新工具](https://twitter.com/isaacbmiller1/status/2013371005960401327)
> DSPy在v3.1.2版本中发布了`dspy.RLM`（递归语言模型）模块，旨在与现有Signatures即插即用。社区认为这为长上下文和迭代处理开启了新的实验可能性，无需将所有内容塞入单个上下文窗口。

---

### 4. [Vercel推出开源“技能”生态系统，作为智能体能力包管理器](https://xcancel.com/rauchg/status/2012345679721771474?s=46)
> Vercel宣布推出“技能”，这是一个用于智能体能力的开源生态系统/包管理器。安装流程类似于`npx skills i vercel-labs/agent-skills`。开发者认为这是标准化智能体工具集成的务实方法，避免了定制化的工具连接。

---

### 5. [华为/中国推理系统“2025旗舰作品”总结，聚焦端到端系统设计](https://twitter.com/ZhihuFrontier/status/2013127635589800172)
> 一份来自知乎贡献者的总结，详细列出了针对KV缓存容量墙、PD拆分/合并利用率、混合调度、缓存亲和性/负载均衡以及以KVCache为中心的智能体内存等一系列系统设计理念。核心观点是，重心正从孤立的内核转向端到端的服务等级目标与吞吐量系统设计。

---

### 6. [Fal平台推出多种按需视频生成模型](https://twitter.com/fal/status/2013292351192490257)
> Fal平台发布了多个“按需模型”，包括Wan 2.6 i2v Flash（最长15秒，可选音频）、Vidu Q2参考视频生成（支持多参考和面部参考），以及Flux.2 [klein]训练器和用于外绘/缩放/对象移除/背景移除的LoRA。

---

### 7. [Google推出FunctionGemma调优实验室，指导基于270M参数模型微调函数调用能力](https://twitter.com/osanseviero/status/2013241128934404301)
> Google推出了FunctionGemma调优实验室，这是一个指南和无代码演示，用于微调和导出围绕270M参数模型构建的函数调用模型，并提供了一个Hugging Face Space。

---

### 8. [Claude Cowork开源智能体框架，支持Claude Opus 4.5、Gemini 3 Pro、GPT-5.2](https://twitter.com/Saboo_Shubham_/status/2013090887736472047)
> Claude Cowork是一个开源的智能体框架，可与多个前沿模型协同工作。一个实际案例展示了如何将PDF转换为Markdown以减少幻觉并改进文档理解，该功能基于LlamaParse/semtools构建。

---

### 9. [StirrupJS：强调最小脚手架和强默认值的TypeScript智能体框架](https://twitter.com/ArtificialAnlys/status/2013294230052212792)
> StirrupJS是一个TypeScript智能体框架，强调最小化脚手架和强大的默认值（工具、MCP、浏览、沙箱），并支持多模态。

---

### 10. [WebGPU浏览器视觉演示“YOLO26”实现浏览器内实时姿态/检测](https://twitter.com/mervenoyann/status/2013224180813115626)
> “YOLO26”通过WebGPU在浏览器中实现了实时姿态估计和目标检测，Hugging Face上提供了一个模型和演示的集合。