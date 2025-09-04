## AINews - 2025-09-04

> [原文链接](https://news.smol.ai/issues/25-09-02-anthropic-f/)

## 📰 十大AI新闻要点

### 1. [Anthropic完成130亿美元F轮融资，估值达1830亿美元](https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation)
> Anthropic宣布完成130亿美元F轮融资，投后估值达1830亿美元，由ICONIQ Capital领投。公司收入从2025年1月的约10亿美元年化运行率增长至8月的50亿美元，Claude Code在三个月内使用量增长10倍，现已达到5亿美元年化收入，服务超过30万企业客户。

---

### 2. [Mistral Le Chat新增20+ MCP连接器和记忆功能](https://twitter.com/MistralAI/status/1962881084183527932)
> Mistral Le Chat新增20多个MCP连接器，支持Stripe、GitHub、Atlassian、Linear、Notion、Snowflake等企业服务，具备细粒度访问控制和用户可编辑的持久记忆功能，成为跨SaaS操作和检索的统一界面。

---

### 3. [Artificial Analysis发布智能指数V3，包含代理基准测试](https://twitter.com/ArtificialAnlys/status/1962881314925023355)
> Artificial Analysis更新智能指数至V3版本，新增Terminal-Bench Hard和τ²-Bench（电信领域）基准测试。GPT-5领先，o3紧随其后，xAI的Grok Code Fast 1/Grok 4和Claude/Kimi/gpt-oss系列在工具调用/代理任务中表现良好。

---

### 4. [Salesforce发布MCP-Universe代理评估框架](https://twitter.com/_philschmid/status/1962935890415599650)
> Salesforce推出MCP-Universe评估框架，使用真实MCP服务器（Google Maps、GitHub、Yahoo Finance等）在231个实际任务中评估代理性能，顶级模型成功率达43.7%，性能高度依赖领域，工具过多可能降低效果。

---

### 5. [Zhipu/THUDM开源Slime v0.1.0强化学习基础设施](https://twitter.com/ZhihuFrontier/status/1962751555591086226)
> 智谱AI和THUDM开源Slime v0.1.0，这是GLM-4.5背后的RL基础设施，支持FP8 rollout、DeepEP、多令牌预测、推测解码等功能，使GLM-4.5解码速度从<10 token/秒提升至60-70 token/秒。

---

### 6. [微软发布rStar2-Agent模型，数学和工具性能达前沿水平](https://twitter.com/iScienceLuvr/status/1962798181059817480)
> 微软发布14B参数的rStar2-Agent模型，使用GRPO-RoC和多阶段SFT→RL训练方法，在64台MI300X上训练510步，AIME24得分80.6%，AIME25得分69.8%，超越DeepSeek-R1（671B）。

---

### 7. [Nous Research发布Hermes 4开源推理模型](https://twitter.com/gm8xx8/status/1962943078702186627)
> Nous Research发布Hermes 4开源推理模型，基于Llama-3.1的70B/405B参数版本，支持混合显式思维、仅助手损失、长轨迹（最高16k）、工具感知格式化，在数学/代码/对齐方面表现强劲。

---

### 8. [Hugging Face发布Jupyter Agent数据集](https://twitter.com/a_yukh/status/1962911097452683710)
> Hugging Face发布Jupyter Agent数据集，包含来自51k个Kaggle笔记本的20亿令牌和7TB数据集，带有真实代码执行轨迹（Qwen3-Coder + E2B），显著提升代码执行和数据分析能力。

---

### 9. [LangChain/LangGraph发布1.0 alpha版本](https://twitter.com/LangChainAI/status/1962934869065191457)
> LangChain和LangGraph发布1.0 alpha版本，LangGraph作为底层代理编排基础，LangChain 1.0围绕中心代理抽象和标准化内容块重构，保持模型/供应商可移植性。

---

### 10. [OpenAI收购Statsig并任命新CTO](https://twitter.com/OpenAI/status/1962943308935864793)
> OpenAI宣布收购Statsig，创始人Vijaye Raji成为应用CTO（负责ChatGPT/Codex）。同时推出"OpenAI for Science"计划，构建AI驱动的科学仪器，实时API持续成熟。

---

## 🛠️ 十大工具产品要点

### 1. [Anthropic API新增bash和文件操作原语](https://twitter.com/alexalbert__/status/1962912152555225296)
> Anthropic API新增bash支持、视图/创建/字符串替换原语、Seaborn/OpenCV集成，容器生命周期延长至30天，减少令牌使用并支持更丰富的工作流程。

---

### 2. [ZeroGPU AoT编译提升推理性能](https://twitter.com/RisingSayak/status/1962844485118996545)
> Hugging Face Spaces的ZeroGPU支持提前编译模型，减少冷启动时间并提升吞吐量，报告显示FLUX/Wan模型性能提升1.3-1.8倍，已集成到anycoder演示中。

---

### 3. [Qdrant新增搜索后相关性重评分功能](https://twitter.com/qdrant_engine/status/1962876567362617445)
> Qdrant新增搜索后相关性重评分功能，支持新鲜度、接近度、衰减函数等业务逻辑对齐，提升检索结果与业务需求匹配度。

---

### 4. [ChromaSwift为iOS带来本地检索功能](https://twitter.com/trychroma/status/1962917927382122857)
> ChromaSwift（beta）为iOS设备提供本地检索功能，支持设备端MLX嵌入和持久化，实现离线向量搜索和检索体验。

---

### 5. [OpenPipe发布深度研究代理训练方案](https://twitter.com/corbtt/status/1962954306078048297)
> OpenPipe发布通过RL训练深度研究代理的配方，在H200上约30小时（成本约350美元）即可训练出在DeepResearch Bench上超越Sonnet-4的代理模型。

---

### 6. [Galileo发布代理评估工具](https://twitter.com/omarsar0/status/1962880974104014948)
> Galileo推出代理评估工具（实时护栏、Luna-2），针对生产可靠性和成本优化，Gartner预测到2027年40%的项目将因可靠性问题失败。

---

### 7. [xpander代理后端支持自托管](https://twitter.com/_avichawla/status/1962764993587564861)
> xpander代理后端提供内存、工具、状态、护栏等完整功能，支持自托管部署，为企业提供可控制的代理基础设施。

---

### 8. [自适应LLM路由框架优化成本质量比](https://twitter.com/omarsar0/status/1962875108512411938)
> 自适应LLM路由框架将路由器设计为上下文bandit问题，在预算约束下优化质量成本比，支持用户预算策略。

---

### 9. [Google Gemini新增URL上下文处理功能](https://twitter.com/LiorOnAI/status/1962894029152047590)
> Google Gemini新增URL上下文功能，可内联获取和处理最多20个URL，无需额外工具费用，提升多源信息处理能力。

---

### 10. [Chainlit提供快速LLM聊天UI脚手架](https://twitter.com/rasbt/status/1962695306757185647)
> Chainlit继续保持快速LLM聊天UI脚手架定位，为开发者提供简洁的聊天界面构建工具，支持快速原型开发。

---