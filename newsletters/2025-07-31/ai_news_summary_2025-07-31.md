## AINews - 2025-07-31

> [原文链接](https://news.smol.ai/issues/25-07-28-glm-45/)

## 📰 十大AI新闻要点

### 1. [Zhipu AI发布GLM-4.5开源模型](https://z.ai/blog/glm-4.5)
> 中国AI公司Zhipu AI（智谱）发布了GLM-4.5系列开源模型，包括355B/32B和106B/12B两个版本，采用MIT许可。该模型声称在多项基准测试中超越Claude 4 Opus、Grok 4等前沿模型，特别强调在代理任务中的token效率表现。

### 2. [阿里巴巴发布Qwen3模型套件和GSPO算法](https://twitter.com/Alibaba_Qwen/status/1949412072942612873)
> 阿里巴巴Qwen团队推出Group Sequence Policy Optimization (GSPO)强化学习算法，并发布Qwen3系列模型（Instruct/Coder/Thinking）。该算法已集成到Hugging Face的TRL库，被评价为"迄今为止最令人印象深刻的论文"。

### 3. [GPT-5疑似以"Summit"和"Zenith"代号现身LM Arena](https://twitter.com/Teknium1/status/1949116545936110035)
> 代号"Summit"和"Zenith"的神秘模型出现在LM Arena平台，据传可能是GPT-5的早期版本。测试显示这些模型能生成复杂的p5.js代码，知识截止日期为2024年6月。

### 4. [腾讯开源Hunyuan3D世界模型1.0](https://twitter.com/scaling01/status/1949300037051134245)
> 腾讯Hunyuan团队开源了3D世界生成模型Hunyuan3D World Model 1.0，能够创建可探索的3D环境，标志着中国在3D生成AI领域的重要进展。

### 5. [Runway推出Aleph视频模型](https://twitter.com/c_valenzuelab/status/1949872250376667517)
> Runway开始推出其最先进的上下文视频模型Aleph，展示无限摄像机覆盖、对象移除、服装修改等能力，被描述为"新媒体形式"。

### 6. [阿里巴巴发布开源视频模型Wan 2.2](https://wan.video/welcome)
> 阿里巴巴发布全球首个开源MoE架构视频生成模型Wan 2.2，包括27B MoE和5B密集版本，支持文本/图像到视频转换，可在单张RTX 4090上实现24FPS生成。

### 7. [Claude代码插件生态系统发展](https://github.com/vijaythecoder/awesome-claude-agents)
> Claude社区开发出26个专业子代理组成的开发团队模拟系统，以及CCPlugins等命令行工具，显著提升了Claude在代码生成和项目管理方面的能力。

### 8. [OpenAI将实施Claude订阅用户速率限制](https://www.reddit.com/r/ClaudeAI/comments/1mbo1sb/updating_rate_limits_for_claude_subscription/)
> Anthropic宣布将从8月底开始对Claude Pro和Max订阅用户实施每周速率限制，影响约5%的高使用量用户，旨在防止资源滥用。

### 9. [Perplexity推出Comet浏览器代理](https://twitter.com/AravSrinivas/status/1949937085164482846)
> Perplexity AI继续发放其Comet浏览器代理的测试邀请，展示作为旅行代理预订航班的能力，并将Perplexity设为默认搜索引擎。

### 10. [Meta任命OpenAI博士毕业生为首席科学家](https://twitter.com/Yuchenj_UW/status/1948949960877375662)
> Meta任命一位刚从OpenAI毕业的30岁博士担任首席科学家，反映出AI行业"技能>资历"的人才选拔趋势。

---

## 🛠️ 十大工具产品要点

### 1. [GLM-4.5模型技术特点](https://z.ai/blog/glm-4.5)
> GLM-4.5采用混合推理架构，具有"思考"和"非思考"两种模式，内置多token预测层支持推测解码，显著提升CPU+GPU硬件上的推理效率。

### 2. [Wan 2.2视频模型技术细节](https://huggingface.co/Wan-AI)
> Wan 2.2采用基于SNR阈值的MoE扩散架构，包含高噪声和低噪声两个14B专家模型，在Wan-Bench 2.0基准测试中超越KLING 2.0、Sora等商业模型。

### 3. [UIGEN-X-0727 UI设计专用模型](https://huggingface.co/Tesslate/UIGEN-X-32B-0727)
> Tesslate发布的32B参数UI设计专用模型，支持React/Vue/Angular等26+语言框架，在UI/UX设计和前端开发方面表现优异。

### 4. [Qwen3-30B-A3B-Instruct模型](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507)
> 阿里巴巴Qwen团队发布的30B参数指令模型，平衡性能与消费级硬件效率，被社区评价为"日常使用的最佳选择"。

### 5. [ComfyUI-GGUF工作流支持](https://github.com/city96/ComfyUI-GGUF)
> ComfyUI-GGUF扩展支持Wan 2.2等模型的GGUF量化格式运行，使大模型能在消费级GPU上部署。

### 6. [LangGraph v0.6.0发布](https://twitter.com/LangChainAI/status/1949860132642320624)
> LangGraph发布0.6.0版本，新增类型安全的上下文API和依赖注入功能，提升多代理系统开发效率。

### 7. [supervision库突破3万星](https://twitter.com/skalskip92/status/1949857474862866659)
> 计算机视觉开源库supervision在GitHub上突破3万星，成为AI视觉领域的重要工具。

### 8. [Claude自定义子代理框架](https://github.com/vijaythecoder/awesome-claude-agents)
> 开源项目提供26个Claude子代理组成的开发团队模拟，包含技术主管协调机制，可配置并行执行任务。

### 9. [CCPlugins命令行工具集](https://github.com/fcakyon/claude-settings)
> Claude代码插件集合，采用对话式命令设计，支持项目清理、代码审查、测试运行等开发工作流自动化。

### 10. [Hunyuan3D世界模型应用](https://twitter.com/scaling01/status/1949300037051134245)
> 腾讯Hunyuan3D支持生成可交互的3D环境，为游戏开发、虚拟现实等领域提供新的内容创作工具。