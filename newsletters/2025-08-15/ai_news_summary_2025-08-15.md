## AINews - 2025-08-15

> [原文链接](https://news.smol.ai/issues/25-08-13-not-much/)

## 📰 十大AI新闻要点

### 1. [GPT-5新增Auto/Fast/Thinking模式](https://twitter.com/sama/status/1955438916645130740)
> OpenAI CEO Sam Altman宣布GPT-5新增三种模式：Auto(自动平衡速度/深度)、Fast(优先响应速度)和Thinking(深度思考模式，支持196k tokens上下文)。Plus用户每周可使用3000次Thinking模式，超出后自动降级到GPT-5 Thinking mini版本。

---

### 2. [OpenAI动态路由技术引发成本优化讨论](https://twitter.com/dylan522p/status/1955433082397589900)
> 多位观察者指出GPT-5发布的核心创新是其动态路由系统，该系统能将请求智能分配到成本更低的模型以降低计算开销。专家预测路由算法将快速优化，但需要可靠的信号来做出优质路由决策。

---

### 3. [Anthropic推出"Opus规划-Sonnet执行"编程模式](https://twitter.com/_catwu/status/1955694117264261609)
> Anthropic正式支持Claude Code中的模型配对功能，高阶规划由Opus 4.1处理，任务执行由Sonnet 4完成。同时Sonnet 4的API上下文窗口扩展至100万tokens。

---

### 4. [DSPy 3.0发布，引入GEPA优化技术](https://twitter.com/CShorten30/status/1955445406441033906)
> DSPy 3.0正式版发布，新增GRPO/RL训练、SIMBA和GEPA优化器。其中GEPA在提示优化方面表现优于强化学习，开发者已开始将其适配到Observable JS等环境。

---

### 5. [Qwen3-Coder发布并登顶开源模型榜](https://twitter.com/Alibaba_Qwen/status/1955436295603490864)
> 阿里云Qwen3-Coder模型发布，同时在LMArena八月文本竞技场中，Qwen-3-235b-a22b-instruct在开源模型中排名第一，GLM-4.5排名第四，OpenAI gpt-oss-120B排名第七。

---

### 6. [Perplexity推出Comet桌面应用和金融版印度扩展](https://twitter.com/perplexity_ai/status/1955684209483534657)
> Perplexity向美国Pro用户推出Comet桌面应用(Mac/Windows)，同时Perplexity Finance扩展至印度市场，新增BSE/NSE覆盖、实时财报和Excel下载功能。

---

### 7. [Runway Aleph实现视频精准区域编辑](https://twitter.com/runwayml/status/1955615613583519917)
> Runway的Aleph技术可通过单一提示完成视频中的精确区域编辑和重新纹理处理，将复杂的多步骤VFX工作简化为一步操作。

---

### 8. [GPT-OSS-120B成为首个适配H100原生精度的智能模型](https://www.reddit.com/r/LocalLLaMA/comments/1moz341/gptoss120b_most_intelligent_model_that_fits_on_an/)
> 社区评测显示gpt-oss-120B是首个能在H100 GPU上以原生精度运行的智能模型，在"人工分析智能指数"和推理时激活参数间取得良好平衡。

---

### 9. [MiniMax举办15万美元AI智能体黑客松](https://minimax-agent-hackathon.space.minimax.io/)
> MiniMax宣布举办总奖金15万美元的AI智能体挑战赛，参赛者可从头构建或改造现有项目，提交截止日期为8月25日。

---

### 10. [Humanloop团队加入Anthropic](https://twitter.com/humanloop/status/1955487624728318072)
> Humanloop团队宣布加入Anthropic，将加速企业安全采用AI技术。Humanloop此前专注于AI应用开发工具和平台。

---

## 🛠️ 十大工具产品要点

### 1. [GPT-OSS-20B基础模型提取](https://twitter.com/jxmnop/status/1955436067353502083)
> 社区从OpenAI的推理检查点提取出gpt-oss-20b-base模型，下一步将进行记忆化检查、指令微调，并尝试扩展到120B版本。

---

### 2. [Claude API新增1小时提示缓存](https://twitter.com/claude_code/status/1955475387858972986)
> Anthropic为Claude API新增1小时TTL的提示缓存功能，已正式发布，可显著降低重复提示的计算成本。

---

### 3. [Qwen Image编辑功能进入测试](https://twitter.com/Alibaba_Qwen/status/1955656822532329626)
> 阿里云Qwen Image在Qwen Chat上速度提升，同时图像编辑功能正在测试中，展示出强大的图像处理能力。

---

### 4. [qqWen开源金融编程语言训练套件](https://twitter.com/brendanh0gan/status/1955641113693561071)
> qqWen发布1.5B-32B参数的开源微调套件，包含预训练+SFT+RL全流程代码/权重/数据，专注于小众金融编程语言Q。

---

### 5. [LiveMCPBench工具使用基准测试](https://twitter.com/_philschmid/status/1955601309966447074)
> 新发布的LiveMCPBench评估了10个前沿模型在527个工具上的95项时效性任务，Claude Sonnet 4以78.95%成功率领先，主要失败模式是工具发现而非执行。

---

### 6. [LangChain发布深度智能体UI](https://twitter.com/LangChainAI/status/1955674201853247584)
> LangChain推出Deep Agents UI，支持TODO列表、文件系统和子智能体管理，为复杂智能体工作流提供可视化界面。

---

### 7. [vLLM分享CUDA核心转储调试指南](https://twitter.com/vllm_project/status/1955478388178817298)
> vLLM团队发布CUDA核心转储调试指南，推荐特定环境变量设置，帮助开发者解决GPU计算中的疑难问题。

---

### 8. [Jina实现GGUF嵌入优化](https://twitter.com/JinaAI_/status/1955647947359867068)
> Jina在L4 GPU上实现GGUF嵌入优化，使用IQ3_S量化、批次512和c=2048配置，达到约4,143 tok/s速度，仅需约2GB VRAM。

---

### 9. [Anycoder新增Mistral Medium 3.1支持](https://twitter.com/_akhaliq/status/1955621767302808012)
> Anycoder工具新增对Mistral Medium 3.1模型的支持，扩展了代码生成和分析能力。

---

### 10. [Hugging Face TRL支持VLM SFT](https://twitter.com/mervenoyann/status/1955622287920537636)
> Hugging Face TRL现在支持视觉语言模型监督微调(VLM SFT)、多模态GRPO和MPO，为多模态模型训练提供新工具。

---