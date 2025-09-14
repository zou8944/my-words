## AINews - 2025-09-14

> [原文链接](https://news.smol.ai/issues/25-09-12-not-much/)

## 📰 十大AI新闻要点

### 1. [Meta发布MobileLLM-R1小型推理模型](https://twitter.com/_akhaliq/status/1966498058822103330)
> Meta在Hugging Face上发布了参数小于10亿的MobileLLM-R1系列模型，在仅使用4.2T tokens训练的情况下，MATH准确率比Olmo-1.24B高约5倍，比SmolLM2-1.7B高约2倍，在多推理基准测试中匹配或超越Qwen3性能。

---

### 2. [阿里巴巴推出Qwen3-Next-80B混合注意力模型](https://twitter.com/ZhihuFrontier/status/1966419946885493098)
> Qwen3-Next-80B-A3B采用混合注意力设计（Gated DeltaNet + Gated Attention），稀疏度高达约3.8%，原生支持256k上下文窗口，需要SGLang和vLLM进行大量引擎适配。

---

### 3. [SWE-Bench修复代理窥探漏洞](https://twitter.com/TacoCohen/status/1966421688846778561)
> FAIR Codegen发现SWE-Bench存在允许代理窥探未来提交的漏洞并已修复，初步重新运行显示大多数模型未受严重影响，建议实验室和开源项目在修复后的基准上重新发布结果。

---

### 4. [LiveMCP-101推出实时代理评估框架](https://twitter.com/omarsar0/status/1966525731082768782)
> LiveMCP-101引入实时代理框架/基准测试，即使在复杂任务中前沿模型表现不佳（GPT-5在"困难"任务中得分39.02%），并分类了七种常见失败模式。

---

### 5. [VS Code推出语言模型市场API](https://twitter.com/code/status/1966638511269794238)
> VS Code正式推出"语言模型聊天提供商"扩展API，允许安装BYOK提供商作为扩展，提供更多模型选择，并附带教程、视频和自动选择模型体验。

---

### 6. [Hugging Face Transformers v5现代化升级](https://twitter.com/art_zucker/status/1966470835558093226)
> Transformers v5推出更快内核、更智能默认值和清理工作，并悄悄落地连续批处理以简化评估/训练循环，专注于修补/工具箱而非最大吞吐量服务器。

---

### 7. [OpenAI大幅提升GPT-5速率限制](https://twitter.com/OpenAIDevs/status/1966610846559134140)
> OpenAI大幅提升GPT-5和gpt-5-mini across各层的速率限制，同时出现新的"gpt-5-high-new"目标，专注于内置推理默认值。

---

### 8. [Anthropic与安全机构合作加固Claude防护](https://twitter.com/AnthropicAI/status/1966599335560216770)
> 英国AISI和美国CAISI识别Claude Opus 4/4.1的越狱漏洞，帮助部署更强安全防护措施，同时为构建者推荐Claude Code SDK作为自定义代理起点。

---

### 9. [Google发布差分隐私训练的VaultGemma](https://twitter.com/GoogleResearch/status/1966533086914421000)
> Google Research发布VaultGemma，这是通过差分隐私从头训练的10亿参数Gemma变体，声称是以此方式训练的最大开放模型，并提供私有语言模型训练的新缩放定律结果。

---

### 10. [Seedream 4.0登顶图像生成和编辑排行榜](https://twitter.com/lmarena_ai/status/1966562484506230922)
> 在获得超过43,000票后，Gemini 2.5 Flash Image（"nano-banana"）继续位居图像编辑和文本到图像图表首位，ByteDance的Seedream 4现居图像编辑第2位和文本到图像第5位。

---

## 🛠️ 十大工具产品要点

### 1. [MobileLLM-R1边缘推理模型](https://huggingface.co/facebook/MobileLLM-R1-950M)
> Meta发布的~950M参数小型LLM，专为高效设备端/移动推理设计，提供交互式演示空间，专注于在低参数端推动推理准确性。

---

### 2. [Qwen3-Next-80B稀疏激活MoE](https://huggingface.co/collections/Qwen/qwen3-next-68c25fd6838e585db8eeea9d)
> 阿里巴巴的稀疏激活80B MoE模型，每个token约激活30亿参数，推理速度报告快约10倍，支持32k+上下文。

---

### 3. [VS Code语言模型扩展API](https://twitter.com/code/status/1966638511269794238)
> 允许安装BYOK提供商作为扩展，提供更多模型选择，包括Claude、GPT-5/mini、Gemini等模型的自动选择体验。

---

### 4. [Hugging Face Transformers连续批处理](https://twitter.com/LucSGeorges/status/1966550465769775305)
> 简化评估/训练循环的连续批处理功能，专注于修补和工具箱使用，而非追逐最大吞吐量服务器。

---

### 5. [Claude Code SDK自定义代理开发](https://twitter.com/alexalbert__/status/1966601430808088596)
> 为构建者推荐的自定义代理起点，使用与CLI相同的工具链，便于开发定制代理解决方案。

---

### 6. [Qwen Code v0.0.10/11子代理功能](https://twitter.com/Alibaba_Qwen/status/1966451235328008563)
> 添加子代理、Todo Write工具、"Welcome Back"项目摘要、编辑稳定性、更好的IDE/Shell集成和改进的内存/会话管理。

---

### 7. [Seedream 4高分辨率变体](https://twitter.com/lmarena_ai/status/1966673628327801255)
> 支持4096×4096输出的新变体，现已在Arena上线，提供更高分辨率的图像生成能力。

---

### 8. [Microsoft Kosmos-2.5 OCR+布局演示](https://twitter.com/mervenoyann/status/1966487632659005667)
> 在Transformers中落地的Kosmos-2.5，提供OCR+布局演示和笔记本，支持文本和布局理解任务。

---

### 9. [ZeroGPU区域AOT编译加速](https://twitter.com/RisingSayak/status/1966447203381092675)
> 添加区域AOT编译和预编译图共享/加载功能，加速启动时间，提高GPU利用率。

---

### 10. [Skypilot GPU利用率仪表板](https://twitter.com/skypilot_org/status/1966592871600890285)
> 新的GPU利用率仪表板，提供更好的资源监控和优化功能，帮助用户更有效地管理GPU资源。

---