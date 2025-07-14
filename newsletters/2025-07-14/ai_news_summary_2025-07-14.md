## AINews - 2025-07-14

> [原文链接](https://news.smol.ai/issues/25-07-11-kimi-k2/)

## 📰 十大AI新闻要点

### 1. [Kimi K2 1T参数开源模型发布](https://twitter.com/Kimi_Moonshot/status/1943687599727763835)
> 中国AI实验室Moonshot AI发布1万亿参数的Kimi K2模型，采用MIT许可证开源，在多项基准测试中超越DeepSeek V3和GPT-4.1。该模型采用混合专家架构(MoE)，每次推理激活320亿参数，训练使用了15.5万亿token。

---

### 2. [MuonClip优化器创下ML史上最美loss曲线](https://x.com/yuchenj_uw/status/1943721656276726142)
> Moonshot AI团队提出的MuonClip优化器在训练Kimi K2时展现出惊人的稳定性，被研究者誉为"机器学习史上最美的loss曲线"，可能标志着长期主导的AdamW优化器迎来了真正的挑战者。

---

### 3. [xAI发布Grok-4模型](https://twitter.com/perplexity_ai/status/1943437826307297480)
> xAI宣布Grok-4现已面向Perplexity Pro和Max订阅用户开放，号称是"审查最少的尖端模型"，但在处理争议话题时被发现会优先引用Elon Musk的推文作为参考来源。

---

### 4. [Windsurf团队加入Google DeepMind](https://www.theverge.com/openai/705999/google-windsurf-ceo-openai)
> 原计划被OpenAI收购的AI编程初创公司Windsurf交易终止，其CEO、联合创始人和多名团队成员转而加入Google DeepMind，将专注于Gemini中的代理编程功能开发。

---

### 5. [IBM Granite 4.0支持并入llama.cpp](https://github.com/ggml-org/llama.cpp/pull/13550)
> IBM Granite 4.0 LLM系列(混合Mamba-2/Transformer架构)的支持已合并到llama.cpp中，引入了细粒度混合专家模型，结合了Mamba效率和Transformer注意力机制。

---

### 6. [Google发布MedGemma 27B等多款医疗AI模型](https://i.redd.it/r2bp20do39cf1.jpeg)
> Google开源发布了MedGemma 27B多模态模型、MedSigLIP和T5Gemma三款主要医疗AI模型，专注于放射学报告生成、临床推理和EHR摘要等复杂医疗任务。

---

### 7. [NVIDIA市值突破4万亿美元](https://twitter.com/SchmidhuberAI/status/1943671639620645140)
> NVIDIA成为首家市值达到4万亿美元的上市公司，反映出AI计算需求的爆炸式增长，相比1990年代计算成本已降低10万倍。

---

### 8. [微软研究揭示AI实际影响的职业](https://arxiv.org/abs/2507.07935)
> 微软基于20万次Bing Copilot对话的研究显示，AI对创意写作、编程和数据分析等领域的职业影响最为显著，但同时也创造了新的工作机会和技能需求。

---

### 9. [Perplexity推出Comet AI浏览器](https://twitter.com/AravSrinivas/status/1943508746115928315)
> Perplexity发布AI原生浏览器Comet，主打"氛围浏览"、语音命令标签管理等生产力功能，相比Chrome显著降低内存消耗，获得早期用户积极反馈。

---

### 10. [Andrew Ng呼吁暂停美国州级AI监管](https://twitter.com/AndrewYNg/status/1943710282513981881)
> AI专家Andrew Ng发表详细推文，主张暂停美国州级AI监管，认为在技术尚未被充分理解时通过的法律可能具有反竞争性，阻碍开源发展且无法提供真正的安全性。

---

## 🛠️ 十大工具产品要点

### 1. [Kimi K2模型技术细节](https://huggingface.co/moonshotai/Kimi-K2-Instruct)
> 1万亿参数MoE模型，384个专家，基于DeepSeek V3架构，在SWE-Bench上达到65.8%的准确率，采用修改版MIT许可证，要求高用量商业产品(1亿MAU或2000万美元/月收入)显示"Kimi K2"品牌。

---

### 2. [MuonClip优化器](https://x.com/yuchenj_uw/status/1943721656276726142)
> Moonshot AI开发的新型优化器，在训练1T参数模型时展现出前所未有的稳定性，loss曲线被研究者广泛称赞，可能成为下一代大规模模型训练的标准优化器。

---

### 3. [vLLM和Hugging Face支持Kimi K2](https://twitter.com/ClementDelangue/status/1943793114524549380)
> Kimi K2模型已获得vLLM支持，并可通过Hugging Face进行推理，为开发者提供了便捷的部署选项。

---

### 4. [IBM Granite 4.0技术规格](https://huggingface.co/ibm-granite/granite-4.0-tiny-preview)
> 混合Mamba-2/Transformer架构，7B总参数，1B活跃参数，62个专家，每次推理激活6个专家，支持128k上下文窗口。

---

### 5. [Google Veo 3图像转视频功能](https://twitter.com/Google/status/1943738854290125247)
> 现已在Gemini App中向AI Ultra和Pro订阅用户开放，可将照片转换为带声音的8秒视频。

---

### 6. [微软Phi-4-mini-flash-reasoning](https://twitter.com/ClementDelangue/status/1943487803658002720)
> 基于Phi-4-mini架构的轻量级开源模型，在Hugging Face发布，具有增强的推理能力。

---

### 7. [QuACK GPU内核优化库](https://twitter.com/tedzadouri/status/1943522327448195226)
> 新推出的库可使用CuTe-DSL直接在Python中生成高性能GPU内核，在H100上实现峰值内存吞吐量。

---

### 8. [Kontext Komposer图像处理工具](https://x.com/bfl_ml/status/1943635700227739891)
> Black Forest Labs推出的工具，支持场景变换、重新打光等图像转换功能，无需手动文本提示。

---

### 9. [Hugging Face Reachy Mini机器人](https://twitter.com/cognitivecompai/status/1943664752443474046)
> Hugging Face与Pollen Robotics合作推出的开源机器人，专注于人机交互和AI实验，预售额已接近50万美元。

---

### 10. [Perplexity Comet浏览器功能](https://twitter.com/AravSrinivas/status/1943754539322290192)
> AI原生浏览器，支持"氛围浏览"、语音命令标签管理，内存消耗显著低于Chrome，专注于提升生产力。

---