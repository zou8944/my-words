## AINews - 2025-08-07

> [原文链接](https://news.smol.ai/issues/25-08-05-gpt-oss/)

## 📰 十大AI新闻要点

### 1. [OpenAI发布开源权重模型GPT-OSS](https://openai.com/open-models/)
> OpenAI首次自GPT-2后再次开源模型，包含120B和20B两个版本，采用MoE架构和Apache 2.0许可。120B模型性能接近o4-mini，可在单块H100 GPU运行；20B模型仅需16GB内存，适合消费级硬件部署。模型采用创新的Harmony对话格式并内置浏览器/Python执行等智能体能力。

---

### 2. [DeepMind发布Genie 3世界模型](https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/)
> Genie 3能根据文本提示生成可交互的实时模拟环境，保持长达1分钟的环境一致性记忆，支持720p渲染。相比前代，其像素生成能力提升4倍，交互时长延长10倍，被评价为"游戏引擎2.0"。

---

### 3. [Anthropic推出Claude Opus 4.1](https://www.anthropic.com/news/claude-opus-4.1)
> 专注智能体任务和现实世界编程的升级版本，已获Cursor等开发工具集成。官方暗示未来数周将有更大改进，性能表现超越前代编码基准。

---

### 4. [OpenAI发起50万美元红队挑战赛](https://twitter.com/OpenAI/status/1952818694054355349)
> 邀请研究者测试GPT-OSS模型安全性，重点关注生化核武等灾难性风险。METR评估机构参与方法论验证，但社区对模型存在91.4%幻觉率表示担忧。

---

### 5. [Kaggle推出游戏竞技场新基准](https://twitter.com/quocleix/status/1952595046613811555)
> 由Demis Hassabis宣布的AI游戏对战平台，首期聚焦国际象棋，为评估LLM在竞争环境中的策略能力提供新标准。

---

### 6. [Perplexity AI收购Invisible_HQ](https://twitter.com/AravSrinivas/status/1952803397410930807)
> 为增强智能体基础设施能力，Perplexity收购拥有分布式系统专长的团队。此前该公司曾强烈抗议Cloudflare封锁AI爬虫的政策。

---

### 7. [Reflection AI拟融资10亿美元](https://twitter.com/steph_palazzolo/status/1952555858761588892)
> 由DeepMind前研究人员创立的开源模型公司正进行巨额融资谈判，显示市场对开源AI的高度期待。

---

### 8. [KittenTTS发布超小型语音模型](https://github.com/KittenML/KittenTTS)
> 仅25MB大小的文本转语音模型，支持8种音色，可在树莓派等边缘设备运行。80M参数版本即将推出，未来计划扩展多语言支持。

---

### 9. [llama.cpp新增MoE卸载功能](https://github.com/ggml-org/llama.cpp/pull/15077)
> 通过`-n-cpu-moe`参数简化专家模型层卸载，在3x3090显卡配置下实现>45 token/s的GLM-4.5-Air模型推理速度。

---

### 10. [Midjourney创始人警告AI选举风险](https://twitter.com/DavidSHolz/status/1952541453491867792)
> David Holz表示2028年总统大选将面临AI生成内容的严峻挑战，当前社会尚未做好应对准备。同期ChatGPT周活用户已达7亿。

---

## 🛠️ 十大工具产品要点

### 1. [GPT-OSS Playground在线体验](https://gpt-oss.com/)
> OpenAI官方提供的模型测试平台，支持实时体验120B/20B参数版本，展示Harmony格式的多通道对话功能。

---

### 2. [Harmony对话格式开源](https://github.com/openai/harmony)
> 取代ChatML的新一代结构化对话协议，支持消息分通道处理，已集成至HuggingFace Transformers v4.55.0。

---

### 3. [vLLM支持GPT-OSS推理](https://twitter.com/vllm_project/status/1952784530466849091)
> 高性能推理框架首日适配GPT-OSS，提供生产级部署方案，支持动态批处理和连续批处理优化。

---

### 4. [Ollama联合NVIDIA优化本地运行](https://twitter.com/ollama/status/1952782326926328313)
> 与NVIDIA/高通合作加速GPT-OSS在消费硬件的部署，修复了Mac mini 16GB内存的兼容性问题。

---

### 5. [Qwen-Image图像生成模型](https://huggingface.co/city96/Qwen-Image-gguf/tree/main)
> 阿里巴巴20B参数MMDiT模型，特别擅长中文文本和图形生成，已支持ComfyUI和Diffusers集成。

---

### 6. [Alibaba Qwen3-2507 API](https://twitter.com/Alibaba_Qwen/status/1952767585596145773)
> 提供100万token上下文长度的编码模型API，在Terminal-Bench基准测试中超越Claude Opus 4。

---

### 7. [Grok Imagine图像生成开放](https://twitter.com/chaitualuru/status/1952483088510140670)
> xAI的文本转图功能向所有X Premium用户开放，通过Grok应用提供多模态生成服务。

---

### 8. [Meta发布直接空气捕集数据集](https://twitter.com/AIatMeta/status/1952477453857017948)
> 与Georgia Tech合作的最大规模CO2捕集材料数据集，加速气候技术研发。

---

### 9. [LangGraph平台获SOC 2认证](https://twitter.com/LangChainAI/status/1952814314793910599)
> LangChain的智能体开发框架通过Type II合规认证，增强企业级应用的可信度。

---

### 10. [Agent Reinforcement Trainer登顶GitHub](https://twitter.com/corbtt/status/1952477405265989652)
> 新型智能体训练框架成为GitHub趋势榜第一，支持环境快照保存和依赖管理优化。

---