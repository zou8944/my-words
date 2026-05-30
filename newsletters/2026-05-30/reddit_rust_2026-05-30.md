## Reddit Rust - 2026-05-30


### 1. [Roto一年：为Rust打造的编译型脚本语言](https://www.reddit.com/r/rust/comments/1tqvw6t/one_year_of_roto_a_compiled_scripting_language/)
> Roto 发布一年，是一种用于 Rust 应用的静态类型编译脚本语言，作者欢迎提问。

<sub>作者: /u/tertsdiepraam | 发布于: 2026-05-29 08:56</sub>

---

### 2. [SurrealDB 公布全新 3.x 基准测试结果](https://www.reddit.com/r/rust/comments/1tr2s4i/surrealdb_announces_new_3x_benchmarks/)

<sub>作者: /u/DistinctRide9884 | 发布于: 2026-05-29 14:00</sub>

---

### 3. [为什么macro_rules!的作用域规则这么坑爹](https://www.reddit.com/r/rust/comments/1tr35gq/why_are_macro_rules_scope_rules_so_cursed/)
> Rust宏作用域规则复杂，导出宏需用#[macro_export]或pub use，无法直接pub macro_rules!，用户认为设计不合理。

<sub>作者: /u/EtherealElizafox | 发布于: 2026-05-29 14:13</sub>

---

### 4. [Keel：一种用Rust编写的快速、静态类型解释型语言（alpha版）](https://www.reddit.com/r/rust/comments/1tr8u1l/keel_a_fast_staticallytyped_interpreted_language/)
> Keel 是用 Rust 开发的静态类型解释型语言，结合 Rust 语法与 Python 易用性，性能比 Python 快 2-10 倍，支持 C 函数调用。

<sub>作者: /u/horace_h | 发布于: 2026-05-29 17:19</sub>

---

### 5. [技术博客：gRPC-Rust 客户端 API 演进（上篇）](https://www.reddit.com/r/rust/comments/1tr9q6w/tech_blog_grpcrust_client_api_evolution_pt_12/)

<sub>作者: /u/dfawley | 发布于: 2026-05-29 17:48</sub>

---

### 6. [使用 Rust、ort 和 egui 进行 DinoV3 嵌入推理与可视化！](https://www.reddit.com/r/rust/comments/1tr8izs/dinov3_embedding_inference_and_visualization_with/)

<sub>作者: /u/PatagonianCowboy | 发布于: 2026-05-29 17:08</sub>

---

### 7. [为我的点云查看器实现了流形k近邻算法](https://www.reddit.com/r/rust/comments/1tqt8rt/implemented_manifoldknn_for_my_point_cloud_viewer/)
> 开发者用egui创建点云查看器，集成manifold-knn替代kd-tree，大点云速度提升约2倍。

<sub>作者: /u/yehors | 发布于: 2026-05-29 06:29</sub>

---

### 8. [自引用结构体：哪个版本适合你？](https://www.reddit.com/r/rust/comments/1tqu1b1/selfreferential_structs_which_version_is_for_you/)
> 讨论Rust中自引用结构体的三种实现方案：不安全指针、索引偏移和宏crate，各有优缺点，需权衡安全性与便利性。

<sub>作者: /u/GladJellyfish9752 | 发布于: 2026-05-29 07:13</sub>

---

### 9. [zerobrew 0.3.0 版本发布](https://www.reddit.com/r/rust/comments/1tqzz1n/zerobrew_030_release/)
> zerobrew 0.3.0 发布，新增诊断和升级命令，改进Linux支持与稳定性。它是Homebrew的替代方案，更快安装包。

<sub>作者: /u/cachebags | 发布于: 2026-05-29 12:13</sub>

---

### 10. [我用Rust写了一个TUI SSH连接管理器——susshi](https://www.reddit.com/r/rust/comments/1tqxqbs/i_built_a_tui_ssh_connection_manager_in_rust/)
> 作者开发了susshi，一个终端UI的SSH连接管理器，支持分层分组、跳板机、隧道和SCP传输，使用Rust编写。

<sub>作者: /u/Yatoub42 | 发布于: 2026-05-29 10:32</sub>

---

### 11. [AtomicMatrix - 一种用于高性能进程间通信的无锁共享内存区域](https://www.reddit.com/r/rust/comments/1trdno0/atomicmatrix_a_lockfree_shm_memory_arena_for/)
> 失业开发者为解决跨进程状态管理，构建了无锁共享内存分配器AtomicMatrix，项目早期但欢迎反馈。

<sub>作者: /u/DependentJicama4766 | 发布于: 2026-05-29 19:53</sub>

---

### 12. [Renderling 开发日志 - 为 `wgsl-rs` 添加泛型及其他更新](https://www.reddit.com/r/rust/comments/1trakqu/renderling_devlog_generics_for_wgslrs_and_more/)

<sub>作者: /u/schellsan | 发布于: 2026-05-29 18:14</sub>

---

### 13. [从哪里开始学Rust？](https://www.reddit.com/r/rust/comments/1tqo5ow/where_to_start_rust/)
> 初学者询问如何入门Rust，无编程经验，寻求课程或教程推荐。

<sub>作者: /u/the_GoldenDawn | 发布于: 2026-05-29 02:22</sub>

---

### 14. [展示 r/rust：iroh-rings —— iroh 资源的 ReBAC 层](https://www.reddit.com/r/rust/comments/1tr3rtj/show_rrust_irohrings_a_rebac_layer_for_iroh/)
> iroh-rings 是一个基于关系的访问控制层，在 QUIC 连接级别检查权限，支持自定义资源ID和存储后端。

<sub>作者: /u/nrikettsie | 发布于: 2026-05-29 14:35</sub>

---

### 15. [Basedly：无废话的数据库图形界面](https://www.reddit.com/r/rust/comments/1trbzos/basedly_no_bs_database_gui/)
> 基于 Rust + Tauri 开发的轻量级数据库管理器，无广告订阅，支持 AI 操作和撤销功能。

<sub>作者: /u/ignitevm | 发布于: 2026-05-29 18:59</sub>

---

### 16. [我是如何用Rust（wasm-bindgen）构建Ensemble——一个剧本编辑器的](https://www.reddit.com/r/rust/comments/1tr730x/how_i_built_ensemble_a_screenplay_editor_built/)
> 作者介绍自己构建了Ensemble剧本编辑器，愿意回答问题，希望内容对他人有用。

<sub>作者: /u/dovebarra | 发布于: 2026-05-29 16:22</sub>

---

### 17. [mq-bridge - 不同数据流与传输协议之间的桥梁](https://www.reddit.com/r/rust/comments/1tqugkb/mqbridge_a_bridge_between_different_streams_and/)
> 作者分享了一个Rust库mq-bridge，支持HTTP、Kafka等多种传输协议，用于事件共享和微服务通信，内置重试、DLQ和缓冲中间件。

<sub>作者: /u/marco-mq | 发布于: 2026-05-29 07:35</sub>

---

### 18. [zlob rust crate - 比 glob、globset 和 walkdir 快得多的替代方案](https://www.reddit.com/r/rust/comments/1trf93g/zlob_rust_crate_significantly_faster_alternative/)
> zlob是Rust生态中更快的glob实现，支持Windows和SIMD，性能优于同类库，兼容多种glob标准。

<sub>作者: /u/Qunit-Essential | 发布于: 2026-05-29 20:50</sub>

---

### 19. [[P] Talos-XII: 基于Rust的机器学习运行时实验，采用ACHF加速](https://www.reddit.com/r/rust/comments/1trblfr/p_talosxii_rustnative_ml_runtime_experiment_with/)
> Talos-XII是一个纯Rust编写的ML运行时，包含自定义张量/自动求导、DQN/PPO训练和嵌入式Python脚本，核心实验ACHF通过自适应缓存感知路由优化性能。

<sub>作者: /u/zay0kami | 发布于: 2026-05-29 18:47</sub>

---

### 20. [Queryden 专为更快更流畅的性能而打造，告别卡顿](https://www.reddit.com/r/rust/comments/1trakq0/queryden_built_for_faster_and_better_performance/)
> Queryden是一个开源数据库管理工具，解决了其他客户端加载慢、易崩溃的问题，能在几秒内加载大数据集，兼顾安全与性能。

<sub>作者: /u/keens007 | 发布于: 2026-05-29 18:14</sub>

---
