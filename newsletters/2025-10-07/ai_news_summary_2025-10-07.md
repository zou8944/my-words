## AINews - 2025-10-07

> [原文链接](https://news.smol.ai/issues/25-10-03-not-much/)

## 📰 十大AI新闻要点

### 1. [Claude Sonnet 4.5发布，编码能力接近Opus 4.1](https://twitter.com/finbarrtimbers/status/1973922679418974298)
> 经过约30小时测试，Claude Sonnet 4.5在编码任务上表现与Opus 4.1基本相当，具有精良的用户体验，但不如GPT-5 Codex强大。Anthropic强调其在网络安全任务上表现优异，某些任务甚至优于Opus 4.1。

---

### 2. [xAI Grok Code Fast声称在编辑成功率上超越竞品](https://twitter.com/gauravisnotme/status/1974001009778115066)
> Grok Code Fast据称在"更高难度编辑成功率"上超过Claude 4.5和GPT-5 Codex，且成本更低，但需要独立验证。用户更关注编辑可靠性而非原始token指标。

---

### 3. [Google Jules编程助手推出可编程API](https://twitter.com/julesagent/status/1974178592683954252)
> Google的Jules编码助手经过一周预热后推出公共API，使其成为"可编程团队成员"，支持工具集成和CI/CD流水线，可通过npm安装。

---

### 4. [Sora 2 Pro登顶App Store，推动创作者生态系统](https://twitter.com/billpeeb/status/1974035563482116571)
> Sora 2现已成为App Store排名第一的应用，团队正在快速迭代和发放邀请。高质量15秒视频片段正在推出，同时催生了新的创作者生态系统，如水印去除工作流程。

---

### 5. [Terence Tao公开使用GPT-5进行数学研究](https://twitter.com/SebastienBubeck/status/1973977315572154383)
> 菲尔兹奖得主Terence Tao公开记录使用GPT-5和工具来搜索数学反例和启发式方法，这被认为是人类+AI研究工作流程的重要时刻。

---

### 6. [Sakana AI与Daiwa证券签署3400万美元合作协议](https://twitter.com/SakanaAILabs/status/1973935631354245286)
> Sakana AI与Daiwa证券签署约3400万美元多年合作协议，共同构建"全面资产咨询平台"，使用Sakana模型进行研究生成、市场分析和投资组合构建。

---

### 7. [xLSTM在跨熵指标上帕累托优于Transformer](https://twitter.com/maxmbeck/status/1974018534385598895)
> xLSTM在固定FLOP和固定损失两种情况下都报告了帕累托优于Transformer的跨熵表现，并在下游推理效率方面获得增益。

---

### 8. [Perplexity Comet浏览器全球发布](https://www.perplexity.ai/comet)
> Perplexity的AI优先Comet浏览器退出等待列表，向全球用户免费开放，支持并行代理任务，在macOS和Windows上获得热烈反响。

---

### 9. [华为提出无需校准的SINQ量化方法](https://arxiv.org/abs/2509.22944)
> 华为提出SINQ后训练量化方案，通过每矩阵第二轴缩放和Sinkhorn-Knopp启发归一化，无需校准数据，报告比AWQ快30倍的量化速度。

---

### 10. [GLM 4.6在实际工具调用中表现优异](https://www.reddit.com/r/LocalLLaMA/comments/1nx18ax/glm_46_is_a_fuking_amazing_model_and_nobody_can/)
> 用户报告GLM 4.6在生产环境中展现强大的自主代理能力和工具调用准确性，在真实世界任务中优于Claude Sonnet和GPT变体。

---

## 🛠️ 十大工具产品要点

### 1. [Google Jules Tools终端接口发布](https://twitter.com/julesagent/status/1974178592683954252)
> Google推出Jules Tools终端界面，可通过`npm install -g @google/jules`安装，支持异步编码代理功能，与Gemini CLI集成。

---

### 2. [Perplexity Comet浏览器支持并行代理任务](https://www.perplexity.ai/comet)
> AI优先浏览器支持同时运行多个代理任务，提供更智能的搜索体验，设计感觉熟悉但通过非侵入式AI集成增强功能。

---

### 3. [Chrome DevTools MCP标准化发布](https://github.com/ChromeDevTools/chrome-devtools-mcp)
> 规范化的Chrome DevTools MCP发布，为代理提供标准化浏览器调试和自动化接口，已与claude-cli在DeepSeek浏览器测试中展示。

---

### 4. [TorchAO集成INT4量化支持](https://github.com/pytorch/ao?tab=readme-ov-file#-quick-start)
> TorchAO现在支持INT4量化(INT4mm)，使用来自tinygemm的TensorCore内核，针对A100 GPU的高吞吐量部署优化。

---

### 5. [Solveit AI增强开发平台公开](https://twitter.com/jeremyphoward/status/1973857739341508884)
> Jeremy Howard宣布Solveit公开发布，Answer.AI内部使用一年的AI增强开发平台，包含5周实时课程，旨在通过紧密反馈循环对抗"AI疲劳"。

---

### 6. [DeepSeek稀疏注意力CUDA实现](https://github.com/deepseek-ai/FlashMLA)
> 工程师协调在CUDA中实现DeepSeek稀疏注意力，使用FlashMLA和TileLang，包含部分RoPE、FP8稀疏内核和Hopper特定优化。

---

### 7. [KernelBench系统化GPU性能评估](https://harvard-edge.github.io/cs249r_fall2025/blog/2024/10/01/gpu-performance-engineering/)
> KernelBench项目系统化GPU性能评估，包含250个精选PyTorch ML工作负载，引入fast_p加速比指标，强调时钟锁定和预热运行的重要性。

---

### 8. [vLLM在Qwen3-0.6B上实现4300 token/秒](来源：文章内容)
> 在RTX 4070上，Qwen3-0.6B BF16使用vLLM达到4300 token/秒，31个请求，远高于transformers的10-11 token/秒，但低于LM Studio的llamacpp约200 token/秒。

---

### 9. [Ollama简化本地工具调用](https://ollama.com/)
> Ollama提供简单方式使用工具调用(函数调用)，本质上设置与OpenAI API兼容的本地服务器，建议从小模型开始测试兼容性。

---

### 10. [Hugging Face TRL重现"无遗憾LoRA"](https://twitter.com/ben_burtenshaw/status/1974191312229577085)
> Hugging Face TRL重现"无遗憾LoRA"，在熟悉API下暴露更高性能的LoRA实现，提升模型微调效率。

---