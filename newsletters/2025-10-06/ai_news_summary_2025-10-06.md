## AINews - 2025-10-06

> [原文链接](https://news.smol.ai/issues/25-10-03-not-much/)

## 📰 十大AI新闻要点

### 1. [Claude Sonnet 4.5发布，编码能力接近Opus 4.1](https://twitter.com/finbarrtimbers/status/1973922679418974298)
> 经过约30小时测试，Claude Sonnet 4.5在编码任务上表现与Opus 4.1相当，具有抛光良好的用户体验，但不如GPT-5 Codex强大。Anthropic强调其在网络安全任务上表现优异，某些任务甚至优于Opus 4.1。

---

### 2. [xAI Grok Code Fast声称在编辑成功率上超越竞品](https://twitter.com/gauravisnotme/status/1974001009778115066)
> Grok Code Fast据称在较低成本下实现了比Claude 4.5和GPT-5 Codex更高的差异编辑成功率，需要独立验证，但用户更关注编辑可靠性而非原始指标。

---

### 3. [Google Jules编码代理推出可编程API](https://twitter.com/julesagent/status/1974178592683954252)
> Google的Jules编码代理经过一周的预热后推出公共API，使其成为"可编程团队成员"，支持工具集成和CI/CD流水线，标志着编码代理向生产环境迈进。

---

### 4. [Sora 2 Pro登顶App Store，推动创作者生态系统](https://twitter.com/billpeeb/status/1974035563482116571)
> Sora 2现已成为App Store排名第一的应用，团队正在快速迭代和发放邀请。高质量15秒视频片段正在推出，同时催生了包括水印移除工作流在内的新创作者工具生态。

---

### 5. [Terence Tao公开使用GPT-5进行数学研究](https://twitter.com/SebastienBubeck/status/1973977315572154383)
> 菲尔兹奖得主Terence Tao公开记录使用GPT-5和工具来搜索数学反例和启发式方法，这被认为是人类+AI研究工作流程的重要时刻。

---

### 6. [Sakana AI与Daiwa证券签署3400万美元合作协议](https://twitter.com/SakanaAILabs/status/1973935631354245286)
> Sakana AI与Daiwa证券签署多年期约3400万美元协议，共同构建"全面资产咨询平台"，使用Sakana模型进行研究生成、市场分析和投资组合构建。

---

### 7. [xLSTM架构报告显示在跨熵指标上帕累托优于Transformer](https://twitter.com/maxmbeck/status/1974018534385598895)
> xLSTM在固定FLOP和固定损失两种机制下都报告了在跨熵指标上帕累托优于Transformer，并在下游推理效率方面获得收益。

---

### 8. [Perplexity Comet浏览器全球发布](https://www.perplexity.ai/comet)
> Perplexity的AI优先Comet浏览器退出等待名单，向全球用户免费开放，支持并行代理任务执行，早期采用者称赞其速度和更智能的搜索功能。

---

### 9. [华为SINQ量化方法实现30倍加速](https://arxiv.org/abs/2509.22944)
> 华为提出SINQ后训练LLM量化方案，添加每矩阵第二轴尺度和快速Sinkhorn-Knopp启发归一化，报告显示比AWQ快约30倍，在4位及以下精度上改进了困惑度。

---

### 10. [Vision/LM Arena显示顶级模型四强并列第一](https://twitter.com/arena/status/1974215622474293262)
> Vision/LM Arena显示顶级梯队异常接近：Sonnet 4.5（标准和32k Thinking）、Claude Opus 4.1和Gemini 2.5 Pro四强并列第一，OpenAI模型都在一个评分点内。

---

## 🛠️ 十大工具产品要点

### 1. [Google Jules Tools终端界面发布](https://twitter.com/julesagent/status/1974178592683954252)
> 可通过`npm install -g @google/jules`安装，提供异步编码代理的终端界面，从网页代理演变为命令行伴侣，支持工具和CI/CD集成。

---

### 2. [Chrome DevTools MCP标准化发布](https://github.com/ChromeDevTools/chrome-devtools-mcp)
> 规范的Chrome DevTools MCP发布，为代理提供标准化的浏览器调试和自动化接口，用户展示了与claude-cli在DeepSeek浏览器测试中的工作流程。

---

### 3. [TorchAO集成INT4量化支持](https://github.com/pytorch/ao?tab=readme-ov-file#-quick-start)
> TorchAO现在支持INT4量化（INT4mm），使用从tinygemm库适配的TensorCore内核，针对A100部署的高吞吐量场景，贡献者可以扩展INT4路径和优化操作符覆盖。

---

### 4. [Solveit开发平台公开发布](https://twitter.com/jeremyphoward/status/1973857739341508884)
> Jeremy Howard宣布Solveit公开发布，这是Answer.AI内部使用一年的AI增强开发平台，包含5周直播课程，旨在通过紧密反馈循环对抗"AI疲劳"。

---

### 5. [KernelBench系统化GPU性能评估](https://harvard-edge.github.io/cs249r_fall2025/blog/2024/10/01/gpu-performance-engineering/)
> KernelBench项目系统化GPU性能评估，包含250个精选PyTorch ML工作负载，引入speedup度量fast_p，即使前沿推理模型大多也无法超越PyTorch基线。

---

### 6. [DeepSeek稀疏注意力CUDA实现](https://github.com/deepseek-ai/FlashMLA)
> 工程师协调使用FlashMLA和TileLang在CUDA中实现DeepSeek的稀疏注意力，文档详细介绍了部分RoPE、FP8稀疏内核和Hopper特定优化。

---

### 7. [vLLM在Qwen3-0.6B上实现4300 t/s吞吐量](来源：文章内容)
> 在RTX 4070上，Qwen3-0.6B BF16使用vLLM在31个请求中达到约4300 t/s，远高于transformers的10-11 t/s，但低于LM Studio的llamacpp约200 t/s。

---

### 8. [Hugging Face TRL重现"无遗憾LoRA"](https://twitter.com/ben_burtenshaw/status/1974191312229577085)
> Hugging Face TRL重现了"无遗憾LoRA"，在熟悉的API下暴露了更高性能的LoRA实现，为参数高效微调提供改进方案。

---

### 9. [Ollama简化本地工具调用](https://ollama.com/)
> Ollama提供简单方式使用工具调用（函数调用），本质上设置了一个与OpenAI API兼容的本地服务器，建议从小模型开始测试兼容性。

---

### 10. [Red Hat发布FP8量化Qwen3-VL-235B](https://twitter.com/RedHat_AI/status/1973932224400798163)
> Red Hat发布FP8量化的Qwen3-VL-235B-A22B-Instruct，减少约50%磁盘/GPU内存使用，同时保持>99.6%的准确率保留。

---