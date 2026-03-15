## AINews - 2026-03-15

> [原文链接](https://news.smol.ai/issues/26-03-03-not-much/)

## 📰 十大AI新闻要点

### 1. 谷歌发布Gemini 3.1 Flash-Lite，主打动态思考层级与性价比
> Google DeepMind发布了Gemini 3.1 Flash-Lite（预览版），定位为3系列中最快、最具成本效益的端点，强调低延迟和高吞吐量。其核心创新是“动态思考层级”，允许根据任务复杂度动态调整计算量。定价为输入$0.25/M，输出$1.50/M，在LMArena上获得1432 Elo评分，GPQA Diamond准确率达86.9%，首令牌生成速度比Gemini 2.5 Flash快2.5倍。
来源：[@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2028872381477929185)

---

### 2. OpenAI发布GPT-5.3 Instant，旨在减少“说教感”并预告GPT-5.4
> OpenAI向所有ChatGPT用户推出GPT-5.3 Instant，旨在回应用户对GPT-5.2“过于谨慎”和“附带过多免责声明”的批评。新版本声称提升了对话自然度，减少了不必要的拒绝和防御性声明，并改善了与搜索结合的答案质量。内部数据显示，幻觉率在使用搜索时降低了26.8%，未使用时降低了19.7%。同时，OpenAI以“比你想象的更快”为口号，预告了GPT-5.4的即将到来。
来源：[@OpenAI](https://x.com/OpenAI/status/2028893701427302559)

---

### 3. 阿里通义千问（Qwen）团队核心成员集体离职，开源未来成疑
> 通义千问（Qwen）项目的技术负责人及多位高级贡献者相继宣布离职。技术负责人Justin Lin的“卸任”帖子引发了广泛关注，随后多名核心成员确认离开。业内普遍认为这是阿里云“踢走”了Qwen的技术领导层。此举引发了对Qwen开源权重发布节奏可能放缓、甚至开源立场改变的担忧，因其在开源模型生态（尤其是<10B参数模型）中扮演着关键基础设施角色。
来源：[@JustinLin610](https://x.com/JustinLin610/status/2028865835373359513)

---

### 4. Together AI发布长上下文训练技术，内存占用最高可降87%
> Together AI的研究论文展示了一种结合上下文并行和序列并行风格的分块技术，声称在8个H100 GPU（单节点）上训练一个拥有500万上下文窗口的80亿参数模型时，可将注意力机制的内存占用减少高达87%。该研究同时指出了当前长上下文模型RL后训练的一个实际瓶颈：由于内存成本，大多数训练仍只在完整上下文的一小部分上进行。
来源：[@rronak_](https://x.com/rronak_/status/2028718679123497007)

---

### 5. 苹果发布M5 Pro和M5 Max芯片，宣称LLM提示处理速度比M4系列快4倍
> 苹果公司发布了M5 Pro和M5 Max芯片，声称其大型语言模型（LLM）提示处理速度比前代M4 Pro和M4 Max快达4倍。M5 Pro支持最高64GB统一内存，带宽307GB/s；M5 Max支持最高128GB统一内存，带宽614GB/s。此外，SSD速度提升至14.5GB/s（2倍于前代），并集成了支持Wi-Fi 7的Apple N1无线芯片。
来源：文章内容

---

### 6. 代理（Agent）工程面临现实挑战：基准测试与真实工作脱节，多代理协调脆弱
> 新的研究指出，当前的AI代理基准测试过度偏重数学和编码，与真实世界的工作分布（如客户服务、内容审核）严重脱节。同时，多代理协调研究显示，即使在没有恶意攻击的情况下，LLM代理之间达成共识也并不可靠，失败常源于停滞或超时，且随着代理数量增加而恶化。Arena推出了“文档竞技场”作为回应，专注于真实的PDF推理评估。
来源：[@ZhiruoW](https://x.com/ZhiruoW/status/2028847081507488011)

---

### 7. OpenAI关键人才流失：后训练副总裁Max Schwarzer转投Anthropic
> OpenAI负责后训练（Post-Training）的副总裁Max Schwarzer宣布离职，并加入竞争对手Anthropic，将回归个人贡献者（IC）角色专注于强化学习研究。Schwarzer曾领导了GPT-5、5.1、5.2和5.3-Codex等模型的后训练和发布。此举被业界视为Anthropic的一次重大人才胜利，也加剧了人们对OpenAI核心人才流失的担忧。
来源：[@max_a_schwarzer](https://x.com/max_a_schwarzer/status/2028939154944585989)

---

### 8. OpenAI与五角大楼合作引发用户强烈反弹，ChatGPT卸载量激增295%
> 在OpenAI与美国国防部（DoD）达成合作的消息传出后，ChatGPT移动应用的卸载量激增了295%，反映出用户对隐私和AI军事化应用的强烈担忧。这一事件也导致竞争对手Claude的下载量上升，显示出市场竞争格局因此类合作而发生变化。社区内要求公开合同具体条款、进行独立法律红队测试的呼声高涨。
来源：文章内容

---

### 9. 通义千问Qwen 3.5系列模型发布，小参数模型性能显著提升
> 阿里发布了Qwen 3.5系列模型，其中包含一个仅8亿参数的版本（Qwen3.5-0.8B），甚至集成了视觉编码器。社区评测显示，该系列模型，特别是9B和27B的密集模型，在知识、STEM、指令遵循、数学和编码等多个基准测试中表现出了超越前代甚至更大规模模型的性能。有用户成功在7年前的三星S10E手机上以12 tokens/s的速度运行Qwen3.5-0.8B，展示了AI模型的高效性和可及性。
来源：[https://www.reddit.com/r/LocalLLaMA/comments/1rjd4pv/qwen_25_3_35_smallest_models_incredible/](https://www.reddit.com/r/LocalLLaMA/comments/1rjd4pv/qwen_25_3_35_smallest_models_incredible/)

---

### 10. 推理市场估值飙升，预计2030年达2550亿美元
> 行业分析师预测，AI推理（Inference）市场的规模到2030年将达到2550亿美元。这一增长主要由生产级AI部署的持续成本驱动，其支出正在超越模型训练成本。这一趋势也印证了当前业界对推理优化（如Taalas专用芯片）和高效部署工具的高度关注。
来源：[https://xcancel.com/meggmcnulty/status/2028532451992314199](https://xcancel.com/meggmcnulty/status/2028532451992314199)

---

## 🛠️ 十大工具产品要点

### 1. Databricks开源FlashOptim优化器，训练内存占用减半
> Databricks MosaicAI团队开源了FlashOptim，这是一套优化器实现（包括AdamW、SGD、Lion），能在保持更新等效性的同时大幅降低内存占用。例如，可将AdamW训练的参数内存开销从约16字节/参数降至7字节（释放梯度后可降至5字节），在一个80亿参数微调示例中，峰值内存从175 GiB降至113 GiB。
来源：[@davisblalock](https://x.com/davisblalock/status/2028943987349045610)

---

### 2. Cursor推出MCP Apps，支持在代理聊天中渲染交互式UI
> AI代码编辑器Cursor推出了“MCP Apps”功能，允许AI代理在聊天界面内直接渲染交互式用户界面（UI）。这标志着模型上下文协议（MCP）的进一步扩展，使代理能够提供更丰富、更动态的用户交互体验，而不仅仅是文本输出。
来源：[@cursor_ai](https://x.com/cursor_ai/status/2028953584407085546)

---

### 3. Unsloth发布针对Qwen 3.5的高效微调方案，仅需约5GB显存
> Unsloth AI发布了针对Qwen 3.5模型（如35B-A3B）的优化版LoRA微调指南和低显存训练方案。据称，使用其方案可以在仅约5GB VRAM的情况下对模型进行微调，并修复了工具调用等问题，使模型在研究任务上表现“惊人”。
来源：[@UnslothAI](https://x.com/UnslothAI/status/2028845314506150079)

---

### 4. SkyPilot提出异构基础设施方案，优化RL后训练工作流
> SkyPilot项目提出，强化学习（RL）后训练应将工作负载拆分到不同的硬件上：使用高性能GPU进行训练，廉价GPU进行模拟推演（rollouts），高内存CPU作为回放缓冲区。其“Job Groups”功能通过单一的YAML文件进行编排，实现协调的生命周期管理和服务发现。
来源：[@skypilot_org](https://x.com/skypilot_org/status/2028878888211013907)

---

### 5. ShadowClaw：用C语言编写的极简单文件个人AI代理
> 社区中出现了一个名为ShadowClaw v1.1的极简主义个人AI代理，完全用C语言编写，生成单个可执行文件。它通过curl与本地LLM（如Ollama）通信，具备执行shell命令、文件读写、HTTP GET和简单数学表达式求值等功能，并自动将状态保存到磁盘。
来源：[https://github.com/webxos/webxos/tree/main/shadowclaw](https://github.com/webxos/webxos/tree/main/shadowclaw)

---

### 6. Perplexity推出“计算机”功能，提供安全沙盒环境运行AI代理
> Perplexity推出了名为“计算机”（Computer）的新产品功能，它是一个安全沙盒环境，允许用户直接在其应用中运行AI代理，而无需管理API密钥。该功能旨在协调多个模型，安全地执行网页浏览、文件操作等任务。
来源：[@AravSrinivas](https://x.com/AravSrinivas/status/2028903680616087946)

---

### 7. TrainTrackLabs推出实时训练可观测性工具
> TrainTrackLabs推出了一款新的可观测性工具，可嵌入PyTorch训练流程，利用“LLM即法官”的方式实时评估模型在训练过程中的幻觉和推理能力。其目标是尽早发现性能回归，避免浪费GPU计算资源。
来源：[https://traintracklabs.com/](https://traintracklabs.com/)

---

### 8. 利用Replay MCP实现AI辅助的“时间旅行调试”
> 开发者利用Replay.io的模型上下文协议（MCP）实现了AI增强的“时间旅行调试”。有案例显示，该工具能将一个React 19升级问题的调试过程，从模糊的错误截图快速定位到根本原因，耗时仅约30秒。
来源：[https://docs.replay.io/basics/replay-mcp/overview](https://docs.replay.io/basics/replay-mcp/overview)

---

### 9. Notion为会议笔记功能集成MCP/API支持
> Notion为其“会议笔记”功能添加了模型上下文协议（MCP）和API支持。用户可以通过Claude Code等平台进行一键式安装和集成，使AI代理能够直接与Notion交互，处理会议记录。
来源：[@zachtratar](https://x.com/zachtratar/status/2028881783551570209)

---

### 10. 基于WebGPU和Transformers.js的浏览器内Qwen 3.5-0.8B演示
> 开发者发布了在浏览器内利用WebGPU和Transformers.js本地运行Qwen 3.5-0.8B模型的演示。该演示展示了在浏览器环境中运行小型但功能齐全的AI模型的潜力，尽管视觉编码器部分被识别为性能瓶颈。
来源：[https://huggingface.co/spaces/webml-community/Qwen3.5-0.8B-WebGPU](https://huggingface.co/spaces/webml-community/Qwen3.5-0.8B-WebGPU)