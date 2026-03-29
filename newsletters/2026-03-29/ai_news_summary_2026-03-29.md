## AINews - 2026-03-29

> [原文链接](https://news.smol.ai/issues/26-03-27-not-much/)

## 📰 十大AI新闻要点

### 1. Anthropic 计划推出超越Opus的新模型层级“Capybara”
> 根据泄露信息和《财富》杂志的报道，Anthropic 正在开发一个名为“Capybara”的新模型层级，定位在 Claude Opus 4.6 之上，据称在编码、学术推理和网络安全方面表现显著提升。其发布受限于高昂的成本和安全考量。
来源：文章内容（引用自 @M1Astra 和 @scaling01 的推文）

---

### 2. Google 接近资助 Anthropic 数据中心建设
> 《金融时报》报道称，Google 即将为 Anthropic 的数据中心提供资金支持。这突显出前沿AI模型的竞争正日益受到算力、能源和资本支出的制约，而不仅仅是算法本身。
来源：文章内容（引用自 @FirstSquawk 的推文）

---

### 3. 智谱AI发布GLM-5.1，开源编码模型性能逼近闭源模型
> 智谱AI向所有编码计划用户开放了GLM-5.1模型。社区评测和Arena排行榜分析均表明，以GLM-5.1为代表的高端中文开源/半开源编码模型，与闭源模型之间的性能差距正在迅速缩小。
来源：https://x.com/Zai_org/status/2037490078126084514

---

### 4. 本地模型部署经济性持续改善，成为可行替代方案
> 多个案例显示，本地模型（如Qwen 3.5 14B/27B/35B）通过量化等技术，已能在消费级硬件上高效运行，为许多工作流提供了成本可控的云端API替代方案，性能损失极小。
来源：https://x.com/TheGeorgePu/status/2037473248577782046

---

### 5. TurboQuant量化技术引发性能争议
> 研究人员 @gaoj0017 对Google的ICLR 2026 TurboQuant论文提出质疑，指控其在理论和基准测试中歪曲了与RaBitQ的比较，包括不公平的CPU与GPU对比。这引发了社区对相关性能宣传的讨论。
来源：https://x.com/gaoj0017/status/2037532673812443214

---

### 6. Nous Research的Hermes Agent成为开源AI智能体焦点
> Hermes Agent集成了Hugging Face作为首要推理提供商，提供28个精选模型，并支持更多模型访问。这标志着开源智能体在记忆、持久化机器访问和模型选择方面迈出了重要一步。
来源：https://x.com/NousResearch/status/2037654827929338324

---

### 7. AI智能体基础设施走向成熟，关注可追溯性、评估与调试
> Hugging Face呼吁建立开放的智能体轨迹数据集，LangChain则发布了一系列面向生产环境的工具，包括智能体评估准备清单、Deep Agents IDE风格UI指南和LangSmith Prompt Hub环境。这表明智能体技术栈正从“带工具的聊天机器人”向具备软件生命周期原语的方向演进。
来源：https://x.com/ClementDelangue/status/2037530125638455610

---

### 8. Meta发布SAM 3.1，显著提升视频分割速度
> Meta发布了SAM 3.1，这是一个支持对象多路复用的即插即用更新，允许单次前向传播处理多达16个对象。据称，在中等对象工作负载下，单个H100上的视频处理吞吐量从约16 FPS提升至32 FPS。
来源：https://x.com/AIatMeta/status/2037582117375553924

---

### 9. 世界模型与机器人学领域出现重要开源发布
> Yann LeCun团队的LeWorldModel论文/代码库发布，这是一个旨在通过SIGReg使表征崩溃在数学上不可能的小型开源世界模型。同时，宇树科技开源了UnifoLM-WBT-Dataset，一个用于人形机器人全身遥操作的真实世界数据集。
来源：https://x.com/LiorOnAI/status/2037484990779339064

---

### 10. 语音与音频领域开源模型表现强劲
> Cohere发布了新的20亿参数、Apache-2.0许可的转录模型，在A100上实现了12分钟转录33小时音频的高吞吐量。同时，Mistral的Voxtral TTS论文和相关演示也受到关注，显示出开源音频模型的活跃发展。
来源：https://x.com/victormustar/status/2037572662659104976

---

## 🛠️ 十大工具产品要点

### 1. TurboQuant vLLM 优化分支
> @iotcoi 发布了一个TurboQuant vLLM分支，融合了Triton KV写入路径和解码注意力机制，针对Qwen3.5-35B AWQ模型，目标支持100万上下文长度和400万KV缓存，旨在提升长上下文推理效率。
来源：https://x.com/iotcoi/status/2037478891179135123

---

### 2. 针对RTX Pro 6000的INT4量化方案
> @bnjmn_marie 对Qwen3.5 27B模型在不同格式和硬件（RTX Pro 6000/B200/H100）上进行了基准测试，结果显示INT4量化在RTX Pro 6000级别硬件上是推理的最佳选择。
来源：https://x.com/bnjmn_marie/status/2037564190802563157

---

### 3. 开源量化新方法 RotorQuant
> RotorQuant 提出了一种利用克利福德代数进行向量量化的新方法，据称比TurboQuant快10-19倍，且参数减少44倍。虽然理论上的最大坐标幅度和MSE可能更高，但在实际KV缓存分布中表现出有价值的性能/质量权衡。
来源：https://github.com/scrya-com/rotorquant

---

### 4. OpenAI Codex 插件生态系统扩展
> OpenAI开发者展示了Codex插件及其用例库，同时Box公司发布了用于自动化Box内容工作流的Codex插件。这表明Codex生态正从简单的提示/响应模式，转向集成持久化工作空间、问题系统、终端和PR流程的深度工作流自动化。
来源：https://x.com/OpenAIDevs/status/2037604273434018259

---

### 5. 实时浏览器会话调试仪表板
> @ctatedev 发布了一个新的智能体-浏览器仪表板，用于实时调试浏览器会话。这是智能体开发工具链走向成熟、提升可调试性的一个例证。
来源：https://x.com/ctatedev/status/2037599050112160165

---

### 6. 面向真实工作负载的智能体基准测试 AA-AgentPerf
> Artificial Analysis 推出了AA-AgentPerf基准测试，专注于真实的编码智能体轨迹、超过10万的序列长度，并以“每加速器/每千瓦/每美元/每机架的并发用户数”来衡量吞吐量。这比合成的令牌基准测试更贴近实际部署需求。
来源：https://x.com/ArtificialAnlys/status/2037562417836929315

---

### 7. 长视野编码评估基准 CursorBench
> CursorBench 基准测试因其使用真实编码会话、未充分指定的提示、更广泛的质量维度以及每个任务中位数181行的代码更改量而受到认可。这比静态的玩具任务更能健康地评估智能体的长程编码能力。
来源：文章内容（引用自 @cwolferesearch 的推文）

---

### 8. 开源机器人操作套件 MolmoBot
> AI2 发布了MolmoBot，这是一个完全在模拟中训练的开源机器人操作套件，提供了代码、训练数据、生成管道和评估方法，旨在提高机器人学研究的可复现性。
来源：https://x.com/allen_ai/status/2037590611990094259

---

### 9. 基于 Clifford 代数的快速量化实现
> RotorQuant 的实现利用了融合的CUDA内核和Metal着色器，在RTX PRO 4000和Apple M4等硬件上显著优于cuBLAS矩阵乘法运算，为本地部署提供了高效的量化选项。
来源：https://www.scrya.com/rotorquant/

---

### 10. 本地模型部署优化实践（TurboQuant + llama.cpp）
> 社区实验成功将Google的TurboQuant压缩方法集成到llama.cpp中，使得Qwen 3.5–9B模型能够在标准MacBook Air (M4, 16GB)上运行20K上下文，这在此类硬件上原本是不可行的，展示了量化技术对扩展本地模型能力的潜力。
来源：https://www.reddit.com/r/LocalLLaMA/comments/1s5kdu0/google_turboquant_running_qwen_locally_on_macair/