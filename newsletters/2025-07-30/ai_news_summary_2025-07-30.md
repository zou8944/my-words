## AINews - 2025-07-30

> [原文链接](https://news.smol.ai/issues/25-07-28-glm-45/)

## 📰 十大AI新闻要点

### 1. [Zhipu AI发布GLM-4.5开源模型](https://z.ai/blog/glm-4.5)
> Zhipu AI（智谱AI）发布GLM-4.5系列开源模型，包括355B/32B和106B/12B两个版本，采用MIT许可。官方宣称其性能超越Kimi K-2等开源模型，并与Claude 4 Opus等商业模型竞争。特别强调了对Agent任务优化的token效率指标。

### 2. [阿里巴巴Qwen3模型套件发布](https://twitter.com/Alibaba_Qwen/status/1949412072942612873)
> 阿里巴巴推出Qwen3系列模型（Instruct/Coder/Thinking），采用新型强化学习算法GSPO（Group Sequence Policy Optimization），已集成至Hugging Face的TRL库。该算法被评价为"迄今最令人印象深刻的论文"。

### 3. [GPT-5疑似以"Summit/Zenith"代号现身](https://twitter.com/Teknium1/status/1949116545936110035)
> LM Arena平台出现代号"Summit"和"Zenith"的神秘模型，据传可能是GPT-5的早期版本。测试显示其能生成复杂的p5.js代码，知识截止日期为2024年6月。

### 4. [腾讯开源Hunyuan3D世界模型](https://twitter.com/scaling01/status/1949300037051134245)
> 腾讯开源Hunyuan3D World Model 1.0，支持生成可探索的3D环境。这是中国AI实验室近期系列重要开源发布之一。

### 5. [Runway推出Aleph视频模型](https://twitter.com/c_valenzuelab/status/1949872250376667517)
> Runway开始推出新一代视频生成模型Aleph，展示无限镜头生成、物体移除、服装修改等能力，被描述为"新媒体形式"。

### 6. [阿里巴巴发布Wan 2.2开源视频模型](https://wan.video/welcome)
> 阿里巴巴发布全球首个基于MoE架构的开源视频生成模型Wan 2.2，包含14B MoE和5B密集版本，支持单张RTX 4090上24FPS生成。

### 7. [Claude代码插件生态系统发展](https://github.com/vijaythecoder/awesome-claude-agents)
> Claude社区开发出26个专业子Agent组成的开发团队模拟系统，以及CCPlugins等实用工具，显著提升代码工作流效率。

### 8. [OpenAI将实施Claude订阅用户速率限制](https://www.reddit.com/r/ClaudeAI/comments/1mbo1sb/updating_rate_limits_for_claude_subscription/)
> Anthropic宣布将于8月下旬对Claude Pro/Max订阅用户实施周速率限制，影响约5%的高强度用户，旨在防止API滥用。

### 9. [Perplexity推出Comet浏览器Agent](https://twitter.com/AravSrinivas/status/1949937085164482846)
> Perplexity AI展示其浏览器Agent Comet作为旅行代理的用例，可完成航班预订和座位选择等复杂任务。

### 10. [新型优化器Muon获大规模验证](https://z.ai/blog/glm-4.5)
> GLM 4.5成为本月第二个验证Muon优化器在大模型上有效性的案例，显示其在高效RL训练方面的潜力。

---

## 🛠️ 十大工具产品要点

### 1. [GLM-4.5模型技术特性](https://huggingface.co/zai-org/GLM-4.5)
> 采用混合推理模式(思考/非思考模式)和原生多token预测(MTP)层，支持推测解码，优化CPU+GPU混合硬件推理效率。

### 2. [Wan 2.2视频模型架构](https://huggingface.co/Wan-AI)
> 14B MoE模型采用双专家系统(高噪声/低噪声)，基于SNR阈值切换，无额外推理成本，在动态运动和文本渲染方面超越商业SOTA。

### 3. [UIGEN-X UI专业模型](https://huggingface.co/Tesslate/UIGEN-X-32B-0727)
> 基于Qwen3微调的32B模型，专攻UI/UX设计，支持26+语言和主流前端框架，需要64GB VRAM运行。

### 4. [Qwen3-30B-A3B指令模型](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507)
> 阿里巴巴发布的30B参数模型，平衡性能与消费级硬件兼容性，被社区期待为本地运行LLM的新标杆。

### 5. [ComfyUI对Wan 2.2的支持](https://docs.comfy.org/tutorials/video/wan/wan2_2)
> 提供专门工作流指南和FP16/FP8重打包模型，支持图像到视频的两阶段处理流程。

### 6. [Claude自定义子Agent系统](https://github.com/vijaythecoder/awesome-claude-agents)
> 包含26个专业角色的协调AI开发团队模拟，通过"技术主管"协调器和CLI配置实现复杂任务分解。

### 7. [LangGraph v0.6.0发布](https://twitter.com/LangChainAI/status/1949860132642320624)
> 新增类型安全的上下文API，支持依赖注入，提升多Agent系统开发效率。

### 8. [supervision库突破3万星](https://twitter.com/skalskip92/status/1949857474862866659)
> 这个开源计算机视觉库在GitHub上获得广泛认可，提供丰富的视觉任务工具集。

### 9. [HuggingFace集成GSPO算法](https://twitter.com/_lewtun/status/1949951668914659636)
> TRL库已集成阿里巴巴的GSPO强化学习算法，支持大规模MoE模型的高效训练。

### 10. [llama.cpp获AMD团队贡献](https://twitter.com/ggerganov/status/1949907603942691027)
> AMD工程师开始为llama.cpp代码库做贡献，预示着更广泛的硬件支持前景。