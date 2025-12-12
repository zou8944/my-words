## AINews - 2025-12-12

> [原文链接](https://news.smol.ai/issues/25-12-10-not-much/)

## 📰 十大AI新闻要点

### 1. 开源数学推理模型Nomos 1在普特南竞赛中取得顶尖成绩
> 来源：文章内容
> NousResearch发布的“Nomos 1”是一个300亿参数的开源数学推理系统，在2024年普特南数学竞赛中取得了87/120的分数，估计在所有3988名参赛者中排名第二。其关键突破在于通过专门的训练后处理和智能体流程，在推理时仅激活约30亿参数，使其能在消费级Mac上运行。这证明了在受限的激活参数下，通过组合推理和专门的训练后处理，开源模型可以在形式数学任务上媲美前沿闭源模型。

---

### 2. 智能体编码系统竞争白热化，Mistral Devstral 2表现突出
> 来源：文章内容
> 从业者报告称，Mistral的Devstral 2 Small模型在71%的第三方偏好评估中“击败或打平”了DeepSeek v3.2，同时模型更小、更快、更便宜。这标志着在编码智能体领域，开源模型正展现出强大的竞争力。

---

### 3. 各大IDE深度集成AI智能体，工作流迈向多智能体协作
> 来源：文章内容
> Cursor 2.2发布了深度智能体原语，包括调试模式、计划模式图表和多智能体评判。VS Code引入了统一的“智能体会话”聊天界面，集成本地、后台和云端智能体，并支持工作树隔离和智能体无缝交接。这标志着AI智能体正从单一工具深度融入开发工作流，并向真正的多智能体协作演进。

---

### 4. 训练与推理效率持续突破，Unsloth实现3倍训练加速
> 来源：文章内容
> Unsloth发布了新的融合变长RoPE和int64 Triton内核，支持无填充训练，为Llama/Qwen/Mistral/Gemma等模型家族带来了高达3倍的训练速度提升和约50%的VRAM减少，且损失和梯度范数保持不变。这大幅降低了在消费级GPU上进行模型微调的门槛。

---

### 5. 多模态模型能力快速迭代，GLM-4.6V与Qwen3-Omni-Flash获好评
> 来源：文章内容
> 智谱AI的GLM-4.6V被早期用户评价在编码和视觉理解上接近Claude Sonnet 4，是首个被认为对设计评审有用的开源视觉模型。阿里通义千问的Qwen3-Omni-Flash（2025年12月更新）大幅升级了实时多轮视频/音频对话能力，支持119种文本和19种语音语言。多模态模型正快速缩小与闭源模型的差距。

---

### 6. 事实性评估基准FACTS发布，Gemini 3 Pro领先
> 来源：文章内容
> Google DeepMind和Google Research发布了FACTS基准测试套件，涵盖内部知识、网络搜索、信息溯源和多模态输入，旨在标准化AI模型的可靠性评估。在该基准上，Gemini 3 Pro以68.8%的得分领先。

---

### 7. 自动驾驶与主动式智能体取得实际进展
> 来源：文章内容
> Wayve与日产签署最终协议，将在下一代ProPILOT中部署Wayve的AI Driver，实现从ADAS到点对点自动驾驶的功能。同时，研究展示了“ProAgent”原型，它能通过可穿戴设备的自我中心传感器（视频/音频/运动/位置）持续感知环境，并主动提供协助（如天气、叫车、比价），在Jetson Orin设备上的延迟约为4.5秒。

---

### 8. AI原生产品循环深入企业运营，Shopify展示完整AI栈
> 来源：文章内容
> Shopify展示了其AI产品栈：SimGym（模拟“数字客户”进行任务完成和零流量A/B测试）、Sidekick Pulse（运行大型HSTU+LLM以发现业务改进点）和Product Network（允许商家通过LLM驱动的匹配和站内结账相互销售产品）。这体现了AI正从工具演变为企业运营的核心基础设施。

---

### 9. 太空计算与芯片成本引发热议
> 来源：文章内容
> Starcloud-1项目宣布在轨道上使用H100 GPU训练了nanoGPT（莎士比亚数据集）并运行了Gemma推理，据称是首次在太空中演示LLM训练。同时，Epoch AI估计NVIDIA B200芯片成本约为6400美元，芯片级利润率约为80%，但捆绑成服务器后实现的利润率会下降。这引发了关于太空数据中心可行性（受真空热辐射限制）与地面计算成本优势的讨论。

---

### 10. OpenAI战略转向与用户流失引发行业关注
> 来源：文章内容
> 据报道，OpenAI CEO Sam Altman发出“红色代码”，要求优先改进ChatGPT而非其他项目（如Sora），标志着公司战略的重大调整。与此同时，Reddit社区出现大量用户取消ChatGPT订阅的讨论，转向Gemini和Claude等替代品，理由包括ChatGPT速度、可靠性和记忆力的下降，以及竞争对手在编码等任务上的优异表现。

---

## 🛠️ 十大工具产品要点

### 1. Claude Code引入异步子智能体执行
> [来源](https://twitter.com/omarsar0/status/1998774531188830304)
> Anthropic为Claude Code发布了v2.0.64更新，支持后台子智能体和异步执行。这使得智能体可以并发地探索解决方案或运行测试，并在完成后“唤醒”主智能体，显著提升了复杂编码任务的解决效率。

---

### 2. LangChain发布“Polly”智能体与调试CLI
> [来源](https://twitter.com/LangChainAI/status/1998807193320305101)
> LangChain发布了名为“Polly”的智能体，专门用于调试其他智能体，同时提供了一个CLI工具来提取追踪和线程信息。这标志着智能体开发工具正从简单的LLM应用调试，向支持长期运行、复杂智能体系统的可观测性迈进。

---

### 3. vLLM集成Intel AutoRound量化技术
> [来源](https://twitter.com/vllm_project/status/1998710451312771532)
> vLLM在其LLM Compressor中集成了Intel的AutoRound训练后量化技术，能够生成W4A16（4位权重，16位激活）的检查点，并可直接通过vLLM在Xeon、Gaudi、Arc GPU等多种硬件上提供服务，提升了模型部署的效率和硬件兼容性。

---

### 4. 轻量级智能体测试框架Stirrup与GDPval-AA排行榜发布
> [来源](https://twitter.com/ArtificialAnlys/status/1998841566627246173)
> 发布了轻量级开源智能体测试框架Stirrup，以及针对OpenAI GDPval任务（涵盖9个行业的真实知识工作）的新排行榜“GDPval-AA”。测试结果显示，Claude Opus 4.5领先，其次是GPT-5、Claude Sonnet 4.5，DeepSeek V3.2与Gemini 3 Pro并列。Stirrup框架在跨模型测试中的表现优于消费级聊天机器人UI。

---

### 5. 模型上下文协议（MCP）被捐赠至Linux基金会
> [来源](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)
> Anthropic宣布将Model Context Protocol（MCP）捐赠给Linux基金会，并由此成立了Agentic AI Foundation。此举旨在标准化工具、数据源和模型在“智能体”工作流中的互操作性，推动建立一个超越单一供应商的开放生态系统。

---

### 6. GitHub Copilot在VS Code中实现自动模型选择
> [来源](https://twitter.com/GHchangelog/status/1998847752050983279)
> GitHub Copilot的自动模型选择功能已在VS Code中正式发布（GA）。该功能能根据代码上下文和任务类型，自动为用户选择最合适的AI模型来提供补全或建议，优化开发体验和效率。

---

### 7. Google Jules智能体新增建议/计划任务与Render集成
> [来源](https://twitter.com/julesagent/status/1998829514634531252)
> Google的Jules智能体新增了“建议/计划任务”功能，并能与Render平台集成，实现自我修复部署。这推动了“持续AI”理念进入开发运维循环，使AI能够更主动地参与和管理软件生命周期。

---

### 8. Perceptron发布开源机器人感知模型Isaac-0.2
> [来源](https://twitter.com/perceptroninc/status/1998812935821697363)
> Perceptron发布了Isaac-0.2，这是一个包含10亿和20亿参数的混合推理视觉语言模型（结合SigLIP与Qwen），旨在为机器人提供强大的感知主干。其代码和权重已开源，并提供了API，路线图中包括视频原生和控制模态。

---

### 9. 开源视频生成与控制研究取得新进展
> 来源：文章内容
> Meta的研究展示了OneStory（具有自适应记忆的连贯多镜头视频生成）和Wan-Move（通过潜在轨迹引导实现运动可控的视频生成），扩展了视频生成的可控性。另一项研究“通过高效适配扩散Transformer实现反射消除”展示了高效的窗户反光清理技术。这些进展预示着视频生成与编辑能力正快速提升。

---

### 10. llama.cpp合并全新命令行界面体验
> [来源](https://github.com/ggml-org/llama.cpp/pull/17824)
> 流行的本地推理项目llama.cpp合并了一个全新的命令行界面（CLI）体验。新CLI提供了更友好的用户交互，支持`exit`、`regenerate`、`clear`、`read`等命令，并显示提示和生成的速度指标，增强了开发者和用户与本地模型交互的便利性。