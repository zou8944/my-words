## AINews - 2025-10-22

> [原文链接](https://news.smol.ai/issues/25-10-20-not-much/)

## 📰 十大AI新闻要点

### 1. [DeepSeek发布革命性OCR模型，实现视觉压缩技术](https://github.com/deepseek-ai/DeepSeek-OCR)
> DeepSeek推出3B参数的DeepSeek-OCR模型，采用创新的"光学上下文压缩"技术，可将长文本作为视觉上下文压缩10-20倍同时保持精度。关键指标：在<10倍压缩下达到约97%解码精度，单A100-40G每天处理约20万页，20个节点每天处理约3300万页。

---

### 2. [Google DeepMind Veo 3.1登顶视频生成排行榜](https://twitter.com/GoogleDeepMind/status/1980261047836508213)
> Veo 3.1在Video Arena上跃升约30分，成为首个在文本到视频和图像到视频类别均超过1400分的模型，在物理真实感方面超越先前领先者，并新增精确编辑功能。

---

### 3. [Krea开源实时视频生成模型](https://twitter.com/krea_ai/status/1980358158376988747)
> Krea发布"Realtime"，一个14B参数的Apache-2.0自回归视频模型，在单个B200上能够实现约11 FPS的长格式生成，权重和报告已在Hugging Face发布。

---

### 4. [Anthropic推出Claude Code并开源沙盒](https://twitter.com/_catwu/status/1980338889958257106)
> Anthropic在浏览器和iOS上推出Claude Code，在云虚拟机中运行任务，新的CLI沙盒模式可将权限提示减少84%，并开源沙盒供一般代理构建者使用。

---

### 5. [AWS us-east-1重大中断影响多个AI应用](https://twitter.com/AravSrinivas/status/1980172632600506579)
> 重大AWS中断导致多个AI应用（如Perplexity和Moondream网站）瘫痪，事件重新强调了多区域/多云策略的重要性，以及最小化供应商锁定的必要性。

---

### 6. [Modular为AMD MI355带来行业领先性能](https://twitter.com/clattner_llvm/status/1980320847475913112)
> Modular在两周内为AMD MI355带来行业领先性能，现在支持3个供应商的7种GPU架构，展示了深度编译器投资的好处。

---

### 7. [真实货币交易评估显示DeepSeek V3.1领先](https://twitter.com/mervenoyann/status/1980178771706835425)
> 社区基准测试为每个模型分配1万美元进行几天交易，报告显示DeepSeek V3.1和Grok 4领先，而GPT-5/Gemini 2.5亏损。

---

### 8. [Anthropic推出生命科学专用AI工具](https://twitter.com/AnthropicAI/status/1980308459368436093)
> Anthropic推出连接器（Benchling、PubMed、Synapse.org等）和代理技能来遵循科学协议，早期用户包括Sanofi、AbbVie和Novo Nordisk。

---

### 9. [Unitree H2机器人展示先进运动能力](https://www.reddit.com/r/singularity/comments/1obbuf9/introducing_unitree_h2_china_is_too_good_at/)
> Unitree Robotics推出Unitree H2，展示先进的运动能力，向更自然流畅的运动迈进，突显中国在机器人领域不断增长的专业知识。

---

### 10. [Ray Kurzweil维持2029年AGI预测](https://www.reddit.com/r/OpenAI/comments/1obh30l/in_1999_most_thought_ray_kurzweil_was_insane_for/)
> Ray Kurzweil自199年以来一直预测人工通用智能将在2029年到来，尽管存在质疑仍维持这一时间线，但缺乏普遍接受的AGI定义使预测复杂化。

---

## 🛠️ 十大工具产品要点

### 1. [DeepSeek-OCR在vLLM中获得Day-0支持](https://twitter.com/vllm_project/status/1980235518706401405)
> DeepSeek-OCR在vLLM中获得Day-0支持，在A100-40G上提供约2,500 tok/s的推理速度，官方支持将在下一个版本中落地。

---

### 2. [TileLang AI DSL达到H100上FlashMLA约95%性能](https://twitter.com/ZhihuFrontier/status/1980170674112188440)
> 新的AI DSL TileLang通过布局推断、交换、warp专业化和流水线，用约80行Python代码在H100上达到FlashMLA约95%的性能。

---

### 3. [GPTQ int4后训练量化内置到Keras 3](https://twitter.com/fchollet/status/1980343806265552918)
> GPTQ int4后训练量化现在内置到Keras 3中，附带供应商无关指南，简化了模型量化部署。

---

### 4. [Cline推出企业版支持多模型提供商](https://twitter.com/cline/status/1980369441079849229)
> Cline宣布企业版本可在开发者工作的地方运行（VS Code/JetBrains/CLI），并支持任何可用的模型/提供商，这种"自带推理"姿态在云中断期间特别有帮助。

---

### 5. [IBM和Groq合作提供5倍速度提升](https://twitter.com/robdthomas/status/1980239227955683598)
> IBM和Groq将watsonx代理与Groq LPU推理配对，声称速度提升5倍且成本仅为20%，并支持vLLM-on-Groq。

---

### 6. [LlamaIndex展示强大的文本到SQL工作流](https://twitter.com/llama_index/status/1980309057287446532)
> LlamaIndex演示了具有语义表检索、OSS text2SQL、多步骤编排和错误处理的强大文本到SQL工作流。

---

### 7. [Moondream 3展示单次JSON解析能力](https://twitter.com/moondreamai/status/1980405287531254089)
> Moondream 3展示复杂停车标志的单次JSON解析能力，无需OCR堆栈，展示了结构化VLM提取的潜力。

---

### 8. [tinygrad为Mac提供eGPU驱动支持](https://twitter.com/__tinygrad__/status/1980082660920918045)
> tiny corp宣布公开测试纯Python驱动程序，通过任何USB4 eGPU扩展坞在Apple Silicon MacBook上支持NVIDIA 30/40/50系列和AMD RDNA2-4 GPU。

---

### 9. [Helion 0.2作为公开测试版发布](https://pypi.org/project/helion/0.2.0/)
> Helion 0.2作为公开测试版在PyPI上发布，定位为基于编译器堆栈的高级内核编写DSL。

---

### 10. [TorchAO改进量化配置支持](https://github.com/pytorch/ao/pull/3083)
> TorchAO将弃用filter_fn以支持quantize_op，转而使用支持正则表达式的ModuleFqnToConfig，简化了大型代码库的选择性量化策略。

---