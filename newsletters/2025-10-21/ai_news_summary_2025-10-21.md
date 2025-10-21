## AINews - 2025-10-21

> [原文链接](https://news.smol.ai/issues/25-10-16-claude-skills/)

## 📰 十大AI新闻要点

### 1. [Anthropic发布Agent Skills技术](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
> Anthropic推出Agent Skills，这是一种使用文件和文件夹构建专用代理的新方法。Skills是包含YAML元数据的Markdown文件，可选附带预写脚本，Claude最近的PDF、Docs和PPT创建能力都是通过Skills实现的。

---

### 2. [Claude 4.5 Haiku发布](https://twitter.com/ArtificialAnlys/status/1978661658290790612)
> Anthropic发布Claude 4.5 Haiku，定价为每100万输入/输出token 1/5美元。在推理模式下获得Artificial Analysis指数55分，比Sonnet 4.5便宜3倍，在长上下文和编码方面表现强劲。

---

### 3. [OpenAI产品更新](https://twitter.com/OpenAI/status/1978608684088643709)
> ChatGPT现在自动管理保存的记忆，具有搜索/排序和重新优先级功能；Sora 2为Pro用户添加故事板功能，所有用户视频长度延长至15秒，Pro用户可达25秒。

---

### 4. [vLLM推出TPU后端](https://twitter.com/vllm_project/status/1978855648176853100)
> vLLM与谷歌合作开发重新设计的TPU后端，通过单一JAX到XLA降低路径统一PyTorch和JAX，具有SPMD-by-default、Ragged Paged Attention v3等功能，吞吐量比2月原型提高2-5倍。

---

### 5. [Meta发布强化学习扩展定律研究](https://twitter.com/iScienceLuvr/status/1978793969384624226)
> Meta与合作者发布"强化学习计算扩展艺术"，40万GPU小时系统研究提出ScaleRL、CISPO损失、FP32 logits等技术，关键发现是目标计算性能可从半计算运行中预测。

---

### 6. [递归语言模型突破长上下文限制](https://twitter.com/a1zhang/status/1978948676287340753)
> 递归语言模型显示，在无界上下文上的递归自调用/工具可以超越标准GPT-5在长上下文任务上的表现，即使在1000万+token时仍保持成本效益。

---

### 7. [Cognition推出SWE-grep快速上下文模型](https://twitter.com/cognition/status/1978867021669413252)
> Cognition发布新的模型家族，用于快速多轮代理搜索，定位"正确文件"比Claude 4.5 Haiku快约20倍，在CodeSearch评估中与前沿模型相媲美。

---

### 8. [HuggingChat v2推出Omni功能](https://twitter.com/victormustar/status/1978817795312808065)
> HuggingChat v2推出"Omni"，基于策略的自动模型选择，覆盖115个开源模型和15个提供商，可以在一个会话中将任务路由到编码和写作模型之间。

---

### 9. [世界实验室发布实时世界模型RTFM](https://twitter.com/theworldlabs/status/1978839171058815380)
> RTFM是实时、持久、3D一致的自回归扩散变换器，在大规模视频上训练，以H100速度进行交互式流式传输。

---

### 10. [谷歌TPU向外部客户销售](https://twitter.com/zephyr_z9/status/1978835094216343820)
> 谷歌TPU现在向外部客户销售，直接与NVIDIA竞争，Baseten报告早期采用NVIDIA Dynamo后延迟降低50%，吞吐量提高60%以上。

---

## 🛠️ 十大工具产品要点

### 1. [Anthropic Skills开源文档技能](https://github.com/anthropics/skills/tree/main/document-skills)
> Anthropic在GitHub上开源了文档技能，涵盖.pdf、.docx、.xlsx和.pptx文件的创建和读取能力，完全通过Skills实现。

---

### 2. [Windows Copilot语音和视觉功能](https://twitter.com/mustafasuleyman/status/1978808627008847997)
> Windows 11添加Copilot语音("Hey Copilot")、跨桌面/应用/文档的视觉功能，以及即将推出的本地文件Copilot Actions。

---

### 3. [Perplexity语言学习和金融功能](https://twitter.com/perplexity_ai/status/1978859991152165125)
> Perplexity发布内置语言学习体验和新的金融功能（内幕交易追踪器），在iOS和网页端可用。

---

### 4. [Cline CLI预览版发布](https://twitter.com/cline/status/1978874789193486749)
> Cline CLI预览版暴露可编写脚本的开放"原始代理循环"，专为子代理和可组合工作流设计。

---

### 5. [Open Agent Builder开源画布](https://twitter.com/firecrawl_dev/status/1978878728827478289)
> 开源n8n风格画布，连接Firecrawl、LLM、逻辑节点和MCP，用于API可部署的工作流。

---

### 6. [Sourceful Riverflow 1图像编辑模型](https://twitter.com/ArtificialAnlys/status/1978891167795417092)
> Sourceful的Riverflow 1在Artificial Analysis图像编辑"全部"榜单中排名第一，结合VLM和开放扩散，定价为每1000张图像66美元。

---

### 7. [mixedbread.ai发布ColBERT边缘模型](https://twitter.com/mixedbreadai/status/1978853869557055492)
> mxbai-colbert-edge-v0提供可重现的ColBERT训练，17M模型在LongEmbed上排名小于10亿模型的第一，Apache 2.0许可。

---

### 8. [Alibaba开源Qwen3Guard安全组件](https://twitter.com/Alibaba_Qwen/status/1978732145297576081)
> 阿里巴巴开源Qwen3Guard组件，包括Qwen3-4B-SafeRL和Qwen3GuardTest，用于分类中间"思考"和逐token审核。

---

### 9. [Karpathy nanochat项目](https://twitter.com/karpathy/status/1978615547945521655)
> Karpathy的nanochat d32项目从零开始花费1000美元，将CORE改进到0.31，GSM8K达到约20%，完整报告和脚本已发布。

---

### 10. [Meta MobileLLM-Pro发布](https://twitter.com/_akhaliq/status/1978916251456925757)
> Meta发布MobileLLM-Pro 1B基础+指令检查点，针对高质量、高效的设备端推理，在推理/知识/长上下文检索上超越Gemma 3 1B和Llama 3.2 1B。

---