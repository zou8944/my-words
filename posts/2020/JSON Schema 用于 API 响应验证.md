---
created_at: 2020-10-03 23:40:52.0
updated_at: 2021-11-08 16:25:55.614
slug: json-schema-validate-api-response
tags: 
- JSON Schema
- API
---

## API的响应需要约束

目前我们开发Web API的方式是通过定义Open API描述文件来定义请求约束。约束能够保证所有请求参数按照正确的格式和必要性传输，从而规范化输入。这保护了服务端内部的安全——输入约束不变的情况下，输入的值总是合法可期的。

尽管Open API也提供了对Response Body的定义，允许用户描述响应的消息格式，但由于其不具有强制性——语法上可以不写，写了也不与实际返回内容有深入结合，因此无法验证真实API的响应是否符合预期，这也是从一开始不愿写响应体的原因。

而关于验证API响应的重要性，是不言而喻的，截止目前，至少有两个时刻让我有了“如果能够在单元测试就验证响应体格式就好了”的想法。

其一：今年上半年的一次down time，彼时是上线真米视频，其video id要做到可控（手动编写，数位字符串），而原逻辑使用了阿里云生成的video id——32位字符串。使用的方案是将手动生成的video id替换了阿里云video id，结果由于测试上的不周全导致所有视频的video id都被替换，对于那些没有分配手动id的音视频，其video id自然变成了null。而该问题因为机缘巧合对视频无影响，仅对音频产生影响。导致较长时间才发现。回首该问题，出在video id字段的格式上，如果有对响应体做约束——要求video id必须有值，且长度为32位，则该问题能够在单元测试就发现。

<!-- more -->

其二：呼啦亲子项目已进行了多次迭代，大致如下

- 初版
- 增加了呼啦圈，其内容与文章接近，封面图需要记录宽高和媒体类型；为了保持格式一致，原本文章的封面格式也改为如此
- 首页文章的封面的显示增加多图效果，其它页面保持原有格式不变，且多图效果要求类随机——即要对封面字段格式化输出
- 创作者中心用于编辑上面多图的选项，因此获取的封面字段要原样输出
- 每一次升级都要兼容之前的版本

光看文章这一项的元数据，就有下面四种格式

首页文章格式（其中coverSrc用于兼容最初版本、cover用于兼容次初版本API、covers+style是最新版的API需要的字段）

```json
"meta": {
    "title": "各国孩子吃什么零食之法国篇",
    "covers": [
        {
            "url": "https://qinzi.static.hulaplanet.com/ttp/editor/94d53aa2e67acaf5bdac445eb1ed2144.jpg?x-oss-process=image/auto-orient,1/interlace,1/resize,m_lfit,w_828/quality,q_90/format,jpg",
            "width": 800,
            "height": 600,
            "mediaType": "image"
        }
    ],
    "coverSrc": "https://qinzi.static.hulaplanet.com/ttp/editor/94d53aa2e67acaf5bdac445eb1ed2144.jpg",
    "cover": {
        "url": "https://qinzi.static.hulaplanet.com/ttp/editor/94d53aa2e67acaf5bdac445eb1ed2144.jpg?x-oss-process=image/auto-orient,1/interlace,1/resize,m_lfit,w_828/quality,q_90/format,jpg",
        "width": 800,
        "height": 600,
        "mediaType": "image"
    },
    "style": "singleMinImage"
}
```

普通文章列表页格式（多图显示仅对首页生效，普通列表页保持次初版本格式）

```json
"meta": {
    "title": "各国孩子吃什么零食之法国篇",
    "coverSrc": "https://qinzi.static.hulaplanet.com/ttp/editor/94d53aa2e67acaf5bdac445eb1ed2144.jpg",
    "cover": {
        "url": "https://qinzi.static.hulaplanet.com/ttp/editor/94d53aa2e67acaf5bdac445eb1ed2144.jpg?x-oss-process=image/auto-orient,1/interlace,1/resize,m_lfit,w_828/quality,q_90/format,jpg",
        "width": 800,
        "height": 600,
        "mediaType": "image"
    }
}
```

文章详情页格式（多出来了jsVersion和cssVersion）

```json
"meta": {
    "title": "各国孩子吃什么零食之法国篇",
    "coverSrc": "https://qinzi.static.hulaplanet.com/ttp/editor/94d53aa2e67acaf5bdac445eb1ed2144.jpg",
    "cover": {
        "url": "https://qinzi.static.hulaplanet.com/ttp/editor/94d53aa2e67acaf5bdac445eb1ed2144.jpg?x-oss-process=image/auto-orient,1/interlace,1/resize,m_lfit,w_828/quality,q_90/format,jpg",
        "width": 800,
        "height": 600,
        "mediaType": "image"
    },
    "jsVersion": "awbegiwaubegwug",
    "cssVersion": "weignwoegowibhg"
}
```

创作者中心文章格式（多出来了jsVersion, cssVersion, coverDisplayCount(用于用户选择该文章显示几张图)）

```json
"meta": {
    "title": "各国孩子吃什么零食之法国篇",
    "covers": [
        {
            "url": "https://qinzi.static.hulaplanet.com/ttp/editor/94d53aa2e67acaf5bdac445eb1ed2144.jpg?x-oss-process=image/auto-orient,1/interlace,1/resize,m_lfit,w_828/quality,q_90/format,jpg",
            "width": 800,
            "height": 600,
            "mediaType": "image"
        }
    ],,
    "jsVersion": "awbegiwaubegwug",
    "cssVersion": "weignwoegowibhg",
    "coverDisplayCount": 1
}
```

一个文章的mata就有四种格式，再加上呼啦圈的meta格式，如果需要同时对他们进行修改，一定会令人相当头大。此时如果能够在单元测试约束meta的格式，要求哪些字段是必须的，不需要哪些字段，则可大大减轻心智负担，对API质量也是一个保证。

## 可能的约束方法

那么有什么好的方法来做这件事呢？一般我们有几种方法

**编程测试**

最原始也是最直接的方法，直接编程验证每个字段的格式。这种方式砖量太大，如果要对拥有数十个字段的响应，针对每个字段验证类型、长度、多余字段等。如果多几个这样的接口，会头晕的。

有针对此做一些优化的，即使用一些json validator进行验证，但这些工具的局限性太大，不能完全满足需求。

使用编程测试最终的归宿很可能会变成只测试几个重要的字段的格式，但**往往出问题的都是没有关注的字段，而重视的字段一般没那么容易出问题**。

**使用JSON Schema**

铺垫那么多，就是想说JSON Schema。一个真正满足需求的东西。JSON Schema是一个规范，用于全方位描述json的格式，包括一个json中必须包含哪些字段、只能包含哪些字段、字段的类型、是否可为空、字段最大最小值、字段的长度等。如同我们使用Open API描述文件来描述我们接口的输入参数；使用JSON Schema描述API响应消息体并在单元测试进行验证。这样把控API输入和输出，在安全性上会有比较大的提升。

## Json Schema

JSON Schema官网https://json-schema.org/，目前最新版是2019-09.

按照官网的话说，JSON Schema是一个用于描述和验证JSON文档的规范。

使用JSON Schema时最大的问题是会把描述文件写得太大，尤其是使用JSON Schema生成工具(https://jsonschema.net/home)时。刚开始将/feeds接口的响应自动生成了数百行描述文件，这无疑是不可接受的。

解决此问题的最好办法，以目前我的认知来看，是全部手写+定义复用的方式——仅增加自己需要的特性，再将公共结构抽取出来，在合适的地方使用$ref引用。具体可参考[如何定义一个复杂的schema](https://json-schema.org/understanding-json-schema/structuring.html)（该文章对应的书籍[Understanding Json Schema](https://json-schema.org/understanding-json-schema/index.html)也是学习JSON Schema的不错的资料）。

同时，官网也列出了[各语言下验证JSON Schema的库](https://json-schema.org/implementations.html)，在Java下，我推荐[这个](https://github.com/networknt/json-schema-validator)

## 使用JSON Schema

我们举例如何使用JSON SChema验证/feeds接口文章类型的数据

### 定义Schema

#### 公共属性

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "definitions": {
    "nullableString": {
      "oneOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ]
    },
    "encodedId": {
      "type": "string",
      "minLength": 20
    },
    "mediaType": {
      "enum": [
        "image",
        "video"
      ]
    },
    "stateEnum": {
      "enum": [
        "normal",
        "draft"
      ]
    },
    "postFeedStyle": {
      "enum": [
        "textOnly",
        "singleMinImage",
        "singleMaxImage",
        "twoImages",
        "threeImages"
      ]
    }
  }
}
```

#### 作者

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "id": {
      "$ref": "../../public-definitions.json#/definitions/encodedId"
    },
    "nickname": {
      "$ref": "../../public-definitions.json#/definitions/nullableString"
    },
    "avatar": {
      "$ref": "../../public-definitions.json#/definitions/nullableString"
    }
  },
  "required": [
    "id",
    "nickname",
    "avatar"
  ],
  "additionalProperties": false
}
```

#### 媒体类型

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "url": {
      "$ref": "../../public-definitions.json#/definitions/nullableString"
    },
    "width": {
      "type": "integer"
    },
    "height": {
      "type": "integer"
    },
    "mediaType": {
      "$ref": "../../public-definitions.json#/definitions/mediaType"
    }
  },
  "required": [
    "url",
    "width",
    "height",
    "mediaType"
  ],
  "additionalProperties": false
}
```

#### 标签类型

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "id": {
      "$ref": "../../public-definitions.json#/definitions/encodedId"
    },
    "name": {
      "type": "string"
    },
    "hotted": {
      "type": "boolean"
    }
  },
  "required": [
    "id",
    "name",
    "hotted"
  ],
  "additionalProperties": false
}
```

#### 元数据

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    },
    "coverSrc": {
      "type": "string",
      "description": "为了兼容最初的API而留存的字段"
    },
    "cover": {
      "$ref": "../../base/media.json",
      "description": "为了兼容V2.0前期而存在的字段"
    },
    "covers": {
      "type": "array",
      "description": "目前线上版本在用的字段",
      "items": [
        {
          "$ref": "../../base/media.json"
        }
      ]
    },
    "style": {
      "$ref": "../../../public-definitions.json#/definitions/postFeedStyle"
    }
  },
  "required": [
    "title",
    "cover",
    "covers",
    "coverSrc",
    "style"
  ],
  "additionalProperties": false
}
```

#### 汇总成/feeds接口返回的数据

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "definitions": {
    "item": {
      "allOf": [
        {
          "$ref": "base/public-properties.json"
        },
        {
          "properties": {
            "meta": {
              "$ref": "base/meta-feed.json"
            },
            "author": {
              "$ref": "../base/author.json"
            }
          },
          "required": [
            "meta",
            "author"
          ]
        }
      ]
    }
  },
  "properties": {
    "list": {
      "type": "array",
      "items": [
        {
          "$ref": "#/definitions/item"
        }
      ]
    }
  },
  "required": [
    "list"
  ]
}
```

可以看到，最终定义的文章schema也没有很长，而前面的公共属性、作者等提取出来的结构由于会被众多其它定义使用，因此总体长度是可以接受的。

### 使用schema验证响应体

我们使用json-schema-validator库加载定义好的schema来验证接口响应。

```kotlin
suspend fun WebClient.validateAPIResponseSchema(
  path: String, params: Map<String, String> = mapOf(), schemaPath: String
) {
  val request = this
    .get(path)
    .host(serverHost)
    .port(serverPort)
    .putHeader("token", testToken)

  params.forEach { (k, v) -> request.addQueryParam(k, v) }

  val response = request.expect(ResponsePredicate.JSON)
    .expect(ResponsePredicate.SC_OK)
    .sendAwait().bodyAsJsonObject()

  val schemaURI = File(schemaPath).toURI()
  val schema = JsonSchemaFactory.getInstance(SpecVersion.VersionFlag.V7).getSchema(schemaURI)
  val node = withContext(Dispatchers.IO) { ObjectMapper().readTree(response.encode()) }
  schema.assertLegal(node)
}

  @Test
  fun testGetPostFeeds(vertx: Vertx, tc: VertxTestContext) {
    launch5e(tc) {
      webClient.validateAPIResponseSchema(
        path = "/feeds",
        params = mapOf("content_type" to "post", "limit" to "20"),
        schemaPath = "src/main/resources/jsonschema/content/post/profile-feed.json"
      )
    }
  }
```

运行测试函数testGetPostFeeds，如果验证失败，可得到具体错误原因，方便排查。

至此，使用JSON Schema进行API响应的验证就完成了。只要描述文件不动，就能及时发现响应格式上的错误，保证了接口的正确性。

## Open API与Json Schema

不止一次前端或客户端的同志直接或间接要求我们写Response格式描述，但由于写起来耗时且该描述与实际响应没有强耦合关系，改动很可能不及时，带来很多问题。如果能够将上面定义的JSON Schema描述文件应用到Open API描述文件中，岂不美哉。

然而现实是残酷的，Swagger确实[支持JSON Schema](https://swagger.io/docs/specification/data-models/keywords/)，但支持的是个子集，因此无法直接使用上面定义的描述文件。美梦落空。。。淡淡的忧桑。