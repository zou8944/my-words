## AINews - 2025-11-07

> [原文链接](https://news.smol.ai/issues/25-11-05-not-much/)

## 📰 十大AI新闻要点

### 1. [Kimi-K2推理模型集成到vLLM和SGLang](https://twitter.com/scaling01/status/1986071916541870399)
> Moonshot AI的Kimi-K2推理模型已合并到vLLM推理框架，SGLang也计划在发布时提供支持。据讨论透露，Kimi-K2的MoE配置约为1.2万亿总参数/300亿激活参数，与近期大型稀疏模型类似。

---

### 2. [Perplexity发布万亿参数MoE内核研究论文](https://twitter.com/perplexity_ai/status/1986101355896098836)
> Perplexity发布首篇研究论文和大型MoE内核，声称在AWS EFA上可实现云可移植的万亿参数部署。vLLM暗示将集成这些快速通信内核，为大规模模型推理提供新解决方案。

---

### 3. [Anthropic发布代码执行+MCP模式优化指南](https://twitter.com/omarsar0/status/1986099467914023194)
> Anthropic发布指南展示如何通过将MCP服务器表示为代码API、渐进式工具发现和环境内数据处理，将工具密集型代理的上下文从约15万token减少到约2千token，降幅达98.7%。

---

### 4. [VS Code引入"代理会话"原生功能](https://twitter.com/code/status/1986113028387930281)
> VS Code新增"代理会话"视图，统一在编辑器内启动和监控代理，包括Copilot和外部代理。团队正在就术语和用户体验征求反馈，标志着IDE向代理原生开发环境演进。

---

### 5. [字节跳动发布BindWeave主题一致视频生成](https://twitter.com/_akhaliq/status/1986058046876070109)
> 字节跳动通过跨模态集成实现新的主题一致图像到视频生成，模型卡片和论文已在Hugging Face发布，展示在保持主题一致性方面的技术进步。

---

### 6. [OpenAI推出印度语言基准IndQA](https://twitter.com/OpenAI/status/1985950264525013210)
> OpenAI推出IndQA基准，专门针对印度语言和日常文化背景进行评估，这是评估非英语/本地知识更广泛努力的一部分，旨在改善AI在印度实际用例中的表现。

---

### 7. [Perplexity成为Snapchat默认AI合作伙伴](https://twitter.com/Snap/status/1986191838529601835)
> Perplexity将从2026年1月起成为Snapchat聊天中的默认AI，这一重大合作标志着AI搜索服务向主流社交平台的深度集成。

---

### 8. [Gemini深度集成Google产品生态系统](https://twitter.com/Google/status/1986190599150518573)
> Gemini Deep Research现在可以从Workspace（Gmail、Drive、Chat）提取信息生成全面报告，同时Gemini也集成到Google Maps中，支持免提路由查询和复杂多步骤请求。

---

### 9. [Apple Siri将集成Google Gemini模型](https://www.macrumors.com/2025/11/05/apple-siri-google-gemini-partnership/)
> Apple将集成Google的1.2万亿参数Gemini AI模型到Siri中，据报道这一合作每年将花费Apple 10亿美元，标志着Apple AI战略的重大转变。

---

### 10. [Roblox开源大规模PII分类器](https://huggingface.co/Roblox/roblox-pii-classifier)
> Roblox开源其PII分类器AI用于聊天安全，该工具每天处理约61亿条消息，峰值可达20万QPS，P90延迟低于100毫秒，为大规模AI安全应用提供工业级解决方案。

---

## 🛠️ 十大工具产品要点

### 1. [vLLM v1正式支持混合模型](https://twitter.com/PyTorch/status/1986192579835150436)
> IBM的vLLM团队在vLLM v1中将混合模型（密集+稀疏专家）作为一等公民支持，超越v0中的实验性方案。现支持Qwen3-Next、Nemotron Nano 2、Granite 4.0等模型。

---

### 2. [Graphiti MCP实现跨应用共享内存](https://twitter.com/_avichawla/status/1985958015452020788)
> 实际演示展示如何将本地Graphiti MCP服务器连接到Claude Desktop和Cursor，作为"代理内存"跨工具持久化和检索时序知识图，完全在本地运行。

---

### 3. [Cursor报告语义搜索显著提升代码检索准确性](https://twitter.com/cursor_ai/status/1986124270548709620)
> Cursor报告在大型代码库中使用语义搜索相比grep获得显著收益，包括训练代码检索嵌入，为代码理解和代理工作流提供重要改进。

---

### 4. [MotionStream实现单H100实时视频生成](https://twitter.com/_akhaliq/status/1986054085766750630)
> MotionStream在单个H100上达到约29 FPS/0.4秒延迟，具有交互式运动控制，为实时视频生成应用开辟新可能性。

---

### 5. [Google Veo 3.1支持后期相机编辑](https://twitter.com/TheoMediaAI/status/1986104791454388289)
> Google的Veo 3.1"相机调整"功能支持对先前生成的剪辑进行角度/运动更改，早期用户测试显示强大的后期制作控制能力。

---

### 6. [LM Studio 0.3.31发布VLM OCR和Flash Attention优化](https://cdn.discordapp.com/attachments/1111797717639901324/1435707995685392524/lms-runtime-demo5.mp4)
> LM Studio 0.3.31提供更快的VLM OCR性能，默认在CUDA GPU上启用Flash Attention，添加图像输入大小控制（默认2048px），包含macOS 26兼容性修复和MiniMax-M2工具调用支持。

---

### 7. [TinyCorp发布tinybox pro v2工作站](https://tinycorp.myshopify.com/products/tinybox-pro-v2)
> TinyCorp开放tinybox pro v2订单，这是5U可上架工作站，配备8×RTX 5090，定价5万美元，目标在GPU租赁网站上达到3-4美元/小时的专业级计算。

---

### 8. [Windsurf推出Codemaps代码理解工具](https://x.com/windsurf/status/1985757575745593459)
> Windsurf推出由SWE-1.5和Sonnet 4.5驱动的Codemaps，定位为代理工作流的基础，认为"编码能力的最大约束是你理解正在处理的代码的能力"。

---

### 9. [Hugging Face发布200+页Smol训练手册](https://twitter.com/LoubnaBenAllal1/status/1986110843600117760)
> Hugging Face发布200多页的Smol训练手册，涵盖架构/训练前/训练中/训练后/评估，配有可视化解释器，为AI训练提供全面指导。

---

### 10. [Unsloth AI发布DeepSeek-OCR微调笔记本](https://x.com/UnslothAI/status/1985728926556307471)
> Unsloth AI推出DeepSeek-OCR微调笔记本，用户报告比TRL提供速度提升和更低内存使用，通过修补TRL和Transformers添加自身优化来降低VRAM使用。

---