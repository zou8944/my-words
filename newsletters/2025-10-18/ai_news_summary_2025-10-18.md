## AINews - 2025-10-18

> [原文链接](https://news.smol.ai/issues/25-10-16-claude-skills/)

## 📰 十大AI新闻要点

### 1. [Anthropic发布Agent Skills技术](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
> Anthropic推出Agent Skills，这是一种通过Markdown文件和文件夹构建专用代理的新方法。该技术已用于实现Claude的PDF、Docs和PPT文档创建与读取功能，被认为是比MCP更重要的技术突破。

---

### 2. [Claude 4.5 Haiku发布](https://twitter.com/ArtificialAnlys/status/1978661658290790612)
> Anthropic发布性价比更高的Claude 4.5 Haiku模型，定价为每100万输入/输出token 1美元/5美元，在推理模式下获得Artificial Analysis指数55分，比Sonnet 4.5便宜3倍，在长上下文和编码方面表现强劲。

---

### 3. [OpenAI多项产品更新](https://twitter.com/OpenAI/status/1978608684088643709)
> ChatGPT新增自动内存管理功能，解决"内存已满"问题；Sora 2为Pro用户添加故事板功能，所有用户视频长度提升至15秒，Pro用户可达25秒。

---

### 4. [vLLM推出TPU后端](https://twitter.com/vllm_project/status/1978855648176853100)
> vLLM与谷歌合作开发重新设计的TPU后端，通过单一JAX到XLA降低路径统一PyTorch和JAX，相比2月原型吞吐量提升2-5倍，支持Trillium和v5e。

---

### 5. [Meta发布强化学习扩展定律研究](https://twitter.com/iScienceLuvr/status/1978793969384624226)
> Meta与合作者发布40万GPU小时的系统性研究"强化学习计算扩展艺术"，提出ScaleRL方法，关键发现是目标计算性能可以从半计算运行中预测。

---

### 6. [递归语言模型突破长上下文限制](https://twitter.com/a1zhang/status/1978948676287340753)
> 递归语言模型通过无限制上下文的自调用和工具使用，在长上下文任务上超越标准GPT-5，即使在1000万+token时仍保持成本效益。

---

### 7. [Cognition推出快速上下文搜索模型](https://twitter.com/cognition/status/1978867021669413252)
> Cognition发布SWE-grep模型系列，吞吐量超过2800 TPS，在代码搜索评估中比Claude 4.5 Haiku快20倍，同时与前沿模型性能相当。

---

### 8. [Google TPU向外部客户销售](https://twitter.com/zephyr_z9/status/1978835094216343820)
> Google TPU现在直接向外部客户销售，与NVIDIA展开直接竞争，标志着AI硬件市场竞争格局的重大变化。

---

### 9. [实时世界模型RTFM发布](https://twitter.com/theworldlabs/status/1978839171058815380)
> World Labs推出RTFM，这是一个实时、持久、3D一致的自回归扩散变换器，在大规模视频上训练，可在H100速度下进行交互式流式传输。

---

### 10. [HuggingChat v2推出Omni功能](https://twitter.com/victormustar/status/1978817795312808065)
> HuggingChat v2推出"Omni"功能，基于策略在115个开源模型和15个提供商间自动选择模型，可在单个会话中在编码和写作模型间路由任务。

---

## 🛠️ 十大工具产品要点

### 1. [Anthropic Skills开源文档技能](https://github.com/anthropics/skills/tree/main/document-skills)
> Anthropic开源了基于Skills技术实现的文档处理技能，涵盖.pdf、.docx、.xlsx和.pptx文件格式的创建和读取功能。

---

### 2. [Windows Copilot新增语音和视觉功能](https://twitter.com/mustafasuleyman/status/1978808627008847997)
> Windows 11新增Copilot语音唤醒、跨桌面/应用/文档的视觉功能，以及即将推出的本地文件Copilot Actions。

---

### 3. [Perplexity新增语言学习和金融功能](https://twitter.com/perplexity_ai/status/1978859991152165125)
> Perplexity发布内置语言学习体验和新的金融功能（内幕交易追踪器），在iOS和网页端可用。

---

### 4. [Cline CLI预览版发布](https://twitter.com/cline/status/1978874789193486749)
> Cline CLI预览版提供可编写脚本的开放"原始代理循环"，专为子代理和可组合工作流设计。

---

### 5. [Open Agent Builder开源](https://twitter.com/firecrawl_dev/status/1978878728827478289)
> 开源n8n风格画布，连接Firecrawl、LLM、逻辑节点和MCP，用于API可部署的工作流。

---

### 6. [Google Veo 3.1集成到LTX Studio](https://twitter.com/LTXStudio/status/1978827563926716704)
> Google Veo 3.1在LTX Studio和Synthesia中上线，提供更清晰的真实感、音频支持和完整的关键帧支持。

---

### 7. [Sourceful Riverflow 1图像编辑模型](https://twitter.com/ArtificialAnlys/status/1978891167795417092)
> Sourceful的Riverflow 1在Artificial Analysis图像编辑排行榜上排名第一，结合VLM和开放扩散，定价为每1000张图像66美元。

---

### 8. [mixedbread.ai发布超紧凑ColBERT模型](https://twitter.com/mixedbreadai/status/1978853869557055492)
> mixedbread.ai发布mxbai-colbert-edge-v0（17M, 32M）模型，在LongEmbed上小于10亿参数的模型中排名第一，Apache 2.0许可。

---

### 9. [Alibaba开源Qwen3Guard安全组件](https://twitter.com/Alibaba_Qwen/status/1978732145297576081)
> Alibaba开源Qwen3Guard组件，包括Qwen3-4B-SafeRL和Qwen3GuardTest，用于分类中间"思考"和逐token审核。

---

### 10. [Karpathy nanochat项目进展](https://twitter.com/karpathy/status/1978615547945521655)
> Karpathy的nanochat d32项目CORE提升至0.31（超过GPT-2的0.26），GSM8K达到约20%，完整报告和脚本已发布，社区正在集成到Transformers和vLLM。

---