## AINews - 2026-01-22

> [原文链接](https://news.smol.ai/issues/26-01-20-not-much/)

## 📰 十大AI新闻要点

### 1. X（原Twitter）开源其“For You”推荐算法
> X Engineering 宣布开源其新的推荐/排名算法栈，该算法采用与 xAI 的 Grok 模型相同的 Transformer 架构。代码已发布在 GitHub 上，引发了社区关于算法透明度、公平性以及平台产品激励的广泛讨论。
> 来源：https://twitter.com/XEng/status/2013471689087086804

---

### 2. GLM-4.7-Flash 成为本地推理新宠
> Z.ai 发布的 GLM-4.7-Flash（30B-A3B MoE）模型因其卓越的每参数性能受到关注。该模型支持 200K 上下文，声称在 SWE-Bench 和 GPQA 等基准测试中表现最佳，并能在 24GB 内存的机器上本地运行，已迅速集成到 llama.cpp 和 Ollama 等生态中。
> 来源：https://huggingface.co/zai-org/GLM-4.7-Flash

---

### 3. Google AI 揭示推理模型的“思想社会”机制
> Google AI 的研究论文指出，像 OpenAI o-series、DeepSeek-R1 这样的推理模型的性能提升，不仅源于“思考更久”，更关键的是模型内部出现了类似辩论的模式（质疑、探索替代方案、分歧、收敛）。这种“思想社会”机制被证明能带来超过 20% 的准确率优势。
> 来源：https://twitter.com/rohanpaul_ai/status/2013431689889095767

---

### 4. 微软暂停内部 Claude Code 部署，力推 GitHub Copilot
> 据报道，微软 CEO 萨提亚·纳德拉介入，暂停了 Claude Code 在内部的广泛部署，转而要求员工使用 GitHub Copilot，理由是后者已“基本弥补了与 Claude Code 的差距”。此举被视为微软推动自身产品内部使用的战略举措。
> 来源：文章内容

---

### 5. OpenAI 全球推出 ChatGPT 年龄预测功能
> OpenAI 宣布在全球范围（欧盟稍后）推出年龄预测功能，以检测可能的未成年账户并应用青少年安全保护措施。成年用户可通过验证进行覆盖。此举引发了关于其动机（如广告策略）的讨论。
> 来源：https://twitter.com/OpenAI/status/2013688237772898532

---

### 6. 递归语言模型（RLM）被视为生产级 Agent 的关键抽象
> 社区讨论认为，RLM 是管理长运行系统（如 Agent）中计算、上下文和递归的有前景的抽象。其核心优势在于“符号递归”，允许模型委托许多子任务而无需将所有中间步骤作为 Token 输出，从而避免上下文窗口爆炸。
> 来源：https://twitter.com/doesdatmaksense/status/2013534540300722278

---

### 7. DeepMind 联合创始人哈萨比斯在达沃斯谈 AI 治理与突破
> 在达沃斯论坛上，DeepMind 联合创始人德米斯·哈萨比斯强调了“科学家主导”的实验室在安全治理上的优势，并指出物理智能/机器人学是近期可能取得突破的领域。他表示，如果全球协调一致，他会支持暂停 AI 研发。
> 来源：https://twitter.com/scaling01/status/2013651299519074729

---

### 8. DeepSeek-R1 发布一周年，其影响持续发酵
> 社区纪念 DeepSeek-R1 发布一周年，认为其“DeepSeek 时刻”深刻影响了行业：强调了推理作为核心能力、推广了高效的训练方法、鼓励了更小更智能的模型开发，并促进了在新兴市场的采用和模块化 AI 系统的趋势。
> 来源：文章内容

---

### 9. 合成推理数据研究：在相同计算预算下，“更多采样”优于“更大模型”
> DeepMind 的研究总结指出，在匹配计算预算的情况下，使用更小的模型生成更多的合成推理数据尝试，比使用更大模型生成更少数据效果更好。这种方法能提升数据覆盖度（+11%）和多样性（+86%），报告的训练收益最高达 31.6%。
> 来源：https://twitter.com/LiorOnAI/status/2013582631124771104

---

### 10. 文档处理成为企业级 Agent 的主导工作流
> 随着 LightOn 发布开源的 10 亿参数 OCR 模型，文档处理智能体的成本持续下降。行业观察指出，文档处理（尤其是在金融服务领域）正成为企业部署 AI Agent 的主要工作流基础。
> 来源：https://twitter.com/jerryjliu0/status/2013695214008049890

---

## 🛠️ 十大工具产品要点

### 1. GLM-4.7-Flash 模型发布与本地优化
> GLM-4.7-Flash 是一个 30B-A3B 的混合专家模型，专为高效部署设计。它采用 MLA 注意力机制以最小化 KV 缓存内存占用，支持 200K 上下文。社区已为其提供了 GGUF 量化版本，并集成到 llama.cpp、vLLM、SGLang 等框架中，但量化版本存在循环问题，建议使用 BF16 或调整 `--dry-multiplier` 参数。
> 来源：https://huggingface.co/unsloth/GLM-4.7-Flash-GGUF

---

### 2. Liquid AI 发布超小型设备端推理模型 LFM2.5-1.2B-Thinking
> Liquid AI 发布了 LFM2.5-1.2B-Thinking，这是一个专为手机级硬件设计的设备端推理模型，内存占用约 900MB。它强调简洁的推理轨迹，并在工具使用、数学和指令遵循方面表现良好，已迅速被 Ollama 收录。
> 来源：https://twitter.com/liquidai/status/2013633347625324627

---

### 3. Unsloth 提供 GLM-4.7-Flash 的优化运行方案
> Unsloth 积极推广 GLM-4.7-Flash 的本地运行故事，提供具体的配置建议，如使用 UD-Q4_K_XL 及以上量化、设置 `--temp 0.2 --top-k 50 --top-p 0.95 --min-p 0.01 --dry-multiplier 1.1` 以减少重复，并详细说明了 KV 缓存和 MLA 的实际成本。
> 来源：https://twitter.com/UnslothAI/status/2013482180564132092

---

### 4. 纯 JavaScript + WebGPU 在浏览器中运行 1 亿参数语音模型
> 开发者展示了使用纯 JavaScript 和 WebGPU（通过 jax-js）在浏览器中运行约 1 亿参数的 Kyutai 语音模型。这一部署壮举突出了低依赖摩擦和实用的语音克隆灵活性。
> 来源：https://twitter.com/ekzhang1/status/2013455049175748791

---

### 5. LightOn 发布开源 10 亿参数 OCR 模型
> LightOn 在 Apache-2.0 许可证下发布了一个 10 亿参数的 OCR 模型，声称具有强大的速度/成本特性（例如“每千页成本低于 0.01 美元”），并支持 transformers 库。
> 来源：https://twitter.com/mervenoyann/status/2013577704419819942

---

### 6. LangChain 推出基于 Trace 的“洞察智能体”
> 随着每日 Trace 数量超过 10 万，LangChain 提出需要“洞察智能体”来对 Trace 进行聚类和模式发现，以应对传统监控和手动日志审查的不足，将 Trace 理解提升为产品的一级需求。
> 来源：https://twitter.com/LangChain/status/2013642970944413905

---

### 7. Weaviate 支持在 NVIDIA Jetson 上进行本地 CLIP 推理
> Weaviate 增加了对 NVIDIA Jetson 上 CLIP 推理的支持，使得构建本地多模态嵌入/搜索管道成为可能，无需云端往返即可实现文本-图像检索。
> 来源：https://twitter.com/philipvollet/status/2013630649492468041

---

### 8. 社区展示 4 台 M4 Pro Mac Mini 集群运行 GLM-4.7-Flash
> 开发者利用 RDMA over Thunderbolt 和 MLX 后端，在 4 台 M4 Pro Mac Mini 上通过张量并行运行 GLM-4.7-Flash，实现了约 100 tok/s 的吞吐量，目标是达到 200 tok/s。
> 来源：https://twitter.com/alexocheema/status/2013694573910937980

---

### 9. 开发者构建 768GB VRAM 的移动式 10 GPU AI 系统
> 有开发者分享了一个定制构建的移动 AI 系统，采用 Threadripper Pro 3995WX CPU、512GB RAM，并组合了 8 块 RTX 3090 和 2 块 RTX 5090 GPU，总成本约 1.7 万美元，旨在本地运行 DeepSeek、Kimi K2 等大型 MoE 模型。
> 来源：文章内容

---

### 10. Ollama 正式支持将 Claude Code 与本地模型结合使用
> Ollama 宣布官方支持将 Claude Code 与本地模型（如 GLM-4.7-Flash）结合使用。这允许开发者在本地环境中利用 Claude Code 的界面和工具调用能力，配合私有 LLM 进行无限次数的迭代开发。
> 来源：文章内容

---