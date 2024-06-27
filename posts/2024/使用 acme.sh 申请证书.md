---
title: 使用 acme.sh 申请证书
slug: apply-cert-with-acmesh
created_at: 2024-06-27 12:00:00
updated_at: 2024-06-27 12:00:00
categories:
  - 解决方案
  - 小文章
tags:
  - acme.sh
---

## 问题

自动云平台申请的免费证书有效期从一年变成三个月后，更换证书变得麻烦了起来。以前一年一换没觉得有什么不妥，如今三个月一换，证书稍多就觉应付不来。

<!-- more -->

两方面问题：

- 证书申请：走云平台申请，每个账号只能申请 20 个免费证书（不支持通配符证书）；证书所有权验证需要手动添加 DNS 记录也比较麻烦。
- 证书部署：证书部署的环境比较复杂：不同账号下的 CDN 服务、ECS 服务器、K8s 集群等。

## 方案

证书部署没有太好的解决方法，但证书申请可以用 acme.sh 来简化过程，做到一键申请。

## acme 协议简介

acme 是 auto certificate management environment （自动证书管理环境）的简称，用于证书管理。

该协议规定了自动证书管理的步骤和流程。实现该协议的客户端可以直接向实现该协议的服务端申请证书。

1. 注册账户

   ACME客户端需要首先在ACME服务器上注册一个账户。注册账户的过程如下：

   - **账户创建**：客户端发送一个POST请求到注册端点，包含用户的联系信息（如电子邮件地址）。

   - **响应**：服务器返回一个带有账户URL的响应，客户端需要保存这个URL以便后续操作。

 2. 申请证书

    当账户注册成功后，客户端可以开始申请证书。申请证书的过程包括以下步骤：

    - **证书申请**：客户端发送一个POST请求到新订单端点，包含希望获得证书的域名（标识符）。

    - **订单创建**：服务器创建一个订单并返回订单对象，包含授权URL和挑战（challenge）信息。

3. 标识符授权

   为了证明对域名的控制权，客户端需要完成一个或多个挑战。授权过程如下：

   - **获取挑战**：客户端从订单对象中获取授权URL，并发送GET请求获取具体的挑战信息。

   - **完成挑战**：客户端按照挑战要求（如在DNS记录中添加特定的TXT记录或在HTTP服务器上创建特定的资源）完成挑战。

   - **提交响应**：客户端完成挑战后，向服务器发送POST请求提交响应。

4. 服务器验证

   服务器接收到客户端提交的挑战响应后，会进行验证：

   - **验证过程**：服务器检查客户端提供的证明，以确认客户端对域名的控制权。

   - **状态更新**：验证成功后，服务器将订单状态更新为“有效”，表示客户端已通过验证。

5. 证书颁发

   在验证成功后，客户端可以请求颁发证书：

   - **证书请求**：客户端生成一个证书签名请求（CSR），并发送POST请求到最终化端点，包含CSR。

   - **证书生成**：服务器生成证书并返回证书对象，包含证书URL。

   - **获取证书**：客户端发送GET请求到证书URL，下载并保存证书。

6. 证书吊销

   如需吊销证书，客户端可以向ACME服务器请求吊销：

   - **吊销请求**：客户端发送POST请求到吊销端点，包含要吊销的证书及相关的验证信息。

   - **确认吊销**：服务器验证请求后，更新证书状态为“吊销”。

> 关于 acme v1 和 acme v2
>
> acme v1 于 2014 年启动，v2 于 2019 年启动。目前（2024 年）Let‘s Encrypt 仅支持 acme v2，[不再支持 v1](https://community.letsencrypt.org/t/end-of-life-plan-for-acmev1/88430/27)。
>
> 相较于 v1，v2 主要是修改端点、增加状态粒度、增加资源查询粒度等。

## acme.sh 简介

acme.sh 是 acme 协议的客户端实现，用于向支持 acme 协议的 CA 证书提供商请求证书。目前支持的提供商包括：ZeroSSL、Letsencrypt、ByPass、SSL.com、Google.com Pulic、Pebble 等。

- 几个默认

  - 默认使用的 CA 厂商为 ZeroSSL。需要更换需指定 `--server`

  - 默认使用 HTTP Challenge 的形式验证域名所有权，即在服务器暴露一个文件，让 CA 厂商访问。可通过 `--dns` 更换为 dns 方式验证

- 几种模式

  模式就是域名所有权验证的方式。有这么几种：

  - nginx 模式：如果 acme.sh 运行在 nginx 服务器所在机器上，设置 nginx 模式时，acme.sh 将自动在 nginx 服务器下创建 HTTP Challenge 所需文件，验证完成后删除该文件。

    ```shell
    acme.sh --issue --nginx -d example.com -d www.example.com -d cp.example.com
    ```

  - apache 模式：类似 nginx 模式，只不过服务器换成 apache。

    ```shell
    acme.sh --issue --apache -d example.com -d www.example.com -d cp.example.com
    ```

  - standalone 模式：这是相对 nginx 和 apache 模式而言的，如果当前机器上没有运行任何服务，standalone 模式会自己在 80 端口上启动一个服务，完成 HTTP Challenge 。

  - dns 自动模式：使用 DNS Challenge 验证域名所有权，DNS 记录通过 API 自动添加。需要配置 DNS 服务商的访问秘钥，参考[此处](https://github.com/acmesh-official/acme.sh/wiki/dnsapi#11-use-aliyun-domain-api-to-automatically-issue-cert)

    ```shell
    export Ali_Key="<key>"
    export Ali_Secret="<secret>"
    
    ./acme.sh --issue --dns dns_ali -d example.com -d *.example.com
    ```

  - dns 手动模式：执行到需要配置 dns txt 记录时停下，等待手动配置后继续。

    ```shell
    # 运行这个
    acme.sh --issue --dns -d example.com -d www.example.com -d cp.example.com
    
    # 等待控制台输出需要配置的 txt 记录，到 dns 服务商处配置
    
    # 配置后执行如下命令刷新该证书
    acme.sh --renew -d example.com
    ```

- acme.sh 只生成证书，不替换证书。即使在 nginx、apache 等模式下，也只是用来进行域名所有权验证。
- 只有通过 DNS Challenge 的方式才可以申请通配符证书。

## acme.sh 使用

以使用 dns 自动模式，dns 服务商为阿里云为例

- 安装

  ```shell
  wget -O -  https://get.acme.sh | sh -s email=my@example.com
  ```

  > 注意事项：这里的 email 需要换成一个真实的邮箱，否则在使用 letsencrypt 时会失效

  > 安装过程做了三件事
  >
  > - 将 `acme.sh` 复制到 `~/.acme.sh/`
  > - 添加别名 `acme.sh=~/.acme.sh/acme.sh`
  > - 在系统内创建一个 cron job 用于定期刷新证书

- 配置阿里云访问凭证

  ```shell
  export Ali_Key="<key>"
  export Ali_Secret="<secret>"
  ```

  > 运行一次后，这两个凭证会被加入 `~/.acme.sh/account.conf` 
  >
  > 也可以直接将 Ali_Key 和 Ali_Secret 加到 `~/.acme.sh/account.conf`

- 生成证书（使用 Letsencrypt）

  ```shell
  acme.sh --issue --dns dns_ali --server letsencrypt -d minbay.com -d '*.minbay.com'
  ```

- 将证书应用于 nginx

  上述命令会提示证书输出位置。对于 nginx，使用的 `cert key`  作为证书秘钥， `full chain certs` 作为证书本体。

  ![image-20240627094337194](https://static.zou8944.com/2024-06/b440b3a943d0412ab98d2f08f3d305c3.png)

## 参考

- [acme.sh 项目](https://github.com/acmesh-official/acme.sh)
- [How to use DNS API](https://github.com/acmesh-official/acme.sh/wiki/dnsapi#11-use-aliyun-domain-api-to-automatically-issue-cert)

- [RFC8555 (acme v2 协议)](https://datatracker.ietf.org/doc/html/rfc8555)
- [End of Life Plan for ACMEv1](https://community.letsencrypt.org/t/end-of-life-plan-for-acmev1/88430/27)
