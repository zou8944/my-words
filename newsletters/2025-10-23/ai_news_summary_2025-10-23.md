## AINews - 2025-10-23

> [原文链接](https://news.smol.ai/issues/25-10-21-chatgpt-atlas/)

## 📰 十大AI新闻要点

### 1. [OpenAI发布ChatGPT Atlas浏览器](https://chatgpt.com/atlas)
> OpenAI正式推出基于Chromium的AI浏览器ChatGPT Atlas，目前仅支持macOS，Windows、iOS和Android版本即将推出。浏览器集成了Agent模式和"浏览器记忆"功能，可将ChatGPT嵌入整个系统，并能在登录网站上执行操作。

---

### 2. [LangChain完成1.25亿美元B轮融资](https://twitter.com/LangChainAI/status/1980678921839603948)
> LangChain获得1.25亿美元B轮融资，由IVP领投，CapitalG、Sapphire、Sequoia、Benchmark等参与投资，公司估值达12.5亿美元。同时发布了LangChain和LangGraph的1.0版本。

---

### 3. [DeepSeek-OCR技术引发行业讨论](https://github.com/deepseek-ai/DeepSeek-OCR)
> DeepSeek发布OCR技术，通过将文本渲染为图像并使用视觉编码器+MoE解码器解码，实现大规模长上下文压缩。技术声称能以约10倍更少的"视觉"token实现97%的重建精度。

---

### 4. [Qwen3-VL视觉语言模型发布](https://twitter.com/Alibaba_Qwen/status/1980665932625383868)
> 阿里巴巴发布Qwen3-VL-2B和Qwen3-VL-32B视觉语言模型，包括FP8变体和"思考"/指导类型，在STEM、VQA、OCR、视频和代理任务中表现优异，32B模型在OSWorld基准测试中与更大模型表现相当。

---

### 5. [Meta发布PyTorch新训练库](https://twitter.com/eliebakouch/status/1980637130687942805)
> Meta发布torchforge（可扩展RL训练）、OpenEnv（代理环境）和torchcomms等新PyTorch库，围绕Monarch和TorchTitan构建"训练未来"路线图。

---

### 6. [Claude Desktop全面上市](https://claude.com/download)
> Anthropic的Claude Desktop现已在Mac和Windows上全面上市，支持企业部署，提供与本地工作环境的无缝集成，包括截图捕获、窗口共享和语音命令功能。

---

### 7. [亚马逊计划用机器人替代60万工人](https://www.reddit.com/r/singularity/comments/1occruc/amazon_hopes_to_replace_600000_us_workers_with/)
> 根据泄露文件，亚马逊计划到2027年用机器人替代60万美国工人，每件商品成本可能降低30美分，这是应对劳动力短缺和提高履约中心效率的长期战略。

---

### 8. [持续学习内存层技术突破](https://twitter.com/realJessyLin/status/1980662516285075762)
> 研究人员开发稀疏微调内存层技术，相比完整微调/LoRA，在事实任务上的遗忘率显著降低（-11% vs -89%/-71%），为增量模型更新提供了实用路径。

---

### 9. [Google AI Studio推出AI优先编码功能](https://twitter.com/OfficialLoganK/status/1980674135693971550)
> Google AI Studio推出重新设计的构建模式，集成多能力脚手架功能，目标是加速从提示到生产的迭代过程，为Gemini应用开发提供更快的工作流程。

---

### 10. [Anthropic发布Claude机制解释研究](https://twitter.com/wesg52/status/1980680563582538099)
> Anthropic对Claude 3.5 Haiku进行机制解释分析，揭示了清晰的几何变换和分布式注意力算法，被认为是迄今为止最深层次理解的行为机制之一。

---

## 🛠️ 十大工具产品要点

### 1. [ChatGPT Atlas Agent模式](https://twitter.com/OpenAI/status/1980685612538822814)
> ChatGPT Atlas的Agent模式可在网页上执行操作，包括访问登录网站，通过本地浏览器而非远程方式重新激活Operator功能，能够使用用户的登录信息。

---

### 2. [LangChain v1.0代理工程栈](https://twitter.com/hwchase17/status/1980680421706006663)
> LangChain发布1.0版本，包括LangChain、LangGraph、LangSmith洞察代理和无代码代理构建器，强调受控的生产优先代理运行时和可观察性。

---

### 3. [vLLM kvcached多模型服务](https://twitter.com/vllm_project/status/1980776841129701411)
> vLLM的kvcached功能支持在同一GPU上服务多个模型共享未使用的KV缓存块，提高GPU资源利用率。

---

### 4. [FlashInfer-Bench基准测试工作流](https://flashinfer.ai/2025/10/21/flashinfer-bench.html)
> FlashInfer-Bench引入自改进基准测试工作流，标准化LLM服务内核签名，自动发现最快内核，支持FlashInfer、SGLang和vLLM的day-0集成。

---

### 5. [Runway自服务模型微调](https://twitter.com/runwayml/status/1980620538906054691)
> Runway宣布自服务模型微调和基于节点的Workflows系统，可链接模型/模态/中间步骤，用于生产创意流水线。

---

### 6. [Together AI视频图像生成API](https://twitter.com/togethercompute/status/1980746093932515697)
> Together AI现在通过相同的文本推理API提供视频和图像生成模型访问，包括Sora 2、Veo 3等模型。

---

### 7. [LlamaIndex llamactl CLI工具](https://twitter.com/llama_index/status/1980673952033976824)
> LlamaIndex发布llamactl CLI，用于本地LlamaAgents开发部署，提供开箱即用的文档代理模板和文档中心工作流的私有预览托管。

---

### 8. [OpenRouter TypeScript SDK](https://www.npmjs.com/package/@openrouter/sdk)
> OpenRouter发布TypeScript SDK测试版，为300多个模型提供完全类型化的请求/响应，内置OAuth支持，Python、Java和Go版本即将推出。

---

### 9. [Chandra OCR开源工具](https://twitter.com/VikParuchuri/status/1980667137606971423)
> Chandra OCR发布完整布局提取、图像/图表标题、手写和表格支持，与Transformers/vLLM兼容。

---

### 10. [Tinygrad支持Apple Silicon eGPU](https://x.com/__tinygrad__/status/1980082660920918045)
> Tinygrad团队宣布通过USB4在Apple Silicon上启用NVIDIA eGPU的早期公开测试，使用ADT-UT3G扩展坞和NVK基础的tinymesa编译器，实现约3GB/s PCIe带宽。

---