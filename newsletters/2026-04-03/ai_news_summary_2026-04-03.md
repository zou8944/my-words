## AINews - 2026-04-03

> [原文链接](https://news.smol.ai/issues/26-04-01-not-much/)

## 📰 十大AI新闻要点

### 1. Arcee发布开源推理大模型Trinity-Large-Thinking
> Arcee发布了Trinity-Large-Thinking模型，采用Apache 2.0开源协议，总参数量4000亿，激活参数量130亿。该模型在PinchBench上排名第二（仅次于Opus 4.6），在Tau2-Airline上达到SOTA水平，并具备前沿的电信任务处理能力，旨在为希望检查、托管、蒸馏和微调自有系统的开发者和企业提供支持。
来源：https://x.com/arcee_ai/status/2039369121591120030

---

### 2. Z.ai推出原生多模态视觉编码模型GLM-5V-Turbo
> Z.ai发布了GLM-5V-Turbo模型，这是一个原生多模态融合的视觉编码模型，能够处理图像、视频、文档布局和设计稿，同时保持纯文本编码性能。其性能提升归功于下一代CogViT编码器、30+任务的协作式强化学习以及合成智能体数据生成。
来源：https://x.com/Zai_org/status/2039371126984360085

---

### 3. Anthropic的Claude Code源代码意外泄露
> Anthropic的Claude Code CLI源代码通过npm注册表中的.map文件意外泄露，包含约50万行TypeScript代码。泄露的代码揭示了其多智能体编排系统的核心是一个简单的`while(true)`循环，并包含4层上下文压缩栈、40+工具模块化架构、并行工具执行等设计细节。
来源：https://x.com/ZhihuFrontier/status/2039229986339688581

---

### 4. 开源智能体框架Nous Hermes Agent获得社区青睐
> 在Claude Code泄露后，社区对开源智能体替代方案的关注度激增。许多用户反馈，Nous Hermes Agent比OpenClaw或基于Claude的堆栈更容易部署和操作，因其近乎零的配置需求和更好的本地工作流。
来源：https://x.com/NousResearch/status/2039402523711140094

---

### 5. 研究显示自组织智能体角色优于人工预设角色
> DAIR总结的一项新研究显示，在多达256个智能体、25000个任务的环境中，自组织角色在性能上超越了预定义的规划者/编码者/审查者层级结构。自组织方法实现了比集中式方法高14%的性能，并涌现出5000多个角色，开源模型能以更低成本达到闭源模型95%的质量。
来源：https://x.com/dair_ai/status/2039350842382512455

---

### 6. DeepMind研究揭示针对AI智能体的网页攻击面
> DeepMind一篇关于“AI智能体陷阱”的新论文将智能体安全的重心从模型越狱转向了网页/文档中的对抗性内容。研究指出，隐藏在HTML/CSS中的提示词注入攻击成功率高达86%，而潜在的记忆污染攻击在污染率低于0.1%的情况下成功率超过80%。
来源：https://x.com/omarsar0/status/2039383554510217707

---

### 7. Hugging Face发布TRL v1.0统一后训练框架
> Hugging Face发布了TRL（Transformer Reinforcement Learning）v1.0，这是一个重要的版本，将监督微调（SFT）、奖励建模、DPO（直接偏好优化）和GRPO（群体相对策略优化）等开源后训练方法统一到一个生产就绪的软件包中。
来源：https://x.com/RussellQuantum/status/2039270550099443954

---

### 8. OpenAI重置所有计划的Codex使用限额
> OpenAI工程师宣布，由于不明原因的用户速率限制激增以及通过清除欺诈账户回收了算力，已重置所有订阅计划的Codex使用限额。社区将此解读为在编码智能体市场中，速率限制的慷慨程度已成为一个直接的竞争维度。
来源：https://x.com/thsottiaux/status/2039248564967424483

---

### 9. TII发布早期融合多模态模型Falcon Perception
> 阿联酋技术创新研究所（TII）发布了Falcon Perception，这是一个开放词汇的指代表达式分割模型。其显著设计特点是采用“早期融合”Transformer，从第一层就开始混合图像和文本信息，而不是依赖多阶段流水线和后期融合。同时发布的还有一个声称性能可与大3-10倍的模型竞争的3亿参数OCR模型。
来源：https://x.com/dahou_yasser/status/2039242378809385331

---

### 10. 新基准工具涌现，关注长视野与机器人任务评估
> 新的智能体评估基准和工具不断丰富，包括用于模拟一年期创业历程的YC-Bench，以及CaP-Gym / CaP-X——一个涵盖187个操作任务、12个前沿模型的机器人智能体基准和工具包，其代码采用MIT许可证开源。
来源：https://x.com/DrJimFan/status/2039358115318243352

---

## 🛠️ 十大工具产品要点

### 1. PrismML发布首个商业化可行的1比特大模型Bonsai
> PrismML发布了1比特Bonsai模型（如8B版本），所有组件（包括嵌入层、注意力层、MLP层和语言模型头）均量化至1比特精度。该模型内存占用仅1.15GB，相比全精度模型体积缩小14倍、速度快8倍、能效高5倍，适用于边缘硬件，采用Apache 2.0协议开源。
来源：文章内容

---

### 2. TurboQuant量化技术实现模型高压缩与低性能损失
> TurboQuant的TQ3_1S量化方案应用于Qwen3.5-27B模型，在保持接近Q4_0量化质量的同时，模型体积减小约10%（12.9GB vs 14.4GB），使其能够适配16GB显存的RTX 5060 Ti显卡，为内存有限的用户提供了实用方案。
来源：文章内容

---

### 3. 基于Claude Code泄露代码重构的开源多智能体框架
> 开发者基于泄露的Claude Code源代码，重构并开源了一个模型无关的多智能体编排框架（open-multi-agent）。该框架包含协调器模式、任务调度与依赖解析、智能体间通信等功能，约8000行TypeScript代码，采用MIT许可证。
来源：https://github.com/JackChen-me/open-multi-agent

---

### 4. ZINC：绕过ROCm的AMD GPU本地推理引擎
> ZINC是一个新的推理引擎，通过Vulkan直接与AMD GPU交互，绕过了复杂的ROCm堆栈。在AMD Radeon AI PRO R9700上，相比原方案实现了4倍加速，并能运行在ROCm官方不支持的硬件上。项目已在GitHub开源。
来源：https://github.com/zolotukhin/zinc

---

### 5. MemFactory：面向记忆增强型智能体的统一训练/推理框架
> MemFactory提出了一个为记忆增强型智能体设计的统一推理和训练框架，原生集成GRPO，据称相比基线模型能带来最高14.8%的相对性能提升。
来源：https://x.com/omarsar0/status/2039349083039817984

---

### 6. Baseten发布可压缩KV缓存的感知器模块
> Baseten描述了一个700万参数的感知器模块，能够将KV（键值）缓存压缩8倍，同时保持90%以上的事实保留率，被视为实现模型“从经验中学习”的路径之一。
来源：https://x.com/baseten/status/2039389931328704905

---

### 7. HeavyBall 3.0.0优化器发布，支持FSDP与端到端编译
> HeavyBall 3.0.0版本发布，新增对FSDP（完全分片数据并行）和DDP（分布式数据并行）的支持，通过端到端编译实现了2.5倍的速度提升，并包含了更快的Muon/SOAP变体和新优化器。
来源：https://x.com/Clashluke/status/2039374459375677814

---

### 8. SkyPilot新增原生VAST Data支持
> SkyPilot云编排平台新增了对VAST Data存储系统的原生支持，允许在不同计算后端之间直接高速挂载数据集，提升了数据处理的便捷性。
来源：https://x.com/skypilot_org/status/2039372218031845769

---

### 9. Hugging Face为Spaces推出持久化存储桶
> Hugging Face为其Spaces平台推出了持久化存储桶功能，为托管的应用提供了稳定、可长期存储数据的解决方案。
来源：https://x.com/_akhaliq/status/2039404288082894912

---

### 10. Tinker API为部分开源模型扩展上下文长度至256K
> Tinker API为其支持的部分开源模型扩展了上下文窗口，最高可达256K，这为强化学习和长视野任务实验提供了更有利的条件。
来源：https://x.com/tinkerapi/status/2039424320393621649

---