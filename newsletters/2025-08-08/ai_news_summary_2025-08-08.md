## AINews - 2025-08-08

> [原文链接](https://news.smol.ai/issues/25-08-06-not-much/)

## 📰 十大AI新闻要点

### 1. [OpenAI发布GPT-OSS开源模型](https://twitter.com/arunv30/status/1952881931798143276)
> OpenAI宣布发布gpt-oss-120b和gpt-oss-20b开源模型，这是自GPT-2以来首次开源。模型采用滑动窗口注意力、专家混合(MoE)架构和256k上下文长度，使用新型MXFP4格式。

### 2. [GPT-OSS性能表现参差不齐](https://twitter.com/Teknium1/status/1953063858761023843)
> 社区测试发现GPT-OSS在数学和编码方面表现突出，但在常识和世界知识方面存在缺陷。在Aider Polyglot编码基准测试中仅得41.8%，落后于Kimi-K2(59.1%)和DeepSeek-R1(56.9%)。

### 3. [Google发布Genie 3世界模型](https://twitter.com/denny_zhou/status/1952887267963662429)
> Google DeepMind推出Genie 3，能够从文本或视频输入生成完全交互式的可探索环境，支持720p/24fps实时导航，被认为是世界模型领域的重大突破。

### 4. [OpenAI悬赏50万美元进行红队测试](https://twitter.com/woj_zaremba/status/1952886644090241209)
> OpenAI宣布50万美元赏金计划，邀请研究人员对新模型进行压力测试，测试结果将由OpenAI、Anthropic、Google和英国AISI组成的联盟审查。

### 5. [Qwen3-4B-Thinking-2507模型发布](https://www.reddit.com/r/LocalLLaMA/comments/1mj7t51/qwen34bthinking2507_released/)
> 阿里云发布Qwen3-4B-Thinking-2507模型，在BFCL-v3基准测试中获得71.2分，接近GPT-4o水平，支持256k上下文窗口，社区认为这是小参数模型的重要突破。

### 6. [Elon Musk宣布将开源Grok 2](https://www.reddit.com/r/LocalLLaMA/comments/1mj0snp/elon_musk_says_that_xai_will_make_grok_2_open/)
> Elon Musk表示xAI将在下周开源Grok 2模型，但社区认为该模型在性能上已落后于当前最先进的开源模型。

### 7. [GPT-5即将发布](https://www.reddit.com/r/singularity/comments/1mja836/gpt_5_livestream_thursday_10_am_pt/)
> OpenAI计划在太平洋时间周四上午10点进行GPT-5直播发布，CDN上已出现GPT-5、GPT-5-NANO和GPT-5-MINI的图标文件，暗示多版本发布策略。

### 8. [Claude Opus 4.1展示强大代码重构能力](https://www.reddit.com/r/ClaudeAI/comments/1mj5b6t/in_less_than_24h_opus_41_has_paid_the_tech_debt/)
> Anthropic的Claude Opus 4.1展示了出色的代码重构能力，能够自动分解复杂类、实现策略模式并生成端到端测试，显著改变了软件开发工作流程。

### 9. [IBM Granite 3.1 3B-A800M MoE表现优异](来源：文章内容)
> IBM的Granite 3.1 3B-A800M MoE模型在世界知识基准测试中超越GPT-OSS-20B，社区对即将发布的采用mamba2-transformer混合架构的Granite 4充满期待。

### 10. [Llama.cpp支持MXFP4格式](https://twitter.com/ggerganov/status/1952978670328660152)
> Llama.cpp现已原生支持MXFP4格式，在RTX3090上实现高效推理，社区推测GPT-OSS可能直接使用该格式训练以避免量化误差。

---

## 🛠️ 十大工具产品要点

### 1. [Azure AI Foundry支持GPT-OSS](https://twitter.com/xikun_zhang_/status/1952902211278913629)
> 微软宣布Azure AI Foundry和Windows Foundry Local将支持GPT-OSS模型，为企业用户提供新的模型部署选项。

### 2. [Ollama集成GPT-OSS与网页搜索](https://twitter.com/ollama/status/1952882173255856223)
> Ollama宣布支持GPT-OSS模型并集成网页搜索功能，方便开发者构建具有实时信息获取能力的应用。

### 3. [LlamaIndex金融文档代理集成](https://twitter.com/jerryjliu0/status/1953108641558540720)
> LlamaIndex展示与Delphi合作的金融文档代理解决方案，使用LlamaCloud作为文档摄取上下文层，支持图表等视觉元素的成本效益分析。

### 4. [LangChain推出Open SWE](https://twitter.com/Hacubu/status/1953168346356314376)
> LangChain发布Open SWE，一个开源的云端异步编码代理，可连接到GitHub仓库自主解决问题并创建拉取请求。

### 5. [Google Gemini新增Storybook功能](https://twitter.com/demishassabis/status/1952897414207074810)
> Google Gemini应用新增Storybook功能，可创建个性化插图故事，同时推出包括引导学习、闪卡和集成可视化在内的新学习工具。

### 6. [Anthropic Claude Code安全审查功能](https://twitter.com/AnthropicAI/status/1953135070174134559)
> Anthropic宣布Claude Code现在可自动审查代码中的安全漏洞，与Andrew Ng合作推出高度代理化编码工作流课程。

### 7. [Google AI教育加速器计划](https://twitter.com/Google/status/1953126394847768936)
> Google承诺投入10亿美元用于AI教育，为大学生提供免费AI培训和Google职业证书，推动AI素养提升。

### 8. [Groq实现GPT-OSS-120B高速推理](https://twitter.com/JonathanRoss321/status/1953119620103381440)
> Groq平台运行GPT-OSS-120B模型速度超过500 tokens/秒，Cerebras系统更是达到3,000 tokens/秒，展示硬件加速的强大性能。

### 9. [vLLM对Hopper GPU的支持](https://twitter.com/vllm_project/status/1952940603773468926)
> vLLM项目表示已在Hopper GPU上运行多项评估，确认GPT-OSS在该硬件上的数值计算稳定可靠。

### 10. [AMD GPU本地运行GPT-OSS-20B](https://twitter.com/dzhng/status/1953132623280165193)
> 社区展示在不到1000美元的AMD GPU笔记本上本地运行GPT-OSS-20B模型，速度达到52 tokens/秒，证明消费级硬件的可行性。