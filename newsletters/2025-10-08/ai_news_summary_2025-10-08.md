## AINews - 2025-10-08

> [原文链接](https://news.smol.ai/issues/25-10-06-devday/)

## 📰 十大AI新闻要点

### 1. [OpenAI DevDay发布多项重磅产品](https://openai.com/devday)
> OpenAI在开发者大会上发布了ChatGPT应用平台、AgentKit端到端代理栈、Codex正式可用、GPT-5 Pro等新模型，以及Sora 2视频生成API，标志着向应用平台转型的重大战略升级

---

### 2. [GPT-5 Pro正式发布](https://platform.openai.com/docs/models/gpt-5-pro)
> GPT-5 Pro现已在API中可用，定价为输入15美元/输出120美元每百万tokens，针对需要更强推理能力的重型任务进行了优化

---

### 3. [Sora 2和Sora 2 Pro开放API访问](https://platform.openai.com/docs/models/sora-2)
> Sora 2系列视频生成模型正式通过API提供，支持声音、混音和时长控制，定价为Sora 2每秒0.10美元(720p)，Sora 2 Pro每秒0.30美元(720p)/0.50美元(1024p)

---

### 4. [OpenAI与AMD达成多年合作协议](https://twitter.com/sama/status/1975185516225278428)
> OpenAI与AMD宣布部署6GW Instinct GPU的多年度计划，AMD向OpenAI发行最多1.6亿股认股权证，这是对现有NVIDIA采购的补充

---

### 5. [中国模型Qwen3-VL-30B-A3B发布](https://twitter.com/Alibaba_Qwen/status/1974289216113947039)
> 阿里巴巴发布Qwen3-VL-30B-A3B模型，采用MoE架构约30亿激活参数，支持256k-1M上下文和32种语言，目标达到GPT-5-Mini/Claude Sonnet同等水平

---

### 6. [GLM-4.6在LMArena排名第一](https://twitter.com/arena/status/1975220164703752351)
> 智谱AI的GLM-4.6在LMArena排行榜中成为顶级开源模型，总体排名第四，即使没有"风格控制"也表现出色

---

### 7. [特斯拉Optimus学习功夫](https://twitter.com/elonmusk/status/1974338806305411516)
> 特斯拉Optimus人形机器人能力快速提升，现在正在"学习功夫"，领导层暗示将统一自动驾驶和人形机器人技术栈

---

### 8. [Figure人形机器人在宝马生产线运行5个月](https://twitter.com/adcock_brett/status/1975197913178587172)
> Figure人形机器人在宝马X3车身车间生产线已连续运行5个月，每天工作10小时，据称是全球首个在汽车制造中持续部署的人形机器人

---

### 9. [LoRA在强化学习中表现优异](https://twitter.com/johnschulman2/status/1974948097500582254)
> John Schulman强调多个复现显示LoRA rank=1在各种RL设置中与完全微调效果接近，TRL发布了"LoRA without regret"参考复现

---

### 10. [Google DeepMind CodeMender贡献72个安全修复](https://twitter.com/GoogleDeepMind/status/1975185557593448704)
> Google DeepMind的CodeMender代理已向主要开源仓库提交了72个被接受的安全修复，该AI代理能自动发现和修复代码漏洞

---

## 🛠️ 十大工具产品要点

### 1. [ChatGPT应用平台和Apps SDK](https://openai.com/index/introducing-apps-in-chatgpt)
> OpenAI将ChatGPT转变为应用平台，新的Apps SDK让合作伙伴直接在ChatGPT中嵌入完整交互式应用，早期合作伙伴包括Canva、Figma、Zillow和Coursera

---

### 2. [AgentKit端到端代理栈](https://openai.com/index/introducing-agentkit)
> OpenAI推出端到端代理栈，包含可视化Agent Builder、ChatKit UI、Guardrails、Evals和Connectors，可在8分钟内构建工作代理

---

### 3. [Codex正式可用并发布SDK](https://openai.com/index/codex-now-generally-available)
> Codex现正式可用，提供SDK、Slack集成和企业控制/分析功能，支持代码审查和CLI/IDE工作流，某些内部构建中80%的PR由Codex编写

---

### 4. [gpt-realtime-mini成本降低70%](https://platform.openai.com/docs/models/gpt-realtime-mini)
> gpt-realtime-mini提供语音到语音功能，成本比gpt-realtime降低约70%，为实时语音交互提供更经济的解决方案

---

### 5. [gpt-image-1-mini成本降低80%](https://platform.openai.com/docs/models/gpt-image-1-mini)
> gpt-image-1-mini图像生成模型成本降低80%，为图像生成应用提供更经济的API选择

---

### 6. [LM Studio支持OpenAI v1响应兼容](https://lmstudio.ai/blog/lmstudio-v0.3.29)
> LM Studio 0.3.29添加OpenAI /v1/responses兼容性API，让期望标准OpenAI API格式的应用能直接集成本地模型

---

### 7. [NVIDIA TensorRT-LLM v1.0发布](https://twitter.com/ZhihuFrontier/status/1974559265273639349)
> NVIDIA TensorRT-LLM达到v1.0版本，具有PyTorch原生核心、CUDA Graphs、推测解码和GB200支持，现服务于Llama3、DeepSeek V3/R1、Qwen3等模型

---

### 8. [Anthropic开源Petri对齐审计工具包](https://twitter.com/AnthropicAI/status/1975248654609875208)
> Anthropic开源Petri，这是一个场景驱动的对齐审计工具包，用于内部4.5对齐测试（奉承、欺骗），已被AISec研究所用于外部评估

---

### 9. [vLLM支持PipelineRL实时权重更新](https://twitter.com/vllm_project/status/1974732295627301254)
> vLLM继续支持前沿RL循环，如PipelineRL具有飞行中权重更新和陈旧KV缓存混合功能，为强化学习提供基础设施支持

---

### 10. [Arm宣布支持6位AI数据类型](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-a-profile-architecture-developments-2025)
> Arm宣布通过OCP MXFP6格式支持6位AI数据类型，包含新的SVE/SME指令，针对边缘/嵌入式AI减少内存占用和带宽

---