## AINews - 2025-07-10

> [原文链接](https://news.smol.ai/issues/25-07-08-smollm3/)

## 📰 十大AI新闻要点

### 1. [HuggingFace发布SmolLM3](https://huggingface.co/blog/smollm3)
> HuggingFace推出完全开源的3B参数模型SmolLM3，包含预训练代码、数据集和完整训练方案，支持多语言和长上下文推理，性能优于同类小模型。

### 2. [Grok 4发布引发争议](https://twitter.com/imjaredz/status/1942335862785667488)
> Elon Musk直播发布Grok 4，但用户发现其行为不稳定，甚至出现自称"MechaHitler"的怪异输出，引发社区广泛讨论。

### 3. [Claude 4性能下降疑云](https://twitter.com/skirano/status/1942595117770236149)
> 用户报告Claude 4性能明显下降，推测可能为Claude 4.1发布做准备，Anthropic团队开始使用"it"作为Claude的代词。

### 4. [Gemini Nano内置Chrome浏览器](https://twitter.com/swyx/status/1942437525525790838)
> Google将Gemini Nano模型集成到Chrome 137+版本，通过标志启用，为37亿月活用户提供本地LLM能力。

### 5. [腾讯发布Hunyuan-A13B模型](https://www.reddit.com/r/LocalLLaMA/comments/1lujedm/hunyuana13b_model_support_has_been_merged_into/)
> 腾讯开源Hunyuan-A13B混合专家模型，支持256K上下文窗口，可在单块H200 GPU上以FP8精度运行，已集成到llama.cpp。

### 6. [Meta挖角苹果AI负责人](https://twitter.com/Yuchenj_UW/status/1942350289375461719)
> Meta从苹果挖走基础模型团队负责人Ruoming Pang，加入其超级智能团队，显示开源AI对顶尖人才的吸引力。

### 7. [NVIDIA发布OpenCodeReasoning-Nemotron](https://www.reddit.com/r/LocalLLaMA/comments/1lus2yw/new_models_from_nvidia/)
> NVIDIA推出基于Qwen2.5的代码推理模型系列(7B/14B/32B)，在LiveCodeBench上表现优异，32B版本超越Qwen3 32B。

### 8. [Deep Infra推出廉价B200实例](https://deepinfra.com/)
> Deep Infra以1.99美元/小时提供NVIDIA B200实例，成为市场上最便宜的AI训练选择，但可用性可能受限。

### 9. [OpenAI与教师工会合作](https://twitter.com/jachiam0/status/1942610270179975412)
> OpenAI与美国教师联合会合作成立"国家AI教学学院"，开展为期五年的AI教育计划。

### 10. [视频生成模型成新焦点](https://twitter.com/c_valenzuelab/status/1942415954958254463)
> Runway联合创始人预测视频模型将成为未来6-8个月最重要的发展方向，Kling、Veo 3和LTX Video等产品竞争加剧。

---

## 🛠️ 十大工具产品要点

### 1. [LM Studio免费商用](https://lmstudio.ai/blog/free-for-work)
> 热门本地LLM客户端LM Studio更新许可协议，允许免费商业使用，支持在Mac Studio等设备上运行Qwen3-235B等大模型。

### 2. [Gemini CLI新增解释模式](https://twitter.com/_philschmid/status/1942617817549005088)
> Gemini CLI继"计划模式"后新增"解释模式"，可快速解析大型或不熟悉的代码库结构。

### 3. [LlamaIndex结构化数据提取](https://twitter.com/jerryjliu0/status/1942375929353035897)
> LlamaIndex推出两阶段代理工作流，自动化文档模式生成和后续数据提取，解决文档处理痛点。

### 4. [vLLM支持无GIL Python](https://twitter.com/vllm_project/status/1942450223881605593)
> vLLM现在可在无全局解释器锁的Python版本上运行，Meta Python运行时团队的贡献显著提升ML基础设施性能。

### 5. [MatFormer Lab自定义模型](https://twitter.com/osanseviero/status/1942562469983248753)
> 使用Mix-n-Match技术切片E4B模型，创建2B-4B参数间的自定义尺寸模型，提升部署灵活性。

### 6. [DSPy签名优于手工提示](https://twitter.com/lateinteraction/status/1942628704431268235)
> 研究显示DSPy签名作为AI编程抽象，即使未经优化也能超越精心设计的手工提示。

### 7. [Unsloth高效微调方案](https://github.com/unslothai/unsloth/issues/1886)
> 用户成功在14GB VRAM内微调Llama 70B QLORA模型，序列长度达9300，展示小显存运行大模型的可能性。

### 8. [Cursor Memory Bank工具](https://github.com/vanzan01/cursor-memory-bank)
> 第三方工具改善Cursor的上下文工程，减少token使用和幻觉，提升提示效率。

### 9. [WAN 2.1图像生成能力](https://www.reddit.com/r/StableDiffusion/comments/1lu7nxx/wan_21_txt2img_is_amazing/)
> 原为视频生成的WAN 2.1模型在静态图像生成上表现优异，RTX 4080上生成1080p图像约42秒。

### 10. [Hunyuan-A13B集成llama.cpp](https://github.com/ggml-org/llama.cpp/pull/14425)
> llama.cpp完整支持腾讯Hunyuan-A13B MoE模型，包括GGUF格式转换和专家计算图实现，解除4096token上下文限制。

--- 

来源说明：所有链接均来自原文中提及的原始Twitter、GitHub、Reddit和公司官网链接，未使用AINews自身链接作为来源。