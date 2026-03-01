## Reddit Rust - 2026-03-01


### 1. [手机搜索1GB JSON文件：从44秒到1.8秒的优化之路，我试遍了所有错误方法](https://www.reddit.com/r/rust/comments/1rgzhhl/searching_1gb_json_on_a_phone_44s_to_18s_a/)
> 作者发现Android应用中使用Rust库memchr进行JSON搜索时性能异常，最终查明是调试模式编译导致。修正后性能恢复正常，SIMD降级问题不存在。

<sub>作者: /u/kotysoft | 发布于: 2026-02-28 10:40</sub>

---

### 2. [Servo v0.0.5 版本发布](https://www.reddit.com/r/rust/comments/1rh8w41/servo_v005_released/)

<sub>作者: /u/Right-Grapefruit-507 | 发布于: 2026-02-28 17:44</sub>

---

### 3. [我开发了一个1GB/s文件加密命令行工具，采用io_uring、O_DIRECT和无锁三重缓冲技术](https://www.reddit.com/r/rust/comments/1rh9tj5/i_built_a_1_gibs_file_encryption_cli_using_io/)
> 作者因传统加密工具处理大文件速度慢，开发了Concryptor。它采用无锁三缓冲和零拷贝等技术，实现CPU满载下1+ GiB/s的加密速度。

<sub>作者: /u/supergari | 发布于: 2026-02-28 18:20</sub>

---

### 4. [东京之外的生活：Compio与io_uring运行时的成功案例](https://www.reddit.com/r/rust/comments/1rh7lfe/life_outside_tokio_success_stories_with_compio_or/)
> 讨论基于io_uring的异步运行时前景，比较compio与tokio性能，分享epoll之外异步方案的使用案例。

<sub>作者: /u/rogerara | 发布于: 2026-02-28 16:54</sub>

---

### 5. [使用 `array.get(idx).ok_or(Error::Whoops)` 相比 `array[idx]` 会有明显的性能损失吗？](https://www.reddit.com/r/rust/comments/1rhb97r/is_there_any_significant_performance_cost_to/)
> 用户询问在Rust中，使用`array.get(idx).ok_or(Error::Whoops)`进行索引访问是否比显式使用`if`语句检查边界性能更好。

<sub>作者: /u/Perfect-Junket-165 | 发布于: 2026-02-28 19:15</sub>

---

### 6. [用GPUI为Zaku打造高性能编辑器](https://www.reddit.com/r/rust/comments/1rhdp64/building_a_performant_editor_for_zaku_with_gpui/)
> 作者基于Zed的文本处理库构建了一个高性能编辑器，用于处理大文件（如1.5GB响应），性能优于Postman等工具。

<sub>作者: /u/errmayank | 发布于: 2026-02-28 20:52</sub>

---

### 7. [发布我的第一个crate——为修复我引发的严重生产故障](https://www.reddit.com/r/rust/comments/1rhc7ac/published_my_first_crate_in_response_to_a_nasty/)
> 作者为解决WebSocket连接中难以复现的阻塞问题，开发了首个Rust库，提供原始套接字与Axum请求的集成及合理配置建议。

<sub>作者: /u/sonthonaxrk | 发布于: 2026-02-28 19:53</sub>

---

### 8. [Stoolap中的向量与语义搜索](https://www.reddit.com/r/rust/comments/1rhc2ce/vector_and_semantic_search_in_stoolap/)

<sub>作者: /u/Competitive-Weird579 | 发布于: 2026-02-28 19:48</sub>

---

### 9. [又一个 Rust 极简数量库（主要用于练习，欢迎反馈！）](https://www.reddit.com/r/rust/comments/1rhcaxs/another_minimal_quantity_library_in_rust_mainly/)
> 作者分享了一个用于练习Rust过程宏的物理量库项目，并寻求关于代码风格和接口测试的反馈。

<sub>作者: /u/EveningLimp3298 | 发布于: 2026-02-28 19:57</sub>

---

### 10. [fastdedup：Rust与Python数据集去重对比——处理1500万条记录，耗时2:55对7:55，内存占用688MB对22GB](https://www.reddit.com/r/rust/comments/1rhc5kq/fastdedup_rust_dataset_deduplication_vs_python/)
> Rust工具fastdedup在数据集去重基准测试中表现优异，相比DuckDB和Python方案，在速度和内存占用上均有显著优势。

<sub>作者: /u/wapplewhite4 | 发布于: 2026-02-28 19:51</sub>

---

### 11. [oken —— 带模糊主机选择器的小巧 SSH 封装工具](https://www.reddit.com/r/rust/comments/1rh7rxu/oken_a_small_ssh_wrapper_with_a_fuzzy_host_picker/)
> 介绍一个名为oken的SSH包装工具，提供模糊主机选择器，可按标签筛选主机，并保持原有SSH配置。

<sub>作者: /u/toxic2soul | 发布于: 2026-02-28 17:01</sub>

---

### 12. [脚本](https://www.reddit.com/r/rust/comments/1rh732q/scripts/)
> 用户询问是否有人能提供适用于游戏机的新版Rust反后坐力脚本。

<sub>作者: /u/CarryInteresting7859 | 发布于: 2026-02-28 16:34</sub>

---

### 13. [llm-pipeline：Rust中LLM调用的防御性输出解析与重试机制](https://www.reddit.com/r/rust/comments/1rgrdqq/llmpipeline_defensive_output_parsing_and_retry/)
> 作者发布首个Rust库llm-pipeline，用于解决LLM输出JSON格式不一致的问题，提供预处理、修复和重试机制，支持多种输出策略和模拟测试。

<sub>作者: /u/RudeChocolate9217 | 发布于: 2026-02-28 03:04</sub>

---

### 14. [Rust能否在不依赖框架的情况下打造自定义3D游戏引擎？](https://www.reddit.com/r/rust/comments/1rh7nw8/can_rust_make_a_custom_3d_game_engine_without/)
> 用户询问Rust能否像C++一样制作无需外部库的自定义3D游戏引擎。

<sub>作者: /u/Basic_Librarian2380 | 发布于: 2026-02-28 16:57</sub>

---
