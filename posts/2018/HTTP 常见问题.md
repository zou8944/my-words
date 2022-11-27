---
created_at: 2018-10-15 22:31:33.0
updated_at: 2021-02-16 23:26:58.938
slug: http-related-questions
tags: 
- HTTP
---



## Http全称？

	超文本传输协议：Hypertext Transfer protocol

<!-- more -->

## 常用状态码

```html
- 200	响应正常
- 400	Bad Request，请求数据有问题
- 401	Unauthorized，权限不足，资源存在但不让访问
- 403	Forbidden，你的IP被屏蔽时会出现
- 404	资源找不到
- 301	重定向
- 500	服务器内部错误
```

## 常用method

```html
- get		用于获取资源
- post		用于发送数据到服务端，常用于提交表单数据
- put		用于修改资源属性
- delete	用于删除资源
```

## Http协议格式

	请求和响应的消息协议是一样的：起始行、消息头、消息体。三部分以CRLF分隔，最后一个消息头有两个CRLF，表示接下来是消息体的内容了。

### 起始行

	请求的起始行称为请求行，格式：method uri http/version，如 get /index.html http/1.1
	
	响应的起始行称为状态行，格式 ：http/version code desc，如 http/1.1 200 ok。第三个字段是状态码的简单描述信息。

### 消息头

	消息头由很多键值对组成，键值对之间以CRLF作为分隔。

### 消息体

	消息体是一个字符串，字符串长度由消息头中的Content-length字段指定。没有指定则没有消息体。

## 分块传送

	当浏览器向服务器请求一个资源时，该资源是一个动态资源，服务器无法预知该资源的大小。此时会采用分块传送。
	
	服务器先生成一个chunk，发送这个chunk，再生成一个chunk，再发送一个chunk，直到全部资源传送完成。分块传送需要在请求头增加一个特殊的键值对transfer-encoding: chunked，那么消息体的内容便是分块传送的。
	
	chunked传输格式如下图所示，由一段一段的分块组合而成，每个块由一个长度行和一个分块体组成，最后一个分块长度为0表示结束。

![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9zczAuYmFpZHUuY29tLzZPTldzamlwMFFJWjh0eWhucS9pdC91PTIzNjg2NDEwMjEsMTU4MTE3ODM1MiZmbT0xNzMmYXBwPTI1JmY9SlBFRw?x-oss-process=image/format,png)

## 持久连接的机制是怎样的

	早期的Http 1.0每个请求都会发起一个连接，每个页面数百个请求就会发起数百个连接，非常浪费服务器资源。因此在Http 1.1加入了持久连接的机制，Keep-Alive，使得一个连接可以连续服务多个请求。节省了资源
	
	持久连接并不会一直保持连接，而是通过设置 Keep Alive Timeout和Keep Alive Request限制单个连接的持续时长和最多的请求次数。
	
	如果 Keep Alive Timeout设置为0，则退化到非持久连接。如果Keep Alive Timeout设置为超长，当然也不会一直保持，各个浏览器都有相关的控制。

## 什么叫Pipeline管线化

	这也是Http 1.1新引入的特性。之前的请求模式是：一个请求发起，服务器响应完了，再进行下一个请求的发起和响应，这样当请求一多时就会很慢
	
	改进的方式是，将多个请求按顺序打包一起发给服务器，服务器再按顺序将多个响应一起打包回复。这样就快很多了。如下图示很形象地描述了管线化前和管线化后

![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9zczAuYmFpZHUuY29tLzZPTldzamlwMFFJWjh0eWhucS9pdC91PTM0MDIwNDQ4MzgsNzAzNzIwMjE1JmZtPTE3MyZhcHA9MjUmZj1KUEVH?x-oss-process=image/format,png)

![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9zczIuYmFpZHUuY29tLzZPTllzamlwMFFJWjh0eWhucS9pdC91PTEyOTc0NTkzNDksMTU2MTg5NTk3MSZmbT0xNzMmYXBwPTI1JmY9SlBFRw?x-oss-process=image/format,png)

## 如何理解Http协议的无状态性

	无状态指的是服务器的协议层无需为不同请求之间建立任何相关关系。不过这是协议规定的，但建立在Http协议上的应用会通过Session的方式来达到状态保存的目录。

## GET和POST的区别

- GET用于获取资源，POST用于向服务器发送数据
- GET将数据添加到URL后，POST则是将数据放在请求消息体中
- 由第二点导致了如下三点的不同
  - GET相对POST能让用户看到传输内容，不安全
  - GET由于URL长度的限制传输内容有限，POST则好很多
  - GET由于URL的编码限制只能传输ASCII码，而POST则可以传输正常编码格式的文件

## 常见Http消息头字段

### 通用头部字段

```html
- Date				报文创建时间
- Connection		连接的管理：连续或是此次发送后关闭连接
- Cache-Control		缓存控制，如值为max-age=120，表示缓存120秒有效
- Transfer-Encoding	报文的传输编码格式
```

### 请求头部字段

```html
- Host				请求资源所在服务器：主机+端口
- User-Agent		客户端将本地的操作系统、浏览器和其它属性发送给服务器，非必须，可修改
- Accept			客户端希望接收的媒体类型，如 image/webp,image/apng,image/*,*/*;q=0.8
- Accept-Charset	客户端可接收的字符集
- Accept-Encoding	客户端可接收的内容编码，如 gzip, deflate, br
- Accept-Language	客户端可接收的自然语言，如 zh-CN,zh;q=0.9
- Authorization		用于证明客户端有权查看某个资源
- refer				

举例
GET /form.html HTTP/1.1 (CRLF)

Accept:image/gif,image/x-xbitmap,image/jpeg,application/msword,*/* (CRLF)
Accept-Language:zh-cn (CRLF)
Accept-Encoding:gzip,deflate (CRLF)
If-Modified-Since:Wed,05 Jan 2007 11:21:25 GMT (CRLF)
If-None-Match:W/"80b1a4c018f3c41:8317" (CRLF)
User-Agent:Mozilla/4.0(compatible;MSIE6.0;Windows NT 5.0) (CRLF)
Host:www.guet.edu.cn (CRLF)
Connection:Keep-Alive (CRLF)
```

### 响应头部字段

```html
- Accept-Ranges		可接受的字节范围
- Location			让客户端重定向到的URL
- Server			Http服务器的安装信息，如 Apache-Coyote/1.1
```

### 实体头部字段

```html
- Allow				资源可支持的Http方法
- Content-type		实体内容的类型
- Content-Encoding	实体内容的编码方式
- Content-Language	实体内容的语言
- Content-length	实体内容的长度，单位是字节
- Content-Range		实体内容的位置范围，一般是发出部分请求时使用
- Last-Modified		请求资源最后修改时间
```

## 其它知识补充

### 应用层协议

- HTTP
- FTP
- SMTP
- DNS
- TELNET