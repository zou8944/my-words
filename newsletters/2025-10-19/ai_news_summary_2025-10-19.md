## AINews - 2025-10-19

> [原文链接](https://news.smol.ai/issues/25-10-16-claude-skills/)

## 📰 十大AI新闻要点

### 1. [Anthropic发布Agent Skills技术](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
> Anthropic推出Agent Skills，这是一种使用文件和文件夹构建专门代理的新方法。Skills是包含YAML元数据的Markdown文件，可选的脚本和文档，让模型能够执行特定任务。Claude最近的PDF、Docs和PPT创建和阅读功能都是通过Skills实现的。

---

### 2. [Claude 4.5 Haiku发布，性价比极高](https://twitter.com/ArtificialAnlys/status/1978661658290790612)
> Anthropic发布Claude 4.5 Haiku，定价为每100万输入/输出token 1/5美元。在推理模式下，在Artificial Analysis指数上得分为55，比Sonnet 4.5便宜3倍，在长上下文和编码方面表现强劲。

---

### 3. [vLLM推出重新设计的TPU后端](https://twitter.com/vllm_project/status/1978855648176853100)
> vLLM与谷歌合作开发了重新设计的TPU后端，通过单一JAX到XLA降低路径统一PyTorch和JAX，具有SPMD-by-default、Ragged Paged Attention v3等功能，吞吐量比2月原型提高2-5倍。

---

### 4. [Meta发布强化学习扩展定律研究](https://twitter.com/iScienceLuvr/status/1978793969384624226)
> Meta与合作者发布"强化学习计算扩展艺术"，这是一个40万GPU小时的系统研究，提出了ScaleRL、CISPO损失、FP32 logits等技术。关键发现：目标计算性能可以从半计算运行中预测。

---

### 5. [递归语言模型在长上下文任务中超越GPT-5](https://twitter.com/a1zhang/status/1978948676287340753)
> 递归语言模型(RLMs)显示，在无限制上下文上的递归自调用/工具可以超越标准GPT-5在长上下文任务中的表现，即使在1000万+token时仍保持成本效益。

---

### 6. [Cognition推出快速上下文搜索模型](https://twitter.com/cognition/status/1978867021669413252)
> Cognition推出新的模型家族(>2800 TPS)，用于快速多轮代理搜索，在Cognition的CodeSearch评估中比Claude 4.5 Haiku快约20倍，同时与前沿模型相媲美。

---

### 7. [OpenAI更新ChatGPT记忆和Sora功能](https://twitter.com/OpenAI/status/1978608684088643709)
> ChatGPT现在自动管理保存的记忆，具有搜索/排序和重新优先级功能；Sora 2为Pro用户添加故事板功能，并将视频长度扩展到所有用户15秒，Pro用户25秒。

---

### 8. [Google TPU现在向外部客户销售](https://twitter.com/zephyr_z9/status/1978835094216343820)
> Google TPU现在直接向外部客户销售，与NVIDIA直接竞争。Baseten报告早期采用NVIDIA Dynamo后延迟降低50%，吞吐量提高60%以上。

---

### 9. [Windows 11添加Copilot语音和视觉功能](https://twitter.com/mustafasuleyman/status/1978808627008847997)
> Windows 11添加"Hey Copilot"语音命令、跨桌面/应用/文档的视觉功能，以及即将推出的本地文件Copilot Actions。

---

### 10. [HuggingChat v2推出Omni模型选择系统](https://twitter.com/victormustar/status/1978817795312808065)
> HuggingChat v2推出"Omni"，基于策略的自动模型选择，涵盖115个开源模型和15个提供商，可以在一个会话中在编码和写作模型之间路由任务。

---

## 🛠️ 十大工具产品要点

### 1. [Anthropic Skills GitHub仓库](https://github.com/anthropics/skills/tree/main/document-skills)
> Anthropic开源了Skills仓库，包含.pdf、.docx、.xlsx和.pptx文件的文档创建技能，这些技能完全使用Skills技术实现。

---

### 2. [Cognition SWE-grep快速搜索](https://cognition.ai/blog/swe-grep)
> Cognition的SWE-grep模型专为快速代理搜索设计，吞吐量超过2800 TPS，在Windsurf中通过Fast Context子代理集成，比之前快20倍。

---

### 3. [HuggingFace Modular Diffusers自定义块](https://huggingface.co/docs/diffusers/main/en/modular_diffusers/pipeline_block)
> HuggingFace的Modular Diffusers现在支持自定义块，允许开发人员实现新功能并无缝集成到核心库中。

---

### 4. [PyTorch 2.9对称内存功能](https://pytorch.org/blog/pytorch-2-9/)
> PyTorch 2.9引入对称内存功能，简化了多GPU内核编程，支持内核内通信、超低延迟远程访问和自定义通信模式。

---

### 5. [mixedbread.ai的ColBERT边缘模型](https://twitter.com/mixedbreadai/status/1978853869557055492)
> mixedbread.ai发布mxbai-colbert-edge-v0(17M, 32M)模型，提供可重现的ColBERT训练，17M版本在LongEmbed上排名第一。

---

### 6. [Sourceful Riverflow 1图像编辑](https://twitter.com/ArtificialAnlys/status/1978891167795417092)
> Sourceful的Riverflow 1在Artificial Analysis图像编辑排行榜上排名第一，结合VLM和开放扩散，定价为每1000张图像66美元。

---

### 7. [Alibaba Qwen3Guard安全组件](https://twitter.com/Alibaba_Qwen/status/1978732145297576081)
> Alibaba开源Qwen3Guard组件，包括Qwen3-4B-SafeRL和Qwen3GuardTest，用于分类中间"思考"和逐token审核。

---

### 8. [Cline CLI代理循环](https://twitter.com/cline/status/1978874789193486749)
> Cline CLI(预览版)暴露可编写脚本的开放"原始代理循环"，IDE Cline可以编排，专为子代理和可组合工作流设计。

---

### 9. [Open Agent Builder工作流工具](https://twitter.com/firecrawl_dev/status/1978878728827478289)
> Open Agent Builder是一个n8n风格的开源画布，连接Firecrawl、LLM、逻辑节点和MCP，用于API可部署的工作流。

---

### 10. [PaddleOCR-VL文档智能](https://twitter.com/PaddlePaddle/status/1978809999263781290)
> PaddleOCR-VL(0.9B)针对工业文档智能(文本、表格、公式、图表、手写)，支持109种语言，由NaViT + ERNIE提供支持。

---