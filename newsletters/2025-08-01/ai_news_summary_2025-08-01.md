## AINews - 2025-08-01

> [原文链接](https://news.smol.ai/issues/25-07-30-not-much/)

## 📰 十大AI新闻要点

### 1. [中国开源模型爆发：GLM-4.5、Qwen3和Kimi K2发布](https://twitter.com/Yuchenj_UW/status/1950034092457939072)
> 中国实验室7月集中发布多个高性能开源模型，包括Zhipu AI的GLM-4.5（355B MoE）、阿里Qwen3-235B系列和Moonshot AI的Kimi K2（1T MoE），均采用宽松许可证。分析师指出西方开源进度放缓可能造成竞争劣势。

---

### 2. [Zhipu AI发布MIT许可的GLM-4.5系列](https://twitter.com/Zai_org/status/1950164491125043515)
> GLM-4.5（355B参数MoE）和轻量版GLM-4.5-Air在部分基准测试超越Gemini 2.5 Pro，接近Claude 4 Opus水平。因需求激增，公司正紧急扩容计算资源，社区已快速适配MLX/DeepInfra平台。

---

### 3. [Qwen3 Coder展现顶尖编程能力](https://twitter.com/cline/status/1949973297455599998)
> 阿里Qwen3 Coder在Cline测试中仅5.32%编辑失败率，与Claude Sonnet 4持平。30B MoE版本支持256K上下文，已可通过MLX/Ollama本地运行，成本仅$0.3-0.45/百万token。

---

### 4. [xAI推出Grok Imagine图像视频生成工具](https://twitter.com/chaitualuru/status/1949946519869685952)
> 马斯克旗下xAI发布Grok Imagine进入等待名单，同期Wan2.2视频模型展示创新I2V技术——每潜在帧独立去噪时间步，理论上支持无限长视频生成。

---

### 5. [Meta宣布收紧AI开源策略](https://www.meta.com/superintelligence/)
> 扎克伯格声明因安全考虑将限制最先进模型的开源，标志从Llama系列宽松政策转向。社区批评其违背早期开放承诺，但实际影响有限因现有开源模型已超越Llama 4。

---

### 6. [Runway Aleph视频模型颠覆传统工作流](https://twitter.com/c_valenzuelab/status/1950138170806312974)
> 新视频模型只需提示词即可完成"昼夜转换"、"场景去车"等复杂编辑，对比传统需多步骤手动处理。展示案例包括[爆炸特效添加](https://twitter.com/c_valenzuelab/status/1950257984715571606)。

---

### 7. [单卡H200实现120万token长度训练](https://twitter.com/StasBekman/status/1950232169227624751)
> 结合ALST、FlashAttention-3和Liger-Kernel技术，Llama-8B模型在单张H200上突破120万序列长度训练，int64索引问题已获修复。

---

### 8. [AMD正式参与llama.cpp开发](https://twitter.com/ggerganov/status/1950047168280060125)
> AMD工程师开始为llama.cpp提交代码，预示该流行推理框架将获得更广泛硬件支持，可能改变当前NVIDIA主导的AI加速格局。

---

### 9. [GPT-5发布迹象集中出现](https://i.redd.it/xk0egrlaxzff1.png)
> ChatGPT macOS客户端代码泄露"gpt-5-auto"和"gpt-5-reasoning"模型选项，配合官方推特神秘日文预告，强烈暗示GPT-5即将发布。

---

### 10. [AI人才拒绝Meta 4亿美元offer引热议](https://twitter.com/willdepue/status/1950253835064086979)
> 顶尖AI研究者接连拒绝Meta天价报价，引发行业对神秘竞品公司的猜测。同期讨论指出能源供给已成比GPU资本更严重的算力扩展瓶颈。

---

## 🛠️ 十大工具产品要点

### 1. [Qwen3-30B-A3B本地推理方案](https://huggingface.co/unsloth/Qwen3-30B-A3B-Thinking-2507-GGUF)
> 量化版Qwen3-30B-A3B可在消费级笔记本无GPU下实现5-10 token/s速度，社区提供GGUF格式适配llama.cpp，复杂任务建议输出长度设为81k token。

---

### 2. [WAN 2.2全合一视频模型合并](https://huggingface.co/Phr00t/WAN2.2-14B-Rapid-AllInOne)
> 整合WAN 2.2高/低模块与2.1输出块，支持4步1CFG采样，保留2.1 LoRA兼容性。12GB显卡实测T2V性能强劲但输出多样性略有降低。

---

### 3. [Claude移动端通信自动化](http://claude.ai/download)
> 新增邮件/短信/会议预约起草功能，通过系统意图调用保护隐私。Android实现仅预填内容字段，需用户手动指定收件人。

---

### 4. [BlockDL可视化Keras设计工具](https://twitter.com/fchollet/status/1950244806967603207)
> Keras之父发布免费开源GUI工具，支持神经网络可视化设计，降低深度学习入门门槛。

---

### 5. [LangGraph代理工作流指南](https://twitter.com/LangChainAI/status/1950226846538485918)
> 提供6种上下文工程实践的视频代码示例，包括自修正RAG代理构建方案，LangSmith Traces新增服务日志集成。

---

### 6. [Perplexity Comet浏览器实操演示](https://twitter.com/AravSrinivas/status/1949937085164482846)
> 内置Perplexity搜索的浏览器完成联合航空订票全流程（含选座），展示复杂任务自动化潜力。

---

### 7. [StepMesh开源通信库](https://twitter.com/teortaxesTex/status/1950127131754651655)
> 中国StepFun公司发布Attention-FFN解耦的推理系统通信库，优化大模型分布式推理效率。

---

### 8. [Qdrant Edge设备端向量搜索](https://twitter.com/qdrant_engine/status/1950165409639833603)
> 轻量级嵌入式搜索引擎私有测试启动，面向机器人/移动/IoT场景，实现本地化向量检索。

---

### 9. [SmolLM3完整训练代码开源](https://twitter.com/LoubbaBenAllal1/status/1950139809034305568)
> 包含nanotron预训练、TRL对齐和100+中间检查点的全栈代码Apache 2.0发布。

---

### 10. [Ideogram角色一致性模型](https://twitter.com/hojonathanho/status/1950261122365333806)
> 单参考图像即可维持多帧角色一致性，解决AI视频生成中的形象漂移问题。