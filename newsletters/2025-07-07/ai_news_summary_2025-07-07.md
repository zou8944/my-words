## AINews - 2025-07-07

> [原文链接](https://news.smol.ai/issues/25-07-03-not-much/)

## 📰 十大AI新闻要点

### 1. [Ilya Sutskever正式担任Safe Superintelligence Inc. CEO](https://twitter.com/ilyasut/status/1940802278979690613)
> OpenAI前首席科学家Ilya Sutskever宣布正式担任SSI公司CEO，Daniel Levy任总裁，Daniel Gross已离职。Sutskever强调公司拥有充足算力和团队，并驳斥收购传闻。

---

### 2. [Perplexity AI整合银行卖方研究数据](https://twitter.com/AravSrinivas/status/1940813462994932092)
> Perplexity CEO宣布将整合银行卖方研究报告，并已免费提供Morningstar金融研究报告。还透露未来产品将原生集成笔记、会议和头脑风暴功能。

---

### 3. [Google Veo 3视频生成模型全球开放](https://twitter.com/demishassabis/status/1940616072304251152)
> Google DeepMind CEO宣布Veo 3视频生成模型现已向全球Gemini Pro用户开放，包括欧洲地区，标志着视频生成技术进入新阶段。

---

### 4. [DeepSeek发布R1T2模型，速度提升200%](https://twitter.com/reach_vb/status/1940536684061643239)
> DeepSeek新发布的R1T2模型采用专家组装方法，在GPQA和AIME 24等基准测试中表现显著提升，速度是前代的2倍，MIT许可开源。

---

### 5. [OpenAI推出高价Deep Research API](https://twitter.com/ArtificialAnlys/status/1940896348364210647)
> OpenAI新推出的深度研究API端点价格高达每次调用30美元，o3-deep-research定价40美元/百万输出token，远高于标准API。

---

### 6. [Together AI发布DeepSWE软件工程代理](https://twitter.com/tri_dao/status/1940765882227347585)
> Together AI基于Qwen3-32B开发的DeepSWE代理在SWE-Bench-Verified测试中达到59%准确率，完整训练工具包和方法开源。

---

### 7. [Kyutai开源TTS和Unmute语音模型](https://twitter.com/ClementDelangue/status/1940784886509682935)
> 法国AI实验室Kyutai发布开源文本转语音模型，支持实时语音克隆和长文本生成，单GPU可同时服务32个用户。

---

### 8. [NVIDIA GB300 NVL72开始部署](https://twitter.com/weights_biases/status/1940818055271272917)
> CoreWeave成为首家部署NVIDIA GB300 NVL72系统的云服务商，该平台专为AI训练和推理设计，性能显著提升。

---

### 9. [MIT研究揭示ChatGPT对不同学习者的影响差异](https://arxiv.org/pdf/2506.08872)
> MIT研究发现高能力学习者使用LLM进行知识整合，而低能力学习者倾向于直接获取答案，可能影响深度学习效果。

---

### 10. [AI基础设施耗电量惊人](https://twitter.com/scaling01/status/1940536579183067540)
> OpenAI计划中的Stargate数据中心预计耗电5GW，相当于430万美国家庭用电量，凸显AI发展的能源挑战。

---

## 🛠️ 十大工具产品要点

### 1. [Kyutai TTS语音合成工具](https://github.com/kyutai-labs/delayed-streams-modeling/)
> 开源实时TTS系统，支持10秒语音克隆，延迟仅220ms，但限制直接访问语音嵌入模型以确保伦理使用。

---

### 2. [DeepSWE软件工程代理](https://huggingface.co/agentica-org/DeepSWE-Preview)
> 基于Qwen3-32B的RL训练代理，在SWE-Bench测试中表现优异，完整工具链开源。

---

### 3. [PrivateScribe.ai本地转录平台](http://privatescribe.ai/)
> 医疗法律专用全本地化AI转录工具，整合Whisper和Ollama，MIT许可支持自定义模型。

---

### 4. [ZLUDA非NVIDIA GPU的CUDA兼容方案](https://www.tomshardware.com/software/a-project-to-bring-cuda-to-non-nvidia-gpus-is-making-major-progress)
> 使CUDA应用能在AMD等GPU运行，面临法律和技术挑战，但取得显著进展。

---

### 5. [OmniAvatar Wan 1.3B语音驱动虚拟形象](https://github.com/Omni-Avatar/OmniAvatar)
> 8GB显存即可运行的虚拟形象生成模型，支持实时音频驱动，社区正开发ComfyUI插件。

---

### 6. [mem0.ai长期记忆集成方案](http://mem0.ai/)
> 与Gemini 2.5集成的长期记忆系统，使AI应用能记住历史对话，提升个性化体验。

---

### 7. [Claude Code编程辅助工具](https://github.com/Veraticus/nix-config/tree/main/home-manager/claude-code)
> Anthropic的编程专用模型，用户分享高级配置模板，显著提升开发效率。

---

### 8. [lm_eval评估工具标准化](https://github.com/EleutherAI/lm-evaluation-harness/issues/3083)
> 通过惰性加载将启动时间从9秒降至0.05秒，改进任务发现和评估流程。

---

### 9. [Torch.compile性能优化工具](https://peps.python.org/pep-0562/#rationale)
> 通过Dynamo追踪Python代码生成优化内核，避免运行时编译开销，显著提升性能。

---

### 10. [CuTeDSL Hopper架构开发工具](https://veitner.bearblog.dev/cutedsl-on-hopper-wgmma-and-tma-intro/)
> 详解NVIDIA Hopper架构WGMMA和TMA原子操作，帮助开发者充分利用硬件潜力。