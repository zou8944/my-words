## AINews - 2025-06-26

> [原文链接](https://news.smol.ai/issues/25-06-25-context-eng/)
## 📰 十大AI新闻要点

### 1. [Context Engineering成为AI工程关键趋势](https://cognition.ai/blog/dont-build-multi-agents)
> Cognition AI的Walden Yan提出"Context Engineering"概念，多位AI领袖（包括Karpathy、LangChain创始人等）认同这是比"Prompt Engineering"更准确的术语，指管理LLM上下文窗口的复杂技术，涉及RAG、工具调用、状态维护等。

### 2. [Google发布开源Gemini CLI工具](https://x.com/googleaidevs/status/1937861646082515205)
> Google推出Apache 2.0许可的Gemini终端代理，提供每日1000次免费请求和100万token上下文窗口，支持MCP协议，被视为与Anthropic的Claude Code直接竞争。

### 3. [Anthropic图书扫描训练数据获法院支持](https://storage.courtlistener.com/recap/gov.uscourts.cand.434709/gov.uscourts.cand.434709.231.0_3.pdf)
> 联邦法官裁定Anthropic购买并扫描实体书训练Claude模型属于合理使用，但保留700万盗版电子书的行为构成侵权，赔偿金额将由陪审团决定。

### 4. [DeepMind发布AlphaGenome基因组分析模型](https://deepmind.google/discover/blog/alphagenome-ai-for-better-understanding-the-genome/)
> 新型混合卷积+Transformer架构可处理100万碱基对输入，在转录调控和剪接预测等任务上达到SOTA，R值达0.8-0.85。

### 5. [Jan-nano-128k小模型性能超越大模型](https://huggingface.co/Menlo/Jan-nano-128k)
> Menlo Research发布的4B参数模型在SimpleQA基准测试中得分83.2，超过Deepseek-671B(78.2)和GPT-4o(62.5)，采用YaRN扩展技术实现128k上下文窗口。

### 6. [OpenAI为Pro用户新增云存储连接器](https://twitter.com/OpenAI/status/1937681383448539167)
> ChatGPT现可连接Google Drive、Dropbox、SharePoint和Box，允许用户将工作文件内容作为上下文使用（EEA、瑞士和英国除外）。

### 7. [DSPy框架获Shopify CEO公开推荐](https://twitter.com/lateinteraction/status/1938005712489083252)
> Tobi Lütke称DSPy是其"首选Context Engineering工具"，该框架基于Signatures和Modules的编程模型正在获得学术界和业界的广泛关注。

### 8. [Mistral Small 3.2展现超规格性能](https://huggingface.co/unsloth/Mistral-Small-3.2-24B-Instruct-2506-GGUF)
> 24B参数模型在写作和逻辑任务上超越Gemma 3 27B和Llama 3.3 70B，推荐推理参数：temperature 0.15, top-p 1.0。

### 9. [AI视频生成技术新突破](https://twitter.com/Kling_ai/status/1937838997730148766)
> Kling AI推出Motion Control功能可将源视频动作迁移到新图像，RunwayML的Gen-4 References模型也同期发布API版本。

### 10. [Perplexity CEO呼吁重建Android系统](https://twitter.com/AravSrinivas/status/1937732846543933569)
> Arav Srinivas认为当前Android系统为广告业务优化，需要为AI时代重构，并预言浏览器将成为AI智能体进化的"原始汤"。

---

## 🛠️ 十大工具产品要点

### 1. [Gemini CLI终端工具](https://blog.google/technology/developers/introducing-gemini-cli/)
> 开源终端代理，支持1百万token上下文，60 RPM速率限制，1000次/日免费请求，需要Gemini云API但提供数据收集退出选项。

### 2. [LM Studio新增MCP支持](https://lmstudio.ai/blog/mcp)
> v0.3.17版本新增Model Compatibility Protocol支持，可连接本地LLM，新增33种语言界面和Solarized Dark主题。

### 3. [ThermoAsk自调节温度技术](https://github.com/amanvirparhar/thermoask)
> 让LLM动态设置自身temperature参数的技术实现，已提供Ollama Python SDK和Qwen2.5-7B的示例代码。

### 4. [OpenRouter模型可用性API](https://x.com/OpenRouterAI/status/1937869909448441980)
> 新增API可监控各模型在线状态，BYOK功能支持密钥预测试和用量限制。

### 5. [LlamaIndex发布MCP服务器模板](https://twitter.com/jerryjliu0/status/1937653599972286873)
> 开源Next.js模板可快速构建Claude兼容的MCP服务器。

### 6. [Anthropic Artifacts Gallery](https://video.twimg.com/amplify_video/1937926883707891713/vid/avc1/1920x1080/3Gu7ntwPGQT0j8dX.mp4)
> 新功能允许用户在Claude内部构建和共享AI生成内容，支持实时协作。

### 7. [MakoGenerate GPU内核生成器](https://generate.mako.dev/)
> AI代理可自动生成优化GPU内核代码，支持H100/B200部署，VS Code扩展开发中。

### 8. [Hyperbolic XYZ廉价GPU租赁](https://app.hyperbolic.xyz/)
> 提供H100每小时$0.99、RTX 4090每小时$0.28的租赁服务，适合预算有限的开发者。

### 9. [BitNet演示版表现惊艳](https://bitnet-demo.azurewebsites.net/)
> 1.58-bit量化模型在速度和响应质量上获得好评，Hugging Face Space已开放。

### 10. [Cerebras云服务性价比突出](https://www.cerebras.ai/cloud)
> 晶圆级GPU服务价格与Blackwell相当但带宽较低，适合大规模训练任务。
