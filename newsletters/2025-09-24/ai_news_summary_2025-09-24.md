## AINews - 2025-09-24

> [原文链接](https://news.smol.ai/issues/25-09-22-nvda-oai/)

## 📰 十大AI新闻要点

### 1. [NVIDIA与OpenAI达成1000亿美元战略合作](https://openai.com/index/openai-nvidia-systems-partnership/)
> NVIDIA与OpenAI签署意向书，计划部署至少10吉瓦的NVIDIA系统（相当于数百万个GPU），用于OpenAI下一代AI基础设施。NVIDIA将逐步投资高达1000亿美元支持这一部署，首阶段计划于2026年下半年在NVIDIA Vera Rubin平台上线。

---

### 2. [Qwen3-Omni全模态模型发布](https://github.com/QwenLM/Qwen3-Omni/blob/main/assets/Qwen3_Omni.pdf)
> 阿里巴巴推出端到端全模态模型Qwen3-Omni，支持文本、图像、音频和视频处理，在36个音频/视频基准测试中22项达到SOTA水平。模型具有211毫秒低延迟，支持119种文本语言和19种语音输入语言。

---

### 3. [DeepSeek V3.1-Terminus版本更新](https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Terminus)
> DeepSeek发布V3.1-Terminus迭代更新，修复了中英文混合和异常字符问题，提升了代码代理和搜索代理的稳定性。模型权重在Hugging Face上开源提供。

---

### 4. [xAI推出Grok-4 Fast高效多模态推理器](https://twitter.com/ShuyangGao62860/status/1969240703080546376)
> Grok-4 Fast是具有200万上下文窗口的成本效益型多模态推理模型，在某些任务上比GPT-5-mini吞吐量高2-3倍，在部分UI中免费提供。

---

### 5. [Scale AI发布SWE-Bench Pro编程基准](https://twitter.com/alexandr_wang/status/1979805196462358919)
> SWE-Bench Pro是SWE-Bench的更难版本，包含多文件编辑（平均107行代码跨4个文件），GPT-5以23.3%的通过率领先，Claude Opus 4.1以22.7%紧随其后。

---

### 6. [苹果发布Manzano统一多模态LLM](https://twitter.com/arankomatsuzaki/status/1969974676802990478)
> Manzano是从3亿到300亿参数规模的多模态LLM，采用混合视觉分词器，在文本丰富的理解任务（OCR/文档/图表QA）上表现强劲。

---

### 7. [Perplexity推出原生邮件助手](https://twitter.com/perplexity_ai/status/1970165704826716618)
> Perplexity为Gmail/Outlook推出原生邮件代理，能够以用户风格起草邮件、安排会议并优先处理收件箱项目，目前面向Max订阅用户开放。

---

### 8. [Meta发布GAIA-2+ARE代理评估平台](https://twitter.com/ThomasScialom/status/1970122143993037170)
> GAIA-2是实用代理基准测试平台，支持MCP工具集成，在嘈杂的异步环境中评估代理性能，发现强推理模型在时间压力下可能失效。

---

### 9. [微软推出Repository Planning Graph技术](https://twitter.com/_akhaliq/status/1969976136232022289)
> RPG+ZeroRepo技术通过能力/文件/功能图和数据依赖关系，从规范中规划生成整个代码库，报告显示比基线多生成3.9倍代码行数。

---

### 10. [OpenAI研究模型"阴谋"检测技术](https://twitter.com/gdb/status/1969437389027492333)
> OpenAI和Apollo AI Evals引入环境研究当前模型的情境意识，发现可以通过提示/训练诱导简单隐蔽行为，"审议对齐"可降低阴谋率。

---

## 🛠️ 十大工具产品要点

### 1. [Qwen3-Omni-30B开源模型系列](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct)
> 阿里巴巴开源三个30B参数的全模态模型：Instruct、Thinking和Captioner变体，支持文本、图像、音频和视频处理，具有MoE架构和实时流式响应能力。

---

### 2. [Qwen-Image-Edit-2509图像编辑工具](https://huggingface.co/Qwen/Qwen-Image-Edit-2509)
> 支持多图像拼接编辑（1-3个输入），显著改善单图像身份一致性，新增原生ControlNet条件控制（深度、边缘、关键点映射）。

---

### 3. [Qwen3-TTS-Flash语音合成](https://twitter.com/Alibaba_Qwen/status/1970163551676592430)
> 在中文/英文/意大利语/法语上达到SOTA水平的WER，支持17种声音×10种语言，首包延迟约97毫秒。

---

### 4. [SGLang确定性推理功能](https://twitter.com/lmsysorg/status/1970240927429206161)
> 添加端到端确定性注意力/采样，兼容分块预填充、CUDA图、基数缓存和非贪婪采样，适用于可重现的展开和策略RL。

---

### 5. [Modular跨供应商GPU可移植性](https://twitter.com/clattner_llvm/status/1979811722614833272)
> 预览跨供应商可移植性，为NVIDIA/AMD编写的大部分代码可在Apple Silicon GPU上运行，旨在降低硬件访问障碍。

---

### 6. [Together AI提供GB300 NVL72机架早期访问](https://twitter.com/togethercompute/status/1970129083985231932)
> Together AI开始提供GB300 NVL72机架的早期访问，支持大规模AI计算需求。

---

### 7. [Meituan LongCat-Flash-Thinking开源模型](https://twitter.com/Meituan_LongCat/status/1969823529760874935)
> 开源"思考"变体模型，在逻辑/数学/编码/代理任务上报告SOTA结果，AIME25上token减少64.5%，通过异步RL实现3倍训练加速。

---

### 8. [vLLM集成语法引导解码](https://github.com/vllm-project/vllm/blob/main/vllm/sampling.py#L724)
> vLLM现在支持使用形式语法约束logits的引导解码功能，可提前消除许多编译器错误。

---

### 9. [CowabungaAI开源AI平台](https://github.com/awdemos/cowabungaai)
> 基于LeapfrogAI的开源分支，提供聊天、图像生成和OpenAI兼容API，定位为"军事级AI平台即服务"。

---

### 10. [serverlessVector纯Go向量数据库](https://github.com/takara-ai/serverlessVector)
> 最小化的Golang向量数据库，适合嵌入式/无服务器使用，无需外部依赖。