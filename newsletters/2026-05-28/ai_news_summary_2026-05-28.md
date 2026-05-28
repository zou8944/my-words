## AINews - 2026-05-28

> [原文链接](https://news.smol.ai/issues/26-05-26-not-much/)

## 📰 十大AI新闻要点

### 1. [“Harness工程”成为编码Agent的核心差异化因素](https://x.com/ZhihuFrontier/status/2059180748637376843)
> 多位专家一致认为，当前Agent的制胜关键在于 **模型 + Harness + 评估循环**，而非仅仅依赖更强的基座模型。DeepSeek正在组建专门的Harness团队，以闭环模型输出、运行时反馈、验证和修正。Google的Gemini Managed Agents指南将Agent基础设施封装为单一API调用，而LangChain和dair.ai也正式化了这一堆栈，核心包括：**上下文治理、可信记忆、动态技能路由**。

---

### 2. [DeepSWE基准测试：更贴近真实开发者体验](https://x.com/serenaa_ge/status/2059308218564890875)
> 新推出的Agent编码基准测试DeepSWE获得了从业者的强烈认可，被誉为“首个与实际使用这些模型编码的感觉一致的代码基准”。它在顶尖模型间创造了比公开SWE排行榜更大的区分度。同时，Qwen3.7 Max在Code Arena: Frontend上排名第4，与Claude Opus 4.6在Agentic Web开发任务上大致持平。

---

### 3. [Claude Mythos解决埃尔德什难题#90，揭示模型能力“过剩”](https://x.com/__alpoge__/status/2059298565093196012)
> 一位数学家报告称，Claude Mythos成功解决了埃尔德什难题#90，并且常常收敛到与OpenAI早期路径不同的、更简洁的证明路径。微软研究院的Sébastien Bubeck指出，在**合适的Harness**下，Mythos和GPT-5.5都能复现内部模型一次完成的任务，这意味着标准聊天界面下隐藏着大量未被发掘的潜在能力。

---

### 4. [“语言模型需要睡眠”：长上下文记忆的新方案](https://x.com/iScienceLuvr/status/2059221770075562113)
> 一篇名为《Language Models Need Sleep》的论文获得了显著关注。其机制是引入一个**类似睡眠的巩固阶段**，将近期上下文转换为持久的快速权重，然后清除KV缓存，将计算转移到离线阶段，同时保持唤醒时的低延迟。这被视为处理长轨迹Agent时，应对不断增长的KV缓存的一种替代方案。

---

### 5. [DeepSeek推进102.9亿美元融资，坚持开源路线](https://www.bloomberg.com/news/articles/2026-05-22/deepseek-founder-declares-agi-goal-as-10-billion-round-advances)
> 据报道，DeepSeek正在推进一笔**102.9亿美元**的融资，创始人梁文峰重申了以AGI为导向的路线图，并承诺继续发布/开源AI模型，而非优先考虑短期商业化。评论认为，这是一个战略赌注，即模型优势的半衰期很短，开源研究比封闭的人才/模型护城河更能加速迭代。

---

### 6. [OpenRouter完成1.13亿美元B轮融资，周Token量增长5倍](https://x.com/OpenRouter/status/2059277623629664758)
> 模型路由和多模型基础设施平台OpenRouter宣布完成**1.13亿美元**的B轮融资，并透露其周Token量在六个月内从**5万亿增长到25万亿**。这标志着路由和多模型基础设施已被视为一个持久的平台层。

---

### 7. [华为“τ Scaling”论文：被视为工程路线图而非新定律](https://x.com/ZhihuFrontier/status/2059118295580852374)
> 对华为“τ Scaling”论文的详细解读认为，它应被解读为一份**战略宣言/白皮书**。其核心提议是将时间常数τ，而非工艺节点，作为跨器件、芯片和数据中心规模的统一度量。最具体的声明涉及未来麒麟芯片上的**LogicFolding**，包括+55%密度、+41%能效和+13%频率，但分析指出这些数据**未经验证**。

---

### 8. [vLLM合并Rust前端，吞吐量提升5倍](https://x.com/vllm_project/status/2059344804295942513)
> vLLM项目合并了一个**Rust前端**，作为Python API服务器的即插即用替代方案。早期数据显示，在处理预处理密集型工作负载时，单进程吞吐量达到**约837 req/s**，而Python版本仅为**约162 req/s**。这对于遇到CPU/API服务器瓶颈的高吞吐量服务场景意义重大。

---

### 9. [Anthropic推出Claude Code安全插件，减少30-40%安全评论](https://x.com/ClaudeDevs/status/2059385239781384341)
> Anthropic为Claude Code发布了一个安全指导插件。内部使用数据显示，该插件使与安全相关的PR评论减少了**30-40%**。这是一个将具体产品发布与内部度量指标相结合的典型案例。

---

### 10. [Epoch AI警告：推理算力可能面临短缺](https://x.com/EpochAIResearch/status/2059372951338909717)
> Epoch AI估计，AI推理计算需求增长可能快于服务能力，尤其是在长上下文工作负载下。其粗略模型表明，虽然当前全球Blackwell供应在有利假设下可以满足今日需求，但长上下文会严重降低吞吐量，且需求增长可能已经超过供应增长。

---

## 🛠️ 十大工具产品要点

### 1. [Anthropic Claude Code /workflows 功能](https://www.reddit.com/r/ClaudeCode/comments/1tkjy4u/claude_code_dropped_workflows/)
> Claude Code短暂曝光了一个名为`/workflows`的新系统，旨在用代码驱动的`workflow.js`控制器取代基于LLM的编排器。其特点包括：结构化阶段、并行扇出、条件/循环/预算、重试、后台执行，并通过在阶段间传递子Agent输出来减少上下文窗口的“Token税”。该功能随后被从更新日志中移除。

---

### 2. [Anthropic推出13+免费AI课程（含证书）](https://www.anthropic.com/learn)
> Anthropic通过其Skilljar平台推出了一个免费的官方培训目录，涵盖Claude、Claude Code、Claude API、MCP/Agent工作流等主题，并颁发证书。其中，MCP和高级MCP模块因其对`STDIO`和`StreamableHTTP`传输协议的实用讲解而受到特别推荐。

---

### 3. [W&B推出MCP服务器，让编码Agent检查实验](https://x.com/wandb/status/2059384552725025226)
> Weights & Biases (W&B) 发布了一个MCP服务器，允许编码Agent检查实验和训练运行。该服务器采用以Schema为先的重新设计，旨在避免上下文窗口爆炸，使Agent能更高效地与W&B平台交互。

---

### 4. [Unsloth支持在本地UI中运行GPT、Claude等API](https://x.com/UnslothAI/status/2059277719633101291)
> Unsloth在其本地UI中增加了对运行GPT、Claude等外部API的支持，包括提示缓存和代码执行功能。这使得用户可以在一个统一的界面中，结合本地模型和云端API进行工作。

---

### 5. [Cloudflare重启初创企业计划，提供最高35万美元积分](https://x.com/kristianfreeman/status/2059188629780545973)
> Cloudflare重新启动了其初创企业计划，为符合条件的初创公司提供高达**35万美元**的云服务积分。这对于依赖Cloudflare基础设施的AI初创企业来说是一个重要的成本节约机会。

---

### 6. [PrismML发布Bonsai Image 4B，含1-bit和Ternary变体](https://x.com/PrismML/status/2059339157600969199)
> PrismML发布了Bonsai Image 4B模型，其中包括**1-bit和Ternary**变体，旨在本地笔记本电脑和手机上运行。后续消息指出，该模型可在浏览器中本地执行，占用空间约**3GB**。

---

### 7. [Microsoft MAI-Image-2.5在Image Arena排名第三](https://x.com/MicrosoftAI/status/2059344061358563838)
> 微软的MAI-Image-2.5模型在Image Arena排行榜上首次亮相即获得**第三名**，打破了此前由OpenAI和Google主导的前五名俱乐部。Arena报告其得分为**1,254**。

---

### 8. [Tencent发布Z-Image 6B，无需VAE的像素空间生成](https://nju-pcalab.github.io/projects/L2P)
> 腾讯发布了Z-Image 6B模型，其关键技术特点是**无需VAE**，直接在像素空间进行图像生成，并支持**1k分辨率**。这代表了图像生成架构中一个值得关注的趋势。

---

### 9. [Qwen3.6 35B A3B在12GB显存上实现110 tok/s](https://www.reddit.com/r/LocalLLaMA/comments/1tjh7az/110_toks_with_12gb_vram_on_qwen36_35b_a3b_and_ik/)
> 用户报告称，使用`ik_llama.cpp`和`IQ4_XS`量化，在**RTX 4070 Super 12GB**显卡上运行Qwen3.6-35B-A3B MTP模型，实现了**110.24 tok/s**的推理速度，比上游`llama.cpp`快**23%**。这展示了在消费级硬件上运行大型MoE模型的可能性。

---

### 10. [Open Source QUEST模型：用于长周期事实搜索的深度研究Agent](https://x.com/iScienceLuvr/status/2059223911011930606)
> 一个名为QUEST的开放模型系列（**2B–35B**）被发布，专门用于长周期事实搜索、引用溯源和报告合成，定位为通用型深度研究Agent。这为开源社区提供了一个强大的研究工具。