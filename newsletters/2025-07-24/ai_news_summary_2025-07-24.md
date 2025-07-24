## AINews - 2025-07-24

> [原文链接](https://news.smol.ai/issues/25-07-22-not-much/)

## 📰 十大AI新闻要点

### 1. [Kimi K2 技术报告发布，声称在代理任务上达到SOTA](https://twitter.com/Kimi_Moonshot/status/1947520758760313170)
> Moonshot AI发布了Kimi K2的技术报告，这是一个1万亿参数的超稀疏混合专家(MoE)模型。报告详细介绍了用于稳定训练的MuonClip优化器、使用超过20,000个工具的大规模代理数据合成管道，以及联合RL对齐方法。该模型被描述为类似DeepSeekV3风格的MoE，但具有更高的稀疏性，并且是开源的。

---

### 2. [Qwen3-235B-A22B挑战Kimi K2，夺回基准榜首](https://twitter.com/huybery/status/1947345040470380614)
> 阿里巴巴更新了Qwen3模型，Qwen3-235B-A22B变体重新夺回基准榜首。该模型比Kimi 2小4.25倍(235B vs 1T参数)，但具有更多层并使用GQA而非MLA。据报道，它在GPQA、AIME和LiveCodeBench等基准上击败了Kimi-K2、Claude-4 Opus和DeepSeek V3。

---

### 3. [Qwen3-Coder-480B-A35B发布，专为高级代码生成设计](https://twitter.com/scaling01/status/1947732150872084693)
> 阿里巴巴发布了Qwen3-Coder，这是一个总参数480B、活跃参数35B的MoE模型，专为编码和代理任务设计。该模型具有100万token的上下文窗口，在SWE-bench上表现出色。架构上比基础Qwen3更宽更浅，有62层、6144隐藏维度和160个专家。

---

### 4. [Google推出Gemini 2.5 Flash-Lite](https://twitter.com/Google/status/1947689382892204542)
> Google宣布稳定发布Gemini 2.5 Flash-Lite，这是其2.5系列中最具成本效益和最快的模型。Google DeepMind表示它比2.0 Flash模型更快、更具成本效益，同时在编码、数学和多模态理解方面表现更好。

---

### 5. [Google DeepMind的Gemini正式获得IMO金牌](https://twitter.com/AndrewLampinen/status/1947370582393425931)
> Demis Hassabis宣布，Gemini Deep Think的高级版本在国际数学奥林匹克(IMO)中获得了金牌级别的分数(35/42)，这是AI模型的首次。

---

### 6. [OpenAI宣布与Oracle合作建设"Stargate"5GW数据中心](https://twitter.com/OpenAI/status/1947628731142648113)
> OpenAI宣布正在与Oracle合作开发额外的4.5千兆瓦"Stargate"数据中心容量，使总容量超过5GW。位于德克萨斯州Abilene的Stargate I站点已开始上线。

---

### 7. [Perplexity Comet浏览器获得关注](https://twitter.com/AravSrinivas/status/1947407684996894969)
> Perplexity AI的新浏览器Comet的等待名单自推出以来翻了一番。早期用户反馈表明它使传统聊天界面"感觉过时"。CEO关于是否想要一个代理来处理会议的推文获得了超过3,300次印象，显示出对其代理能力的强烈兴趣。

---

### 8. [LangChain 1.0即将发布](https://twitter.com/hwchase17/status/1947376920355917909)
> Harrison Chase宣布团队正在努力推出langchain 1.0，将专注于成为构建LLM应用的最简单起点，提供改进的文档和基于LangGraph构建的通用代理架构。LangGraph被描述为较低级别的"代理运行时"，而LangChain将提供更高级别的抽象。

---

### 9. [xAI的Colossus超级集群扩展](https://x.com/elonmusk/status/1947701807389515912)
> Elon Musk透露，Colossus 2将托管超过550,000个NVIDIA GB200和GB300 GPU。Colossus 1目前运行230,000个GPU(包括30,000个GB200)用于xAI的Grok模型训练。Musk声称，根据Jensen Huang的说法，xAI的速度"无与伦比"。

---

### 10. [AMD推出Strix Halo"Ryzen AI MAX"APU](https://wccftech.com/amd-strix-halo-ryzen-ai-max-apus-diy-pc-new-modt-mini-itx-motherboards-128-gb-lpddr5x-memory/)
> AMD的Strix Halo"Ryzen AI MAX"APU通过新的MoDT Mini-ITX主板提供给DIY PC制造商，支持高达128GB的LPDDR5X内存。这些主板针对紧凑型AI/ML和边缘计算应用，但缺乏标准PCIe扩展插槽。

---

## 🛠️ 十大工具产品要点

### 1. [Qwen3-Coder-480B-A35B-Instruct](https://app.hyperbolic.ai/models/qwen3-coder-480b-a35b-instruct)
> 阿里巴巴发布的480B参数MoE模型，专为编码设计，具有100万token上下文窗口，已在Hyperbolic AI平台上线。

---

### 2. [MegaTTS 3语音克隆](https://huggingface.co/spaces/mrfakename/MegaTTS3-Voice-Cloning)
> ByteDance的MegaTTS 3的WavVAE编码器已发布，支持多样化的口音和音色，在Hugging Face上提供模型和演示。

---

### 3. [vLLM与Hugging Face Transformers集成](https://twitter.com/vllm_project/status/1947756551663718754)
> vLLM项目宣布支持开箱即用的视觉语言模型与Transformers集成，简化了多模态模型的部署和推理。

---

### 4. [LlamaIndex开源RFP响应代理](https://twitter.com/jerryjliu0/status/1947465066892431792)
> LlamaIndex构建了一个完全开源的代理，用于自动化请求提案(RFP)响应，处理文档提取、分析和报告生成。

---

### 5. [Perplexity Comet浏览器](https://www.perplexity.ai/)
> Perplexity AI的新浏览器，具有代理能力，等待名单自推出以来翻了一番，早期用户反馈积极。

---

### 6. [LangChain 1.0](https://twitter.com/hwchase17/status/1947376920355917909)
> 即将发布的LangChain 1.0将专注于成为构建LLM应用的最简单起点，提供改进的文档和基于LangGraph构建的通用代理架构。

---

### 7. [Anthropic增强移动端Artifacts](https://twitter.com/AnthropicAI/status/1947690894888513964)
> Anthropic推出了与移动端Artifacts互动的新方式，允许用户创建交互式工具、浏览画廊并直接从手机分享作品。

---

### 8. [OpenAI临床副驾驶在肯尼亚](https://twitter.com/gdb/status/1947732134430687351)
> OpenAI与肯尼亚的PendaHealth合作，研究了一个OpenAI驱动的临床副驾驶在40,000次患者就诊中的表现。

---

### 9. [ik_llama.cpp仓库恢复](https://github.com/ikawrakow/ik_llama.cpp)
> 提供Llama模型C++推理代码的ik_llama.cpp仓库在GitHub上恢复，强调了定期备份关键仓库的重要性。

---

### 10. [AMD Strix Halo"Ryzen AI MAX"APU](https://wccftech.com/amd-strix-halo-ryzen-ai-max-apus-diy-pc-new-modt-mini-itx-motherboards-128-gb-lpddr5x-memory/)
> AMD的Strix Halo"Ryzen AI MAX"APU通过新的MoDT Mini-ITX主板提供给DIY PC制造商，支持高达128GB的LPDDR5X内存，针对紧凑型AI/ML和边缘计算应用。