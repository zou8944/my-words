## AINews - 2025-11-12

> [原文链接](https://news.smol.ai/issues/25-11-10-not-much/)

## 📰 十大AI新闻要点

### 1. [Moonshot AI发布Kimi K2 Thinking模型](https://www.reddit.com/r/LocalLLaMA/comments/1oth5pw/ama_with_moonshot_ai_the_opensource_frontier_lab/)
> Moonshot AI的Kimi K2 Thinking模型在多项评测中表现优异，在LisanBench上排名第7位（介于GPT-5和GPT-5-Mini之间），在LM Arena Text排行榜上排名开源模型第2位。该模型采用混合注意力架构（KDA + NoPE MLA），原生支持INT4量化，训练成本仅460万美元，支持200-300个工具调用的复杂代理工作流。

---

### 2. [Meta发布Omnilingual ASR语音识别套件](https://twitter.com/AIatMeta/status/1987946571439444361)
> Meta开源发布覆盖1600+语言的语音识别模型套件（300M-7B参数），其中包含500种首次获得服务的语言。同时发布7B参数的Omnilingual wav2vec 2.0表示模型和涵盖350种服务不足语言的Omnilingual ASR语料库。

---

### 3. [SYNTH合成数据集和Baguettotron模型发布](https://twitter.com/Dorialexander/status/1987930819021635964)
> 研究人员发布完全合成的通用预训练数据集SYNTH，以及仅用200B tokens训练的两个新推理模型。Baguettotron在其规模级别中表现最佳，在非代码任务（包括数学）上达到SOTA水平，标志着向"认知核心"方向的重要进展。

---

### 4. [AMD与Modular在MI355X上实现2.2倍推理加速](https://twitter.com/AMD/status/1987898172484567238)
> AMD和Modular报告在14天内将Instinct MI355X的推理性能提升2.2倍。同时NVIDIA详细介绍了TensorRT-LLM在GB200 NVL72系统上的Wide Expert Parallelism技术，用于MoE模型扩展。

---

### 5. [Epoch AI预测GW级数据中心将于2026年上线](https://twitter.com/EpochAIResearch/status/1987938542094610927)
> Epoch AI通过许可证和卫星图像分析预测，首个千兆瓦级数据中心将于2026年上线，超大规模厂商已将建设时间压缩至1-2年。同时发布了Frontier Data Centers数据集和方法说明。

---

### 6. [OpenAI与Bain发布自进化代理框架GEPA](https://twitter.com/DSPyOSS/status/1988021062727020589)
> OpenAI与Bain合作发布新框架，展示能够反思、从反馈中学习并自我进化指令的代理系统。GEPA框架支持开发者创建能够动态调整行为的智能代理，已有开发者展示Python inspect与GEPA的创造性组合。

---

### 7. [10,000小时自我中心机器人数据集开源发布](https://twitter.com/eddybuild/status/1987951619804414416)
> 研究人员发布包含2,153名工作者、10.8亿帧的大规模自我中心机器人数据集，标志着"机器人数据规模化时代的到来"，为机器人学习研究提供重要资源。

---

### 8. [Google推出Nested Learning持续学习新范式](https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/)
> Google引入Nested Learning机器学习新范式，通过将模型视为嵌套优化器层来解决灾难性遗忘问题。该框架旨在实现模型在持续学习过程中的稳定性能保持。

---

### 9. [Fei-Fei Li阐述空间智能与世界模型构建](https://twitter.com/drfeifei/status/1987891210699379091)
> 李飞飞发表关于构建和使用世界模型以解锁空间智能的论述，强调"将视觉转化为推理"的重要性，为AI空间理解能力的发展提供理论框架。

---

### 10. [ARC-AGI v1声称以<$10k成本达到人类水平](https://twitter.com/jerber888/status/1987982067116777521)
> 研究人员声称使用多代理进化测试时间计算和GPT-5 Pro，在12小时内以低于1万美元成本达到85%的人类水平AGI性能，目前正在接受社区严格审查。

---

## 🛠️ 十大工具产品要点

### 1. [Kimi K2 Thinking低成本INT4推理服务](https://twitter.com/arena/status/1987947219224526902)
> Kimi K2 Thinking通过量化感知训练实现原生INT4支持，在非Blackwell GPU上提供低成本推理，定价为$0.15/$2.5每百万tokens，相比Claude Sonnet 4.5的$3/$15具有显著成本优势。

---

### 2. [Gelato-30B-A3B计算机使用模型](https://twitter.com/anas_awadalla/status/1987913284989985092)
> 新发布的计算机使用模型在ScreenSpot-Pro上达到63.8%，OS-World-G上达到69.1%，超越专门的GTA1-32B模型，甚至优于规模大8倍的VLMs，为GUI操作代理提供即时性能提升。

---

### 3. [Qwen3-VL-8B OCR能力表现卓越](https://www.reddit.com/r/LocalLLaMA/comments/1ot95gj/qwen3vls_perceptiveness_is_incredible/)
> Qwen3-VL-8B模型在OCR任务中展现出色性能，能够准确识别4K图像中的文字并提供精确边界框，在多项测试中超越Gemini 2.5 pro、Claude Opus 4等更大模型。

---

### 4. [dLLM库将BERT转换为聊天机器人](https://www.reddit.com/r/LocalLLaMA/comments/1osydym/berts_that_chat_turn_any_bert_into_a_chatbot_with/)
> dLLM库利用离散扩散技术将任何BERT模型转换为聊天机器人，ModernBERT-large在对话任务中表现可与Qwen1.5-0.5B相媲美，提供并行token生成能力。

---

### 5. [Maya1开源语音AI支持20种人类情感](https://huggingface.co/maya-research/maya1)
> 新发布的SOTA开源语音AI Maya1具有3B参数，支持单H100运行，能够识别和表达20种人类情感，在语音设计和情感表达方面实现重要突破。

---

### 6. [INT8 GEMM内核实现300.26 T-ops/s性能](https://colab.research.google.com/drive/1D-KihKFEz6qmU7R-mvba7VeievKudvQ8?usp=sharing)
> 开发者发布GMP验证的精确INT8×INT8→INT32 GEMM内核，在A100上达到300.26 T-ops/s的宏吞吐量，展示位对位正确性，代码开源供社区验证。

---

### 7. [Modular MAX引擎在B200和MI355X上超越竞品](https://twitter.com/AMD/status/1987898172484567238)
> Modular的MAX推理引擎在Mojo中实现，在B200上超越TensorRT，在MI355X上超越AMD方案，为HPC开发者提供避免C++包移植到GPU的解决方案。

---

### 8. [AutoXLA为TPU提供4倍加速性能](https://github.com/Locutusque/AutoXLA)
> AutoXLA实验库自动化大型语言模型在TPU上的分布、优化和量化，相比标准Flash Attention实现达到4倍性能提升，扩展Hugging Face Transformers接口支持TPU感知功能。

---

### 9. [ComfyUI专业工作流实现生产级图像生成](https://github.com/NexusAI-Lab/ComfyUI-Professional-Workflows)
> NexusAI发布稳定、生产就绪的ComfyUI工作流套件，针对照片级真实感、动漫和商业图像生成进行优化，提供一键式工作流程，确保不同随机种子下的细节一致性。

---

### 10. [Ploke为Rust编程提供开源AI接口](https://github.com/josephleleg/ploke)
> 新发布的开源AI接口专门为Rust编程设计，通过原生项目解析和自动语义搜索增强LLM上下文管理的相关性和效率，支持通过交互式覆盖选择OpenRouter托管的模型。

---