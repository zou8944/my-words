## AINews - 2025-12-28

> [原文链接](https://news.smol.ai/issues/25-12-24-nvidia-groq/)

## 📰 十大AI新闻要点

### 1. [英伟达以约200亿美元现金“非独家许可协议”形式收购Groq核心团队](https://www.cnbc.com/2025/12/24/nvidia-buying-ai-chip-startup-groq-for-about-20-billion-biggest-deal.html)
> 英伟达在2025年平安夜宣布与AI芯片初创公司Groq达成一项“非独家许可协议”，以约200亿美元现金收购Groq大部分领导团队及其知识产权，而GroqCloud业务和现任CFO将留在原公司。这是英伟达历史上规模最大的交易，远超其2019年70亿美元收购Mellanox的记录，旨在将Groq的低延迟处理器整合到其AI工厂架构中，以服务更广泛的AI推理和实时工作负载。

---

### 2. [OpenAI强调2026年重点在于弥合“部署鸿沟”](https://twitter.com/OpenAI/status/2003594025098785145)
> OpenAI在推文中指出，2026年的进展将不仅关乎前沿模型能力，更在于如何让模型在医疗保健、商业和日常生活工作流中得到有效应用，强调了当前存在的“能力过剩”或“部署鸿沟”问题。

---

### 3. [特斯拉FSD v14被描述为通过“物理图灵测试”](https://twitter.com/DrJimFan/status/2003593613918531891)
> 英伟达AI科学家Jim Fan将特斯拉FSD v14描述为第一个在日常使用中感觉与人类驾驶员无异的消费级AI，强调了AI从“超现实”到“常规”再到“依赖”的快速转变过程。

---

### 4. [基准测试的脆弱性引发行业关注](https://twitter.com/EpochAIResearch/status/2003592566772822516)
> Epoch AI的研究指出，模型基准测试分数高度依赖于推理提供商的行为（如超时、速率限制、分词差异、参数缺失、瞬时错误），新模型/提供商受影响尤甚。这暴露了评估流程的脆弱性，使得分数更多反映的是提供商可靠性和集成债务，而非纯粹的模型质量。

---

### 5. [英伟达发布全面的机器人技术栈进展](https://twitter.com/DrJimFan/status/2003879965369290797)
> Jim Fan概述了英伟达在机器人领域的系列发布，包括开源的GR00T视觉语言动作模型检查点、GR00T Dreams世界模型、SONIC全身控制基础模型以及从仿真到仿真的强化学习后训练方案，将机器人定位为“最后的重大挑战”。

---

### 6. [Character.AI披露大规模预训练优化技巧“Squinch”](https://twitter.com/simon_mo_/status/2003608325624406482)
> Character.AI的技术博客分享了其在大规模预训练中维持高模型浮点利用率（MFU）的技巧，核心是使用了Noam Shazeer的梯度压缩算法“Squinch”，以及其他优化方法，以在GCP H100-TCPX集群上克服网络限制。

---

### 7. [MiniMax M2.1模型展开大规模分发攻势](https://twitter.com/arena/status/2003585316029104383)
> MiniMax的M2.1模型在多个开发者平台（如LMArena Code Arena、Cline、Kilo、Roo Code、Ollama、BlackboxAI）同步上线，并在SWE-bench变体和SciCode等基准测试中表现强劲。该公司宣称其长程编码能力接近Opus，但价格仅为十分之一。

---

### 8. [智谱AI推动GLM-4.7开源与MCP工具集成](https://twitter.com/Zai_org/status/2003828175089098943)
> 智谱AI持续推动GLM-4.7模型的开源，使其在Hugging Face趋势榜排名第一。同时，该公司推出了类似MCP的开发者工具，如“Zread MCP”，允许在智能体对话流中直接搜索和读取代码库文件。

---

### 9. [端到端强化学习训练工具使用智能体取得显著进展](https://twitter.com/omarsar0/status/2003862504490086596)
> 一项名为Agent-R1的研究提出，由于工具/环境反馈的随机性，智能体训练本质上是强化学习问题。该方法通过显式掩码进行信用分配，在多项选择题（如GRPO EM 0.3877 vs RAG EM 0.1328）上相比传统RAG取得了巨大提升。

---

### 10. [人形机器人展示自主交互与语音操控能力](https://twitter.com/adcock_brett/status/2003598494838431874)
> Figure AI创始人Brett Adcock发布演示视频，展示其人形机器人在没有远程操控的情况下与人互动并响应语音指令，强调了从意图到像素再到动作的“语音-操控”耦合能力。

---

## 🛠️ 十大工具产品要点

### 1. [Windsurf发布Wave 13：并行多智能体工作流与免费SWE-1.5模型](https://discord.com/channels/1027685395649015980/1027688115592237117/1453488772837671157)
> Windsurf推出“Wave 13: Shipmas Edition”，新增并行多智能体级联工作流、专用的zsh终端、Git工作树支持、多级联窗格和标签页等功能，并宣布其接近前沿水平的编码模型SWE-1.5在未来3个月内对所有用户免费开放。

---

### 2. [Mistral Vibe CLI推出可复用的“技能”模块](https://twitter.com/MistralAI/status/2003843358054068327)
> Mistral的Vibe CLI工具引入了“技能”作为可复用的规则包，支持推理模型和终端主题定制，旨在推动可共享、项目级的智能体策略工件发展。

---

### 3. [OpenRouter与Open-WebUI集成管道发布](https://github.com/rbb-dev/Open-WebUI-OpenRouter-pipe)
> 社区开发者发布了将OpenRouter的Responses API集成到Open-WebUI的管道项目，允许用户在Open-WebUI界面中直接使用OpenRouter提供的多种模型。

---

### 4. [ElevenLabs成为多模型AI视频生成中心](https://elevenlabs.io/)
> 用户报告使用ElevenLabs平台可以一站式生成Sora 2、Google Veo 3.1和Kling 2.6等多种模型的视频，无需在不同平台间切换，且部分模型生成的视频不带水印。

---

### 5. [FlashSR音频超分辨率模型实现200倍实时处理速度](https://xcancel.com/Yatharth3501/status/2003884180577702074)
> FlashSR是一个快速的音频增强/超分辨率模型，处理速度超过实时200倍，已集成到MiraTTS中，并在Hugging Face和GitHub上开源，适用于对延迟敏感的语音产品。

---

### 6. [通义千问开源图像编辑模型Qwen-Image-Edit-2511](https://twitter.com/Alibaba_Qwen/status/2003751934013100458)
> 阿里巴巴开源了图像编辑模型Qwen-Image-Edit-2511，并在Replicate等平台上线。同时，社区工具支持其LoRA微调，并推出了“3位精度恢复适配器”，使得在小于24GB VRAM的显卡上进行微调成为可能。

---

### 7. [Microsoft发布轻量级2D转3D模型TRELLIS.2-4B](https://huggingface.co/microsoft/TRELLIS.2-4B)
> 微软发布了参数量为40亿的TRELLIS.2-4B模型，能够将2D图像转换为3D，基于SigLIP视觉编码器和Qwen-3语言主干，可在8GB GPU上运行1536分辨率的任务。

---

### 8. [Qwen 2.5VL-3B实现低成本多模态推理](https://huggingface.co/)
> 用户报告，通过4位量化（视觉层保持全精度），Qwen 2.5VL-3B模型可以在P100显卡（约5GB VRAM）上处理约1400x900像素的大图像，使得在消费级硬件上进行严肃的多模态工作成为可能。

---

### 9. [DeepWiki工具助力大型开源代码库理解](https://twitter.com/eliebakouch/status/2003604370534072445)
> DeepWiki被工程师用作“代码考古”工具，能够有效挖掘大型开源仓库，当开发者知道某个功能已在某知名开源项目中良好实现时，它能帮助快速定位相关文件和实现细节。

---

### 10. [Anthropic临时加倍Claude Pro/Max使用限额以鼓励智能体工作流](https://twitter.com/claudeai/status/2003918730833608902)
> Anthropic宣布在元旦前临时加倍Claude Pro和Claude Max用户的额度限制，明确鼓励开发者更积极地尝试和构建智能体工作流。