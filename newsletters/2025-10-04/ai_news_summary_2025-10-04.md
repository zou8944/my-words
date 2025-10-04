## AINews - 2025-10-04

> [原文链接](https://news.smol.ai/issues/25-10-02-not-much/)

## 📰 十大AI新闻要点

### 1. [Kling 2.5 Turbo登顶视频生成排行榜](https://twitter.com/ArtificialAnlys/status/1973570493753204953)
> Kling 2.5 Turbo在Artificial Analysis视频竞技场中同时领跑文生视频和图生视频，击败了海螺02 Pro、Google Veo 3和Luma Ray 3，生成5-10秒1080p视频，FAL API定价约4.20美元/分钟，比竞品更具价格优势

---

### 2. [OpenAI Sora 2展示强大指令跟随能力但存在物理不一致问题](https://twitter.com/altryne/status/1973568567489798144)
> Sora 2在实际使用中展现出令人印象深刻的指令跟随和混音能力，但评测发现存在物理不一致性和过度营销问题，在特定物理场景测试中表现不如Veo 3

---

### 3. [Google Gemini 2.5 Flash图像模型正式发布](https://twitter.com/sundarpichai/status/1973788714758517147)
> Gemini 2.5 Flash图像模型（代号"Nano Banana"）正式发布，支持10种宽高比、多图像融合和纯图像输出，定价为每张图像0.039美元，已集成到合作伙伴产品中

---

### 4. [IBM Granite 4.0开源混合架构模型发布](https://www.ibm.com/new/announcements/ibm-granite-4-0-hyper-efficient-high-performance-hybrid-models)
> IBM发布Granite 4.0系列模型，采用Mamba/Transformer混合架构，在减少内存使用的同时保持准确性，包含32B/9B、7B/1B、3B/3B等规格，128K上下文，Apache 2.0许可

---

### 5. [Claude Sonnet 4.5在LM Arena登顶](https://twitter.com/arena/status/1973828836510085385)
> Claude Sonnet 4.5在LM Arena文本排行榜上与Claude Opus 4.1并列第一，在编程和创意写作等类别表现强劲，基于数万人类投票排名

---

### 6. [开源代码编辑代理接近闭源模型性能](https://twitter.com/cline/status/1973870619013136850)
> 在Cline的diff-edit测试中，GLM-4.6达到94.9%成功率，接近Claude 4.5的96.2%，但成本仅为后者的约10%，用户开始相应调整工作流程

---

### 7. [Tinker推出灵活微调API支持LoRA共享](https://twitter.com/Smol_AI/status/1973622595124863044)
> Thinking Machines的Tinker API允许编写CPU训练循环并在分布式GPU上运行，支持包括大型MoE模型在内的开源模型，实现高效的LoRA资源共享

---

### 8. [rank-1 LoRA在推理任务中媲美全微调](https://twitter.com/zzlccc/status/1973612326747336767)
> 多项复制研究表明rank-1 LoRA在推理任务中可匹配全微调质量，同时节省约43% VRAM，支持在更大模型上进行强化学习

---

### 9. [DeepSearch将MCTS引入训练循环](https://twitter.com/omarsar0/status/1973781658772951320)
> DeepSearch通过Tree-GRPO稳定化和高效缓存/过滤将蒙特卡洛树搜索移入训练循环，在AIME/AMC上达到62.95%，仅用约330 GPU小时

---

### 10. [Perplexity Comet全球正式发布](https://twitter.com/perplexity_ai/status/1973795224960032857)
> Perplexity的Comet AI浏览器全球正式发布，Comet Plus同步推出并与主要出版商建立合作关系，Pro/Max用户将捆绑获得Plus功能

---

## 🛠️ 十大工具产品要点

### 1. [Kling 2.5 Turbo视频生成工具](https://twitter.com/Kling_ai/status/1973581864679121374)
> 支持文本到视频和图像到视频生成，可生成5-10秒1080p视频，通过应用积分约0.15美元/视频，在价格和性能上具有竞争优势

---

### 2. [IBM Granite 4.0模型生态系统](https://huggingface.co/collections/ibm-granite/granite-40-language-models-6811a18b820ef362d9e5a82c3)
> 模型已在HuggingFace、Replicate、Ollama等平台部署，H Small定价为每100万输入/输出token 0.06/0.25美元，支持GGUF格式和Unsloth微调

---

### 3. [Tinker微调API](https://twitter.com/TheTuringPost/status/1973827605448306883)
> 提供灵活的微调服务，支持分布式GPU训练，保持算法/损失控制，同时管理调度、资源分配和故障处理，支持大型MoE模型

---

### 4. [Unsloth训练栈更新](https://docs.unsloth.ai/new/how-to-train-llms-with-unsloth-and-docker)
> 发布跨平台Docker镜像，支持Windows/Linux无依赖训练，报告最快的gpt-oss RL循环，VLM RL速度提升2倍，VRAM使用减少90%

---

### 5. [Flash-MoE推理优化](https://flash-moe.github.io/)
> Thinking Machines发布Flash-MoE，Flash Attention的稀疏专家变体，结合非确定性LLM推理解决方案，提升MoE推理的可扩展性

---

### 6. [vLLM扩展支持BERT](https://twitter.com/vllm_project/status/1973805307878142297)
> vLLM推理引擎现在支持BERT模型，进一步扩展其模型支持范围，提升推理效率

---

### 7. [LlamaIndex SemTools基准测试](https://twitter.com/llama_index/status/1973783798044307741)
> 基于1000篇arXiv论文的基准测试显示，带有语义搜索的代理比仅使用CLI工具的代理在各种问题类型上产生更完整的答案

---

### 8. [Goodfire Scribe笔记本执行系统](https://twitter.com/GoodfireAI/status/1973789154174754877)
> 基于MCP的开源系统，使代理能够运行笔记本单元并接收Jupyter输出，分享"实验者代理"与"软件开发代理"的经验教训

---

### 9. [Jules Tools代理CLI](https://twitter.com/julesagent/status/1973812188977508755)
> Google的Jules Tools提供代理CLI，可通过npm安装，镜像浏览器功能，增强命令行AI能力

---

### 10. [OpenRouter性能标签](https://x.com/OpenRouterAI/status/1773733582763069916)
> 推出性能标签可视化提供商指标，引发关于量化级别过滤的讨论，需要FP4 vs BF16等精度设置进行公平比较

---