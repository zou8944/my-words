## AINews - 2025-09-26

> [原文链接](https://news.smol.ai/issues/25-09-24-not-much/)

## 📰 十大AI新闻要点

### 1. [阿里发布Qwen3系列模型](https://twitter.com/huybery/status/1970649341582024953)
> 阿里云通义千问发布Qwen3-Max旗舰模型和开源Qwen3-VL多模态模型，后者支持256K上下文（可扩展至1M）、32种语言OCR、2小时视频事件定位、GUI操作编码等功能，已在Hugging Face、ModelScope等平台上线

---

### 2. [OpenAI发布GPT-5 Codex](https://twitter.com/gdb/status/1970631954887565823)
> OpenAI推出专为智能体优化的GPT-5 Codex变体，支持400K上下文长度，采用自适应推理技术，简单任务消耗更少token，复杂任务使用更多token，定价为1.25/10美元每百万token

---

### 3. [Meta发布Code World Model 32B](https://twitter.com/AIatMeta/status/1970963571753222319)
> Meta FAIR发布32B参数的开源代码世界模型，将代码生成建模为基于代码执行世界模型的规划任务，在SWE-bench Verified上达到65.8% pass@1，采用研究许可证发布

---

### 4. [vLLM 0.10.2支持解码上下文并行](https://twitter.com/vllm_project/status/1970814441718755685)
> vLLM新版本引入由Kimi/Moonshot贡献的解码上下文并行技术，可在单节点H200上实现8倍KV缓存和2-3倍吞吐量提升，特别适合强化学习和离线数据生成工作负载

---

### 5. [阿里Wan2.5-Preview原生多模态架构](https://twitter.com/Alibaba_Wan/status/1970697244740591917)
> 阿里推出Wan2.5-Preview，采用原生多模态对齐架构，联合训练文本、图像、视频和音频，支持同步多说话者音视频生成、1080p 10秒电影级视频和像素级图像编辑

---

### 6. [Runway发布A2D自回归到扩散VLM](https://twitter.com/runwayml/status/1970866494729781623)
> Runway推出自回归到扩散的视觉语言模型转换技术，可将现有AR VLMs适配为并行扩散解码，在速度和质量间实现更好权衡，无需从头训练

---

### 7. [NVIDIA Lyra单图像3D/4D场景重建](https://twitter.com/_akhaliq/status/1970949464606245139)
> NVIDIA发布Lyra模型，通过视频扩散自蒸馏技术实现从单张图像或视频的3D和4D场景重建，权重已在Hugging Face发布

---

### 8. [RLPT技术在预训练数据上实现强化学习](https://twitter.com/arankomatsuzaki/status/1970684035258294548)
> RLPT方法在预训练语料库上使用自监督奖励进行训练，无需人工标注，在Qwen3-4B上实现MMLU +3.0、GPQA-Diamond +8.1的显著提升

---

### 9. [Google Test-Time Diffusion深度研究](https://twitter.com/omarsar0/status/1970864565710921891)
> Google推出测试时扩散深度研究技术，将扩散式迭代优化应用于长格式研究任务，在某些任务上相比OpenAI深度研究达到74.5%胜率

---

### 10. [MiniModel-200M单卡训练突破](https://huggingface.co/xTimeCrystal/MiniModel-200M-Base)
> MiniModel-200M在单张RTX 5090上仅用1天训练10B token，采用自适应Muon优化器和Float8预训练等技术，实现高效的小模型训练，Apache-2.0许可发布

---

## 🛠️ 十大工具产品要点

### 1. [Unsloth发布DeepSeek-V3.1动态GGUF量化](https://docs.unsloth.ai/new/unsloth-dynamic-ggufs-on-aider-polyglot)
> Unsloth推出DeepSeek-V3.1 Terminus的动态GGUF量化版本，通过每层智能1-bit量化将原715GB模型压缩80%，在Aider Polyglot基准测试中达到75.6%，超越Claude-4-Opus

---

### 2. [Chrome DevTools MCP公开预览](https://x.com/chromiumdev/status/1970505063064825994)
> Google推出Chrome DevTools MCP公开预览版，支持AI编码智能体通过CDP/Puppeteer控制实时Chrome浏览器，包含性能追踪、DOM检查、截图和网络捕获功能

---

### 3. [GitHub Copilot新嵌入模型](https://twitter.com/pierceboggan/status/1970950784251724007)
> GitHub Copilot发布新的嵌入模型和训练方法，实现更快更准确的代码搜索，提升开发者体验

---

### 4. [Figma MCP服务器登陆VS Code](https://twitter.com/code/status/1970621943821861217)
> Figma的MCP服务器现可在VS Code中使用，支持"设计到代码"工作流，也可在OpenHands中集成

---

### 5. [Modular完成2.5亿美元融资](https://twitter.com/Modular/status/1970881293933273524)
> Modular宣布完成2.5亿美元融资，加速推进统一AI基础设施平台建设，计划加快功能交付速度

---

### 6. [Gemini Live模型发布](https://x.com/OfficialLoganK/status/1970546338858246255)
> Google推出Gemini Live模型，支持原生音频功能、改进的函数调用和更自然的对话体验，但存在iOS Safari兼容性和背景噪音敏感性问题

---

### 7. [Qwen Image Edit 2509版本升级](https://preview.redd.it/6vbfk01cs1rf1.png)
> Qwen Image Edit发布2509版本，需要配合新的QwenImageEditPlus文本编码器使用，在风格保持和构图一致性方面显著提升，同时带来5-10%的速度提升

---

### 8. [Mojo支持Metal GPU目标](https://cdn.discordapp.com/attachments/1300872762163728550/1420526659001389056/image.png)
> Mojo编程语言新增Metal GPU目标支持，包含自定义bitcode写入器，可用于将DSL定向到Metal GPU，提升跨栈可移植性

---

### 9. [Weaviate获得ISO 27001认证](https://twitter.com/weaviate_io/status/1970912361381843104)
> 向量数据库Weaviate获得ISO 27001信息安全认证，增强企业级部署的可信度和合规性

---

### 10. [AMD与Cohere扩大合作](https://twitter.com/AMD/status/1970824479279317446)
> AMD扩大与Cohere的合作关系，在AMD Instinct上部署Cohere模型，加强主权AI战略布局