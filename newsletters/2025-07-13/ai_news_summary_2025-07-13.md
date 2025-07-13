## AINews - 2025-07-13

> [原文链接](https://news.smol.ai/issues/25-07-11-kimi-k2/)

## 📰 十大AI新闻要点

### 1. [Moonshot AI发布1万亿参数开源模型Kimi K2](https://twitter.com/Kimi_Moonshot/status/1943687599727763835)
> 中国AI实验室Moonshot AI推出1万亿参数的Kimi K2模型，采用混合专家架构(MoE)，每次推理激活320亿参数，在多项基准测试中超越DeepSeek V3和GPT-4.1。该模型使用创新的MuonClip优化器，训练过程零不稳定，采用MIT许可证开源。

---

### 2. [xAI发布Grok-4模型](https://twitter.com/perplexity_ai/status/1943437826307297480)
> xAI宣布Grok-4正式上线，号称"审查最少的尖端模型"，在长上下文处理方面表现优异，但被发现会优先检索Elon Musk的推文来回答争议性话题，引发关于模型偏见的讨论。

---

### 3. [MuonClip优化器突破](https://twitter.com/yuchenj_uw/status/1943721656276726142)
> Moonshot AI团队开发的MuonClip优化器创造了"机器学习史上最漂亮的损失曲线"，有望取代长期主导的AdamW优化器，为大规模模型训练带来新突破。

---

### 4. [Windsurf团队加入Google DeepMind](https://www.theverge.com/openai/705999/google-windsurf-ceo-openai)
> 原计划被OpenAI收购的AI编程初创公司Windsurf交易终止，其CEO和核心团队转而加入Google DeepMind，将专注于Gemini的智能体编程能力开发。

---

### 5. [IBM Granite 4.0模型架构](https://github.com/ggml-org/llama.cpp/pull/13550)
> IBM推出Granite 4.0系列模型，采用Mamba-2/Transformer混合架构，支持精细混合专家模式(MoE)，已合并到llama.cpp项目，为本地推理带来新选择。

---

### 6. [Google发布医疗AI模型套件](https://twitter.com/Google/status/1943738854290125247)
> Google开源发布MedGemma 27B多模态模型、MedSigLIP和T5Gemma，专注于医疗影像分析、临床推理和电子健康记录处理，推动AI在医疗领域的应用。

---

### 7. [微软Phi-4-mini推理增强版](https://twitter.com/ClementDelangue/status/1943487803658002720)
> 微软在Hugging Face发布Phi-4-mini-flash-reasoning，基于Phi-4-mini架构的轻量级开源模型，特别增强了推理能力。

---

### 8. [Perplexity推出AI浏览器Comet](https://twitter.com/AravSrinivas/status/1943508746115928315)
> Perplexity发布AI原生浏览器Comet，支持"氛围浏览"、语音命令管理标签页等功能，内存消耗显著低于Chrome，专注于提升生产力体验。

---

### 9. [NVIDIA市值突破4万亿美元](https://twitter.com/SchmidhuberAI/status/1943671639620645140)
> NVIDIA成为首家市值达到4万亿美元的上市公司，反映出AI计算需求的爆炸式增长，相比1990年代计算成本已降低10万倍。

---

### 10. [Andrew Ng呼吁暂停州级AI监管](https://twitter.com/AndrewYNg/status/1943710282513981881)
> AI专家Andrew Ng发表长篇论述，呼吁暂停美国州级AI监管，认为在技术尚未完全理解前制定的法律可能反竞争并阻碍开源发展。

---

## 🛠️ 十大工具产品要点

### 1. [Kimi K2模型技术细节](https://huggingface.co/moonshotai/Kimi-K2-Instruct)
> 1万亿参数MoE架构，384个专家，基于DeepSeek V3架构，训练15.5万亿token，支持vLLM推理，在Hugging Face提供两种变体：基础版和研究版。

---

### 2. [MuonClip优化器特性](https://twitter.com/yuchenj_uw/status/1943721656276726142)
> 新型优化器实现前所未有的训练稳定性，特别适合超大规模模型训练，可能彻底改变深度学习优化领域。

---

### 3. [IBM Granite 4.0技术规格](https://huggingface.co/ibm-granite/granite-4.0-tiny-preview)
> 7B总参数，1B激活参数，62个专家，每次激活6个，128k上下文窗口，混合Mamba效率和Transformer注意力机制。

---

### 4. [Google Veo 3图像转视频](https://twitter.com/Google/status/1943738854290125247)
> Gemini App中新增功能，可将照片转换为8秒带声音视频，目前仅限AI Ultra和Pro订阅用户使用。

---

### 5. [QuACK GPU内核优化库](https://twitter.com/tedzadouri/status/1943522327448195226)
> 直接在Python中使用CuTe-DSL生成高性能GPU内核，在H100上实现峰值内存吞吐量。

---

### 6. [Kontext Komposer图像处理工具](https://x.com/bfl_ml/status/1943635700227739891)
> Black Forest Labs推出的自动化图像转换工具，支持场景变更、重新打光等复杂操作，无需手动编写提示词。

---

### 7. [Hugging Face机器人Reachy Mini](https://twitter.com/cognitivecompai/status/1943664752443474046)
> 开源的拟人化机器人平台，专为人机交互和AI实验设计，预售额已接近50万美元。

---

### 8. [MedSigLIP医疗图像嵌入模型](https://twitter.com/osanseviero/status/1943584472206549453)
> 轻量级(0.4B参数)模型，专注于医疗图像检索和分类，采用可扩展的视觉语言预训练方法。

---

### 9. [SYNTHETIC-2推理轨迹数据集](https://twitter.com/_lewtun/status/1943441695472832701)
> 包含400万条已验证推理轨迹的开放数据集，可用于训练和评估AI系统的推理能力。

---

### 10. [DSPy智能体开发框架](https://twitter.com/lateinteraction/status/1943408500874580252)
> 强调将工作委派给智能体而非微观管理的开发范式，简化复杂AI系统的构建流程。

---