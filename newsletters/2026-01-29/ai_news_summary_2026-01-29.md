## AINews - 2026-01-29

> [原文链接](https://news.smol.ai/issues/26-01-27-kimi-k25/)

## 📰 十大AI新闻要点

### 1. [Moonshot AI发布Kimi K2.5，在多项基准测试中取得SOTA](https://www.kimi.com/blog/kimi-k2-5.html)
> Moonshot AI正式发布了Kimi K2.5模型，这是一个32B激活参数、1T总参数的混合专家模型。该模型在多项关键基准测试中取得了领先成绩，包括在HLE完整集上达到50.2%，在BrowseComp上达到74.9%，同时在MMMU Pro和SWE-bench Verified等开源视觉与编码基准测试中也位居榜首。

---

### 2. [Kimi K2.5引入原生多模态与“智能体集群”功能](https://x.com/Kimi_Moonshot/status/2016024049869324599)
> Kimi K2.5首次实现了“原生多模态”能力，支持图像和视频理解，能够从屏幕录制视频中重建网站。同时，模型推出了“智能体集群”功能，可动态生成并协调多达100个子智能体并行工作，执行高达1500个协调步骤，据称可将复杂任务速度提升高达4.5倍。

---

### 3. [Arcee与Prime Intellect联合发布400B MoE模型Trinity Large预览版](https://x.com/arcee_ai/status/2016278017572495505)
> Arcee与Prime Intellect合作发布了Trinity Large模型的预览版权重。这是一个拥有4000亿参数、130亿激活参数的混合专家模型，在约17000亿token的数据集上训练完成，旨在成为西方开源社区对标前沿闭源模型的一次尝试。

---

### 4. [OpenAI推出面向科学家的AI原生协作平台Prism](https://x.com/OpenAI/status/2016209462621831448)
> OpenAI发布了名为Prism的新产品，这是一个由GPT-5.2驱动的免费AI原生工作空间，专为科学家设计。它集成了LaTeX写作、文献搜索、校对和引文管理等功能，被社区视为“带有AI的Overleaf”，旨在提升科研协作效率。

---

### 5. [DeepSeek发布DeepSeek-OCR 2，大幅提升文档理解效率](https://x.com/vllm_project/status/2016065526058090967)
> DeepSeek发布了新一代OCR模型DeepSeek-OCR 2。该模型引入了视觉因果流学习排序和DeepEncoder V2，实现了高达16倍的视觉token压缩（每图256-1120个token），并在OmniDocBench v1.5基准上取得了91.09%的成绩，提升了3.73%。

---

### 6. [谷歌推出“智能体视觉”技术，将代码执行循环引入视觉任务](https://x.com/GoogleAI/status/2016267526330601720)
> 谷歌正在产品化一种名为“智能体视觉”的技术，该技术为视觉模型引入了“思考-行动-观察”循环。模型可以编写并执行Python代码来裁剪、缩放、注释图像，据称能在多个视觉基准测试上带来5-10%的质量提升。

---

### 7. [Hugging Face发布Transformers v5，为MoE模型带来6-11倍加速](https://github.com/huggingface/transformers)
> Hugging Face发布了Transformers库的v5最终版。此版本针对混合专家模型进行了重大优化，实现了6到11倍的推理速度提升。同时，它简化了API，支持MoE模型的动态权重加载、量化、张量并行和PEFT，并移除了快/慢分词器的区分。

---

### 8. [谷歌研究发布ATLAS，揭示大规模多语言模型的扩展定律](https://x.com/GoogleResearch/status/2016234343602258274)
> 谷歌研究团队发布了ATLAS项目，旨在探索大规模多语言语言模型的扩展定律。该研究提供了数据驱动的指导，帮助在模型大小与多语言数据混合之间取得平衡，为高效训练支持多种语言的模型提供了理论依据。

---

### 9. [Unsloth宣布MoE训练速度提升14倍，并支持Transformers v5](https://x.com/UnslothAI/status/2015935368525447395)
> Unsloth AI宣布其优化技术现在可以使混合专家模型的训练速度比v4版本快14倍，并预计未来优化将再次翻倍，达到总计30倍的加速。团队还推出了对Transformers v5的全面支持。

---

### 10. [Anthropic研究揭示微调可能重新激活模型中的生物安全风险](https://arxiv.org/pdf/2601.13528)
> 来源：文章内容
> Anthropic的一项研究论文指出，对开源模型进行微调（即使是使用前沿模型的输出），可能会解除先前安全训练所抑制的有害能力，例如生物风险。这表明模型的“拒绝”机制是脆弱的，可能被少量计算资源绕过，引发了关于双重用途技术的担忧。

---

## 🛠️ 十大工具产品要点

### 1. [Kimi Code：Moonshot开源的Apache-2.0编码智能体](https://twitter.com/Kimi_Moonshot/status/2016034259350520226)
> Moonshot AI开源了Kimi Code，这是一个Apache-2.0许可的编码智能体，可与常见的IDE和编辑器集成。同时发布的还有Agent SDK，允许开发者构建自定义智能体，扩展了Kimi生态系统的工具链。

---

### 2. [vLLM宣布对Trinity Large和DeepSeek-OCR 2提供首日支持](https://x.com/vllm_project/status/2016322567364346331)
> 高性能推理引擎vLLM宣布在发布当天即支持Arcee的Trinity Large模型和DeepSeek-OCR 2模型，确保了这些前沿模型能够被高效地部署和服务。

---

### 3. [Ollama Cloud集成Kimi K2.5，提供便捷的云端体验](https://x.com/ollama/status/2016086374005538932)
> Ollama在其云服务中快速集成了Kimi K2.5模型，为用户提供了开箱即用的体验。Together AI和Fireworks AI也作为合作伙伴提供了对Kimi K2.5 API的访问。

---

### 4. [Mistral发布Vibe 2.0，升级编码智能体功能](https://twitter.com/mistralvibe/status/2016179799689928986)
> Mistral发布了其编码智能体Vibe的2.0版本，新增了子智能体、用户自定义智能体、技能/斜杠命令等功能，并推出了付费计划，标志着其产品化进程的深入。

---

### 5. [Cursor强调语义搜索对编码智能体性能的关键提升](https://x.com/cursor_ai/status/2016202243499073768)
> Cursor指出，对其代码库进行语义搜索索引能显著提升编码智能体的性能，并且为大型代码库建立索引的速度比之前快了“几个数量级”。

---

### 6. [谷歌Jules智能体引入“执行前批判”机制提升可靠性](https://x.com/julesagent/status/2016178107019837917)
> 谷歌的Jules智能体引入了一个“规划批判者”功能，这是一个在计划执行前对其进行审查的第二智能体。据称，这一机制能将任务失败率降低9.5%，从而提高了智能体工作流的可靠性。

---

### 7. [Jan发布v3 Instruct 4B编码模型，在Aider基准上提升40%](https://www.reddit.com/r/LocalLLaMA/comments/1qo3ri5/jan_v3_instruct_a_4b_coding_model_with_40_aider/)
> 来源：文章内容
> Jan项目发布了v3 Instruct，这是一个40亿参数的编码模型。在Aider基准测试中，该模型取得了18分的成绩，相比其他同类模型有超过40%的性能提升，展示了其在轻量级编码辅助任务上的潜力。

---

### 8. [MiniMax推出“智能体桌面”工作空间](https://twitter.com/omarsar0/status/2016149402923200634)
> MiniMax发布了一款名为“智能体桌面”的产品，被描述为一个比Claude Cowork更精致的AI工作空间，专注于提供高度集成的智能体办公体验。

---

### 9. [Figure发布Helix 02，实现全身自主机器人控制](https://x.com/Figure_robot/status/2016207013236375661)
> Figure公司发布了Helix 02，这是一个用于自主全身机器人控制的系统。结合其演示，这表明在具身智能和机器人控制领域取得了实质性进展。

---

### 10. [社区开发者构建Claude Code的“蜂群思维”多智能体系统](https://github.com/blackms/aistack)
> 一位开发者构建了一个为Claude Code设计的“蜂群思维”多智能体协调系统。该系统包含7个具有特定角色的智能体，它们通过消息总线通信，并使用SQLite进行持久化记忆共享，展示了复杂多智能体工作流的实现方案。