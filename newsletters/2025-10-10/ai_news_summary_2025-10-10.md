## AINews - 2025-10-10

> [原文链接](https://news.smol.ai/issues/25-10-08-not-much/)

## 📰 十大AI新闻要点

### 1. [三星发布7M参数递归推理模型TRM](https://arxiv.org/abs/2510.04871)
> 三星研发的7M参数Tiny Recursive Model在ARC-AGI和数独任务上击败了27M参数的HRM，采用单网络设计和全递归反向传播。研究发现减少层数能改善泛化能力（4层→2层：数独准确率从79.5%提升至87.4%），在固定长度上下文中用MLP替换自注意力机制效果更好。

---

### 2. [JEPA-SCORE将编码器转化为密度估计器](https://arxiv.org/abs/2510.05949)
> LeCun团队证明JEPA的抗坍缩项隐式估计数据密度。从任何训练好的JEPA（I-JEPA、DINOv2、MetaCLIP）中，通过雅可比矩阵以闭式形式计算p(x)，可用于数据筛选、异常检测等，无需重新训练。

---

### 3. [AI21发布Apache-2.0许可的Jamba Reasoning 3B模型](https://huggingface.co/ai21labs/AI21-Jamba-Reasoning-3B)
> 混合SSM-Transformer模型在长上下文任务中达到速度/准确率最佳平衡，比Llama 3.2 3B和Qwen3 4B快3-5倍（32K tokens），在iPhone 16 Pro上16K上下文达到约16 tok/s，支持最高64K上下文。

---

### 4. [阿里巴巴发布Qwen3 Omni/Omni Realtime多模态模型](https://twitter.com/ArtificialAnlys/status/1975904190061834602)
> 原生统一音频-视频-文本架构，采用"Thinker"和"Talker"混合专家系统，支持119种文本语言、19种语音输入、10种语音输出。在BigBench Audio上达到58-59%，优于Gemini 2.0 Flash的36%。

---

### 5. [CoreWeave × W&B × OpenPipe推出无服务器强化学习平台](https://twitter.com/weights_biases/status/1975996733269344571)
> 训练智能体更快更便宜且无需基础设施管理。声称比自管理GPU便宜40%，时钟时间快28%，可通过W&B Inference即时部署到生产环境，包含ART训练器和RULER通用验证器。

---

### 6. [斯坦福AgentFlow实现流程内RL用于工具使用和规划](https://twitter.com/lupantech/status/1976016000345919803)
> 由规划器/执行器/验证器/生成器组成的多智能体系统，使用Flow-GRPO在系统内部训练规划器。在10个基准测试中，7B骨干模型在多个类别上击败Llama-3.1-405B和GPT-4o。

---

### 7. [Python 3.14无GIL解释器结束实验阶段](https://twitter.com/charliermarsh/status/1975913762344608129)
> 无全局解释器锁的Python解释器正式结束实验阶段，为多核Python编程带来重大突破，Pydantic 2.12同日发布支持3.14版本。

---

### 8. [Base Power完成10亿美元C轮融资建设电网级电池](https://twitter.com/ZachBDell/status/1975911656698810539)
> 在奥斯汀扩大制造规模，目标为每个家庭配备电池，打造"美国下一代电力公司"，多家顶级投资机构参与。

---

### 9. [Relace获2300万美元a16z投资构建AI代码生成基础设施](https://twitter.com/steph_palazzolo/status/1975934528125554769)
> 在OpenRouter上提供最快的应用模型（10k tok/s），拥有最先进的代码重排序和嵌入技术，正在开发Relace Repos检索原生SCM。

---

### 10. [DeepSeek研究员因公司对华立场离职加入Google DeepMind](https://twitter.com/Yuchenj_UW/status/1975969899102208103)
> 研究员Shunyu Yao因不同意Anthropic将中国列为"敌对国"的公开立场而离职，反映了地缘政治对前沿AI人才招聘的影响。

---

## 🛠️ 十大工具产品要点

### 1. [Google AI Studio新增语音"氛围编程"功能](https://twitter.com/GoogleAIStudio/status/1975946197715320833)
> 通过语音口述应用更改或功能，语音转文本自动清理填充词以获得更清晰的提示，支持更自然的开发交互方式。

---

### 2. [Stripe为AI开发者推出新API](https://twitter.com/emilygsands/status/1975951436006699147)
> 跟踪模型定价变化保护利润，包含智能商务协议和共享支付代币，以及"Gemini内嵌Stripe"商务流程集成。

---

### 3. [Sora 2快速集成和公开演示](https://twitter.com/_akhaliq/status/1976096764781646028)
> Hugging Face提供限时免费文本转视频演示，Sora应用在5天内达到100万下载量，Runway Gen-4 Turbo通过API支持任意2-10秒时长。

---

### 4. [ColBERT Nano微型检索模型](https://twitter.com/neumll/status/1975923919614800347)
> 25万-95万参数的微型检索模型显示后期交互在极小规模下效果惊人，为资源受限环境提供高效检索方案。

---

### 5. [BigCodeArena引入可执行代码评估](https://twitter.com/BigCodeProject/status/1975971050589704358)
> 在可运行代码上进行人工循环评估（而非仅文本偏好数据），跨多种语言开放更可靠的代码生成评估大门。

---

### 6. [Helion高级内核DSL即将发布](https://pytorchconference.sched.com/event/27QDl/helion-a-high-level-dsl-for-kernel-authoring-jason-ansel-meta)
> 在PyTorch大会上发布beta版高级内核DSL，编译到Triton，展示积极的自动调优，探索归约循环、索引变体和驱逐策略。

---

### 7. [人工海马网络压缩长上下文记忆](https://github.com/ByteDance-Seed/AHN)
> 将无损记忆转换为固定大小压缩表示，用于长上下文预测，混合滑动窗口外的无损和压缩记忆，提供可扩展内存的实用方案。

---

### 8. [Self-MCP使Claude实现20万token单轮思考](https://github.com/yannbam/self-mcp)
> 允许Claude在思考/工具调用循环中自我提示，有效实现单轮20万token思考，无需微调即可实现长视野推理。

---

### 9. [HyDRA v0.2混合动态RAG代理](https://github.com/hassenhamdi/HyDRA)
> 多智能体、反射驱动的混合动态RAG堆栈，包含规划器/协调器/执行器，使用3阶段本地检索流程，集成Gemini 2.5 Flash作为推理核心。

---

### 10. [Perplexity推出搜索API](https://www.perplexity.ai/api-platform)
> 在Perplexity AI API平台上推出新的搜索API，为应用开发者开放其检索堆栈的程序化访问，支持将检索集成到智能体和后端中。

---