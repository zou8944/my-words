## AINews - 2025-08-27

> [原文链接](https://news.smol.ai/issues/25-08-25-not-much/)

## 📰 十大AI新闻要点

### 1. [xAI发布Grok-2/2.5开源权重](https://huggingface.co/xai-org/grok-2)
> xAI在Hugging Face上发布了Grok-2和Grok-2.5的开源权重，文件约500GB。模型配置显示使用了μP缩放和独特的"MoE残差"路径，类似共享专家机制。Elon Musk声称Grok 3将在约6个月内开源，并表示2.5是他们去年最好的模型。

---

### 2. [微软开源VibeVoice-1.5B长文本TTS模型](https://huggingface.co/microsoft/VibeVoice-1.5B)
> 微软开源了MIT许可的VibeVoice-1.5B，支持多说话人对话和长达90分钟的连续合成，具有流式支持功能，7B变体即将推出。模型已在Gradio和社区仓库中提供演示和Spaces。

---

### 3. [Motif-2.6B发布详细技术报告](https://twitter.com/eliebakouch/status/1959598428192669870)
> Motif Technology发布了在2.5T tokens上训练的Motif-2.6B技术报告，采用差分注意力和PolyNorm技术，使用简单移动平均集成（最后6个检查点）和精细数据策划。还发布了与FSDP2/HF堆栈兼容的Muon优化器和PolyNorm内核。

---

### 4. [GPT-5在编码工作流中展现强劲表现](https://twitter.com/gdb/status/1959209931267297586)
> 开发者报告GPT-5在代码生成、API设计反馈和错误排查方面表现优异，导致某些任务中Claude Code被降级使用。GPT-5支持的代码工具链正在成为AI编码工作流的重心。

---

### 5. [阿里巴巴Qwen-Code v0.0.8发布深度VS Code集成](https://twitter.com/Alibaba_Qwen/status/1959170659583476026)
> Qwen-Code v0.0.8新增深度VS Code支持，包括上下文感知建议、内联差异、强大的MCP CLI、响应式TUI、反向搜索、上下文压缩控制和多目录自动加载等功能。

---

### 6. [MCP生态系统加速发展](https://twitter.com/omarsar0/status/1960084088133398718)
> MCP生态系统快速发展，包括LiveMCP-101压力测试、"Rube"通用MCP服务器连接数百个应用，以及LangGraph Platform推出回滚和修订队列功能，并与ART集成通过RL训练LangGraph代理。

---

### 7. [DSPy GEPA优化器在v3.0中发布](https://twitter.com/DSPyOSS/status/1960000178179527110)
> DSPy的GEPA优化器在v3.0版本中发布，在各种用例中取得强劲结果，如在500次度量调用中获得40%增益，并提供列表重排序教程。

---

### 8. [TPU与GPU系统架构对比分析](https://twitter.com/JingyuanLiu123/status/1959093411283443726)
> 工程师分析指出TPU v3/v4 pod提供接近NVLink级别的带宽，在2D环面上实现清晰扩展，减轻了并行压力，减少了对PP的需求，特别是在K2/DeepSeek规模下。

---

### 9. [OpenRouter吞吐量爆炸式增长](https://twitter.com/scaling01/status/1960113882607067569)
> OpenRouter的吞吐量在一年内从约111B tokens/周增长到3.21T tokens/周，显示出平台使用的显著增长。

---

### 10. [Google Veo-3免费周末活动](https://twitter.com/sundarpichai/status/1959070813317210260)
> Google在Gemini中举办了Veo-3开放周末活动，扩展了生成限制（免费用户6次，Pro用户6次/天，Ultra用户10次/天），并提供提示技巧。

---

## 🛠️ 十大工具产品要点

### 1. [InternVL3.5开源多模态模型发布](https://huggingface.co/internlm/InternVL3_5-241B-A28B)
> InternVL3.5系列发布，包括241B-A28B检查点，在开源VLMs中实现最先进的聚合分数，扩展了多模态"代理"功能，如GUI和具身代理，并发布多个检查点包括小型变体。

---

### 2. [阿里巴巴WAN 2.2-S2V音频驱动视频生成系统](https://twitter.com/Alibaba_Wan/status/1959963989703880866)
> 阿里巴巴WAN团队预告WAN 2.2-S2V，一个开源的音频驱动电影视频生成系统，支持从声音/语音直接生成视频，即将发布。

---

### 3. [GTPO优化器改进GRPO训练稳定性](https://github.com/winstonsmith1897/GTPO)
> GTPO（基于组相对轨迹的策略优化）作为GRPO的修改版本，避免梯度冲突和政策崩溃，跳过"冲突token"的负更新，并在无参考模型的情况下实现更稳定的训练。

---

### 4. [llama.ui隐私聚焦聊天界面](来源：文章内容)
> llama.ui是一个极简、隐私聚焦的聊天客户端，专为本地/自托管LLM工作流设计，提供稀疏聊天窗格、预设快速操作和最近对话侧边栏，强调简单性和隐私。

---

### 5. [Google AI Studio即将更新](https://aistudio.google.com/)
> Google AI Studio预告本周将有重大更新，可能包括多个功能/产品推出，而非核心模型发布，开发者提示关注AI Studio频道。

---

### 6. [Microsoft Copilot Excel功能发布](https://www.microsoft.com/microsoft-copilot)
> Microsoft推出Excel中的Copilot功能，支持生成公式、总结表格和运行自然语言分析，但警告不要用于需要准确性或可重复性的任务。

---

### 7. [Perplexity iOS应用重新设计](https://twitter.com/AravSrinivas/status/1959317364228641130)
> Perplexity发布重新设计的iOS应用，支持手势导航、即将集成的SuperMemory和出色的语音听写UX，获得广泛好评。

---

### 8. [Genspark浏览器IDE发布](https://twitter.com/fchollet/status/1959083315878928808)
> Genspark推出浏览器IDE，支持"描述→迭代"编码和多模型后端，强调为非专家提供低门槛工具。

---

### 9. [vLLM分布式推理和采样控制改进](https://twitter.com/vllm_project/status/1959277423729500565)
> vLLM推出新的采样控制PR，支持最先进的推理评估，并在上海Meetup中深入探讨分布式推理、ERNIE集成、缓存和硬件支持。

---

### 10. [Mac MLX本地大模型实验](https://twitter.com/TheZachMueller/status/1959643512695054638)
> 通过TB4上的RAID0在Mac MLX上加载Qwen3-480B，TTFT约25-46秒，提供详细的构建说明和性能数据，支持本地大模型实验。

---