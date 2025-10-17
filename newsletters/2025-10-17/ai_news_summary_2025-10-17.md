## AINews - 2025-10-17

> [原文链接](https://news.smol.ai/issues/25-10-15-haiku-45/)

## 📰 十大AI新闻要点

### 1. [Claude Haiku 4.5发布：速度翻倍，成本降低三分之二](https://www.anthropic.com/news/claude-haiku-4-5)
> Anthropic发布Claude Haiku 4.5，完全跳过Haiku 4.0和4.1版本。该模型性能接近Sonnet 4.5，但速度快2倍以上，成本降低3倍。定价为输入1美元/百万token，输出5美元/百万token。

---

### 2. [Google和Yale发布27B癌症研究模型，生成已验证的癌症假说](https://twitter.com/sundarpichai/status/1978507110477332582)
> Google和Yale联合发布基于Gemma的27B基础模型Cell2Sentence-Scale，该模型生成的关于癌细胞行为的新假说已在活细胞中得到实验验证。团队开源了模型权重和相关资源。

---

### 3. [Apple发布M5芯片，LLM提示处理速度提升3.5倍](https://www.reddit.com/r/LocalLLaMA/comments/1o7b5i4/apple_unveils_m5/)
> Apple发布M5芯片，配备iPhone 17时代的设备端AI加速器，声称使用8B参数模型时，LLM提示处理速度比M4快约3.5倍，SSD速度提升2倍，统一内存带宽达150GB/s。

---

### 4. [Google Veo 3.1视频模型发布，增强原生音频和电影风格](https://twitter.com/OfficialLoganK/status/1978492626371289108)
> Google发布Veo 3.1和3.1 Fast视频模型，新增更丰富的原生音频、改进的电影风格、视频到视频参考、更平滑的过渡和视频扩展功能。

---

### 5. [ChatGPT记忆功能升级，支持自动管理和重新排序](https://twitter.com/OpenAI/status/1978608684088643709)
> ChatGPT现在可以自动管理和重新排序保存的记忆，支持按最近时间搜索和排序，该功能正在向Plus/Pro网页版用户推出。

---

### 6. [Meta发布无奖励训练方法，提升AI代理泛化能力](https://arxiv.org/abs/2510.08558)
> Meta论文《Agent Learning via Early Experience》报告通过隐式世界建模和自我反思训练AI代理，无需奖励或演示，在8个环境中提升网络导航(+18.4%)、复杂规划(+15.0%)和科学推理(+13.3%)能力。

---

### 7. [日本要求OpenAI停止在动漫和漫画上的版权侵权](https://www.reddit.com/r/OpenAI/comments/1o71jra/japan_wants_openai_to_stop_copyright_infringement/)
> 日本正推动OpenAI停止在动漫和漫画IP上的训练，并遏制模仿受保护角色的输出，理由是标志性设计具有文化价值，这与日本宽松的文本和数据挖掘例外条款形成冲突。

---

### 8. [MIT DSPy实验室宣布递归语言模型，处理无限上下文](https://twitter.com/a1zhang/status/1978469116542337259)
> MIT DSPy实验室宣布递归语言模型(RLMs)，可处理无限上下文并减少上下文衰减，据报道在1000万+token上获得114%的性能提升，即将推出DSPy模块。

---

### 9. [Poolside与CoreWeave合作获得4万+ NVIDIA GB300 GPU](https://twitter.com/eisokant/status/1978453140656517215)
> Poolside宣布与CoreWeave合作，从2025年12月开始获得40,000+ NVIDIA GB300 GPU，同时启动德克萨斯州西部的2GW AI园区项目Horizon，实现从基础设施到智能的全栈建设。

---

### 10. [OpenAI发布gpt-5-search-api，价格降低60%](https://twitter.com/openaidevs/status/1978224165997195559)
> OpenAI发布gpt-5-search-api，支持域名过滤，价格为10美元/千次调用，比之前降低约60%，提供更高精度的网络查询功能。

---

## 🛠️ 十大工具产品要点

### 1. [Claude Haiku 4.5在SWE-bench上取得73%+成绩](https://openrouter.ai/anthropic/claude-haiku-4-5)
> Claude Haiku 4.5在OpenRouter上发布，在SWE-bench Verified基准测试中取得超过73%的成绩，在计算机使用任务上超越Sonnet 4，提供接近前沿智能的推理能力。

---

### 2. [Windsurf集成Haiku 4.5，以1倍积分提供编码服务](https://twitter.com/windsurf/status/1978512184343662707)
> Windsurf添加Haiku 4.5支持，以1倍积分提供Sonnet 4级别的编码性能，成本仅为三分之一，速度提升2倍以上，用户报告工具调用体验良好。

---

### 3. [Alibaba发布Qwen3-VL 4B/8B紧凑视觉语言模型](https://twitter.com/alibaba_qwen/status/1978150959621734624)
> 阿里巴巴Qwen发布密集的Qwen3-VL 4B和8B模型，在FP8精度下运行，VRAM需求低，在STEM、VQA、OCR、视频理解和代理任务上超越Gemini 2.5 Flash Lite和GPT-5 Nano。

---

### 4. [Unsloth提供Qwen3-VL微调笔记本](https://docs.unsloth.ai/models/qwen3-vl-run-and-fine-tune)
> Unsloth确认Qwen3-VL微调功能正常，并发布可运行的笔记本文档，支持视觉语言SFT/LoRA微调，提供稳定的模板和评估指南。

---

### 5. [NVIDIA DGX Spark基准测试显示推理性能有限](https://twitter.com/nisten/status/1978204860227948815)
> 早期基准测试显示，4,000美元的NVIDIA DGX Spark(128GB)在gpt-oss-120b-fp4上仅达到约11 tokens/秒，而4,800美元的M4 Max MacBook Pro达到约66 tokens/秒，主要受LPDDR5X带宽限制。

---

### 6. [retrieve-dspy模块化集合发布，比较复合检索策略](https://twitter.com/CShorten30/status/1978567334424932523)
> 发布retrieve-dspy，一个模块化DSPy集合，用于比较HyDE、ThinkQE、重排序变体等复合检索策略，提升检索增强生成效果。

---

### 7. [Pydantic AI 1.1.0集成Prefect进行代理编排](https://twitter.com/AAAzzam/status/1978611295243981273)
> Pydantic AI 1.1.0版本集成Prefect工作流管理器，提供更强大的代理编排能力，支持复杂的多步骤AI代理任务管理。

---

### 8. [NotebookLM for arXiv将AI论文转为对话式概述](https://twitter.com/askalphaxiv/status/1978466642146545838)
> NotebookLM for arXiv功能可将密集的AI论文转换为具有跨论文上下文的对话式概述，支持研究人员快速理解多篇相关论文内容。

---

### 9. [nanochat d32模型发布，训练成本约1,000美元](https://twitter.com/karpathy/status/1978615547945521655)
> Andrej Karpathy发布nanochat d32模型，训练约33小时，成本约1,000美元，在CORE基准上达到0.31(GPT-2约0.26)，GSM8K从8%提升至约20%。

---

### 10. [Hugging Face Agents & MCP Hackathon回归](https://huggingface.co/Agents-MCP-Hackathon-Winter25)
> Hugging Face Agents & MCP Hackathon将于2025年11月14-30日回归，规模扩大3倍，上次活动有4,200注册、630提交，分发超过100万美元API积分。

---