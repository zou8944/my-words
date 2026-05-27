## AINews - 2026-05-27

> [原文链接](https://news.smol.ai/issues/26-05-21-not-much/)

## 📰 十大AI新闻要点

### 1. [OpenAI Codex 实现远程跨设备操作](https://x.com/OpenAIDevs/status/2057536706778378692)
> OpenAI 宣布 Codex 现在可以在 Mac 锁定时，通过手机安全地控制 Mac 上的应用。这标志着 AI 代理产品形态正从聊天式 IDE 向持久的跨设备操作员工作流转变。同时，Codex 还推出了 Appshots 功能，可捕获 Mac 应用窗口的截图和文本以丰富工作上下文。

---

### 2. [RAEv2 实现 10 倍以上训练加速](https://x.com/1jaskiratsingh/status/2057568174590304421)
> 研究人员发布了 RAEv2，这是表示自编码器的重要更新，在统一视觉理解和生成方面取得突破。该版本实现了 **>10 倍更快的收敛速度**，更好的重建和生成效果，并已扩展到文本到图像和世界模型测试。核心发现包括：对最后 K 个编码器层求和可同时改善重建和生成，RAE 和 REPA 在语义与空间结构上互补。

---

### 3. [NVIDIA 推出 Gated DeltaNet-2 线性注意力架构](https://x.com/ahatamiz1/status/2057586630450610673)
> NVIDIA 发布了 Gated DeltaNet-2，通过通道级门控机制在线性注意力中解耦了“擦除”和“写入”操作。在 1.3B 参数规模下，该模型在语言建模和常识推理上超越了 KDA 和 Mamba-3，并在 RULER 长上下文检索任务上表现突出。Sebastian Raschka 称其为“更有趣的混合注意力方向之一”。

---

### 4. [数据过滤的惊人发现：最优过滤器可能是“无过滤”](https://x.com/tatsu_hashimoto/status/2057489411768803526)
> Tatsu Hashimoto 在 DCLM 数据集上报告了一个令人惊讶的扩展结果：在足够计算资源下，最佳的数据过滤器可能是 **不进行过滤**。投影显示，对于互联网规模的数据池，交叉点大约在 **1e30 FLOPs** 附近。这意味着随着计算量增加，原始数据的多样性可能比精心筛选的数据更有价值。

---

### 5. [turbopuffer 实现 1 亿美元年收入，仅融资不到 100 万美元](https://x.com/Sirupsen/status/2057470756070781400)
> 搜索/检索基础设施公司 turbopuffer 在 3 月突破了 **1 亿美元年经常性收入**，距离达到 100 万美元仅过去 19 个月，且公司已实现盈利，总融资额不到 100 万美元。这被广泛视为“AI 基础设施才是真正赚钱的地方”的典型案例，因为前沿团队发现“AI 的魔力在于拉取正确的上下文”，这本质上是一个搜索/检索问题。

---

### 6. [Modal 完成 3.55 亿美元 C 轮融资，估值 46.5 亿美元](https://x.com/bernhardsson/status/2057530320790995262)
> AI 云基础设施公司 Modal 宣布完成 **3.55 亿美元** 的 Series C 轮融资，估值达到 **46.5 亿美元**。投资者强调其从零开始为 AI 工作负载重建云堆栈的理念，具有强大的性能和开发者体验。这与其他信号（如 Daytona 的 60ms 沙箱、RL/评估工作负载占使用量一半）一起表明，代理原生计算正在成为独立品类。

---

### 7. [Hark 融资 7 亿美元，估值 60 亿美元，进军 AI 硬件](https://x.com/adcock_brett/status/2057462134989263047)
> Hark 宣布完成 **7 亿美元** 融资，估值 **60 亿美元**，资金将用于 GPU 基础设施、未来模型开发、硬件以及多模态/个人智能产品。该公司还报告其 F.03 系统实现了 **200 小时** 不间断自主运行。尽管技术细节有限，但融资规模显示了投资者对垂直整合 AI 设备押注的巨大兴趣。

---

### 8. [Runway 推出 Aleph 2.0 和 Edit Studio，实现单帧编辑传播](https://x.com/runwayml/status/2057530497597600169)
> Runway 发布了 Aleph 2.0 和新版 Edit Studio，允许用户编辑视频中的单个帧，然后将该编辑自动传播到整个视频。这是“参考引导编辑传播”问题的实用产品化。同时，阿里巴巴研究人员的 MIGA 方法被标记为一种 **无需训练** 的无限帧视频生成方法，采用两阶段对齐机制实现时间一致性。

---

### 9. [Gemini 3.5 Flash 登顶 APEX-Agents-AA 排行榜](https://x.com/OfficialLoganK/status/2057460544643404125)
> Gemini 3.5 Flash 在 APEX-Agents-AA 排行榜上排名 **第一**，超越了更大的模型。在应用方面，有开发者展示了使用 **单个 Gemini API 调用** 构建的 GitHub Issue 分类代理，无需任何编排框架。Google 还扩展了 Gemini 的行动面，包括 Daily Brief 以及与 OpenTable、Canva 和 Instacart 的连接应用操作。

---

### 10. [Meta 裁员 8000 人，AI 驱动重组](https://www.reddit.com/r/singularity/comments/1tiosgg/mark_zuckerbergs_meta_kicks_off_major_bloodbath/)
> Meta 宣布全球裁员约 **8000 人**（约占员工总数的 10%），分三波进行。裁员被归因于 AI 驱动的重组。评论者质疑 Meta 的 **2000 亿美元 AI 资本支出** 是否合理，并认为 AI 采用正在推动持续的运营模式转变，大型组织可能面临每年 10-20% 的裁员。

---

## 🛠️ 十大工具产品要点

### 1. [physics-intern：科学问题代理框架，让 Gemini 3.1 Pro 超越 GPT 5.5 Pro](https://x.com/lvwerra/status/2057476832664953225)
> 发布了 **physics-intern**，一个科学问题代理框架（harness），能将 Gemini 3.1 Pro 的得分从 17.7 提升至 31.4，在该设置下超越 GPT 5.5 Pro。值得注意的是，GPT 5.5 Pro 本身并未从该框架中受益，表明模型对脚手架技巧的吸收具有特异性。

---

### 2. [Weaviate 内置 MCP 服务器，实现混合检索](https://x.com/weaviate_io/status/2057476556449010024)
> Weaviate 在数据库中内置了 **MCP 服务器**，使编码代理能够摄取代码仓库并使用 **混合 BM25 + 向量检索**，无需额外进程。这简化了 AI 代理的检索增强生成（RAG）架构。

---

### 3. [LangChain 推出沙箱认证代理和类型化流协议](https://x.com/LangChain/status/2057508777759236401)
> LangChain 引入了 **沙箱认证代理** 用于控制代理与世界之间的边界，以及新的 **类型化流协议**，将工具、子代理、媒体和中断作为一等公民投影而非令牌流进行渲染。这标志着代理基础设施在安全性和可观察性方面的成熟。

---

### 4. [vLLM 推出弹性专家并行，实现 MoE 动态调整](https://x.com/vllm_project/status/2057602243860574463)
> vLLM 实现了 **弹性专家并行**，允许在不完全重启的情况下实时调整 MoE 的 DP/EP 拓扑，通过 NVLink/RDMA 进行直接的 GPU 到 GPU 传输。这对扩展和未来的容错服务都至关重要。

---

### 5. [LeRobot Humanoid：2500 美元的开源人形机器人](https://x.com/robotsdigest/status/2057507896129380581)
> Hugging Face 发布了 **LeRobot Humanoid**，一个完整的开源人形机器人套件，成本约 **2500 美元**，采用 **3D 打印** 制造。包含完整的硬件/CAD、校准/运行时、仿真、识别工具和训练流水线。关键点不仅在于价格，更在于可修复性和迭代速度。

---

### 6. [Carbon DNA 模型在 Trainium2 上运行](https://x.com/Shekswess/status/2057468970471448787)
> Hugging Face Bio 的 **Carbon** DNA 模型家族（Carbon-500M、3B 和 8B）被展示在单个 **Trainium2 trn2.3xlarge** 实例上使用 NxD Inference 编译和运行。这验证了生物基础模型在 AWS 专用 AI 芯片上的部署可行性。

---

### 7. [OlmoEarth v1.1：3 倍更便宜/更快的地球观测模型](https://x.com/cgeorgiaw/status/2057481909802774664)
> **OlmoEarth v1.1** 通过改变多分辨率 Sentinel-2 输入的标记化方式，将令牌数量减少 **3 倍**，利用二次计算节省实现了 **3 倍更便宜/更快** 的推理。这是地理空间 AI 模型效率提升的典型案例。

---

### 8. [Cohere 发布 Command A+：首个开源 MoE 模型](https://cohere.com/blog/command-a-plus)
> Cohere 发布了 **Command A+**，其首个 **混合专家（MoE）** 开源模型，采用 **Apache 2.0** 许可。Cohere 声称通过大量量化工作，该模型可在 **1-2 个 GPU** 上实际部署，面向代理/企业工作负载和较小的开发者团队。

---

### 9. [Anthropic 推出 13+ 免费 AI 课程，含 MCP 和 Claude Code](https://www.anthropic.com/learn)
> Anthropic 发布了免费官方培训目录，涵盖 **MCP/代理 AI**、**Claude Code**、Claude API 使用以及 Amazon Bedrock 和 Google Cloud Vertex AI 的企业部署路径。技术亮点包括 MCP 高级课程（覆盖 STDIO 和 StreamableHTTP 传输协议）以及 Claude Code 的“计划模式”工作流。

---

### 10. [Qwen3.6-35B-A3B 在 12GB VRAM 上实现 110 tok/s](https://www.reddit.com/r/LocalLLaMA/comments/1tjh7az/110_toks_with_12gb_vram_on_qwen36_35b_a3b_and_ik/)
> 用户使用 **ik_llama.cpp** 在 **RTX 4070 Super 12GB** 上运行 Qwen3.6-35B-A3B-MTP，实现了平均 **110.24 tok/s** 的推理速度，比标准 llama.cpp 提升 23%。使用了 IQ4_XS 4.19 bpw 量化、131072 上下文和 MTP 推测解码。这展示了 MoE 模型在消费级 GPU 上的高效部署潜力。