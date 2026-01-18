## Reddit Rust - 2026-01-18


### 1. [一款极速™并发有序映射](https://www.reddit.com/r/rust/comments/1qfn6fr/a_blazingly_fast_concurrent_ordered_map/)
> 作者将C++的Masstree高性能并发有序映射移植到Rust，在高并发场景下性能优于标准库的RwLock<BTreeMap>，并提供了基准测试和代码库链接。

<sub>作者: /u/Consistent_Milk4660 | 发布于: 2026-01-17 19:59</sub>

---

### 2. [我实现了Rust的热重载，你也可以做到](https://www.reddit.com/r/rust/comments/1qfct1t/i_hotreload_rust_and_so_can_you/)

<sub>作者: /u/emschwartz | 发布于: 2026-01-17 13:09</sub>

---

### 3. [WSIStreamer：无需下载，直接从S3流式传输千兆级医学影像](https://www.reddit.com/r/rust/comments/1qf823k/wsistreamer_streaming_gigabyte_medical_images/)
> 介绍一种无需下载整个文件即可流式查看大型医学图像的方法：通过HTTP范围请求读取索引，按需获取图块，并利用缓存优化性能。

<sub>作者: /u/Psychological-Ad5119 | 发布于: 2026-01-17 08:36</sub>

---

### 4. [我为终端制作了一个浏览和阅读漫画的界面，欢迎查看我的代码库。](https://www.reddit.com/r/rust/comments/1qfl7w3/i_made_a_terminal_interface_for_browsing_and/)

<sub>作者: /u/northern_intro | 发布于: 2026-01-17 18:43</sub>

---

### 5. [Rust的测试生态还缺什么？](https://www.reddit.com/r/rust/comments/1qfiltg/what_is_rusts_testing_ecosystem_missing/)
> 一位有测试背景的Rust学习者，在学完基础后，想了解Rust测试生态中缺少哪些工具或功能，并征求社区意见。

<sub>作者: /u/_raisin_bran | 发布于: 2026-01-17 17:05</sub>

---

### 6. [嵌入式 Rust 开发者通讯第63期](https://www.reddit.com/r/rust/comments/1qf4q7o/the_embedded_rustacean_issue_63/)

<sub>作者: /u/TheEmbeddedRustacean | 发布于: 2026-01-17 05:28</sub>

---

### 7. [如何在Freenet上使用Rust和WebAssembly构建去中心化网络应用](https://www.reddit.com/r/rust/comments/1qfllw1/how_to_build_decentralized_web_apps_on_freenet/)

<sub>作者: /u/sanity | 发布于: 2026-01-17 18:57</sub>

---

### 8. [cargo 没有手册页吗？](https://www.reddit.com/r/rust/comments/1qflxq7/no_man_page_for_cargo/)
> 用户发现Ubuntu 24.04中通过官方命令安装Rust后，`cargo`命令没有对应的`man`手册页，但可以通过`cargo help`获取帮助。

<sub>作者: /u/ohiidenny | 发布于: 2026-01-17 19:09</sub>

---

### 9. [[媒体] 自定义 Slint UI 源文件图标。](https://www.reddit.com/r/rust/comments/1qf3ixd/media_custom_slint_ui_source_file_icon/)
> 受他人为Rust文件制作图标的启发，作者为Slint UI源文件创建了自定义图标，并提供了下载链接。

<sub>作者: /u/MMIStudios | 发布于: 2026-01-17 04:28</sub>

---

### 10. [实时通话：采用纯 Rust 编写的 SIP/WebRTC 语音代理，搭载优化的 VAD/音频编解码器](https://www.reddit.com/r/rust/comments/1qfcqqn/active_call_pure_rust_sipwebrtc_voice_agent_with/)
> 介绍Active Call：一个用Rust编写的AI语音代理框架，支持SIP/WebRTC协议，包含纯Rust实现的快速语音检测和用于管理通话的LLM剧本系统。

<sub>作者: /u/Familiar-Chance-4290 | 发布于: 2026-01-17 13:05</sub>

---

### 11. [将egui应用编译为自定义网页组件](https://www.reddit.com/r/rust/comments/1qfl5rb/compiling_egui_applications_into_custom_web/)
> 作者介绍了如何将egui应用封装为Web组件，并提供了示例和代码链接，认为这能更好地隔离HTML与Rust代码。

<sub>作者: /u/0x53A | 发布于: 2026-01-17 18:40</sub>

---

### 12. [Continuum：跨设备持久化终端任务（早期版本，欢迎反馈）](https://www.reddit.com/r/rust/comments/1qfkcdx/continuum_durable_multidevice_terminal_tasks/)
> 作者开发了一个用Rust编写的守护进程，用于管理可跨设备持久运行、远程监控和交互的长时间任务，旨在解决现有工具在远程反馈和工作流迭代方面的不足。

<sub>作者: /u/resourceful_sloth | 发布于: 2026-01-17 18:10</sub>

---

### 13. [schema-gateway：基于 Rust 的轻量级 JSON Schema 验证代理](https://www.reddit.com/r/rust/comments/1qfee9m/schemagateway_a_lightweight_json_schema/)
> 作者分享了一个用Rust编写的轻量级JSON模式验证网关，支持JSON Schema和OpenAPI，用于在请求转发前进行验证，并强调其高性能和类型安全等特性。

<sub>作者: /u/Helpful_Rate_3427 | 发布于: 2026-01-17 14:20</sub>

---

### 14. [Google Cloud PubSub 库有什么问题？](https://www.reddit.com/r/rust/comments/1qfcaca/what_is_wrong_with_google_cloud_pubsub_crate/)
> Rust新手在使用Google Cloud PubSub时遇到文档链接失效问题，导致开发受阻。

<sub>作者: /u/nekkoMaster | 发布于: 2026-01-17 12:43</sub>

---

### 15. [utf8proj：用Rust实现的可解释项目调度引擎（含关键路径法、资源平衡与WASM在线演示）](https://www.reddit.com/r/rust/comments/1qfqmdi/utf8proj_explainable_project_scheduling_engine_in/)
> 介绍utf8proj项目：这是一个注重解释性的确定性项目调度引擎，提供可追溯的决策诊断，支持多种依赖关系和渲染格式，使用Rust开发。

<sub>作者: /u/Putrid_War_4842 | 发布于: 2026-01-17 22:18</sub>

---

### 16. [关于《Rust编程语言》最后一章中Web服务器扩展的问题](https://www.reddit.com/r/rust/comments/1qfn1f3/question_on_expanding_on_the_webserver_from_the/)
> 用户学完Rust书籍后，尝试扩展书中的Web服务器项目，仅使用标准库。目前遇到URL路由设计问题，希望找到一种既保持性能又提升代码可读性和减少冗余的解决方案。

<sub>作者: /u/FranzHenry | 发布于: 2026-01-17 19:53</sub>

---

### 17. [你对Leptos有什么看法？](https://www.reddit.com/r/rust/comments/1qfd9bm/what_do_you_think_about_leptos/)
> 用户询问使用Leptos框架构建现代响应式UI的看法和建议，目前正在阅读其官方文档。

<sub>作者: /u/Ok_Chemistry7082 | 发布于: 2026-01-17 13:30</sub>

---

### 18. [闪电搜索：一款适用于Windows的高性能开源文件搜索引擎（Rust + Iced + Rayon）](https://www.reddit.com/r/rust/comments/1qfccak/flash_find_a_highperformance_opensource_file/)
> 为解决Windows文件搜索延迟问题，作者用Rust开发了开源工具Flash Find。它能在25毫秒内索引140万文件，空闲时零CPU占用，并计划未来支持MFT解析以进一步提升速度。

<sub>作者: /u/kcvabeysinghe | 发布于: 2026-01-17 12:46</sub>

---

### 19. [克隆Hyper请求与响应结构](https://www.reddit.com/r/rust/comments/1qfakt8/cloning_hyper_request_and_response_structures/)
> 开发者在尝试克隆Hyper请求和响应以进行分析时遇到困难，因为body无法克隆且相关方法已被弃用，寻求解决方案。

<sub>作者: /u/the-handsome-dev | 发布于: 2026-01-17 11:10</sub>

---

### 20. [Apalis v1.0.0-rc-2 助手配置指南](https://www.reddit.com/r/rust/comments/1qf9ets/aide_configuration_apalis_v100rc2/)

<sub>作者: /u/dev-damien | 发布于: 2026-01-17 10:00</sub>

---
