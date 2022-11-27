---
created_at: 2021-07-07 21:09:39.905
updated_at: 2021-07-07 21:09:39.905
slug: a-way-to-convert-html-to-formatted-text
---

## 需求

html渲染是一个相对常见的需求，在web前端做起来比较容易。Java中很多组价也支持直接填入html原始数据进行格式化渲染。但有时我们需要将html转换为格式化文本，举例来说，满足如下条件

- 反转html实体，如&amp;
- 去除所有标签
- 除换行之外的所有格式全都去除

<!-- more -->

## 实现

目前市面上并没有一步实现该需求的方案，最为接近可行的方案是Jsoup:[https://github.com/jhy/jsoup](https://github.com/jhy/jsoup)；它能够将html文本转换为dom树，并能提取其中文本和元素。

我们的实现逻辑如下：

```yaml
private fun Document.format(): String {
    return StringBuffer().apply { this@format.body().format(this) }.toString()
}

private fun Element.format(sb: StringBuffer) {
    if (this.childNodeSize() == 0) return
    this.childNodes().forEach {
        when (it) {
            is TextNode -> {
                sb.append(it.wholeText.trim())
            }
            is Element -> when (it.tagName()) {
                "div", "p", "ul" -> {
                    it.format(sb)
                }
                "li" -> {
                    sb.append("- ")
                    it.format(sb)
                }
                "span", "pre" -> {
                    it.format(sb)
                    sb.append(" ")
                }
                "br" -> Unit
                "a" -> {
                    sb.append("<${it.attr("href")}>")
                    it.format(sb)
                }
                else -> println(it)
            }
            is Comment -> Unit
            else -> println(it)
        }
        // 如果下一个标签是这些，则需要换行
        if (it.nextSibling() is Element &&
            (it.nextSibling() as Element).tagName() in listOf("div", "p", "ul", "li", "a", "br")
        )
            sb.append("\n")
    }
}

fun main() {
    val html = """
        这是你的html温拌
    """.trimIndent()
    println(Jsoup.parse(html).body())
    println(Jsoup.parse(html).format())
}
```

我们输入如下内容

```yaml
 <div>
  18/47/284
 </div>
 <div>
  <br>
 </div>
 <div>
  <br>
 </div>
 <div>
  北京&nbsp;
 </div>
 <div>
  李诞
 </div>
 <div>
  李丹
  <br>
 </div>
 <div>
  <p><br></p>
  <p>成都</p>
  <p>尺子</p>
  <p><br></p>
  <p>上海&nbsp;</p>
  <p>池子</p>
  <p>格桑酒店</p>
  <p><br></p>
  <p>杭州&nbsp;</p>
  <p><br></p>
  <div>
   <p>深圳</p>
   <p>建国</p>
   <p><br></p>
   <p>西安</p>
   <p>李雪琴</p>
   <p><br></p>
   <p>武汉</p>
   <p>王建国</p> 
   <p><br><span></span></p>
  </div>
 </div>
```

得到的输出，完全满足需求

```yaml
18/47/284

北京
李诞
李丹

成都
尺子

上海
池子
格桑酒店

杭州

深圳
建国
```

### 说明

这里说明编写中的注意事项

- dom结构

    明白dom结构很重要，最开始我就搞错了文本本身也是一个节点

    ```html
    <!-- 评论 -->
    文本1
    <div>
      <div>
        文本1
      </div>
    </div>
    <p>
      文本2
    </p>
    ```

    节点结构如下

    ```html
    Comment
    TextNode
    Element(div)
      - Element(div)
        - TextNode
    Element(p)
      - TextNode
    ```

- 换行符的处理

    不能直接在块标签后增加换行符，因为块标签会嵌套，从早造成多余的换行

    取而代之的，应该看下一个兄弟元素是否是块标签或换行标签

    ```html
    <div>
      <div>
        文本1
      </div>
    </div>
    <p>
      文本2
    </p>
    ```

    如上文本肯定想要得到如下结果

    ```html
    文本1
    文本2
    ```

    如果按块标签换行，则会得到如下结果，显然是不正确的。

    ```html
    文本1

    文本2
    ```

    “下一个相邻元素”，jsoup中有提供nextSibling()方法进行获取

- 超链接的处理

    超链接提供getAttr()获取href属性。

- 评论标签的处理

    评论标签有专门的节点类型——Comment，可以直接识别以忽略。