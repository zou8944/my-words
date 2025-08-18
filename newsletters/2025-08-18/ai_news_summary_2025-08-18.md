## AINews - 2025-08-18

> [原文链接](https://news.smol.ai/issues/25-08-15-not-much/)

## 📰 十大AI新闻要点  

### 1. [GPT-5 成为 ChatGPT 默认模型，新增 Auto/Fast/Thinking 模式](https://twitter.com/OpenAI/status/1956212769365352758)  
> OpenAI 宣布 GPT-5 成为 ChatGPT 默认模型，提供 Auto/Fast/Thinking 三种模式。Plus/Team 用户每周可使用 3000 条 GPT-5 Thinking 消息，企业/教育用户已开放访问。  

---

### 2. [GPT-5 推出更友好的默认人格](https://twitter.com/OpenAI/status/1956461718097494196)  
> OpenAI 推出更“温暖”的 GPT-5 人格，声称不会增加谄媚性（sycophancy），用户仍可通过 Custom Instructions 自定义风格。  

---

### 3. [LMSYS 竞技场排名：GPT-5 表现参差](https://twitter.com/lmarena_ai/status/1956399522688692608)  
> GPT-5 默认版本（gpt-5-chat）排名第5，小型变体（mini/nano）表现较弱，而 GPT-5-High 仍居榜首。部分评测指出其在编码任务上逊于中文模型。  

---

### 4. [Google Imagen 4 正式发布，支持 2K 分辨率](https://twitter.com/_philschmid/status/1956351654753673252)  
> Imagen 4 提供 Ultra/Standard/Fast 三档定价（$0.06-$0.02/图），生成速度比前代快 10 倍，开发者已分享 JSON 提示模板优化产品图生成。  

---

### 5. [Gemma 3 270M 超小型开源模型发布](https://twitter.com/GoogleDeepMind/status/1956393664248271082)  
> 参数分配独特（170M 嵌入层 + 100M Transformer），支持 Transformers/JS 等生态，在 iPad Air M3 上达 200 token/s，但存在重复问题争议。  

---

### 6. [XLANG 发布 OpenCUA 开源计算机操作智能体框架](https://twitter.com/xywang626/status/1956400403911962757)  
> 包含 7B/32B 模型和 22.6K 轨迹数据集，32B 版本在 OSWorld 基准上达 34.8%，宣称媲美闭源方案。  

---

### 7. [NVIDIA 开源 Granary 多语言语音数据集](https://twitter.com/Tu7uruu/status/1956350036343701583)  
> 包含 Canary-1b-v2（25 种语言 ASR+翻译）和 Parakeet-tdt-0.6b-v3 SOTA 多语言语音识别模型。  

---

### 8. [Alibaba Ovis2.5 多模态模型刷新 OpenCompass 纪录](https://twitter.com/gm8xx8/status/1956292512030638235)  
> 9B 版本在 OpenCompass 达 78.3 分（<40B 模型 SOTA），支持视频/多图像理解和文档 OCR。  

---

### 9. [HRM 架构被质疑：数据/流程比模型设计更重要](https://twitter.com/arcprize/status/1956431617951740044)  
> ARC Prize 团队复现 HRM 的 ARC-AGI-1 高分，发现其核心优势来自外部精炼循环（refinement loop），而非模型架构本身。  

---

### 10. [Epoch：前沿模型性能 9 个月后可达消费级硬件](https://twitter.com/EpochAIResearch/status/1956468453399044375)  
> 预测开源模型可能在 2026 Q2 追上 Grok 4 水平，引发对能力扩散与安全政策的讨论。  

---

## 🛠️ 十大工具产品要点  

### 1. [OpenAI 开发者面板新增 Quick Eval 功能](https://twitter.com/OpenAIDevs/status/1956410610914414904)  
> 支持对比 GPT-5 变体性能，内置评分器可评估模型响应与用户答案的匹配度。  

---

### 2. [OpenAI 发布《GPT-5 编码六技巧》PDF](https://twitter.com/OpenAIDevs/status/1956439005970801099)  
> 提供优化提示、版本控制等建议，同步上线整合版开发者门户（[developers.openai.com](http://developers.openai.com/)）。  

---

### 3. [Cursor CLI 新增 MCP 工具和 Review Mode](https://twitter.com/cursor_ai/status/1956458242655281339)  
> 支持多文件引用（@-file）和代码压缩，强化工具增强编程体验。  

---

### 4. [Guardrails Snowglobe 模拟百种人格对话测试智能体](https://twitter.com/godofprompt/status/1956359876109652297)  
> 通过故意触发失败生成训练信号，适用于长周期工作流加固。  

---

### 5. [ClipTagger-12B 开源视频标注模型](https://huggingface.co/inference-net/ClipTagger-12b)  
> 基于 Gemma-12B，评测分数超 Claude 4 Sonnet（3.53 vs 3.16），成本低 17 倍（$335/百万帧）。  

---

### 6. [Meta 发布 DINOv3 视觉模型](https://ai.meta.com/dinov3/)  
> 7B 参数 ViT 模型，仅用无标签图像训练，在分割/深度估计等任务达 SOTA，引入 Gram Anchoring 防特征退化。  

---

### 7. [Windsurf Wave 12 IDE 更新](https://windsurf.com/changelog)  
> 新增 DeepWiki 悬停解释、Vibe & Replace 批量编辑、Dev Containers 支持，优化智能体 Cascade 的持续规划能力。  

---

### 8. [MLX Knife 本地 OpenAI 兼容服务器](https://github.com/mzau/mlx-knife)  
> 支持 pip 安装，为 Apple Silicon 提供快速本地模型测试环境。  

---

### 9. [Nous Research 推出推理效率基准](https://nousresearch.com/measuring-thinking-efficiency-in-reasoning-models-the-missing-benchmark/)  
> 显示开源模型token消耗达闭源模型的1.5-4倍，呼吁将效率纳入生产级评估指标。  

---

### 10. [1.58 比特稀疏训练论文](https://arxiv.org/html/2411.06360v3)  
> 提出 α,1-稀疏方法，在超低位宽下实现近无损训练与推理，有望降低部署成本。  

---