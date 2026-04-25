## AINews - 2026-04-25

> [原文链接](https://news.smol.ai/issues/26-04-23-gpt-55/)

## 📰 十大AI新闻要点

### 1. [OpenAI发布GPT-5.5旗舰模型，定位“真实工作与智能体”](https://x.com/OpenAI/status/2047376561205325845)
> OpenAI正式发布GPT-5.5，作为其新一代旗舰前沿模型，主打“真实工作和驱动智能体”。该模型立即在ChatGPT和Codex中上线，但API访问因额外的安全要求而被推迟。定价为每百万输入/输出token $5/$30，Pro版为$30/$180，是GPT-5.4价格的两倍。OpenAI强调其更强的编码、计算机使用、知识工作、科学研究以及更长的多步骤执行能力。

---

### 2. [GPT-5.5在多项基准测试中表现强劲，但独立评估显示幻觉率高达86%](https://x.com/ArtificialAnlys/status/2047378419282034920)
> OpenAI报告的基准测试成绩包括：Terminal-Bench 2.0达82.7%，OSWorld-Verified达78.7%，CyberGym达81.8%，SWE-Bench Pro达58.6%。ARC Prize验证其ARC-AGI-2得分达85.0%。然而，Artificial Analysis的独立评估显示，尽管GPT-5.5在其智能指数中排名第一，但其AA-Omniscience幻觉率高达86%，远高于Claude Opus 4.7的36%和Gemini 3.1 Pro Preview的50%，成为本次发布最重要的警示。

---

### 3. [GPT-5.5的Token效率显著提升，有效抵消了价格上涨](https://x.com/sama/status/2047378254575685707)
> Sam Altman和多位早期测试者指出，GPT-5.5在保持与GPT-5.4相似的每token速度的同时，每个任务使用的token数量显著减少。Artificial Analysis报告称，其Token使用量减少了约40%，使得运行其智能指数的净成本仅上升约20%。OpenAI还表示，Codex与GPT-5.5共同优化了服务栈，将token生成速度提升了20%以上。

---

### 4. [GPT-5.5与Nvidia GB200/GB300协同设计，标志着基础设施层面的深度合作](https://x.com/scaling01/status/2047377992016384068)
> OpenAI相关评论指出，GPT-5.5是与Nvidia GB200/GB300 NVL72协同设计的首个模型。Jonathan Ross也强调了从早期访问观察中看到的GB200 NVL72训练。这标志着模型架构与硬件基础设施之间的深度耦合，可能为未来的AI训练和推理效率带来显著提升。

---

### 5. [Codex随GPT-5.5发布重大升级，新增浏览器控制、文档处理等多项功能](https://x.com/ajambrosino/status/2047381565534322694)
> OpenAI在GPT-5.5发布的同时，对Codex产品进行了重大升级。新功能包括：浏览器控制、Sheets & Slides支持、文档与PDF处理、操作系统级语音输入、自动审查模式以及更广泛的计算机使用工作流。OpenAI明确将Codex + 5.5定位为不仅限于编码，而是适用于电子表格、幻灯片、文档和浏览器工作流的通用工具。

---

### 6. [早期用户报告显示GPT-5.5实现了长时间自主运行和“低微管理”工作模式](https://x.com/tszzl/status/2047386955550470245)
> 多位OpenAI内部用户和早期测试者分享了令人印象深刻的案例：研究人员让GPT-5.5仅凭高层级想法运行过夜实验，第二天早上就完成了完整的实验扫描；一位用户离开数天后回来，发现GPT-5.5监督下完成了一次31小时的工业级强化学习运行。这些案例标志着AI从“问答工具”向“自主工作代理”的转变。

---

### 7. [Google DeepMind发布“Vision Banana”统一视觉模型，重新定义图像生成](https://x.com/arankomatsuzaki/status/2047139493543846251)
> Google DeepMind的“Vision Banana”模型引起了广泛关注，它将图像理解和生成统一为一个模型，将图像生成重新定义为视觉任务的通用接口。支持者认为生成式感知可能成为计算机视觉的基础，但同时也指出扩散延迟和实际限制仍是主要障碍。Sam Altman也表示，OpenAI的Images 2.0已经跨越了一个重要的质量门槛。

---

### 8. [DeepSeek发布DeepEP V2和TileKernels，实现线性扩展的并行处理](https://github.com/deepseek-ai/TileKernels)
> DeepSeek发布了DeepEP V2和TileKernels，这是深度学习并行化技术的重大进展。TileKernels引入了一种新颖的内核执行方法，据称实现了线性扩展，即计算资源翻倍可直接带来处理速度翻倍。这对比OpenAI的封闭模式，DeepSeek的开源策略赢得了社区的广泛赞誉。

---

### 9. [Qwen 3.6-27B发布：27B参数密集模型在编码基准上超越397B MoE模型](https://huggingface.co/Qwen/Qwen3.6-27B)
> 阿里云发布了Qwen 3.6-27B，这是一个仅有27B参数的密集模型，但在主要编码基准测试中超越了其更大的397B MoE模型Qwen3.5-397B-A17B。具体成绩包括：SWE-bench Verified 77.2 vs 76.2，Terminal-Bench 2.0 59.3 vs 52.5。该模型支持“思考”和“非思考”两种模式，并以Apache 2.0许可证完全开源。

---

### 10. [Google DeepMind发布Decoupled DiLoCo，实现跨数据中心异构硬件训练](https://x.com/GoogleDeepMind/status/2047330981145669790)
> Google DeepMind/Google Research发布了Decoupled DiLoCo，这是一种针对低带宽网络、异构硬件且训练不会因硬件故障而中断的多数据中心训练技术。Google表示，他们已成功使用该技术在美国四个地区训练了一个12B Gemma模型，并混合使用了TPU6e和TPUv5p，且未减慢训练速度。这为解决大规模AI训练的基础设施瓶颈提供了重要思路。

---

## 🛠️ 十大工具产品要点

### 1. [GPT-5.5 - OpenAI旗舰模型](https://x.com/OpenAI/status/2047376561205325845)
> OpenAI最新旗舰模型，定价$5/$30（输入/输出每百万token），Pro版$30/$180。支持1M上下文（API）和400K上下文（Codex）。与Nvidia GB200/GB300协同设计，Token效率比GPT-5.4提升约40%。已在ChatGPT和Codex上线，API访问推迟。

---

### 2. [Codex - 升级版AI编程与桌面自动化工具](https://x.com/ajambrosino/status/2047381565534322694)
> 随GPT-5.5发布重大升级，新增功能包括：浏览器控制、Sheets & Slides支持、文档与PDF处理、操作系统级语音输入、自动审查模式。定位从编程工具扩展为通用计算机工作助手，支持长时间自主运行。

---

### 3. [Qwen 3.6-27B - 阿里云开源密集编码模型](https://huggingface.co/Qwen/Qwen3.6-27B)
> 27B参数密集模型，在编码基准上超越397B MoE模型。支持思考/非思考双模式，Apache 2.0开源。社区报告可在16GB VRAM上运行32K上下文，或在24GB VRAM上运行200K上下文。本地运行成本极低（8小时电费<$4 vs API成本$142）。

---

### 4. [DeepSeek TileKernels - 线性扩展并行处理内核](https://github.com/deepseek-ai/TileKernels)
> DeepSeek开源的新型内核执行库，据称实现线性扩展（计算资源翻倍=速度翻倍）。包含针对Engram和mHC的优化内核，部分已用于内部训练和推理。配套发布的DeepEP V2进一步增强了模型效率和可扩展性。

---

### 5. [Qwen3 TTS / Handcrafted Persona Engine - 本地实时语音合成](https://github.com/fagenorn/handcrafted-persona-engine)
> 基于Qwen3 TTS的本地实时语音合成系统，利用滑动窗口解码器架构实现可靠流式传输。集成llama.cpp加速，实现CTC词级对齐和音素提取。支持情感标签和语音克隆微调，被评价为“最具表现力的开源TTS模型之一”。

---

### 6. [Hermes Desktop - 直接SSH桌面代理](https://x.com/DODOREACH/status/2047089899807895903)
> 强调直接SSH连接，无需浏览器/网关层的桌面代理工具。已支持通过ChatGPT/Codex OAuth集成GPT-5.5，提供更直接、低延迟的远程服务器操作体验。

---

### 7. [LangSmith Fleet - 文件编辑与演示构建工具](https://x.com/LangChain/status/2047362259983495215)
> LangChain推出的新功能，支持直接文件创建/编辑和演示文稿构建。使AI代理能够更自然地与办公文档和工作流交互，扩展了AI在生产力工具中的应用场景。

---

### 8. [Trackio - LLM定制实验仪表盘](https://x.com/abidlabs/status/2047337026161184825)
> 解耦前后端，使LLM能够定制实验仪表盘。为AI研究人员和工程师提供了更灵活的实验监控和可视化工具，支持自动化实验管理和结果分析。

---

### 9. [Atomic Chat - 本地模型推理服务器](https://atomic.chat/)
> 支持Qwen3.6 35B和27B模型的本地推理服务器，源代码开源。在MacBook Pro M5Max上，35B模型达到65 tokens/s，27B模型达到24 tokens/s。支持Google TurboQuant等优化技术。

---

### 10. [Hermes Agent - 第三方GPT-5.5集成代理](https://x.com/Teknium/status/2047419336537846193)
> 通过ChatGPT/Codex OAuth快速集成GPT-5.5的第三方代理工具。展示了GPT-5.5生态系统的快速扩展能力，为用户提供了除官方客户端外的更多使用选择。