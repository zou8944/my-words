## AINews - 2026-01-20

> [原文链接](https://news.smol.ai/issues/26-01-16-chatgpt-ads/)

## 📰 十大AI新闻要点

### 1. [OpenAI推出ChatGPT Go订阅层并测试广告](https://twitter.com/OpenAI/status/2012223323812270219)
> OpenAI正式推出新的低成本订阅层“ChatGPT Go”，定价8美元/月，提供10倍消息量、文件上传、图像生成、更长上下文和无限使用GPT-5.2即时模型。同时，公司宣布将在美国和免费层用户中测试广告，并强调广告不会影响回答、会被清晰标注，且对话对广告商保密。

---

### 2. [OpenAI公布广告原则，强调中立性与隐私](https://twitter.com/OpenAI/status/2012223373489614951)
> OpenAI公布了其广告测试的原则，核心是确保广告不影响模型回答、清晰标注广告内容，并保护用户对话隐私，不向广告商提供。此举旨在为拥有9亿周活用户的免费服务探索可持续的商业模式，但引发了社区对激励偏移的担忧。

---

### 3. [Sam Altman预告“非常快的Codex”即将到来](https://twitter.com/sama/status/2012243893744443706)
> OpenAI CEO Sam Altman在X上多次预告“非常快的Codex即将到来！”，暗示其代码模型将有重大速度提升。开发者社区对此表示期待，并讨论了模型速度提升对工作流（如转向更多异步“智能体引导”）的潜在影响。

---

### 4. [人机回环（Human-in-the-loop）被证实为可靠性倍增器](https://twitter.com/lateinteraction/status/2012030585926189148)
> 社区讨论认为，在智能体系统中加入人类“监督员”可以显著提升系统感知可靠性。人类能够捕捉失败、处理模糊性，从而让使用相同底层模型的系统感觉比全自动部署可靠得多。这一观点得到了定量分析的支持。

---

### 5. [Jerry Liu提出“分块已死”，倡导文件优先检索](https://twitter.com/jerryjliu0/status/2012273236042559802)
> LlamaIndex CEO Jerry Liu 提出，RAG（检索增强生成）没有过时，但静态分块（static chunking）已死。如果智能体能够直接打开文件、搜索并动态扩展上下文，对于数百个文档的规模，可以避免脆弱的传统分块/嵌入流程，转而采用更灵活的文件工具方法。

---

### 6. [推理成为新瓶颈，“推理爆炸之年”到来](https://twitter.com/ZhihuFrontier/status/2012080310981374428)
> 一篇来自知乎的长文总结指出，AI瓶颈已从训练转向推理。智能体应用大幅提高了输入/输出比，预填充（Prefill）阶段成为主导，上下文缓存成为默认，而预填充/解码分离的架构对资源利用率构成挑战，需要重新设计调度和内存层次结构。

---

### 7. [OpenBMB开源无需分词的实时语音克隆模型VoxCPM](https://twitter.com/LiorOnAI/status/2012133013967044755)
> OpenBMB开源了VoxCPM的权重，这是一个无需离散音频分词、可直接生成连续语音的实时流式语音克隆模型。据称在单张RTX 4090上可实现约0.15的实时因子，有望显著提升生产级语音智能体的延迟和韵律保真度。来源：文章内容（附推文链接）。

---

### 8. [GLM-Image发布：首个完全基于国产芯片训练的SOTA多模态模型](https://github.com)
> 智谱AI与华为联合发布了GLM-Image，这是一个完全在华为昇腾910芯片上训练出的先进多模态模型。该模型采用自回归与扩散解码器混合架构，擅长中文文本渲染，支持1024到2048分辨率，并声称在“每焦耳令牌数”上比英伟达H200高出60%的计算效率。

---

### 9. [Mamba-2重写核心算法以优化英伟达硬件利用率](https://open.substack.com/pub/lambpetros/p/the-transformer-attractor)
> Mamba-2将其核心算法从并行扫描（仅利用10-20%的张量核心）重构为块对角GEMM（通用矩阵乘法），实现了60-70%的硬件利用率。这凸显了Transformer架构与英伟达GPU的协同进化形成了一个难以打破的稳定“吸引子”，任何新架构都需克服硬件兼容性和机构支持的双重挑战。

---

### 10. [AI数据中心总功耗已达约30吉瓦，堪比纽约州峰值用电](https://twitter.com/EpochAIResearch/status/2012303496465498490)
> Epoch AI研究估计，全球AI数据中心的电力容量已达到约30吉瓦，与纽约州在炎热天气的峰值用电量相当。该估算基于芯片销量、额定功耗并乘以约2.5倍的基础设施开销，但需注意“容量与实际使用”之间的区别。

---

## 🛠️ 十大工具产品要点

### 1. [Codex CLI支持通过Ollama集成开源模型](https://twitter.com/ollama/status/2012046176267440177)
> 用户现在可以通过Ollama在Codex CLI中使用开源模型，命令为 `codex --oss`。建议将上下文长度设置推至≥32K以获得更好的用户体验，这增强了Codex生态系统的灵活性和对开放权重模型的兼容性。

---

### 2. [智能体编排工具Cowork向Anthropic Pro用户开放](https://twitter.com/alexalbert__/status/2012230110745702563)
> Anthropic的智能体协作工具Cowork现已向“Pro”订阅用户开放。该工具仍处于研究预览阶段，包含会话重命名、连接器改进等功能，标志着智能体编排工具正成为主流开发工具的一部分。

---

### 3. [OpenWork为Mac添加原生Ollama集成，支持全本地智能体](https://twitter.com/_orcaman/status/2012210613712281646)
> OpenWork平台为其Mac应用添加了原生Ollama集成，允许用户在本地计算机（支持Gemma、Qwen、DeepSeek、Kimi等模型）上运行完全本地的计算机智能体，增强了隐私和离线工作能力。

---

### 4. [FLUX.2 [klein]图像模型获vLLM-Omni当日支持](https://twitter.com/vllm_project/status/2012110024294965406)
> Black Forest Labs的开源图像生成模型FLUX.2 [klein]在发布当天就获得了vLLM-Omni的支持。该模型体积较小（约13GB VRAM），推理速度亚秒级，采用Apache-2.0许可证，在多个开源模型排行榜上表现强劲。

---

### 5. [Claude Flow v3发布，号称可将Claude Max使用量提升2.5倍](https://github.com/ruvnet/claude-flow)
> Claude Flow v3是一个用TypeScript和WASM重建的AI编排平台，采用模块化架构，支持部署具有共享内存和持续学习能力的多智能体集群。据称可减少75-80%的令牌消耗，并将订阅容量提升250%，同时支持本地模型离线执行。

---

### 6. [Kling AI推出运动控制与“AI动捕”工作流](https://twitter.com/Kling_ai/status/2012155500134105149)
> Kling AI展示了其视频生成模型的运动控制功能，支持快速角色替换和可转移的表演/动作，实现了类似“AI动作捕捉”的效果，用户可以将动作、表情、口型从一个角色复制粘贴到另一个角色。

---

### 7. [Hawk Ultra模型号称能单次生成超2万行代码](https://x.com/movementlabsAI/status/2011964766533632380)
> MovementLabs.AI发布的Hawk Ultra模型被宣传为“代码生成水龙头”，据称能够从单个提示中生成9500多行甚至超过20000行代码，社区将其视为与Claude Opus竞争的“代码专用”模型。

---

### 8. [Claude API支持单次请求中的并行工具调用](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use#controlling-claudes-output)
> Anthropic的文档显示，Claude模型可以通过API在单个请求中执行多个工具调用（并行工具使用）。这为智能体架构减少了请求/响应循环次数，有望降低复杂工作流的延迟和成本。

---

### 9. [Unsloth实现7倍上下文长度扩展的强化学习](https://www.reddit.com/r/LocalLLaMA/comments/1qdna3t/7x_longer_context_reinforcement_learning_in/)
> Unsloth宣布其新技术可将强化学习训练的上下文长度扩展高达7倍（某些情况下达12倍）。例如，可在24GB显存的显卡上以QLoRA方式训练具有20K上下文的gpt-oss 20b模型，且不损失精度，这得益于新的数据移动和批处理算法。

---

### 10. [TiinyAI发布可本地运行120B参数模型的小型AI计算机](https://www.reddit.com/r/LocalLLM/comments/1qcu498/small_ai_computer_runs_120b_models_locally_any/)
> TiinyAI开发了一款紧凑型AI设备，配备80GB RAM，功耗仅30W，能够本地运行1200亿参数模型。该设备主打便携性和隐私保护，可作为DGX Spark等大型系统的替代品，适用于网络受限或需要数据本地的场景。

---