## AINews - 2025-10-20

> [原文链接](https://news.smol.ai/issues/25-10-16-claude-skills/)

## 📰 十大AI新闻要点

### 1. [Anthropic发布Agent Skills框架](https://www.anthropic.com/news/skills)
> Anthropic推出Agent Skills，这是一种使用Markdown文件和文件夹构建专用代理的新方法。该框架包含可选的脚本和文档，模型可以在运行时加载以完成任务。Claude最近的PDF、Docs和PPT创建功能都是通过Skills实现的。

---

### 2. [Claude 4.5 Haiku发布](https://twitter.com/ArtificialAnlys/status/1978661658290790612)
> Anthropic发布价值级模型Claude 4.5 Haiku，定价为每100万输入/输出token 1/5美元。在推理模式下，该模型在Artificial Analysis指数上得分为55，比Sonnet 4.5便宜3倍，在长上下文和编码方面表现强劲。

---

### 3. [OpenAI产品更新：ChatGPT记忆管理和Sora 2增强](https://twitter.com/OpenAI/status/1978608684088643709)
> ChatGPT现在可以自动管理保存的记忆，具有搜索/排序和重新优先级排序功能，解决了"内存已满"问题。Sora 2为Pro用户添加了故事板功能，并将视频长度扩展到所有用户15秒，Pro用户25秒。

---

### 4. [vLLM推出TPU后端](https://twitter.com/vllm_project/status/1978855648176853100)
> vLLM与Google合作开发了重新构想的TPU后端，通过单一JAX到XLA降低路径统一了PyTorch和JAX，具有SPMD-by-default、Ragged Paged Attention v3等功能，吞吐量比2月原型提高了2-5倍。

---

### 5. [Meta发布强化学习扩展定律研究](https://twitter.com/iScienceLuvr/status/1978793969384624226)
> Meta与合作者发布了"为LLMs扩展强化学习计算的艺术"，这是一个40万GPU小时的系统研究，提出了ScaleRL、CISPO损失、FP32 logits等技术，关键发现是目标计算性能可以从半计算运行中预测。

---

### 6. [递归语言模型在长上下文任务中表现出色](https://twitter.com/a1zhang/status/1978948676287340753)
> 递归语言模型显示，在无界上下文上的递归自调用/工具可以超越标准GPT-5在长上下文任务上的表现，即使在1000万+token时仍保持成本效益。

---

### 7. [Cognition推出快速上下文搜索模型](https://twitter.com/cognition/status/1978867021669413252)
> Cognition的新模型家族(>2,800 TPS)用于快速多轮代理搜索，定位"正确文件"的速度比Claude 4.5 Haiku快20倍，同时在CodeSearch评估中与前沿模型相媲美。

---

### 8. [HuggingChat v2推出Omni功能](https://twitter.com/victormustar/status/1978817795312808065)
> HuggingChat v2推出"Omni"，基于策略的自动模型选择，涵盖115个开源模型和15个提供商，可以在一个会话中将任务路由到编码和写作模型之间，100%开源。

---

### 9. [Windows 11 Copilot功能增强](https://twitter.com/mustafasuleyman/status/1978808627008847997)
> Windows 11添加了Copilot Voice("Hey Copilot")、跨桌面/应用/文档的Vision功能，以及即将推出的本地文件Copilot Actions。

---

### 10. [Google TPU现在向外部客户销售](https://twitter.com/zephyr_z9/status/1978835094216343820)
> Google TPU现在直接向外部客户销售，与NVIDIA直接竞争，标志着AI硬件市场竞争格局的重大变化。

---

## 🛠️ 十大工具产品要点

### 1. [Anthropic Skills GitHub仓库](https://github.com/anthropics/skills/tree/main/document-skills)
> Anthropic在GitHub上开源了文档技能，包括.pdf、.docx、.xlsx和.pptx文件的创建能力，这些完全使用Skills框架实现。

---

### 2. [Cline CLI预览版发布](https://twitter.com/cline/status/1978874789193486749)
> Cline CLI预览版暴露了一个可编写脚本的、开放的"原始代理循环"，IDE Cline可以编排这些循环，专为子代理和可组合工作流设计。

---

### 3. [Open Agent Builder开源画布](https://twitter.com/firecrawl_dev/status/1978878728827478289)
> 类似n8n风格的开源画布，连接Firecrawl、LLMs、逻辑节点和MCPs，用于API可部署的工作流。

---

### 4. [Sourceful Riverflow 1图像编辑工具](https://twitter.com/ArtificialAnlys/status/1978891167795417092)
> Sourceful的Riverflow 1在Artificial Analysis的图像编辑"全部"列表中排名第一，结合了VLM和开放扩散，定价为每1000张图像66美元。

---

### 5. [mixedbread.ai的ColBERT嵌入模型](https://twitter.com/mixedbreadai/status/1978853869557055492)
> mixedbread.ai的mxbai-colbert-edge-v0(17M, 32M)提供可重现的ColBERT训练，17M版本在LongEmbed上排名小于10亿参数模型的第一，Apache 2.0许可。

---

### 6. [Alibaba开源Qwen3Guard安全组件](https://twitter.com/Alibaba_Qwen/status/1978732145297576081)
> Alibaba开源了Qwen3Guard组件，包括Qwen3-4B-SafeRL(WildJailbreak从64.7提升到98.1而不影响一般性能)和Qwen3GuardTest用于分类中间"思考"和逐token审核。

---

### 7. [Karpathy的nanochat项目](https://twitter.com/karpathy/status/1978615547945521655)
> Karpathy的nanochat d32(从头开始花费1000美元)将CORE改进到0.31(> GPT-2 ~0.26)，GSM8K达到约20%，发布了完整报告/脚本，社区正在集成到Transformers和vLLM中。

---

### 8. [Meta MobileLLM-Pro发布](https://twitter.com/_akhaliq/status/1978916251456925757)
> Meta发布MobileLLM-Pro(1B)基础+指令检查点(带有量化变体)，针对高质量、高效的设备上推理，在推理/知识/长上下文检索上优于Gemma 3 1B和Llama 3.2 1B 5.7%和7.9%。

---

### 9. [Google torchax项目](https://twitter.com/gallabytes/status/1978860154008240142)
> Google发布torchax，探索PyTorch→JAX降低，为跨框架互操作性提供新工具。

---

### 10. [World Labs RTFM实时世界模型](https://twitter.com/theworldlabs/status/1978839171058815380)
> World Labs的RTFM是实时、持久、3D一致的自回归扩散变换器，在大规模视频上训练，以H100速度进行交互式流式传输，带有实时演示。

---