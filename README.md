# my-words

我的博客数据源

## What

这是我的博客数据源，所有平台文章都从此处加载。文章的添加和修改也应在此处执行。

## Why

前前后后用过 wordpress、hexo 等博客系统，最近又在折腾自己的博客系统。

每次博客搬家时，面临的最大问题是数据迁移。不同系统往往有不同的格式需求，迁移起来比较麻烦。

但是文章本身是独立的，它不应该受限于展示它的系统，所以有必要将其解耦。

再者，写文章其实和写代码很像，有固定的格式、需要错字纠察，此时 lint 工具就排上了用场。

## 文章规范

- 格式：Markdown
- 元数据：
  - 标题：以文档标题为准
  - 分类：[categories.json](./posts/categories.json)
  - 标签：[tags.json](./posts/tags.json)
  - 创建时间：front matter - created_at
  - 更新时间：front matter - updated_at
  - 期望slug: front matter - slug
- 概览： \<!--more-->

文档标题建议：关键词前移

## To do

- [x] 以往博客整理
- [ ] 以往博客分类
- [x] 文章规范
- [ ] 文章规范 lint 工具
- [ ] markdown lint 接入
- [ ] chinese lint 接入
- [ ] hexo 连接工具
- [ ] CSDN 连接工具
- [ ] 自定义博客 连接工具
