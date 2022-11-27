---
created_at: 2020-02-22 21:05:35.0
updated_at: 2021-02-16 23:23:37.898
slug: nginx-server-and-location-match-algorithm
tags: 
- Nginx
---

> 前两天使用K8S的ingress配置，遇到两个有包含关系的uri需要匹配到两个不同的容器中的情况，找了一下具体的匹配规则，主要来自[这篇文章](https://www.digitalocean.com/community/tutorials/understanding-Nginx-server-and-location-block-selection-algorithms)

根据墨菲定律，可能会发生的事就一定会发生。如果对Nginx的路径配置一直存疑，迟早会出问题。因此，搞懂很重要。

总体来说，Nginx将配置根据不同的server分成了不同的块，每当一个请求过来时，Nginx都会根据一定的算法确定哪一个配置块来处理该请求。其中起关键性作用的是server块和location块。前者定义了一个虚拟服务器，管理员通常会定义多个server块，然后根据请求的域名，端口或IP决定匹配到哪一个；后者存在于server块内，根据URI对虚拟服务器进行更加详细的区分。二者组合起来能够实现非常灵活的配置。

<!-- more -->

# server

在server块内，主要通过listen指令和server_name指令配置

## listen

首先，Nginx查看请求的IP地址和端口，将它与每个server块的listen匹配。

listen指令用于定义server块需要响应的IP和端口。默认情况下，任何不包含listen指令的server块都将被分配一个默认值：对于root用户，将被设置为0.0.0.0:80；对于普通用户，将被设置为0.0.0.0:8080。

listen指令有如下几种可能性。

- IP + Port
- 单独的IP，此时Port将被设为默认值80
- 单独的Port， 此时将会监听该端口上的所有接口
- Unix的socket文件路径

匹配时，算法如下

- 首先将不完整的listen指令使用默认值填充完整
  - 没有设置listen指令的，使用0.0.0.0:80替换
  - 单独的IP，端口默认设为80
  - 单独的端口，IP默认设为0.0.0.0
- 将IP-Port和请求的IP-Port对比
- 如果只有一个server块匹配成功，则该server为最终结果。如果有多个server块匹配成功，则继续根据server_name进行匹配。

注意哟：server_name只有在需要区分listen匹配的多个结果时才会被使用。一个典型的例子，如果example.com被解析到192.168.1.10，此时要在80上进行匹配。则下面两个配置永远只会匹配到第一个。

```nginx
server {
    listen 192.168.1.10;
    . . .
}

server {
    listen 80;
    server_name example.com;
    . . .
}
```

## server_name

当listen指令匹配到多个结果时，server_name就发挥作用了。

Nginx会检查请求的**Host头部**，根据如下算法，将其值与server_name指令配置内容进行对比

- 首先进行精确匹配，如果匹配数量为1，则使用；如果精确匹配到多个，则使用第一个；如果匹配为0，则继续
- 匹配以*开头的配置值，如匹配数量为1，则使用；如匹配到多个，则使用最长那个；如果匹配为0，则继续
- 匹配以*结尾的配置值，如匹配数量为1，则使用；如匹配到多个，则使用最长那个；如果匹配为0，则继续
- 使用正则表达式匹配，使用匹配到的第一个；如果匹配为0，则继续
- 到这里还没有匹配到，则使用该IP和Port对应的默认server块

注意哟：一个IP和Port对应的默认server块，就是根据listen匹配结果集的第一个，或包含了default_server选项的server块。

例一：host1.example.com会匹配第二个server块。满足算法第一点。

```nginx
server {
    listen 80;
    server_name *.example.com;
    . . .
}

server {
    listen 80;
    server_name host1.example.com;
    . . .
}
```

例二：www.example.org匹配第二个server块。满足算法第二点。

```nginx
server {
    listen 80;
    server_name www.example.*;
    . . .
}

server {
    listen 80;
    server_name *.example.org;
    . . .
}

server {
    listen 80;
    server_name *.org;
    . . .
}
```

例三：www.example.org匹配第三个server块。满足算法第三点。

```nginx
server {
    listen 80;
    server_name host1.example.com;
    . . .
}

server {
    listen 80;
    server_name example.com;
    . . .
}

server {
    listen 80;
    server_name www.example.*;
    . . .
}
```

例四：www.example.org匹配第二个server块。满足算法第四点。

```nginx
server {
    listen 80;
    server_name example.com;
    . . .
}

server {
    listen 80;
    server_name ~^(www|host1).*\.example\.com$;
    . . .
}

server {
    listen 80;
    server_name ~^(subdomain|set|www|host1).*\.example\.com$;
    . . .
}
```

# location

## 语法

介绍算法前，先讲讲语法，标准语法如下

```nginx
location optional_modifier location_match {
    . . .
}
```

其中optional_modifier取下面几种可能的值

- (none) : 即没有optional_modifier，按照前缀进行匹配
- = : 完全匹配
- ~ : 按照大小写敏感的正则表达式匹配
- ~* : 按照大小写不敏感的正则表达式匹配
- ^~ : 不按照正则表达式匹配，注意，这里是显式地抑制正则表达式的解析

下面举例

```nginx
# 匹配/site /site/page/index.html /site/index.html等
location /site {
    . . .
}

# 只能匹配 /site
location = /site {
     . . .
}

# 可匹配/hello.jpg，但是不能匹配/hello.JPG
location ~ \.(jpe?g|png|gif|ico)$ {
    . . .
}
# 上面的大小写不敏感版本
location ~* \.(jpe?g|png|gif|ico)$ {
    . . .
}

# 能够匹配/customs/hello.html
location ^~ /customs {
    . . . 
}
```

## 匹配算法

location的匹配方式和server块类似，都是找最优匹配，具体算法如下

- 找出所有匹配URI前缀的location块，作为备选
- 检查精确匹配的项（即=修饰的项），如果有结果，则直接使用它最为最终匹配结果。否则进行下一步
- 如果没有精确项匹配，开始匹配不精确项。找出最长前缀匹配的项，按照如下规则检查
  - 若最长前缀匹配的项被^~修饰，则使用它作为结果
  - 若最长前缀匹配的项未被^~修饰，则此结果会被Nginx暂存起来
- 解析正则表达式（包含了大小写敏感和不敏感），在上面的按照最长前缀匹配的项中有任何包含正则表达式的项，则进行正则表达式匹配。一旦匹配成功，则用它作为结果
- 如果没有正则表达式匹配成功，就使用之前被暂存的匹配项作为结果

注意哟：这里所说的基于前缀，意思是location指定的值和请求URI的前缀能够匹配。比如 URI 为 /customs/hello/halo时，`location /custom`、`location /custom/hello`、`location ~ /.*/hello`都是能够匹配的

注意哟：所谓最长前缀匹配项，即尽可能多地匹配URI。比如`location /custom/hello`相比`location /custom`，就是较长的匹配项。

注意哟：默认情况下，相对使用前缀，Nginx会优先使用正则表达式进行匹配。但在这里，ngin首先检查所有前缀location，从而允许我们使用=和^~修饰符来覆盖这个原则。

注意哟：Nginx会匹配最长最具体的location，但当一个location被当做匹配结果时，正则表达式的解析就停止了，因此location之间的相对位置也会有所影响。比如例四。

下面举例

例一：访问 /hello/hello，匹配到的是第一个。满足匹配算法第二点。

```nginx
location = /hello/hello {
}

location ~* /.*/hello {
}
```

例二：访问/hello/hello，匹配到的是第二个。满足匹配算法第四点。

```nginx
location /hello/hello {
}

location ~* /.*/hello {
}
```

例三：访问/custom/hello，匹配到第一个。满足匹配算法第五点。

```nginx
location /custom/hello {
}

location /custom {
}
```

例四：访问/custom/hello，匹配到第一个。在前缀匹配长度上，他们一致，在解析正则表达式时，第一个首先被解析，符合要求，这样尽管第二个也符合要求，但此时正则表达式的解析已经停止了。

```nginx
location ~ /.*/hello {
}

location ~ /custom/.* {
}
```

继续上例，依旧访问/custom/hello，还是匹配到第一个，原因同上。

```nginx
location ~ /custom/.* {
}

location ~ /.*/hello {
}
```

## location跳到其它location的情况

一般来说，匹配到一个location后，之后的工作都会在该location下完成。但有几个特殊的场景将会重新触发location匹配。比如如下几个指令。

- index

  index如果用来处理请求，则始终会导致重定向。如果我们将一个精确匹配的location配置为一个目录，则可能将其重定向到其它位置。比如下面的配置。

  ```nginx
  # 当方位 /exact，会被重定向到/index.html，从而重定向到第二个location
  index index.html;
  
  location = /exact {
      . . .
  }
  
  location / {
      . . .
  }
  
  # 解决方案是关闭index并开启autuindex
  location = /exact {
      index nothing_will_match;
      autoindex on;
  }
  ```

- try_files

  该指令告诉Nginx检查是否存在一组命名的文件或目录。 最后一个参数可以是Nginx将对其进行内部重定向的URI。考虑下面的例子。

  ```nginx
  root /var/www/main;
  location / {
      try_files $uri $uri.html $uri/ /fallback/index.html;
  }
  
  location /fallback {
      root /var/www/another;
  }
  ```

  这里，如果来的请求是/balabala，则Nginx会尝试在/var/www/main下依次尝试寻找balabala、balabala.html、balabala/等文件或文件夹，如果都没有则内部重定向到/fallback/index.html。此时会匹配到第二个location块。

- rewrite

  rewrite指定将匹配的uri重写成新的uri，并重新匹配新的location。

  ```nginx
  # 如果uri为/rewriteme/fallback，则重写后的uri变成/fallback，会匹配到下面那个location
  root /var/www/main;
  location / {
      rewrite ^/rewriteme/(.*)$ /$1 last;
      try_files $uri $uri.html $uri/ /fallback/index.html;
  }
  
  location /fallback {
      root /var/www/another;
  }
  ```

  当然在使用return指令发送301、302重定向时，也会发生类似效果，但那是标准重定向，可以看做新的请求，所以他们还是不同的。

- error_page

  error_page类似try_files形成的效果，执行的错误页面路径可能在另一个location中。

  ```nginx
  root /var/www/main;
  
  location / {
      error_page 404 /another/whoops.html;
  }
  
  location /another {
      root /var/www;
  }
  ```

# kubernetes ingress

ingress是K8S中的概念，用于将请求路由到指定的服务，本质上是对nginx的包装。所有配置的ingress都将被转换成nginx的location块。

```yaml
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: test-ingress
  annotations:
    nginx.ingress.kubernetes.io/use-regex: "true"
spec:
  rules:
  - host: test.com
    http:
      paths:
      - path: /foo/.*
        backend:
          serviceName: test
          servicePort: 80
```

上述配置将被翻译成如下配置

```nginx
location ~* "^/foo/.*" {
  ...
}
```

本文比较关心的是ingress中配置的路径优先级。

在Nginx中，正则表达式遵循最先匹配原则，因此为了更加准确地进行匹配，在写入nginx配置前，ingress首先会根据路径的长度倒序排序，然后才写入nginx配置。

注意哟，注意下面这种情况此时test.com/foo/bar/bar将会匹配第一个location，而不是第二个location，因为整个ingress开启了正则表达式。当然，如果需要匹配第二个，可以将正则表达式关闭，从而设置 `location = /foo/bar/bar`

```yaml
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: test-ingress-3
  annotations:
    nginx.ingress.kubernetes.io/use-regex: "true"  # 注意这里
spec:
  rules:
  - host: test.com
    http:
      paths:
      - path: /foo/bar/bar
        backend:
          serviceName: test
          servicePort: 80
      - path: /foo/bar/[A-Z0-9]{3}
        backend:
          serviceName: test
          servicePort: 80
```

将会被翻译成

```nginx
location ~* "^/foo/bar/[A-Z0-9]{3}" {
  ...
}

location ~* "^/foo/bar/bar" {
  ...
}
```

# 总结

详细了解nignx这些特性，在做网站或接口配置时非常有用。比如有如下需求。

在我开发的项目中，大多数接口均以/admin打头，但只有一个接口以/swagger开头，现在出于需要，我要将项目配置到 www.example.com/abc/admin下。

- 在详细了解Nginx配置之前，我的解决方案如下

  将接口的admin前缀去除，然后将location为/abc/admin/下的请求转发给我的服务。

  ```nginx
  location /abc/admin/ {
      proxy_pass http://127.0.0.1:19898/;
  }
  ```

- 熟悉后，我可以在不改动原来前缀的基础上进行修改。这样看来，上面的操作相当于把Nginx的开发转移到了业务代码中，非常的不好。

  ```nginx
  location /abc/admin/ {
      proxy_pass http://127.0.0.1:19898/admin/;
  }
  
  location /abc/admin/swagger/ {
      proxy_pass http://127.0.0.1:19898/swagger/;
  }
  ```

# 参考资料

1. [Understanding Nginx Server and Location Block Selection Algorithms](https://www.digitalocean.com/community/tutorials/understanding-nginx-server-and-location-block-selection-algorithms)
2. [Kubernetes Ingress Path Matching](https://kubernetes.github.io/ingress-nginx/user-guide/ingress-path-matching/#path-priority)
3. [Nginx官方手册](https://www.nginx.com/resources/wiki/start/)