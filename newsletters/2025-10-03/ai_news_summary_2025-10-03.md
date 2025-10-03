## AINews - 2025-10-03

> [原文链接](https://news.smol.ai/issues/25-10-01-thinky/)

## 📰 十大AI新闻要点

### 1. [Thinking Machines发布首个产品Tinker](https://thinkingmachines.ai/blog/announcing-tinker/)
> Thinking Machines在融资20亿美元后推出首个产品Tinker，这是一个面向研究者的微调管理服务，提供低级别API原语（forward_backward、sample等），支持SFT、RL、LoRA等后训练方法，让研究者保留算法创意控制的同时外包基础设施管理

---

### 2. [OpenAI Sora 2作为消费社交应用发布](https://openai.com/index/sora-2/)
> OpenAI将Sora 2视频+音频模型集成到首个消费社交应用中，引发大规模参与和争议，包含"cameo"功能实现跨生成角色一致性，但面临滥用风险和"AI内容工厂"批评

---

### 3. [DeepSeek V3.2引入稀疏注意力技术](https://twitter.com/ArtificialAnlys/status/1973230103854456993)
> DeepSeek V3.2 Exp引入DeepSeek Sparse Attention技术，每个token仅关注约2048个token，使解码内存/FLOPs保持O(2048)复杂度，输入输出定价分别下降>50%和75%，MIT许可证

---

### 4. [Claude Sonnet 4.5发布编码和代理能力升级](https://twitter.com/augmentcode/status/1973431992097308983)
> Claude Sonnet 4.5在真实工作流程中显示更快的推理链和更高成功率，特别是在编码代理和Claude Code风格循环中，减少奉承行为，主动反驳错误前提

---

### 5. [智谱GLM-4.6专注效率优先发布](https://twitter.com/ZhihuFrontier/status/1973447038818762841)
> GLM-4.6优先考虑token效率和响应速度而非性能突破，在内部任务中对Claude Sonnet 4.5达到48.6%胜率，200K上下文，定价$0.60/$2.20每百万token

---

### 6. [阿里巴巴Qwen路线图曝光极端扩展计划](https://www.reddit.com/r/LocalLLaMA/comments/1nq182d/alibaba_just_unveiled_their_qwen_roadmap_the/)
> 阿里巴巴Qwen路线图显示激进扩展计划：上下文长度从1M→100M token，模型规模从~1T→10T参数，预训练数据从10T→100T token，测试时计算预算从64k→1M

---

### 7. [腾讯混元图像3.0预告开源文本到图像模型](https://www.reddit.com/r/LocalLLaMA/comments/1nqaiaz/tencent_is_teasing_the_worlds_most_powerful/)
> 腾讯预告"世界最强大"开源文本到图像模型混元图像3.0，传闻需要~96GB VRAM进行推理，但缺乏技术细节和基准测试验证

---

### 8. [中国风华3号GPU声称支持CUDA和DirectX](https://www.reddit.com/r/LocalLLaMA/comments/1nq1ia2/china_already_started_making_cuda_and_directx/)
> 中国风华3号GPU声称支持现代图形API包括DirectX 12、Vulkan 1.2和OpenGL 4.6，甚至支持CUDA，可能成为NVIDIA CUDA生态系统的替代方案

---

### 9. [Cerebras Systems完成11亿美元G轮融资](https://www.cerebras.ai/press-release/series-g)
> Cerebras Systems宣布完成11亿美元G轮融资，估值81亿美元，用于扩展AI处理器研发、美国制造和全球数据中心

---

### 10. [Ring-1T预览版开源"思考"模型发布](https://xcancel.com/antlingagi/status/1972711364876697612)
> 研究人员发布开源"思考"模型Ring-1T-preview（1T参数），声称在AIME25和HMMT25数学测试中获得顶级分数，分别为92.6和84.5

---

## 🛠️ 十大工具产品要点

### 1. [Tinker Cookbook开源库发布](https://github.com/thinking-machines-lab/tinker-cookbook)
> Thinking Machines发布Tinker Cookbook开源库，包含在现代后训练方法的实现，运行在Tinker API之上，帮助用户获得良好结果

---

### 2. [OpenRouter集成Stripe实时计费](https://x.com/OpenRouterAI/status/1973220421601468689)
> OpenRouter宣布与Stripe集成，实现实时LLM会计和基于使用的计费迁移，仅共享会计数据而保持提示词私密

---

### 3. [OpenRouter提供百万免费BYOK请求](https://openrouter.ai/announcements/1-million-free-byok-requests-per-month)
> 从2025年10月1日起，OpenRouter为所有用户提供每月100万免费BYOK请求，超出部分按标准5%费率收费

---

### 4. [Hugging Face发布Trackio本地实验跟踪](https://github.com/gradio-app/trackio)
> Hugging Face推出Trackio，作为Weights & Biases的本地优先免费替代品，支持指标/表格/图像/视频记录，注重隐私和可重现性

---

### 5. [vLLM实现极高吞吐性能](https://docs.vllm.ai/en/latest/serving/parallelism_scaling.html)
> vLLM在RTX 4070上运行Qwen3 0.6B模型，10个并发请求达到~1470.4 token/秒吞吐量，得益于PagedAttention和调度优化

---

### 6. [Wan-Alpha透明视频生成框架](https://github.com/WeChatCV/Wan-Alpha)
> Wan-Alpha提出RGBA视频生成框架，通过设计将alpha通道编码到RGB潜在空间的VAE，在多样化RGBA视频数据集上训练扩散变换器

---

### 7. [Wan-Alpha ComfyUI节点可用](https://huggingface.co/htdong/Wan-Alpha_ComfyUI)
> Wan-Alpha提供ComfyUI节点，便于集成到现有I2V工作流程和节点图中，支持LoRA控制和风格混合

---

### 8. [FlashMLA集成DeepSeek稀疏注意力](https://github.com/deepseek-ai/FlashMLA/pull/98)
> FlashMLA拉取请求讨论集成DeepSeek稀疏注意力v3.2及其"类似Mamba选择性"子注意力机制，旨在收紧焦点和减少计算

---

### 9. [Unsloth AI支持Blackwell GPU优化](来源：文章内容)
> Unsloth AI社区讨论Blackwell GPU（RTX 50xx系列）上的Xformers兼容性问题，需要手动编译以解决兼容性问题

---

### 10. [GRPO训练器在Colab上实现](https://colab.research.google.com/drive/1NhzJEDB7_vNw7gB49y3MrTWiNLJX1gPT)
> 社区成员创建首个GRPO训练器并在Colab笔记本中记录，虽然比LoRA微调慢，但训练损失接近零而奖励值缓慢上升

---