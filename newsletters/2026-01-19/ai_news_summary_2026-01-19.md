## AINews - 2026-01-19

> [原文链接](https://news.smol.ai/issues/26-01-16-chatgpt-ads/)

## 📰 十大AI新闻要点

### 1. [OpenAI推出ChatGPT Go订阅层并测试广告](https://twitter.com/OpenAI/status/2012223323812270219)
> OpenAI宣布推出新的低成本订阅层“ChatGPT Go”，定价为8美元/月，提供10倍更多消息、文件上传、图像生成、更多内存和更长上下文，并包含对GPT-5.2 instant的无限使用。同时，OpenAI宣布将在免费版和Go版中测试广告，并公布了广告原则：广告不影响回答、清晰标注、用户对话对广告商保密。

---

### 2. [OpenAI公布广告原则，强调不影响回答](https://twitter.com/OpenAI/status/2012223373489614951)
> OpenAI正式公布了其在ChatGPT中测试广告的原则。核心承诺是广告永远不会影响模型的回答，并且会进行清晰标注。测试将首先在美国的免费版和Go版用户中展开，而付费计划（Plus/Pro/Enterprise）将不会看到广告。

---

### 3. [Sam Altman预告“非常快的Codex即将到来”](https://twitter.com/sama/status/2012243893744443706)
> OpenAI首席执行官Sam Altman在X上多次预告“非常快的Codex即将到来！”，引发了开发者社区的广泛讨论。这暗示OpenAI可能在推理速度方面有重大突破，或将改变AI工作流的构建方式。

---

### 4. [SWE-bench 2025年12月榜单更新，Claude Opus 4.5领先](https://swe-rebench.com/?insight=dec_2025)
> 2025年12月的SWE-bench（软件工程基准测试）榜单更新，评估了多个模型在48个新GitHub PR任务上的表现。Claude Opus 4.5以63.3%的解决率领先，GPT-5.2 xhigh以61.5%紧随其后。开源模型GLM-4.7表现突出，跻身前列，而Gemini 3 Flash Preview的表现也超出预期。

---

### 5. [智谱AI与华为发布首个完全基于国产芯片训练的SOTA多模态模型GLM-Image](https://github.com)
> 智谱AI与华为合作发布了GLM-Image，这是一个在华为昇腾910芯片上完全训练而成的先进多模态模型。该模型采用混合自回归和扩散解码器架构，擅长中文文本渲染，支持1024到2048分辨率，并声称在“每焦耳令牌数”上的计算效率比英伟达H200高60%。

---

### 6. [Mamba-2重写核心算法以优化英伟达硬件利用率](https://open.substack.com/pub/lambpetros/p/the-transformer-attractor)
> Mamba-2将其核心算法从并行扫描（仅利用10-20%的张量核心容量）重构为块对角GEMM（通用矩阵乘法），实现了60-70%的硬件利用率。这一变化突显了Transformer架构与英伟达GPU硬件生态的“共同进化”趋势，使得替代性架构难以获得足够的硬件兼容性和机构支持。

---

### 7. [Epoch AI估计AI数据中心总功耗已达30GW](https://twitter.com/EpochAIResearch/status/2012303496465498490)
> 研究机构Epoch AI发布估算，全球AI数据中心的电力容量已达到约30吉瓦（GW），相当于美国纽约州在炎热天气下的峰值用电量。该估算基于芯片销售数量、额定功耗并乘以约2.5倍的数据中心设施开销，但需注意“容量与实际使用量”之间的区别。

---

### 8. [OpenBMB开源无需分词的实时语音克隆模型VoxCPM](https://twitter.com/LiorOnAI/status/2012133013967044755)
> OpenBMB开源了VoxCPM模型的权重，这是一个用于实时流式语音克隆的模型。其关键创新在于直接生成连续语音，避免了传统方法中离散音频分词带来的伪影问题。据称在单张RTX 4090上可实现约0.15的实时因子，有望提升语音代理的延迟和韵律保真度。

---

### 9. [Jerry Liu提出“分块已死”，倡导基于文件的动态检索](https://twitter.com/jerryjliu0/status/2012273236042559802)
> LlamaIndex创始人Jerry Liu提出，RAG（检索增强生成）没有过时，但静态分块（static chunking）已死。他认为，如果AI代理具备打开文件、搜索（ls/grep）和动态扩展上下文的能力，就可以避免为许多中小规模应用构建脆弱的“分块-嵌入”流水线，转而采用更灵活的文件优先检索方式。

---

### 10. [“人在回路”被强调为提升AI系统可靠性的关键](https://twitter.com/lateinteraction/status/2012030585926189148)
> 社区讨论中反复出现一个主题：在AI系统中加入人类“监督员”（人在回路）可以极大地提升系统感知上的可靠性。人类可以充当手动安全阀，捕捉失败案例并绕过模糊性，这使得使用相同底层模型的系统比完全自主部署时感觉可靠得多。

---

## 🛠️ 十大工具产品要点

### 1. [OpenAI Codex CLI支持通过Ollama使用开源模型](https://twitter.com/ollama/status/2012046176267440177)
> 用户现在可以通过Ollama，使用 `codex --oss` 命令在Codex CLI中调用开源模型。社区建议将上下文长度设置调整为≥32K以获得更好的用户体验。

---

### 2. [FLUX.2 [klein]图像模型获广泛支持，性能强劲](https://twitter.com/vllm_project/status/2012110024294965406)
> Black Forest Labs的开源图像生成模型FLUX.2 [klein]获得了“Day-0”支持，已集成到vLLM-Omni中。该模型被定位为对消费者友好（约需13GB VRAM）、支持亚秒级推理的Apache-2.0许可模型，并在多个图像生成排行榜上取得了强劲名次。

---

### 3. [Anthropic Claude支持并行工具调用](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use#controlling-claudes-output)
> Anthropic的官方文档显示，Claude模型可以在单个API请求中执行多个工具调用（并行工具使用）。这被视为智能体架构的一个重要解锁，可以减少请求-响应循环，实现更简洁的工具编排，并可能降低复杂工作流的延迟和成本。

---

### 4. [Unsloth宣布实现7倍更长上下文的强化学习训练](https://www.reddit.com/r/LocalLLaMA/comments/1qdna3t/7x_longer_context_reinforcement_learning_in/)
> Unsloth发布新功能，声称可将强化学习训练的上下文长度延长高达7倍（某些情况下可达12倍）。例如，可以在24GB显存的显卡上训练具有20K上下文的gpt-oss 20b QLoRA模型，且不损失准确性。这得益于新的数据移动和批处理算法。

---

### 5. [Claude Cowork正式向“Pro”订阅用户开放](https://www.reddit.com/r/ClaudeAI/comments/1qeo736/official_claude_cowork_is_now_available_to_pro/)
> Anthropic的Claude Cowork功能（研究预览版）现已向Claude“Pro”订阅用户开放。该功能包括会话重命名、连接器改进以及基于早期反馈的修复，旨在处理更复杂的多步骤任务，但用户反映可能因此更快触及使用限制。

---

### 6. [Google发布Translate Gemma多语言翻译模型](https://huggingface.co/collections/google/translategemma)
> Google在Hugging Face上发布了Translate Gemma模型集合。该模型因在多语言翻译（包括马来语等）上的广泛覆盖度和在分词器/数据方面的工作而受到关注，并已集成到Ollama中，需使用特定的提示格式。

---

### 7. [开源智能体UI“sled”支持通过Agent Control协议跨设备控制](https://twitter.com/dctanner/status/2012212217677070796)
> 一个新的开源UI工具“sled”允许用户通过Agent Control Protocol（ACP）将Claude Code或OpenAI Codex从电脑“传送”到手机上进行控制，展示了智能体跨设备交互的新可能。

---

### 8. [Moonshot AI的K2 Turbo模型在基准测试中达到约73 tps](来源：文章内容)
> 据Discord社区用户基准测试，Moonshot AI的K2 Turbo模型生成速度达到约每秒73个令牌（tps），显著高于标准K2模型的约28 tps。同时，其新推出的“Slides + Vision”功能由更新的K2视觉模型驱动，可以联网搜索视觉参考。

---

### 9. [Hawk Ultra模型号称能单次生成超2万行代码](https://x.com/movementlabsAI/status/2011964766533632380)
> MovementLabs.AI发布的Hawk Ultra模型在社区引发热议，据称能够从单个提示中生成9500+甚至20000+行代码，被赋予“Opus杀手”的称号，被视为一种新的“代码洪流”模型类别。

---

### 10. [TiinyAI推出可本地运行120B参数模型的小型AI计算机](https://www.reddit.com/r/LocalLLM/comments/1qcu498/small_ai_computer_runs_120b_models_locally_any/)
> TiinyAI开发了一款紧凑型AI设备，配备80GB RAM，功耗仅30W，声称可本地运行1200亿参数模型。该设备主打便携性和隐私保护，作为DGX Spark等大型系统的替代方案，适用于网络受限或注重数据隐私的场景。