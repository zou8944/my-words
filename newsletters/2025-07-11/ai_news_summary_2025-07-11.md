## AINews - 2025-07-11

> [原文链接](https://news.smol.ai/issues/25-07-10-grok-4/)

## 📰 十大AI新闻要点

### 1. [xAI发布Grok 4及Grok 4 Heavy](https://www.youtube.com/watch?v=MtYsUdfZPMA&t=390s)
> xAI在成立两周年之际发布Grok 4系列模型，包含基础版和300美元/月的高端版Grok 4 Heavy。该模型据传拥有2.4万亿参数，在HLE、GPQA、ARC-AGI等多个基准测试中创下新高。

---

### 2. [Grok 4系统提示词泄露](https://github.com/xai-org/grok-prompts)
> Grok 4的系统提示词显示其具备分析Twitter内容、处理多模态输入等能力，但要求图像生成前需用户确认。社区指出这并非真正泄露，而是xAI主动公开的透明举措。

---

### 3. [Grok 4性能争议](https://x.com/Teknium1/status/1943354860608589836)
> 尽管Grok 4在ARC-AGI-2基准达到15.9%准确率，但开发者实测发现其Java/Node.js代码生成存在错误，引发对基准测试实际意义的质疑。

---

### 4. [Mistral发布Devstral 2507模型](https://huggingface.co/mistralai/Devstral-Small-2507)
> Mistral AI推出24B参数的Devstral-Small-2507，在SWE-bench验证集上以53.6%准确率超越GPT-4.1-mini和Claude 3.5 Haiku，专为软件工程工作流优化。

---

### 5. [微软发布Phi-4-mini-flash-reasoning](https://huggingface.co/microsoft/Phi-4-mini-flash-reasoning)
> 微软推出3.8B参数的数学推理专用模型，采用创新的SambaY混合解码器架构，在AIME24/25等数学基准表现突出，推理吞吐量提升10倍。

---

### 6. [Perplexity推出Comet浏览器](https://x.com/perplexity_ai/status/1943437826307297480)
> Perplexity发布基于Chromium的AI浏览器Comet，初期面向Max订阅用户，具备多模态搜索和文档生成功能，计划逐步开放更多访问权限。

---

### 7. [METR研究显示AI编程助手可能降低效率](https://twitter.com/METR_Evals/status/1943401701052158240)
> 随机对照试验发现，2025年初的AI编程助手反而使经验丰富的开源开发者在复杂任务上速度变慢，尽管开发者主观感觉更高效。

---

### 8. [Figure机器人公司宣布重大进展](https://twitter.com/adcock_brett/status/1943029976573579586)
> Figure CEO宣布团队扩大至293人，新园区将支持10万台机器人的制造目标，宣称"通用机器人技术触手可及"。

---

### 9. [Google推出Veo 3视频生成功能](https://twitter.com/Google/status/1943328300517958101)
> Google为Veo 3增加照片转视频功能，支持生成带声音的视频内容，面向AI Pro和Ultra订阅用户开放。

---

### 10. [Liquid AI开源LFM2边缘模型](https://www.liquid.ai/blog/liquid-foundation-models-v2)
> Liquid AI发布第二代液态基础模型(350M-1.2B参数)，采用门控卷积和注意力混合架构，专为CPU设备优化推理速度。

---

## 🛠️ 十大工具产品要点

### 1. [Grok 4 API定价](https://twitter.com/scaling01/status/1943168223102321003)
> Grok 4 API定价为输入token 3美元/百万，输出token 15美元/百万，确认支持256K上下文窗口，已集成至Cursor、LangChain等平台。

---

### 2. [Devstral-Small-2507量化版本](https://huggingface.co/unsloth/Devstral-Small-2507-GGUF)
> 社区提供Devstral-Small-2507的GGUF量化版本，支持工具调用和视觉任务，推荐温度设置为0.0-0.15以获得最佳生成质量。

---

### 3. [LlamaParse文档处理工具](https://twitter.com/jerryjliu0/status/1943107617313984610)
> LlamaIndex展示使用LlamaParse从复杂文档创建自动数据管道到Snowflake Cortex的教程，提升企业文档处理效率。

---

### 4. [Reka Vision多模态平台](https://x.com/RekaAILabs/status/1942621988390088771)
> Reka AI推出视觉代理平台，支持视频/图像搜索、内容创作和实时警报，将多模态数据转化为可操作洞察。

---

### 5. [GenAI Processors库开源](https://twitter.com/osanseviero/status/1943381135825805313)
> Google DeepMind开源Python库GenAI Processors，用于构建异步、基于流的可组合实时AI项目。

---

### 6. [WarpGBM加速方案](https://github.com/jefferythewind/warpgbm)
> 基于CUDA的WarpGBM方案声称比LightGBM更快，获得社区关注，GitHub已收获79星。

---

### 7. [MCP-B.ai协议项目](https://mcp-b.ai/)
> 新兴MCP协议旨在重建适合机器人交互的网络标准，已获LlamaIndex等框架支持，用于自然语言管理数据库。

---

### 8. [Self-Forcing加速技术](https://arxiv.org/abs/2506.08009)
> 论文提出的Self-Forcing技术可将扩散模型速度从20FPS提升至400FPS，但实际应用中遇到流匹配实现难题。

---

### 9. [Gradio 5.36性能升级](https://www.notion.so/swyx/huggingface)
> Gradio 5.36现在仅渲染可见组件，显著降低复杂应用加载时间，通过`pip install --upgrade gradio`即可升级。

---

### 10. [Neurabase MCP代理](https://neurabase.deploya.dev/)
> 该代理将MCP协议集成到聊天机器人中，支持创建自动化安全审计工作流，展示代理协作的新范式。