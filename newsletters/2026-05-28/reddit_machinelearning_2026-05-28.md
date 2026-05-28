## Reddit ML - 2026-05-28


### 1. [AI生成的CUDA内核悄然破坏训练和推理 [R]](https://www.reddit.com/r/MachineLearning/comments/1tpaw6x/aigenerated_cuda_kernels_silently_break_training/)
> AI生成的CUDA内核在基准测试中通过，但在实际训练中因精度问题导致损失发散，需警惕此类隐蔽错误。

<sub>作者: /u/laginimaineb | 发布于: 2026-05-27 16:35</sub>

---

### 2. [[R]用于欺诈检测的GNN模型表现不佳[R]](https://www.reddit.com/r/MachineLearning/comments/1tovj42/rgnn_model_for_fraud_detection_isnt_performing/)
> 用户构建GNN模型用于欺诈检测，使用IEEE CIS数据集，但性能不佳（AUC 0.87），低于SOTA，寻求改进建议。

<sub>作者: /u/LiveAccident5312 | 发布于: 2026-05-27 05:02</sub>

---

### 3. [在不经意间卡住GPU的情况下分析PyTorch训练 [D]](https://www.reddit.com/r/MachineLearning/comments/1tp2nnw/profiling_pytorch_training_without_accidentally/)
> PyTorch训练分析存在测量干扰问题，提出用CUDA事件替代同步操作，实现轻量级性能分析。

<sub>作者: /u/traceml-ai | 发布于: 2026-05-27 11:24</sub>

---

### 4. [[D] IEEE机器学习信号处理研讨会声誉如何？[D]](https://www.reddit.com/r/MachineLearning/comments/1touia2/d_is_ieee_workshop_on_machine_learning_for_signal/)
> 询问IEEE信号处理机器学习研讨会的声誉，以及是否值得投稿，对比ICML等顶级会议。

<sub>作者: /u/B3anman | 发布于: 2026-05-27 04:13</sub>

---

### 5. [视觉Transformer中的EMA门控时序序列压缩 [P]](https://www.reddit.com/r/MachineLearning/comments/1tp3r2f/emagated_temporal_sequence_compression_in_vision/)
> NeuroFlow通过追踪语义变化动态移除冗余背景token，实现ViT视频推理55.8倍加速，无需微调，保持97%保真度。

<sub>作者: /u/Bobby-Ly | 发布于: 2026-05-27 12:14</sub>

---

### 6. [BEAM 100K内存基准测试：CSM与Hindsight本地工件对比 [R]](https://www.reddit.com/r/MachineLearning/comments/1tpjx2m/beam_100k_memory_benchmark_csm_vs_hindsight_local/)
> CSM在BEAM 100K基准测试中得分高于Hindsight，且使用更少上下文令牌，但速度较慢。作者寻求改进评估方法的建议。

<sub>作者: /u/keonakoum | 发布于: 2026-05-27 21:53</sub>

---

### 7. [noisekit - 用于生成ASR基准测试中真实退化语音数据集的CLI工具 [P]](https://www.reddit.com/r/MachineLearning/comments/1tp51a1/noisekit_cli_for_generating_realistic_degraded/)
> noisekit是一个开源工具，通过模拟真实电话噪音、混响等条件，生成带标注的噪声数据集，用于评估STT模型性能。

<sub>作者: /u/Karamouche | 发布于: 2026-05-27 13:06</sub>

---

### 8. [一个能在手机上运行的开源微型自动驾驶AI [P]](https://www.reddit.com/r/MachineLearning/comments/1towqqf/a_tiny_opensource_selfdriving_ai_that_runs_on_a/)
> 一个7MB的开源L4自动驾驶AI，可在手机等轻量级设备上实时运行，学习导航、车道保持和漂移恢复。

<sub>作者: /u/moorish-prince | 发布于: 2026-05-27 06:04</sub>

---

### 9. [Triton中的跨平台融合MoE调度：无需CUDA的可移植专家路由 [R]](https://www.reddit.com/r/MachineLearning/comments/1tpj6e5/crossplatform_fused_moe_dispatch_in_triton/)
> 新预印本提出TritonMoE，用纯Triton编写跨平台MoE推理内核，融合门控与上投影减少35%内存流量，在A100上达Megablocks吞吐量的89-131%。

<sub>作者: /u/bassrehab | 发布于: 2026-05-27 21:25</sub>

---

### 10. [跨物种RSA：相同学习规则（BP、PC、STDP、FA）在人类fMRI和猕猴电生理实验中的对比测试 [P]](https://www.reddit.com/r/MachineLearning/comments/1tp36qb/crossspecies_rsa_same_learning_rules_bp_pc_stdp/)
> 该研究比较了不同学习规则在猕猴和人类视觉皮层的表现，发现早期视觉对齐跨物种保守，但IT区对齐主要受模型容量影响。

<sub>作者: /u/ConfusionSpiritual19 | 发布于: 2026-05-27 11:49</sub>

---

### 11. [用于手语识别的工具 [R]](https://www.reddit.com/r/MachineLearning/comments/1tovz7r/what_to_use_for_sign_language_recognition_r/)
> 学生询问菲律宾手语识别本科论文的架构选择：Mediapipe Holistic+Transformers（已有研究）还是Mamba SSM（不熟悉），寻求建议。

<sub>作者: /u/Unable_Let_6998 | 发布于: 2026-05-27 05:25</sub>

---

### 12. ["统一神经缩放定律"论文发布 [R]](https://www.reddit.com/r/MachineLearning/comments/1tpfqv6/unified_neural_scaling_laws_paper_release_r/)

<sub>作者: /u/Glittering_Author_81 | 发布于: 2026-05-27 19:21</sub>

---

### 13. [[R] 从1000多次工具使用实验中，我学到的关于自我改进代理的知识 [R]](https://www.reddit.com/r/MachineLearning/comments/1tpbp7m/r_what_1000_harness_experiments_taught_me_about/)
> AI代理自我改进工具框架的探索，发现连续自我改进主要是实验系统问题，需安全决定改进方式。

<sub>作者: /u/Megadragon9 | 发布于: 2026-05-27 17:02</sub>

---
