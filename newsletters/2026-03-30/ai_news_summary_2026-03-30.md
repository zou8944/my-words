## AINews - 2026-03-30

> [原文链接](https://news.smol.ai/issues/26-03-27-not-much/)

## 📰 十大AI新闻要点

### 1. Anthropic 被曝正在开发超越Opus的新模型层级“Capybara”（来源：文章内容）
> 据《财富》杂志报道及泄露信息，Anthropic 正在开发一个名为“Capybara”的新模型层级，定位高于当前的 Claude Opus 4.6，据称在编码、学术推理和网络安全方面表现显著提升。其发布受限于高昂的成本和安全考量。

---

### 2. Google 接近资助 Anthropic 数据中心建设，凸显前沿AI竞赛的算力门槛（来源：文章内容）
> 《金融时报》报道称，Google 即将为 Anthropic 的数据中心建设提供资金。这进一步表明，前沿AI模型的竞争正日益被算力、能源和资本支出所限制，而不仅仅是算法本身。

---

### 3. 智谱AI发布GLM-5.1，开源/半开源编码模型性能逼近闭源模型（https://x.com/Zai_org/status/2037490078126084514）
> 智谱AI宣布GLM-5.1向所有编码计划用户开放。社区分析认为，以GLM-5.1为代表的高端中文开源/半开源编码模型正在迅速缩小与闭源模型（如Claude Opus）的性能差距。

---

### 4. 本地模型部署经济性持续改善，成为许多工作流的可行选择（https://x.com/TheGeorgePu/status/2037473248577782046）
> 多个案例显示，本地模型（如Qwen 3.5 14B/27B）在成本效益上已“足够好”，可以替代昂贵的云端订阅服务。技术进步使得在有限显存（如24GB VRAM）下运行大模型（如Qwen3.5-35B）成为可能，且性能损失极小。

---

### 5. Nous Research的Hermes Agent成为开源AI智能体焦点，集成Hugging Face（https://x.com/NousResearch/status/2037654827929338324）
> Hermes Agent 集成了 Hugging Face 作为首要推理服务提供商，提供28个精选模型及更多模型的访问。这被视为向具备记忆、持久机器访问和模型选择能力的“开放智能体”迈出的关键一步，用户体验优于OpenClaw等浏览器自动化方案。

---

### 6. AI智能体基础设施围绕追踪、评估和可调试性走向成熟（https://x.com/LangChain/status/2037590936234959355）
> LangChain 发布了面向生产的工具集，包括智能体评估准备清单、Deep Agents IDE风格UI指南，以及用于提示词管理/回滚的 LangSmith Prompt Hub Environments。行业正从“带工具的聊天机器人”转向为智能体构建软件生命周期基础工具。

---

### 7. OpenAI Codex生态向工作空间原生自动化演进（https://x.com/OpenAIDevs/status/2037604273434018259）
> OpenAI 开发者展示了 Codex 插件和用例库，Box 公司也发布了用于自动化 Box 内容工作流的 Codex 插件。用户反馈表明，重心正从简单的提示/响应转向持久化工作空间、问题系统、终端、PR流程和插件集成。

---

### 8. Meta发布SAM 3.1，通过对象复用实现视频分割速度翻倍（https://x.com/AIatMeta/status/2037582117375553924）
> Meta 发布了 SAM 3.1，作为 SAM 3 的直接升级版，引入了对象复用功能，允许单次前向传播处理多达16个对象。据称，在中等对象负载下，单个H100上的视频处理吞吐量从约16 FPS提升至32 FPS。

---

### 9. 世界模型与机器人学领域出现重要开源发布（https://x.com/LiorOnAI/status/2037484990779339064）
> Yann LeCun 的 LeWorldModel 论文/代码库发布，这是一个旨在通过SIGReg方法从数学上避免表征崩溃的小型开源世界模型，据称规划速度提升48倍，所需token减少约200倍。同时，宇树科技开源了用于人形机器人全身遥操作的真实世界数据集 UnifoLM-WBT-Dataset。

---

### 10. 语音/音频开源模型生态活跃，Cohere发布高性能Apache-2.0转录模型（https://x.com/victormustar/status/2037572662659104976）
> Cohere 新发布的 2B 参数、Apache-2.0 许可的转录模型获得好评。实测显示，在A100上仅用12分钟即可转录33小时的音频，展现了出色的吞吐能力。Mistral 的 Voxtral TTS 论文和相关本地演示也受到关注。

---

## 🛠️ 十大工具产品要点

### 1. TurboQuant 量化技术及其优化变体（https://github.com/TheTom/turboquant_plus）
> Google 的 TurboQuant 压缩技术被集成到 llama.cpp 等框架中，显著提升了在消费级硬件（如MacBook Air）上运行大模型长上下文的能力。后续优化通过利用注意力稀疏性跳过不必要的KV缓存反量化计算，在32K上下文长度下解码速度提升22.8%。

---

### 2. RotorQuant：基于Clifford代数的更快量化替代方案（https://github.com/scrya-com/rotorquant）
> RotorQuant 提出使用 Clifford 旋转子替代 TurboQuant 中的随机正交矩阵，将计算复杂度从数千次FMA降至约100次，实现了10-19倍的速度提升，同时参数减少44倍，在真实模型注意力保真度上表现接近。

---

### 3. Hermes Agent 集成 Hugging Face 模型服务（https://x.com/NousResearch/status/2037654827929338324）
> Hermes Agent 将 Hugging Face 作为核心推理后端集成，为用户提供了从28个精选模型到海量社区模型的便捷访问，降低了构建具备记忆和工具使用能力的持久化智能体的门槛。

---

### 4. LangChain 发布智能体生产就绪工具套件（https://x.com/LangChain/status/2037590936234959355）
> 包括智能体评估准备清单、Deep Agents（提供类似IDE的UI用于智能体开发与调试）以及 LangSmith Prompt Hub Environments（用于提示词版本管理与部署），旨在为智能体开发提供全生命周期支持。

---

### 5. Artificial Analysis 推出面向真实工作负载的智能体基准 AA-AgentPerf（https://x.com/ArtificialAnlys/status/2037562417836929315）
> 该基准专注于真实的编码智能体轨迹、超过10万的序列长度，并以“每加速器/每千瓦/每美元/每机架的并发用户数”来衡量吞吐量，比传统的合成token基准更贴近部署实际。

---

### 6. CursorBench 作为长周期编码评估的新标杆（来源：文章内容）
> CursorBench 基准因其使用真实编码会话、模糊提示、更广泛的质量维度以及每个任务中位数181行的代码更改量而受到认可。它比静态玩具任务更能健康地评估智能体的长周期编码能力。

---

### 7. 用于实时浏览器会话调试的智能体-浏览器仪表板（https://x.com/ctatedev/status/2037599050112160165）
> 新发布的工具提供了对智能体浏览器会话的实时调试界面，有助于开发者理解和优化基于浏览器自动化的智能体行为。

---

### 8. 原子聊天（atomic.chat）应用集成TurboQuant，在Mac上本地运行大模型（来源：文章内容）
> 这款开源应用通过集成 TurboQuant 技术的 llama.cpp 后端，使得在标准配置的 MacBook Air (M4, 16GB) 上运行 Qwen 3.5–9B 模型并处理20K上下文成为可能。

---

### 9. AI2 发布完全在模拟中训练的开源机器人操作套件 MolmoBot（https://x.com/allen_ai/status/2037590611990094259）
> 提供了完整的代码、训练数据、生成流程和评估方法，旨在推动机器人学研究在顶级实验室之外的可复现性。

---

### 10. 针对不同硬件的模型量化格式基准测试（https://x.com/bnjmn_marie/status/2037564190802563157）
> 对 Qwen3.5 27B 模型在不同格式（如INT4）和硬件（RTX Pro 6000, B200, H100）上的推理性能进行了基准测试，为硬件选型和部署优化提供了数据参考，例如INT4在RTX Pro 6000级硬件上表现最佳。