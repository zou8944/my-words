## AINews - 2025-09-20

> [原文链接](https://news.smol.ai/issues/25-09-18-nvidia-intc/)

## 📰 十大AI新闻要点

### 1. [NVIDIA与Intel达成50亿美元战略合作，共同开发x86+RTX芯片](https://www.tomshardware.com/pc-components/cpus/nvidia-and-intel-announce-jointly-developed-intel-x86-rtx-socs-for-pcs-with-nvidia-graphics-also-custom-nvidia-data-center-x86-processors-nvidia-buys-usd5-billion-in-intel-stock-in-seismic-deal)
> NVIDIA投资50亿美元收购Intel股份，双方将联合开发多代x86产品，包括PC端的Intel x86 RTX SoC（采用NVLink实现统一内存访问）和数据中心定制处理器。这标志着长期竞争对手的首次深度合作，对全球技术格局产生深远影响。

---

### 2. [Meta神经腕带+Ray-Ban显示设备现场演示故障引发行业讨论](https://twitter.com/nearcyan/status/1968468841786126476)
> Meta在发布会上演示神经腕带和Ray-Ban显示设备时出现约1分钟故障，引发对硬科技现场演示的讨论。部分观点认为失败的真实演示优于预录视频，同时披露Meta正从Unity转向自研"Horizon Engine"以更好地集成AI渲染技术。

---

### 3. [Mistral发布多模态模型Magistral 1.2系列](https://twitter.com/MistralAI/status/1968670593412190381)
> Magistral 1.2 Small/Medium版本新增视觉编码器，在AIME24/25和LiveCodeBench v5/v6上提升15%，改进了工具使用、语气和格式化能力。Medium版本量化后仍可在32GB MacBook或单张4090上运行。

---

### 4. [Google DeepMind发现流体动力学新解](https://deepmind.google/discover/blog/discovering-new-solutions-to-century-old-problems-in-fluid-dynamics/)
> 使用物理信息神经网络(PINNs)发现了欧拉方程、纳维-斯托克斯方程等多个流体PDE中以前未知的不稳定奇点解，误差达到近机器精度，为纳维-斯托克斯存在性与光滑性问题提供了计算机辅助证明的新途径。

---

### 5. [Anthropic发布Claude生产问题详细事后分析](https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues)
> Anthropic详细披露了影响Claude/Claude Code的三个生产事件的根本原因分析，包括路由错误、TPU配置错误和编译器问题，并实施了更严格的测试、回滚机制和监控改进。

---

### 6. [OpenAI在ICPC世界总决赛中解决12/12问题](https://twitter.com/sama/status/1968474300026859561)
> OpenAI在编程竞赛中完美解决所有12个问题，Google DeepMind以10/12的成绩排名第二（仅次于OpenAI和一支人类队伍），展示了AI在竞争性编程中的强大能力。

---

### 7. [Luma推出首个"推理视频模型"Ray3](https://twitter.com/LumaLabsAI/status/1968684330034606372)
> Ray3号称是首个具备推理能力的视频模型，支持工作室级HDR和草稿模式快速迭代，现已集成到Dream Machine中，代表视频生成技术的重要进步。

---

### 8. [DeepSeek-R1登上《自然》杂志封面](https://twitter.com/vllm_project/status/1968506474709270844)
> DeepSeek-R1强调纯强化学习的推理能力（无监督微调/思维链），完整公开算法细节和超参数，训练成本透明度高（约29.4万美元），获得学术界广泛关注。

---

### 9. [IBM开源Granite-Docling-258M文档VLM](https://twitter.com/rohanpaul_ai/status/1968561354987442246)
> 这款258M参数的文档视觉语言模型专为PDF到HTML/Markdown的布局保真转换而设计，支持公式、表格和代码块，采用SigLIP2视觉编码器和Granite语言模型架构。

---

### 10. [计算即教师(CaT-RL)新方法实现无标注监督](https://twitter.com/iScienceLuvr/status/1968599654507102491)
> 通过滚动组和冻结锚点将推理时计算转化为无参考监督，在MATH-500上提升33%，HealthBench上提升30%，无需人类标注即可提升模型性能。

---

## 🛠️ 十大工具产品要点

### 1. [SongBloom本地音乐生成模型发布](https://huggingface.co/fredconex/SongBloom-Safetensors)
> 本地Suno-like音乐生成器，提供safetensors检查点和ComfyUI节点，约20亿参数，支持12GB VRAM显卡运行，虽然质量不及Suno但代表了本地音乐生成的重要进展。

---

### 2. [DecartAI开源Lucy Edit视频编辑基础模型](https://twitter.com/DecartAI/status/1968769793567207528)
> 文本引导视频编辑的基础模型，支持Hugging Face、FAL和ComfyUI集成，发布一小时内就被集成到anycoder中，展示了快速生态整合能力。

---

### 3. [Hyperscape Capture实现5分钟高斯溅射扫描](https://twitter.com/JonathonLuiten/status/1968474776793403734)
> Quest原生高斯溅射捕获工具，可在约5分钟内扫描"超景观"，为VR内容创作提供了高效的3D场景捕获解决方案。

---

### 4. [Together推出Instant Clusters应对流量峰值](https://twitter.com/togethercompute/status/1968661658617692379)
> 提供HGX H100推理服务，价格低至2.39美元/GPU小时，为应对突发流量需求提供了弹性计算解决方案。

---

### 5. [Hugging Face仓库页面显示总文件大小](https://twitter.com/mishig25/status/1968598133543256151)
> 在Files标签页中显示仓库总大小，方便用户规划下载和部署，提升了开发者体验。

---

### 6. [OpenRouter推出Responses API Alpha](https://openrouter.ai/docs/api-reference/responses-api-alpha/overview)
> 无状态、drop-in兼容的API解决方案，提供10美元信用给前50位反馈用户，但工具调用功能目前存在兼容性问题。

---

### 7. [Weaviate查询代理正式发布](https://twitter.com/bobvanluijt/status/1968609785416196347)
> 可将多源健康数据转化为自然语言查询，案例显示用户参与度提升3倍，分析时间减少60%，具备源引用功能。

---

### 8. [tldraw发布画布代理入门套件](https://twitter.com/tldraw/status/1968655029247648229)
> 提供白板代理功能和代码示例，为开发者构建基于画布的AI应用提供了完整工具链。

---

### 9. [Perplexity推出Enterprise Max版本](https://twitter.com/perplexity_ai/status/1968707003175641098)
> 提供无限Labs使用、10倍文件上传、增强安全性和Comet Max助手，面向企业用户的高端服务方案。

---

### 10. [Chrome集成Gemini AI功能](https://twitter.com/Google/status/1968725752125247780)
> 地址栏直接启动AI模式，提供安全升级等Gemini驱动的功能，代表了浏览器AI集成的重要进展。

---