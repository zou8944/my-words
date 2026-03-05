## AINews - 2026-03-05

> [原文链接](https://news.smol.ai/issues/26-03-03-not-much/)

## 📰 十大AI新闻要点

### 1. Google发布Gemini 3.1 Flash-Lite，主打动态思维层级与性价比
> Google DeepMind推出Gemini 3.1 Flash-Lite（预览版），定位为3系列中最快、最具成本效益的端点，专为高吞吐量、低延迟工作负载设计。其核心创新是“动态思维层级”，允许用户根据任务复杂度调整计算量。定价为输入$0.25/M，输出$1.50/M，在LMArena上获得1432 Elo分，GPQA Diamond准确率达86.9%，首词元生成速度比Gemini 2.5 Flash快2.5倍。
来源：[@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2028872381477929185)

---

### 2. OpenAI发布GPT-5.3 Instant，旨在减少“说教感”并预告GPT-5.4
> OpenAI向所有ChatGPT用户推出GPT-5.3 Instant，直接回应用户对GPT-5.2“过于谨慎”和“附带过多免责声明”的批评。新版本声称提升了对话自然度，减少了不必要的拒绝和防御性声明，并改善了搜索整合答案的准确性。内部数据显示，使用搜索时幻觉率降低26.8%，不使用搜索时降低19.7%。同时，OpenAI以“比你想象的更快”预告了GPT-5.4，引发市场猜测。
来源：[@OpenAI](https://x.com/OpenAI/status/2028893701427302559)

---

### 3. 阿里通义千问（Qwen）团队核心领导层集体离职，开源未来成疑
> 通义千问（Qwen）项目的技术负责人及多位高级贡献者相继宣布离职。技术负责人Justin Lin的“卸任”帖子引发了广泛关注和讨论。业内观察人士认为，这可能是阿里云内部组织架构调整（向CEO汇报）带来的政治压力所致。此举引发了开源社区对Qwen未来开源权重发布节奏和许可政策可能改变的深切担忧，因其模型（尤其是<10B参数模型）被视为开源生态的关键基础设施。
来源：[@JustinLin610](https://x.com/JustinLin610/status/2028865835373359513)

---

### 4. Together AI发布长上下文训练新方法，内存占用最高减少87%
> Together AI的研究人员提出了一种结合上下文并行和序列并行风格头分块的混合方法，声称在8个H100 GPU（单节点）上训练具有500万上下文窗口的80亿参数模型时，可将注意力内存占用减少高达87%。这项研究旨在解决当前长上下文模型RL后训练因内存成本过高而只能使用部分上下文的问题。
来源：[@rronak_](https://x.com/rronak_/status/2028718679123497007)

---

### 5. 苹果发布M5 Pro和M5 Max芯片，宣称LLM提示处理速度比M4系列快4倍
> 苹果公司正式发布M5 Pro和M5 Max芯片，声称其大型语言模型（LLM）提示处理速度最高可达M4 Pro和M4 Max的4倍。M5 Pro支持最高64GB统一内存（带宽307GB/s），M5 Max支持最高128GB统一内存（带宽614GB/s）。此外，SSD速度提升至14.5GB/s（2倍于前代），并集成了支持Wi-Fi 7的Apple N1无线芯片。
来源：文章内容

---

### 6. OpenAI前副总裁Max Schwarzer转投Anthropic，专注RL研究
> OpenAI负责后训练（Post-Training）的副总裁Max Schwarzer宣布离职，并加入竞争对手Anthropic。在OpenAI期间，他领导了GPT-5、5.1、5.2和5.3-Codex等模型的后训练工作。他表示将回归个人贡献者（IC）角色，专注于强化学习（RL）研究。此举被业界视为Anthropic在人才争夺战中的一次重大胜利。
来源：[@max_a_schwarzer](https://x.com/max_a_schwarzer/status/2028939154944585989)

---

### 7. 报告称ChatGPT因国防部合同遭遇用户强烈抵制，卸载量激增295%
> 据TechCrunch报道，在OpenAI与美国国防部（DoD）达成合作的消息传出后，ChatGPT移动应用的卸载量激增了295%。这反映了用户对AI公司与军事机构合作的强烈不满和隐私担忧。同时，竞争对手Claude的下载量出现增长，显示出市场竞争格局因此事件可能发生变化。
来源：文章内容（引用自TechCrunch）

---

### 8. 智能体（Agent）工程面临现实挑战：基准测试与真实工作脱节
> 新的研究指出，当前的AI智能体基准测试过度偏重数学和编码任务，未能反映现实世界中的劳动和资本分布。Arena为此推出了“文档竞技场”（Document Arena），专注于对PDF文档进行真实推理的评估。此外，研究显示多智能体协调非常脆弱，即使在良性环境中，共识失败也经常发生，且随着群体规模扩大而恶化。
来源：[@ZhiruoW](https://x.com/ZhiruoW/status/2028847081507488011)

---

### 9. Anthropic Claude流量意外激增，遭遇服务中断与扩容挑战
> Anthropic报告称，其Claude和Claude Code服务的流量增长远超预期，导致公司不得不紧急扩容基础设施以应对需求。有传言称，中东地区AWS数据中心遭遇袭击导致流量被重定向至北美，加剧了服务压力。与此同时，Claude Code开始向约5%的用户推出新的“语音模式”功能。
来源：文章内容（引用自相关推文及Discord讨论）

---

### 10. 模型控制协议（MCP）生态持续扩展，Notion与Cursor纷纷集成
> 尽管有“MCP已死？”的质疑声，但MCP的采用正在扩大。Notion为其“会议笔记”功能推出了MCP/API支持，可通过Claude Code一键安装。Cursor则推出了“MCP Apps”，允许智能体在聊天界面内渲染交互式UI。这表明MCP作为一种连接智能体与工具的标准化协议，其生态正在走向成熟。
来源：[@cursor_ai](https://x.com/cursor_ai/status/2028953584407085546)

---

## 🛠️ 十大工具产品要点

### 1. Databricks开源FlashOptim优化器，训练内存占用减半
> Databricks MosaicAI团队开源了FlashOptim，这是一组优化器实现（AdamW/SGD/Lion），在保持更新等效性的同时大幅削减内存。例如，可将AdamW训练的参数内存开销从约16字节/参数降至7字节（释放梯度后可降至5字节）。在一个80亿参数微调示例中，峰值内存从175 GiB降至113 GiB。
来源：[@davisblalock](https://x.com/davisblalock/status/2028943987349045610)

---

### 2. SkyPilot推出异构基础设施编排方案，优化RL后训练成本
> SkyPilot提出，RL后训练应将工作负载拆分到不同类型的硬件上：使用高性能GPU进行训练，廉价GPU进行推演（rollouts），高内存CPU管理回放缓冲区。其“Job Groups”功能通过单一的YAML文件进行编排，提供协调的生命周期管理和服务发现，旨在显著降低RL训练成本。
来源：[@skypilot_org](https://x.com/skypilot_org/status/2028878888211013907)

---

### 3. Unsloth发布针对Qwen 3.5的优化微调方案，大幅降低VRAM需求
> Unsloth AI发布了针对Qwen 3.5模型的LoRA微调指南和低VRAM训练方案。据称，使用其方案微调Qwen3.5-35B-A3B模型仅需约5GB VRAM，并在Ryzen AI Max+ 395系统上实现了600+ tokens/秒的提示处理速度。这极大降低了在消费级硬件上微调大模型的门槛。
来源：[@UnslothAI](https://x.com/UnslothAI/status/2028845314506150079)

---

### 4. Cursor推出“MCP Apps”，智能体可在聊天中渲染交互式UI
> Cursor AI发布了“MCP Apps”功能，允许开发者在模型控制协议（MCP）服务器中构建应用，使AI智能体能够在聊天界面内直接渲染出交互式用户界面（如按钮、表单）。这为创建更直观、功能更强大的AI助手体验提供了新的可能性。
来源：[@cursor_ai](https://x.com/cursor_ai/status/2028953584407085546)

---

### 5. ShadowClaw：用C语言编写的极简单文件个人AI智能体
> 开源项目ShadowClaw v1.1发布，这是一个用C语言编写的极简主义个人AI智能体，以单个二进制文件形式存在。它通过curl与本地LLM（如Ollama）通信，支持执行Shell命令、文件读写、HTTP GET和简单数学表达式求值，并能自动将状态保存到磁盘，强调低开销和易部署。
来源：[GitHub - webxos/shadowclaw](https://github.com/webxos/webxos/tree/main/shadowclaw)

---

### 6. Perplexity推出“计算机”功能，提供安全沙箱环境运行多模型
> Perplexity推出了名为“计算机”（Computer）的新产品功能。它被定位为一个安全的沙箱环境，可以编排多个AI模型并直接嵌入到应用程序中，用户无需管理API密钥。该功能旨在提供一个托管式的、安全的“计算机使用”平台，用于复杂的多步骤任务。
来源：[@AravSrinivas](https://x.com/AravSrinivas/status/2028903680616087946)

---

### 7. TrainTrackLabs推出实时训练可观测性工具，用LLM即时评估幻觉
> TrainTrackLabs推出了一款新的可观测性工具，可插入PyTorch训练流程，利用“LLM即法官”的方式实时评估模型在微调过程中的幻觉和推理能力。其目标是尽早发现性能回归，避免浪费GPU算力。
来源：[traintracklabs.com](https://traintracklabs.com/)

---

### 8. 开源项目Transformers.js支持在浏览器WebGPU上本地运行Qwen 3.5 0.8B
> 通过Transformers.js和WebGPU，开发者现在可以在浏览器中本地运行Qwen 3.5 0.8B参数模型。Hugging Face上提供了演示空间，展示了在浏览器中无需服务器即可进行AI推理的潜力，尽管视觉编码器部分被识别为性能瓶颈。
来源：[Hugging Face Demo Space](https://huggingface.co/spaces/webml-community/Qwen3.5-0.8B-WebGPU)

---

### 9. 字节跳动发布CUDA Agent，用于自动生成高性能CUDA内核
> 字节跳动发布了一个“CUDA Agent”项目，旨在自动编写高性能的CUDA内核代码。据称，该智能体在中等规模内核上比`torch.compile`快2倍，并在复杂基准测试中超越了Claude Opus 4.5。这代表了AI在底层硬件优化自动化方面的应用。
来源：[cuda-agent.github.io](https://cuda-agent.github.io)

---

### 10. Replay推出MCP支持，实现AI辅助的“时间旅行调试”
> Replay（一个时间旅行调试器）推出了对模型控制协议（MCP）的支持。开发者可以利用AI智能体与调试会话交互，快速定位问题根源。有案例称，该工具将一个React 19升级调试会话从模糊的错误提示缩短至30秒内找到根本原因。
来源：[Replay MCP 文档](https://docs.replay.io/basics/replay-mcp/overview)

---