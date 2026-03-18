## Reddit ML - 2026-03-18


### 1. [[R] Kimi团队提出注意力残差机制](https://www.reddit.com/r/MachineLearning/comments/1rw1eag/r_attention_residuals_by_kimi_team/)
> 提出注意力残差（AttnRes）替代标准残差连接，通过注意力机制让各层选择性地聚合前层输出，解决深度模型中的隐藏状态稀释问题，提升模型性能。

<sub>作者: /u/Nunki08 | 发布于: 2026-03-17 09:05</sub>

---

### 2. [[P] mlx-tune – 在 Apple Silicon 上用 MLX 微调大语言模型（支持 SFT、DPO、GRPO、VLM）](https://www.reddit.com/r/MachineLearning/comments/1rw58ku/p_mlxtune_finetune_llms_on_apple_silicon_with_mlx/)
> mlx-tune是一个Python库，可在Apple Silicon上使用MLX框架微调大语言模型，支持多种训练方法，并兼容Mac和CUDA。

<sub>作者: /u/A-Rahim | 发布于: 2026-03-17 12:33</sub>

---

### 3. [[N] openreview 个人资料出故障了？？](https://www.reddit.com/r/MachineLearning/comments/1rvy3m4/n_openreview_profile_glitch/)
> 用户发现OpenReview个人资料信息显示异常，其同事也遇到相同问题。

<sub>作者: /u/i_minus | 发布于: 2026-03-17 05:39</sub>

---

### 4. [【研究】基因组大语言模型](https://www.reddit.com/r/MachineLearning/comments/1rvu5df/r_genomic_large_language_models/)
> 研究探索基因组大模型Evo2，发现其能识别序列相似性工具无法检测的基因调控模式，例如两个序列不同但功能相关的基因启动子区域。

<sub>作者: /u/Clear-Dimension-6890 | 发布于: 2026-03-17 02:20</sub>

---

### 5. [[论文] 权重范数裁剪将顿悟速度提升18-66倍 | 300次随机种子实验零失败 | 论文PDF已开源](https://www.reddit.com/r/MachineLearning/comments/1rwl1sq/p_weight_norm_clipping_accelerates_grokking_1866/)
> 研究发现权重范数裁剪技术能显著加速模型“顿悟”过程，在标准测试中最高提速66倍，且代码仅需5行。

<sub>作者: /u/niftylius | 发布于: 2026-03-17 22:05</sub>

---

### 6. [[D] 发布专业级MQM标注机器翻译数据集（16种语言对，48位标注员）](https://www.reddit.com/r/MachineLearning/comments/1rw3a3j/d_releasing_a_professional_mqmannotated_mt/)
> 开源了一个专业翻译质量评估数据集，包含362个翻译片段、16种语言对，由48位专业语言学家标注，遵循WMT标准。

<sub>作者: /u/ritis88 | 发布于: 2026-03-17 10:56</sub>

---

### 7. [[项目] 为自动研究构建置信度评分系统，因为无法复现的保留比丢弃更糟糕](https://www.reddit.com/r/MachineLearning/comments/1rw96pw/p_built_confidence_scoring_for_autoresearch/)
> 作者为解决自动研究中“保留”结果不可靠的问题，开发了三个工具：autojudge评估置信度，autosteer指导实验方向，autoevolve进行多智能体竞争优化。

<sub>作者: /u/dean0x | 发布于: 2026-03-17 15:08</sub>

---

### 8. [[P] 可视化Transformer中的词元级活动](https://www.reddit.com/r/MachineLearning/comments/1rwelsk/p_visualizing_tokenlevel_activity_in_a_transformer/)
> 作者尝试用3D动画可视化LLM推理过程，以节点代表不同组件，动态展示令牌生成路径，旨在让过程更直观，但不确定其准确性与实用性。

<sub>作者: /u/ABHISHEK7846 | 发布于: 2026-03-17 18:17</sub>

---

### 9. [CVPR研讨会投稿编号问题](https://www.reddit.com/r/MachineLearning/comments/1rwgcql/d_submission_id_in_cvpr_workshops/)
> 作者首次向CVPR研讨会投稿，不确定是否必须在官方模板的“Submission ID”栏填写OpenReview上的研讨会投稿编号，担心不填可能导致直接拒稿，而研讨会指南未明确说明。

<sub>作者: /u/OkPack4897 | 发布于: 2026-03-17 19:17</sub>

---

### 10. [【研究】当前视频基准测试中缺少哪些视觉语言模型？](https://www.reddit.com/r/MachineLearning/comments/1rvxztn/r_what_kind_on_video_benchmark_is_missing_vlms/)
> 用户探讨现有视频语言模型评测基准的不足，并寻求创建更贴近物理开放世界数据集的建议。

<sub>作者: /u/Alternative_Art2984 | 发布于: 2026-03-17 05:33</sub>

---

### 11. [[项目] 我开发了一款可视化拖拽式机器学习训练器（无需编程）。免费开源。](https://www.reddit.com/r/MachineLearning/comments/1rwm05e/p_i_built_a_visual_draganddrop_ml_trainer_no_code/)
> MLForge是一款免费开源的拖拽式机器学习训练工具，无需代码即可构建数据预处理、模型和训练流程，支持自动计算参数和导出PyTorch代码。

<sub>作者: /u/Mental-Climate5798 | 发布于: 2026-03-17 22:41</sub>

---

### 12. [[R] 我们测试了LLM对积极结果与零结果是否采用相同的证据标准：结果发现它们并没有。](https://www.reddit.com/r/MachineLearning/comments/1rwloyr/r_we_tested_whether_llms_apply_the_same/)
> 研究发现，GPT-4o等大模型在评估相同证据时，倾向于更相信阳性结果而非无效结果，存在“不对称证明负担”偏差。这可能加剧学术发表偏见。

<sub>作者: /u/galigirii | 发布于: 2026-03-17 22:29</sub>

---

### 13. [[R] 持久多智能体环境中的涌现AI社会（TerraLingua + 数据集 + 代码）](https://www.reddit.com/r/MachineLearning/comments/1rwdrs1/r_emergent_ai_societies_in_a_persistent/)
> 研究AI智能体在共享持久世界中的互动与演化。实验观察到它们自发形成规则、构建基础设施并积累知识，旨在探索开放式协调与文化涌现等现象。

<sub>作者: /u/GiuPaolo | 发布于: 2026-03-17 17:49</sub>

---
