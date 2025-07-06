## AINews - 2025-06-30

> [原文链接](https://news.smol.ai/issues/25-06-27-not-much/)

## 📰 十大AI新闻要点

### 1. [Google发布Gemma 3n多模态边缘设备模型](https://twitter.com/GoogleDeepMind/status/1938394979727999455)
> Google推出Gemma 3n，专为边缘设备设计的文本/音频/图像/视频多模态模型，提供2B和4B参数版本，支持Transformers/vLLM/MLX/Llama.cpp等框架。

### 2. [腾讯开源Hunyuan-A13B MoE大模型](https://github.com/Tencent-Hunyuan/Hunyuan-A13B)
> 80B总参数(13.5B激活)的混合专家模型，具备256K上下文窗口，在工具调用和编码任务上表现优异，采用Mamba层提升推理吞吐量。

### 3. [Black Forest Labs发布FLUX.1 Kontext图像模型](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev)
> 开源图像AI模型在Hugging Face获超2万关注，支持通过fal/Replicate等服务快速部署，商业使用输出需遵守特殊许可条款。

### 4. [Inception AI推出首款商用扩散LLM Mercury](https://twitter.com/tri_dao/status/1938592578183614518)
> 专为聊天应用设计的扩散语言模型，以超快响应速度为特色，开创扩散模型在对话场景的商业化应用。

### 5. [OpenAI开放Deep Research API及完整提示词](https://twitter.com/swyx/status/1938399666330341831)
> 基于o3/o4-mini模型的深度研究API开放完整提示方法论，支持开发者构建多智能体系统(MCP)，已集成LangChain/LangGraph。

### 6. [Gemini CLI终端工具获3万GitHub星](https://github.com/google/generative-ai-cli)
> Google开发的AI终端助手，支持代码编写/调试/应用生成，24小时内获得25.8k星标，显示开发者对Gemini生态的强烈兴趣。

### 7. [LlamaCloud集成MCP多智能体通信协议](https://twitter.com/jerryjliu0/status/1938679670217793573)
> LlamaIndex知识库现支持原生MCP服务器，5分钟内实现无代码高精度文档理解，同步推出自动化表单解析功能。

### 8. [Prime Intellect完成SYNTHETIC-2去中心化数据集](https://x.com/PrimeIntellect/status/1938490370054361422)
> 通过1250+GPU(P2P网络)3天生成400万条验证推理轨迹，50%样本使用Qwen3 4B验证，技术报告即将开源。

### 9. [Neuralink植入手术间隔缩短至1周](https://www.reddit.com/r/singularity/comments/1lm2vnv/neuralink_now_implanted_chips_on_7_individuals/)
> 第7例人类植入完成，手术间隔从最初6个月压缩至1周，显示手术流程显著优化，但设备可靠性问题仍存争议。

### 10. [RTX 3090价格回落至600美元区间](https://www.reddit.com/r/LocalLLaMA/comments/1llms46/fyi_to_everyone_rtx_3090_prices_crashed_and_are/)
> 美国市场RTX 3090价格回归650-750美元基准线，建议购买二手卡时进行FurMark/Heaven压力测试验证稳定性。

---

## 🛠️ 十大工具产品要点

### 1. [FLUX Kontext区域提示编辑功能](https://docs.bfl.ai/guides/prompting_guide_kontext_i2i#visual-cues)
> 通过绘制彩色框(如绿色)实现局部图像编辑指令，支持"在绿框添加带小白鼠的翻盖口袋"等精确控制。

### 2. [单图转LoRA自动化工作流](https://github.com/lovisdotio/workflow-comfyui-single-image-to-lora-flux)
> 使用Gemini生成20提示词→FLUX.1生成变体→训练LoRA的端到端流程，ComfyUI节点优化使复杂度降低90%。

### 3. [PS Vita版LLM客户端](https://github.com/callbacked/vela)
> 为PlayStation Vita开发的LLM接口工具，可连接远程模型端点，利用设备摄像头实现多模态输入，支持TeX/Markdown渲染。

### 4. [OpenEvolve金属内核优化](https://github.com/codelion/openevolve)
> 进化编程发现的Metal内核比人工优化快12.5%(峰值106%)，采用vec<T,8> SIMD和新型双通道softmax算法。

### 5. [Qwen-VLo视觉语言统一模型](https://qwenlm.github.io/blog/qwen-vlo/)
> 支持视觉理解和生成的双模态模型，在图像描述和生成任务中展现强大能力。

### 6. [Kyutai Labs开源语音转文本模型](https://twitter.com/ClementDelangue/status/1938561475930739178)
> 在Open ASR排行榜流式模型中排名第一，支持通过MLX在Mac/iPhone设备本地运行。

### 7. [OmniGen2开源图像编辑模型](https://github.com/VectorSpaceLab/OmniGen2)
> Apache许可的生成模型，可实现"Photoshop级"局部编辑(如改变服装颜色/添加微笑)而保持其他区域不变。

### 8. [Bruteforce种子查找器GPU加速](https://github.com/kr1viah/WKChallengeModeSeedFinder)
> GTX 1660实现比R7 5800X快10倍的暴力破解速度，展示GPU在特定算法中的计算优势。

### 9. [Llama3 SSML语音合成集成](https://arxiv.org/abs/2505.19488v1)
> 结合Azure Voice服务，利用Llama模型生成富有情感的SSML输出，推动语音Avatar技术发展。

### 10. [WeirdML V2机器学习基准](https://twitter.com/scaling01/status/1938610923389727109)
> 专门评估LLM在ML任务表现的测试集，显示o3-pro在数据分布理解任务上符合成本/性能预期。
```