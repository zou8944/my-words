## AINews - 2025-11-13

> [原文链接](https://news.smol.ai/issues/25-11-11-not-much/)

## 📰 十大AI新闻要点

### 1. [GPT-5在数独推理基准测试中取得突破但仍存差距](https://twitter.com/SakanaAILabs/status/1988080410392404021)
> GPT-5在Sudoku-Bench测试中解决了33%的谜题，是之前领先模型的两倍，成为首个解决9x9变体的LLM。但67%的更难变体仍未解决，显示在元推理、空间逻辑和全局一致性方面仍存缺陷。

---

### 2. [百度发布轻量级多模态推理模型ERNIE-4.5-VL](https://twitter.com/Baidu_Inc/status/1988182106359411178)
> ERNIE-4.5-VL-28B-A3B-Thinking采用Apache 2.0许可，具有"超过30亿活跃参数"，声称在文档/图表理解方面达到SOTA，并在特定基准测试中超越Gemini 2.5 Pro和GPT-5 High。

---

### 3. [Databricks推出低成本文档智能服务](https://twitter.com/databricks/status/1988271796076912928)
> Databricks ai_parse_document服务可将PDF/报告/图表转换为结构化数据，成本降低高达5倍，并与Lakehouse工具链深度集成，在文档任务上表现优于GPT-5和Claude等领先VLM。

---

### 4. [LAION启动大规模科学论文结构化项目AELLA](https://twitter.com/laion_ai/status/1988330466706157818)
> 开放计划旨在通过LLM生成的摘要使1亿篇科学论文可访问，发布包括10万摘要数据集、两个微调LLM和3D可视化器。

---

### 5. [AMD GPU内核优化实现2倍性能提升](https://twitter.com/qubitium/status/1988389379984027742)
> 斯坦福HazyResearch的HipKittens在AMD GPU上比ROCm可组合内核基准实现高达2倍加速，为AMD密集型训练堆栈缩小差距。

---

### 6. [机器人抓取合成技术实现10-100倍加速](https://twitter.com/zhaohengyin/status/1988318037804806431)
> Lightning Grasp程序化抓取生成在不同机器人手和挑战性物体上比之前SOTA快10-100倍，论文和代码已开源。

---

### 7. [语音克隆伦理问题引发监管讨论](https://twitter.com/mmitchell_ai/status/1988367909849329777)
> 随着语音克隆技术快速发展，专家提出"语音同意门"概念，纽约州法律已反映"拟人化阻断器"相关努力，为构建语音功能的团队提供设计目标。

---

### 8. [Google Pixel集成Nano Banana图像编辑模型](https://twitter.com/Google/status/1988377964686266518)
> Google 11月Pixel更新包含基于Gemini的图像编辑/生成模型Nano Banana，集成到Messages和Photos中，社区分析其架构可能类似于Hunyuan Image 3。

---

### 9. [VibeThinker 1.5B模型在数学编码基准测试中超越更大模型](https://www.reddit.com/r/LocalLLaMA/comments/1ou1emx/we_put_a_lot_of_work_into_a_15b_reasoning_model/)
> 1.5B参数推理模型在AIME 2024/2025、HMMT 2025和LiveCodeBench V5等基准测试中超越更大模型，挑战了更大模型必然更优的观念。

---

### 10. [Egocentric-10K成为最大自我中心数据集](https://www.reddit.com/r/LocalLLaMA/comments/1ouazho/egocentric10k_is_the_largest_egocentric_dataset/)
> 包含10,000小时视频、来自2,153名工厂工人的10.8亿帧数据，在真实工厂环境中收集，采用Apache 2.0许可，旨在解决人形机器人数据稀缺问题。

---

## 🛠️ 十大工具产品要点

### 1. [Gemini File Search API支持代理RAG模式](https://twitter.com/omarsar0/status/1988236096195776683)
> 开发者构建的MCP服务器利用Gemini File Search对代码库进行语义/代码搜索，简化端到端"读取代码库的代理"系统构建。

---

### 2. [Together AI推出人物驱动代理评估系统](https://twitter.com/togethercompute/status/1988374675093897380)
> Together AI与Collinear的"TraitMix"生成人物驱动代理交互，并与Together Evals集成进行工作流级评估，支持模拟驱动的代理行为开发。

---

### 3. [终端优先实验跟踪工具W&B LEET发布](https://twitter.com/wandb/status/1988401253156876418)
> W&B LEET是直接在终端中运行的实时离线运行监控TUI，适用于无浏览器的隔离/集群工作流。

---

### 4. [Photo-to-Anime LoRA实现风格化任务优化](https://twitter.com/wildmindai/status/1988309389259010112)
> QwenEdit-2509 LoRA用于照片到动漫转换，在风格化任务上优于仅提示方法，模型已在HuggingFace发布。

---

### 5. [本地LLM模拟Twitch聊天应用](https://github.com/EposNix/TwitchChatLLM/blob/main/TwitchChat.py)
> 使用Gemma 3 12B本地LLM观察用户屏幕并模拟Twitch聊天界面，需要pillow、mss和requests等Python库。

---

### 6. [Olares推出专用本地AI MiniPC](https://www.reddit.com/r/LocalLLaMA/comments/1otveug/a_startup_olares_is_attempting_to_launch_a_small/)
> Olares One MiniPC配备NVIDIA RTX 5090 Mobile GPU、24GB VRAM、96GB DDR5 RAM，运行开源Olares OS，售价3,000美元。

---

### 7. [FinePDFs多语言教育语料库更新](https://twitter.com/HKydlicek/status/1988328336469459449)
> 包含350B+ tokens、69种语言的教育资源、69个分类器和每种语言30万+ EDU标注，适用于学术/教育应用。

---

### 8. [Pathwork AI保险承保代理自动化](https://twitter.com/jerryjliu0/status/1988394058197184923)
> 基于LlamaCloud构建的人寿保险承保代理处理大量医疗文档和承运商指南，展示代理的大规模非结构化文档工作流原型。

---

### 9. [LM Studio 0.4.0将支持外部LLM插件](来源：文章内容)
> 即将发布的LM Studio 0.4.0将支持插件，允许与ChatGPT或Perplexity等外部LLM提供商集成。

---

### 10. [SUP Toolbox图像修复和放大工具发布](https://huggingface.co/spaces/elismasilva/sup-toolbox-app)
> 使用SUPIR、FaithDiff和ControlUnion的AI图像修复和放大工具，基于Diffusers和Gradio UI构建。

---