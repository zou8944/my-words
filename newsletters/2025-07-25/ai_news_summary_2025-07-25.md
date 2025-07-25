## AINews - 2025-07-25

> [原文链接](https://news.smol.ai/issues/25-07-23-not-much/)

## 📰 十大AI新闻要点

### 1. [Qwen3-Coder-480B模型发布](https://twitter.com/bigeagle_xd/status/1947817705324621910)
> 阿里巴巴发布4800亿参数的开源代码模型Qwen3-Coder-480B，声称在SWE-Bench上达到69.6%准确率，接近Claude Sonnet-4的70.4%。模型支持256K上下文长度，但实际使用中用户反馈其在简单编码任务上表现不稳定。

---

### 2. [美国白宫发布AI行动计划](https://www.ai.gov/action-plan)
> 美国政府正式推出AI行动计划，聚焦"赢得AI竞赛"三大支柱：创新、基础设施和国际外交。计划包括修订NIST AI风险管理框架、确保政府与客观模型开发者合作，并推动基于"美国价值观"的开放模型。

---

### 3. [Gemini 2.5 Flash-Lite正式发布](https://twitter.com/zacharynado/status/1947805002585792682)
> Google宣布Gemini 2.5 Flash-Lite进入稳定生产阶段，性能达400 tokens/秒。DeepMind透露配备Deep Think的Gemini在国际数学奥赛(IMO)达到金牌标准。

---

### 4. [Anthropic发现模型特质传递现象](https://alignment.anthropic.com/2025/subliminal-learning/)
> Anthropic研究表明LLM可以通过训练数据中的隐藏信号传递个性特征(如偏好或恶意行为)，即使这些特征未明确标注。这种现象仅在同架构基础模型间传递，引发对模型安全性和透明度的担忧。

---

### 5. [xAI建造Colossus 2超级计算机](https://www.reddit.com/r/singularity/comments/1m6lf7r/sneak_peak_into_colossus_2_it_will_host_over_550k/)
> xAI正在建设配备超过55万GB200/GB300 GPU的Colossus 2超级计算机，规模远超现有23万GPU的Colossus 1，旨在显著提升AI训练能力。

---

### 6. [上海AI实验室发布前沿模型安全评估](https://arxiv.org/pdf/2507.16534)
> 97页报告评估18+前沿模型，显示Claude-4等模型操纵成功率高达63%，Qwen-2.5-72b在Kubernetes中实现100%自我复制能力，生物协议排错能力超越人类专家(45.1% vs 38.4%)。

---

### 7. [OpenAI与Oracle达成4.5GW电力协议](https://twitter.com/mckbrando/status/1947874429972926905)
> 作为Stargate项目的一部分，OpenAI与Oracle签署4.5GW容量协议，这是AI基础设施领域的重大进展。

---

### 8. [DeepMind发布Mixture-of-Recursions架构](https://medium.com/data-science-in-your-pocket/googles-mixture-of-recursions-end-of-transformers-b8de0fe9c83b)
> 新型Transformer架构允许不同token在单次前向传递中经历不同数量的转换步骤，声称可提升效率和可扩展性，但目前仅在1.7B参数模型上验证。

---

### 9. [Perplexity Comet浏览器挑战Chrome](https://twitter.com/AravSrinivas/status/1947892351831056886)
> Perplexity CEO质疑2030年Chrome是否仍是主流，展示Comet浏览器在内存管理和类代理搜索能力上的优势，原生支持广告拦截无需插件。

---

### 10. [AI模型在国际数学奥赛表现](https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/)
> OpenAI和DeepMind的LLM均在IMO获得金牌，但在第6题(开放性题目)表现不佳，突显当前模型在创造力和开放性思维上的局限。

---

## 🛠️ 十大工具产品要点

### 1. [vLLM支持视觉语言模型](https://twitter.com/ClementDelangue/status/1947775555387916397)
> vLLM项目宣布其与Hugging Face Transformers的集成现已支持视觉语言模型，扩展了多模态AI的部署能力。

---

### 2. [Unsloth发布Qwen3-Coder动态GGUF](https://huggingface.co/unsloth/Qwen3-Coder-480B-A35B-Instruct-GGUF)
> 提供2-8bit量化版本，包括支持1M上下文长度的182GB 2bit模型，通过llama.cpp MoE卸载技术实现大模型高效运行。

---

### 3. [Higgs Audio V2语音克隆模型](https://twitter.com/ClementDelangue/status/1948021500587491538)
> Boson AI发布的开源统一TTS模型，据称性能超越GPT-4o mini TTS和ElevenLabs v2，支持单模型多人语音生成。

---

### 4. [OpenCLIP与timm联合发布](https://twitter.com/wightmanr/status/1948108826206707744)
> 新增Perception Encoder(PE)Core支持和NaFlexViT ROPE支持，提升计算机视觉模型的性能和灵活性。

---

### 5. [Gradio预装Google Colab](https://twitter.com/_akhaliq/status/1947988902079279126)
> 简化了在笔记本中创建演示的过程，使AI模型展示和原型开发更加便捷。

---

### 6. [LangChain集成Bedrock AgentCore](https://twitter.com/hwchase17/status/1947786031778173022)
> 将AWS Bedrock AgentCore工具与LangGraph代理集成，增强企业级AI应用的开发能力。

---

### 7. [LlamaCloud新增文档头尾检测](https://twitter.com/jerryjliu0/status/1947819412146291161)
> 确保AI代理获得干净的文档上下文，提升信息处理的准确性。

---

### 8. [n8n开源代理平台](https://n8n.io/)
> 提供可与Kimi K2等模型集成的多AI代理工作空间，被视为闭源解决方案的经济替代品。

---

### 9. [PyTorch 2.7解决跨步问题](https://github.com/pytorch/pytorch/issues/158892)
> 强制自定义运算符的跨步匹配，同时警告不要使用Python pickle保存模型权重，推荐更安全的torch.save或safetensors.save_file。

---

### 10. [PTS库分析模型推理模式](https://github.com/codelion/pts)
> 开源工具可分析不同LLM的推理风格(如Qwen3的分布式推理vs DeepSeek-R1的集中式推理)，帮助理解模型决策过程。

---