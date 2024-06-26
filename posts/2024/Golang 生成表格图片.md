---
title: Golang 生成表格图片
slug: golang-table-image
created_at: 2024-06-26 17:27:00
updated_at: 2024-06-26 17:27:00
categories:
  - 解决方案
  - 小文章  
tags:
  - golang
---

## 需求

统计 gitlab 中各仓库的测试覆盖率，以表格的形式发送到企业微信群

<!-- more -->

## 问题

企业微信支持的 markdown 格式消息不支持表格解析，因此无法使用 markdown。不过有支持图片格式消息，所以可以将表格生成图片。

## 方案

[go-chart](https://github.com/wcharczuk/go-chart) 用的比较多，但它不支持表格。

这里有个基于 go-chart 的库 [go-charts](https://github.com/vicanso/go-charts) ，支持表格，试用下来效果还不错。

```go

type covStruct struct {
	projectId      int
	projectName    string
	projectCreator string
	coverage       string
}

func drawTable(covs []covStruct) ([]byte, error) {
	slices.SortFunc(covs, func(a, b covStruct) int {
		return strings.Compare(a.projectCreator+a.projectName, b.projectCreator+b.projectName)
	})
	header := []string{"项目 ID", "项目名称", "创建人", "测试覆盖率"}
	data := lo.Map(covs, func(item covStruct, index int) []string {
		var conv string
		if item.coverage != "" {
			conv = item.coverage + "%"
		} else {
			conv = "无"
		}
		return []string{strconv.Itoa(item.projectId), item.projectName, item.projectCreator, conv}
	})
	spans := []int{1, 4, 2, 2}

	// 支持中文
	fontBs, _ := os.ReadFile("Noto Sans Mono CJKsc-VF.ttf")
	_ = charts.InstallFont("noto", fontBs)
	font, _ := charts.GetFont("noto")
	charts.SetDefaultFont(font)
	p, err := charts.TableOptionRender(charts.TableChartOption{
		Header: header,
		Data:   data,
		Spans:  spans,
		Width:  1300,
	})
	if err != nil {
		return nil, err
	}
	return p.Bytes()
}
```

> 注意事项
>
> 1. 中文支持需要单独下载字体文件并加载。参考：https://github.com/vicanso/go-charts/issues/57
> 2. 宽度可在 `TableChartOption` 中设置，不过此时就需要调用 `charts.TableOptionRender` 函数，而不是例程中的 `charts.TableRender`

将生成的 `[]byte` 写入文件后效果如下

![image-20240626182715573](https://static.zou8944.com/2024-06/294277fbb5f11f28fe90ab3ff471250f.png)

