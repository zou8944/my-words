## AINews - 2025-10-01

> [原文链接](https://news.smol.ai/issues/25-09-29-sonnet-45/)

## 📰 十大AI新闻要点

### 1. [Anthropic发布Claude Sonnet 4.5，创SWE-Bench Verified新纪录](https://www.anthropic.com/news/claude-sonnet-4-5)
> Claude Sonnet 4.5在SWE-Bench Verified上达到77.2%的准确率（并行TTC为82%），在金融、法律和STEM领域有显著改进，支持30+小时的自主编码运行，约11,000行代码的代码库构建和维护

---

### 2. [DeepSeek发布V3.2-Exp稀疏注意力模型，API价格降低50%+](https://twitter.com/deepseek_ai/status/1972604768309871061)
> DeepSeek V3.2-Exp采用学习稀疏注意力方案，在128k上下文长度下，预填充成本降低约3.5倍，解码成本降低约10倍，质量与V3.1相当，同时发布技术报告和内核代码

---

### 3. [OpenAI与Stripe合作推出即时结账和Agentic Commerce Protocol](https://twitter.com/patrickc/status/1972716417280860391)
> ChatGPT现在支持直接在聊天中购买，从Etsy开始，很快将支持超过100万家Shopify商家，ACP是一个开放标准，用于用户、AI代理和企业之间的程序化商务

---

### 4. [阿里巴巴公布Qwen路线图，目标100M上下文窗口和10T参数](https://www.reddit.com/r/LocalLLaMA/comments/1nq182d/alibaba_just_unveiled_their_qwen_roadmap_the/)
> 阿里巴巴的Qwen路线图包括上下文窗口从1M增长到100M tokens，参数数量从约1T增长到10T，测试时计算预算从64k增长到1M，数据规模从10T增长到100T tokens

---

### 5. [RL研究显示LoRA在强化学习后训练中可匹配全参数微调](https://thinkingmachines.ai/blog/lora/)
> 新实验表明LoRA在许多RL后训练机制中可以匹配全参数微调，即使在低秩情况下，由QLoRA经验（超过1500次实验）和最近的GRPO实现证实

---

### 6. [腾讯发布Hunyuan Image 3.0，号称最强开源文生图模型](https://www.reddit.com/r/LocalLLaMA/comments/1nqaiaz/tencent_is_teasing_the_worlds_most_powerful/)
> 腾讯发布Hunyuan Image 3.0开源文本到图像模型，声称将成为"最强大"的开源T2I模型，据称需要96GB VRAM进行推理

---

### 7. [OpenAI推出家长控制功能，加强青少年安全保护](https://twitter.com/OpenAI/status/1972604360204210600)
> OpenAI为所有ChatGPT用户推出家长控制功能，允许父母将账户与青少年账户链接，自动获得更强的安全保护，包括自残风险通知

---

### 8. [中国Fenghua No.3 GPU支持CUDA和DirectX，挑战NVIDIA垄断](https://www.reddit.com/r/LocalLLaMA/comments/1nq1ia2/china_already_started_making_cuda_and_directx/)
> 中国离散GPU"Fenghua No.3"支持现代图形API—DirectX 12、Vulkan 1.2、OpenGL 4.6，并宣传CUDA支持，试图在非NVIDIA硬件上运行CUDA工作负载

---

### 9. [Modal完成8700万美元B轮融资，估值达"B"illion级别](https://twitter.com/bernhardsson/status/1972649681701486821)
> Modal筹集8700万美元B轮融资，现在估值达到"B"illion级别，继续构建ML原生基础设施，客户强调其"远程但感觉本地"的开发体验和扩展人体工程学

---

### 10. [Google发布TimesFM 2.5，更强的零样本时间序列预测器](https://twitter.com/osanseviero/status/1972609699007910071)
> Google发布TimesFM 2.5（2亿参数，16k上下文，Apache-2.0许可），作为更强的零样本时间序列预测器，在多个时间序列预测任务上表现优异

---

## 🛠️ 十大工具产品要点

### 1. [Claude Code v2发布检查点功能和原生VS Code扩展](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)
> Claude Code v2引入检查点功能，保存进度并允许即时回滚到先前状态，刷新终端界面，并发布原生VS Code扩展，新的吉祥物Clawd

---

### 2. [Claude API新增上下文编辑功能和内存工具](https://anthropic.com/news/context-management)
> Claude API新增上下文编辑功能和内存工具，让代理运行更长时间，处理更复杂的任务，Claude Code SDK更名为Claude Agent SDK

---

### 3. [Claude.ai应用集成代码执行和文件创建功能](https://www.anthropic.com/news/create-files)
> Claude应用集成代码执行来分析数据，创建文件（电子表格、幻灯片和文档），并直接在对话中可视化见解，Claude for Chrome扩展现在可供上个月加入等待列表的Max用户使用

---

### 4. [vLLM支持DeepSeek稀疏注意力，提供H200/B200构建](https://twitter.com/vllm_project/status/1972664010702221399)
> vLLM提供DSA支持配方和H200/B200构建，DeepSeek的内核以TileLang/CUDA形式提供，TileLang（TVM）在约80行代码中达到手写FlashMLA的约95%性能

---

### 5. [OpenRouter Auto现在根据需要将提示路由到支持网络的模型](https://openrouter.ai/openrouter/auto)
> OpenRouter Auto现在动态地将提示路由到支持网络的模型，扩大支持的后端，改进实时查询的检索，在合格任务上实现动态在线路由

---

### 6. [Windsurf集成Claude Sonnet 4.5和Code Supernova 100万上下文](https://x.com/windsurf/status/1972712147450048600)
> Windsurf发布code-supernova-1-million（100万上下文升级）并集成Claude Sonnet 4.5，通过并行工具执行加速Cascade代理，个人用户限时免费访问

---

### 7. [Cursor集成Claude Sonnet 4.5并添加浏览器控制](https://twitter.com/cursor_ai/status/1972713190074261949)
> Cursor现在提供Sonnet 4.5，并添加浏览器控制功能，Perplexity和OpenRouter也广泛可用，支持更复杂的代理工作流程

---

### 8. [Anthropic推出Claude使用限制计量器](https://www.reddit.com/r/ClaudeAI/comments/1ntq8tv/introducing_claude_usage_limit_meter/)
> Anthropic在Claude Code（通过/usage斜杠命令）和Claude应用（设置→使用情况）中添加实时使用计量器，预计少于2%的用户会达到限制

---

### 9. [Imagine with Claude生成UI实验研究预览](https://claude.ai/redirect/website.v1.07f611e1-e39b-4e56-8251-b396f9288147/imagine)
> Imagine with Claude是一个生成UI实验研究预览，即时生成软件，无需预写功能，可供Max用户使用5天

---

### 10. [llmq库支持LLaMA/Qwen的完全分片FP8训练](https://github.com/IST-DASLab/llmq)
> 新存储库支持LLaMA/Qwen在纯CUDA/C++中的完全分片FP8训练，旨在实现内存和吞吐量优势，建议实现8位Adam m/v状态以推动大规模训练的优化边界

---