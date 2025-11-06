## AINews - 2025-11-06

> [原文链接](https://news.smol.ai/issues/25-11-04-not-much/)

## 📰 十大AI新闻要点

### 1. [Google太空TPU项目Suncatcher](https://twitter.com/sundarpichai/status/1985754323813605423)
> Google正在轨道上原型化可扩展的ML计算系统以利用丰富的太阳能。早期测试显示Trillium代TPU在粒子加速器辐射中存活；下一个里程碑是到2027年初与Planet合作发射两颗原型卫星。关键挑战包括热管理和在轨可靠性。

---

### 2. [中国数据中心补贴政策影响全球竞争](https://twitter.com/teortaxesTex/status/1985540154065318157)
> 中国对数据中心提供50%电力补贴可能消除每FLOP成本水平的效率差距，能源价格支持抵消了芯片效率劣势；华为计划到2027年为DeepSeek建设千兆瓦级SuperPoD。

---

### 3. [DeepMind发布IMO数学推理基准套件](https://twitter.com/iScienceLuvr/status/1985685404276965481)
> 包含IMO-AnswerBench（答案）、IMO-ProofBench（证明写作）和IMO-GradingBench（LLM评分）。在ProofBench上，Gemini DeepThink在基础集达到89.0%；大多数模型得分<60%。在高级集上，非Gemini模型<25%，而最佳内部模型通过人工评估达到65.7%。

---

### 4. [Generalist AI发布GEN-0机器人基础模型](https://twitter.com/GeneralistAI/status/1985742083806937218)
> 基于27万+小时灵巧数据训练的大型机器人基础模型，报告显示强大的缩放定律（更多预训练+模型大小=更好），强调"物理常识"（抓取、稳定、放置）。定位为由数据丰富驱动的通用机器人发展路径。

---

### 5. [Anthropic推出MCP代码执行工程指南](https://twitter.com/AnthropicAI/status/1985846791842250860)
> 强调使用更多工具来降低token消耗，展示代理如何高效执行代码和管理多个工具。MCP协议正在成为工具启用代理的实际标准模式。

---

### 6. [llama.cpp发布新官方WebUI](https://twitter.com/ggerganov/status/1985727389926555801)
> 为15万+ GGUF模型提供精炼的移动友好本地聊天体验，具有PDF/图像摄取、对话分支、JSON模式约束生成、数学/代码渲染和并行聊天功能，被广泛赞誉为"本地AI最佳"基准。

---

### 7. [Epoch AI发布前沿数据中心追踪平台](https://twitter.com/EpochAIResearch/status/1985788184245293153)
> 通过卫星图像和公开文件追踪1GW+ AI数据中心，数据免费发布。同时批评OSWorld基准测试任务过于简单且评估存在缺陷。

---

### 8. [Deutsche Telekom与NVIDIA宣布11亿美元慕尼黑设施](https://twitter.com/scaling01/status/1985741851991621712)
> 投资11亿美元建设慕尼黑设施，配备1万个GPU（DGX B200 + RTX Pro），显示欧洲在AI计算基础设施方面的重大投资。

---

### 9. [OpenAI限制ChatGPT提供医疗法律建议](https://www.you.wish)
> 由于诉讼担忧，OpenAI正在限制ChatGPT提供医疗、法律和财务建议，引发关于AI监管必要性和潜在过度监管的辩论。

---

### 10. [Getty Images在英国AI图像生成器诉讼中败诉](https://www.reuters.com/sustainability/boards-policy-regulation/getty-images-largely-loses-landmark-uk-lawsuit-over-ai-image-generator-2025-11-04/)
> Getty Images在英国针对AI图像生成器的具有里程碑意义的诉讼中大部分败诉，这对AI生成内容的版权问题产生重要影响。

---

## 🛠️ 十大工具产品要点

### 1. [Reka发布免费MCP服务器](https://twitter.com/RekaAILabs/status/1985794490116780052)
> 在VS Code内部提供搜索/事实检查功能的免费MCP服务器，增强开发者在IDE内的AI辅助工具体验。

---

### 2. [LitServe实现MCP服务器快速部署](https://twitter.com/_avichawla/status/1985595667079971190)
> 使用基于FastAPI的LitServe，约10行代码即可将任何模型/RAG/代理作为MCP服务器提供服务，并可连接到Claude Desktop。

---

### 3. [lighteval基准测试工具更新](https://twitter.com/nathanhabib1011/status/1985720151673880923)
> 添加基准查找器、inspect-ai集成、评估共享和新任务（gsm_plus、MMLU redux、filipino、ifbench、slr-bench等）。

---

### 4. [MLX-Swift添加连续批处理功能](https://twitter.com/ronaldmannak/status/1985693207003275729)
> 为本地多流推理添加连续批处理（在新请求到达时自动将单请求流升级为批处理），提升本地推理效率。

---

### 5. [GitHub Copilot性能大幅提升](https://twitter.com/github/status/1985737580613140747)
> 通过更快的自定义模型实现3倍更高的token吞吐量、12%更高的接受率和35%更低的延迟。

---

### 6. [vLLM持续快速扩展覆盖](https://twitter.com/vllm_project/status/1985589446197330129)
> 支持PaddleOCR-VL并在nightly版本中运行Ouro（循环潜在推理LM），继续引领LLM服务技术发展。

---

### 7. [Fenic与OpenRouter集成](https://github.com/typedef-ai/fenic)
> Fenic数据框架API与OpenRouter集成，在单个会话中运行混合提供者AI工作流程，支持LLM ETL、上下文工程、代理内存和代理工具。

---

### 8. [Windsurf发布Codemaps](https://xcancel.com/windsurf/status/1985757575745593459)
> 使用SWE-1.5和Sonnet 4.5构建的AI驱动工具，创建代码库的交互式可视化地图以增强理解和生产力，对抗"代码混乱"。

---

### 9. [Tritex实现Triton中LLM预训练](https://github.com/martin-kukla/tritex)
> 在Triton中从零开始进行LLM预训练，在A100 SXM上以57.5% MFU复制GPT2 1.6B，展示高效的训练基础设施。

---

### 10. [Roblox开源PII分类器](https://huggingface.co/Roblox/roblox-pii-classifier)
> 处理61亿条日常消息，达到20万查询/秒的处理速度，P90延迟低于100毫秒，为大规模AI应用提供高效PII检测解决方案。

---