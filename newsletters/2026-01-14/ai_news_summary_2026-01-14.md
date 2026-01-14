## AINews - 2026-01-14

> [原文链接](https://news.smol.ai/issues/26-01-12-gemini-apple/)

## 📰 十大AI新闻要点

### 1. [苹果选择谷歌Gemini为下一代Siri提供动力](https://www.wcnc.com/article/news/nation-world/apple-google-gemini-siri-ai-features/507-575faa99-217e-498d-8f34-5455759113f8)
> 苹果宣布与谷歌达成合作，将使用谷歌的Gemini模型和云技术来驱动下一代“苹果基础模型”，为包括“更个性化的Siri”在内的苹果智能功能提供支持。苹果强调将通过其私有云计算（Private Cloud Compute）提供安全层，以维持其隐私标准。此举被视为谷歌的重大胜利，而苹果最初合作的OpenAI则相对失利，这可能与OpenAI传闻中的消费级硬件设备计划有关。

---

### 2. [Anthropic推出“Cowork”：面向非技术工作的Claude Code](https://twitter.com/claudeai/status/2010805682434666759)
> Anthropic发布了名为“Cowork”的研究预览版，将其Claude Code的能力扩展到非编码工作。该工具允许用户将Claude指向电脑上的一个文件夹，使其能够自主读取、编辑和创建文件，执行如自动整理文件夹、根据截图创建电子表格等任务。它集成了现有连接器，并与Chrome中的Claude配对处理浏览器任务。这引发了关于“LLM操作系统”和“代理知识工作”的广泛讨论。

---

### 3. [DeepSeek发布“Engram”：将条件记忆作为新的稀疏性原语](https://github.com/deepseek-ai/Engram/tree/main)
> DeepSeek AI开源了“Engram”（条件记忆通过可扩展查找）项目，为大型语言模型引入了一种新的稀疏性轴。该方法通过哈希N-gram嵌入内存，使模型能够查询并将静态模式的门控到表示中，从而将计算从重建记忆模式中解放出来，让骨干网络专注于推理。社区认为这是一种硬件友好的优化，可以廉价地扩展“知识容量”，同时保持FLOPs稳定。

---

### 4. [OpenAI进军医疗健康领域，推出ChatGPT Health并收购Torch](https://twitter.com/OpenAI/status/2010764845432590469)
> OpenAI推出了“ChatGPT Health”，这是一个独立的聊天空间，用户的健康相关聊天、文件和记忆将被隔离存储，不会流入常规对话。同时，OpenAI宣布收购医疗健康初创公司Torch，以加速ChatGPT Health的能力，整合实验室结果、药物和就诊记录等数据。OpenAI称每周有2.3亿用户使用ChatGPT处理健康相关消息。

---

### 5. [Sakana AI提出“DroPE”：通过丢弃位置编码来扩展上下文](https://twitter.com/SakanaAILabs/status/2010660969719165133)
> Sakana AI的研究提出了“DroPE”方法，旨在扩展模型的上下文长度。其核心思想是：在训练初期使用RoPE（旋转位置编码）以确保收敛，然后在推理时移除位置编码，以避免在扩展上下文时产生语义扭曲。该方法声称在NoPE的训练困难（梯度消失）和RoPE扩展时扭曲低频信号之间找到了一个折中方案，并发布了参考训练器实现。

---

### 6. [NVIDIA/Stanford等提出“端到端测试时训练”作为LLM记忆新范式](https://twitter.com/NVIDIAAIDev/status/2010773774849724858)
> 来自NVIDIA、斯坦福大学和Astera的研究人员提出了“端到端测试时训练”（End-to-End Test-Time Training, TTT-E2E）。该方法允许模型在部署时，基于提供的上下文继续进行下一个token的训练，从而将重要上下文“压缩”到权重中，减少对大型KV缓存的依赖。这被视为实现次二次方长序列建模和LLM记忆的新途径。

---

### 7. [谷歌推出“通用商务协议”，推动代理驱动商务](https://twitter.com/Google/status/2010744570108137524)
> 谷歌宣布了“通用商务协议”（Universal Commerce Protocol, UCP）及相关功能，旨在将AI模型打造为购物界面和交易发起者。新功能包括在AI模式/Gemini中直接结账、与零售商的“商务代理”聊天以及“直接优惠”试点。这标志着谷歌正积极构建AI驱动的商务基础设施。

---

### 8. [智谱与MiniMax IPO叙事分化，反映中国AI商业模式差异](https://twitter.com/ZhihuFrontier/status/2010642118713512174)
> 分析指出，智谱（Zhipu）和MiniMax在IPO市场表现差异源于不同的商业叙事：智谱定位为面向企业和政府的底层基础设施，销售周期长、研发投入大；而MiniMax则定位为面向消费者和全球的平台，具有增长曲线和改善的利润率。这反映了中国AI公司在商业化路径上的不同选择。

---

### 9. [AI21 Labs分享大规模SWE-bench评估经验：基础设施是关键](https://twitter.com/AI21Labs/status/2010738309681823992)
> AI21 Labs透露，他们运行了超过20万次SWE-bench评估，最大的经验教训是基础设施问题。他们采用为每个实例（仓库+依赖+MCP服务器）单独配置并复用的策略，并将生成与评估分离，使得失败的测试可以重试而无需重新生成token。据称，这种方法将失败率从30%降至0，仓库下载量从8000+次减少到500次。

---

### 10. [Ramp开源其内部AI编码代理蓝图，称其编写了30%的合并PR](https://twitter.com/zachbruggeman/status/2010728444771074493)
> 金融科技公司Ramp报告称，其内部开发的AI编码代理在一周内编写了30%已合并的前后端PR。该代理完全在云端运行，基于开源工具构建。Ramp决定开源该系统的“蓝图/规范”，供其他团队参考构建类似系统，展示了AI编码代理在真实生产环境中的成熟应用。

---

## 🛠️ 十大工具产品要点

### 1. [DeepSeek Engram：条件记忆模型](https://github.com/deepseek-ai/Engram)
> DeepSeek开源的Engram模型引入了一种新的稀疏性架构。它通过O(1)查找式的静态N-gram内存，允许模型将大量参数（如嵌入表）卸载到主机内存（RAM甚至NVMe）中，而对推理性能影响极小。据称，一个40B的A3.8B MoE模型可能只需27B的权重保留在快速内存中，这为在消费级硬件上运行更大模型提供了可能。

---

### 2. [Anthropic Claude Cowork](https://claude.com/blog/cowork-research-preview)
> Claude Cowork是Anthropic推出的研究预览工具，旨在将Claude Code的自动化能力扩展到非开发工作流。用户可授权Claude访问特定文件夹，使其能自主执行文件整理、数据提取、报告生成等任务。它集成了浏览器自动化和现有连接器，目前仅向macOS上的Claude Max订阅者开放。

---

### 3. [FASHN Human Parser：时尚人体解析模型](https://huggingface.co/fashn-ai/fashn-human-parser)
> 这是一个针对时尚/电商场景开源的人体解析模型，基于SegFormer-B4微调。它输出18个语义类别（包括身体部位和服装），解决了ATR、LIP、iMaterialist等现有数据集的质量问题。模型输入尺寸为384x576，在GPU上推理约300ms，在CPU上为2-3秒，可通过PyPI和Hugging Face获取。

---

### 4. [Sakana AI DroPE 参考训练器](https://twitter.com/SakanaAILabs/status/2010738878727217595)
> 伴随DroPE论文，Sakana AI发布了该方法的参考训练器实现代码。这为研究人员和开发者实践这种新的上下文扩展技术提供了便利，有助于社区验证和推进长上下文建模的研究。

---

### 5. [Hugging Face 可组合Hub CLI](https://twitter.com/hanouticelina/status/2010664329545224588)
> Hugging Face发布了可组合且易于发现的Hub命令行工具。这些CLI允许编码代理以低上下文消耗的方式探索模型、数据集和Spaces，践行了“Bash即所需”的理念，为AI工作流提供了轻量级接口。

---

### 6. [popcorn-cli v1.2.2：集成NCU性能分析摘要](https://github.com/gpu-mode/popcorn-cli/releases/tag/v1.2.2)
> GPU MODE发布的popcorn-cli工具更新至v1.2.2，新增了与NVIDIA命令行性能分析工具NCU的集成。它可以在命令行中内联渲染性能分析摘要，并下载.ncu-rep工件，旨在为内核开发提供更紧密的反馈循环和可共享的标准性能报告。

---

### 7. [enPurified 净化数据集](https://huggingface.co/enPurified/datasets)
> 该项目通过启发式过滤，从流行的语料库（如smollm-corpus、LongPage、standardebooks、finewiki）中剥离数学、代码、外语和低质量英文文本，生成更干净的监督微调（SFT）就绪数据集。还提供了将FineWeb-edu-dedup转换为OpenAI消息格式的数据集，旨在减少垃圾梯度，加速指令微调。

---

### 8. [Ramp 内部AI编码代理系统蓝图](https://twitter.com/rahulgs/status/2010734253538267197)
> Ramp开源的并非完整代码，而是构建其高效内部AI编码代理的详细蓝图和规范。该系统基于opencode、Modal、Cloudflare等开源工具在云端运行，展示了如何将AI代理深度集成到实际开发工作流中并取得高产出（30%合并PR）。

---

### 9. [Pulse Framework：新的编码工具框架](https://github.com/manuelfussTC/PulseFramework)
> 社区新推出的Pulse框架，加入了日益增长的AI编码工具竞争。它被定位为一个轻量级的编排层，专注于可重复的工作流和集成钩子，使模型切换和工具调用更易于管理，反映了向更务实、少“代理神秘主义”的开发工具趋势。

---

### 10. [Doomlaser Vibe Coding Protocol (DVCP)](https://doomlaser.com/longform/dvcp)
> DVCP是一套详细的、用于LLM辅助编码的结构化协议。它采用“命令与控制”和“行政休息室”双线程架构，并要求模型输出完整文件代码，以避免传统聊天界面中常见的“宜家式”零碎编辑导致的代码质量下降和DOM大小限制问题。该协议旨在将ChatGPT类工具转变为可批处理的重构引擎。