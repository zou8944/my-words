## AINews - 2025-07-08

> [原文链接](https://news.smol.ai/issues/25-07-03-not-much/)

## 📰 十大AI新闻要点

### 1. [Ilya Sutskever正式出任SSI CEO](https://twitter.com/ilyasut/status/1940802278979690613)
> OpenAI前首席科学家Ilya Sutskever宣布正式担任Safe Superintelligence Inc(SSI)的CEO，Daniel Levy任总裁，Daniel Gross已离职。Sutskever强调公司拥有充足算力和团队，并驳斥收购传闻。

---

### 2. [Perplexity AI整合银行卖方研究数据](https://twitter.com/AravSrinivas/status/1940808181296545859)
> Perplexity CEO宣布已免费整合Morningstar金融研究报告，并计划接入更多银行卖方研究数据。同时透露将推出原生集成在Comet中的笔记/会议/头脑风暴功能。

---

### 3. [Gemini Veo 3视频模型全球开放](https://twitter.com/demishassabis/status/1940616072304251152)
> Google DeepMind CEO宣布Veo 3视频生成模型现已向全球Gemini Pro用户开放，包括欧洲地区。该模型支持更高质量的视频生成能力。

---

### 4. [DeepSeek发布R1T2系列模型](https://twitter.com/reach_vb/status/1940536684061643239)
> DeepSeek推出R1T2模型，速度提升200%，在GPQA和AIME 24等基准测试表现优异。采用专家组装方法训练，MIT许可在HuggingFace开源。

---

### 5. [OpenAI推出高价Deep Research API](https://twitter.com/ArtificialAnlys/status/1940896348364210647)
> OpenAI新推出的Deep Research API端点价格高达每次调用30美元，其中o3-deep-research定价40美元/百万输出token，远高于标准API。

---

### 6. [Together AI开源DeepSWE编码代理](https://twitter.com/tri_dao/status/1940765882227347585)
> Together AI基于Qwen3-32B开发的开源软件工程代理DeepSWE，在SWE-Bench-Verified测试中达到59%准确率。完整训练工具包和方法论已开源。

---

### 7. [Kyutai发布开源TTS模型](https://huggingface.co/kyutai/tts-1.6b-en_fr)
> 法国AI实验室Kyutai推出开源文本转语音模型Kyutai TTS和Unmute，支持实时语音合成(220ms延迟)和有限的声音克隆功能。

---

### 8. [NVIDIA GB300 NVL72开始部署](https://twitter.com/weights_biases/status/1940818055271272917)
> CoreWeave成为首家部署NVIDIA GB300 NVL72系统的云服务商，该平台采用新型架构，专为大规模AI训练和推理优化。

---

### 9. [MIT研究揭示ChatGPT对学习的影响](https://arxiv.org/pdf/2506.08872)
> MIT研究发现高能力学习者使用LLM进行主动迭代学习，而低能力学习者倾向于直接获取答案，影响认知负荷和知识建构。

---

### 10. [ZLUDA项目实现非NVIDIA GPU的CUDA兼容](https://github.com/vosen/ZLUDA)
> ZLUDA项目取得重大进展，可在非NVIDIA GPU上运行CUDA二进制文件，但面临法律风险和资源限制的挑战。

---

## 🛠️ 十大工具产品要点

### 1. [DeepSeek R1T2模型](https://huggingface.co/deepseek-ai)
> 200%速度提升的代码模型，MIT许可开源，支持专家组装架构和高效推理。

---

### 2. [Kyutai TTS](https://github.com/kyutai-labs/delayed-streams-modeling/)
> 开源实时TTS系统，220ms延迟，支持流式处理和有限声音克隆。

---

### 3. [DeepSWE编码代理](https://huggingface.co/agentica-org/DeepSWE-Preview)
> 基于Qwen3-32B的RL训练编码代理，SWE-Bench测试59%准确率，完整训练框架开源。

---

### 4. [PrivateScribe.ai本地转录平台](http://privatescribe.ai/)
> MIT许可的完全本地化AI转录平台，整合Whisper和Ollama，专为医疗/法律场景设计。

---

### 5. [OmniAvatar Wan 1.3B](https://github.com/Omni-Avatar/OmniAvatar)
> 音频驱动虚拟形象模型，8GB显存即可运行，支持实时面部动画生成。

---

### 6. [mem0.ai长期记忆系统](http://mem0.ai/)
> 与Gemini 2.5集成的长期记忆服务，支持个性化AI应用开发。

---

### 7. [Claude Code工作流](https://github.com/Veraticus/nix-config/tree/main/home-manager/claude-code)
> Anthropic Claude Code的高级配置模板库，支持自动化编程工作流和调试。

---

### 8. [lm_eval评估工具改进](https://github.com/EleutherAI/lm-evaluation-harness)
> 评估库启动时间从9秒优化至0.05秒，支持惰性加载和更直观的任务发现。

---

### 9. [Torch.compile优化器](https://pytorch.org/docs/stable/torch.compiler.html)
> 通过Dynamo追踪Python代码生成优化内核，自动融合操作并生成高效CUDA/Triton代码。

---

### 10. [CuTeDSL编程框架](https://veitner.bearblog.dev/cutedsl-on-hopper-wgmma-and-tma-intro/)
> 针对NVIDIA Hopper架构的DSL，优化WGMMA和TMA原子操作，提升张量计算效率。