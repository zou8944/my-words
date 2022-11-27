---
created_at: 2021-08-16 22:41:54.931
updated_at: 2021-08-16 22:48:23.816
slug: charles-configuration
---

Charles是Fiddler之外的另一个抓包工具。传说比Fiddler好用，但配置起来其实是有几点坑的。还是可以掰扯掰扯。

<!-- more -->

## 配置步骤概览

我们配置的目的是利用Charles抓取同局域网下的IOS上应用软件的HTTPS包。环境为Mac OS

1. 配置Charles
    1. Proxy → Proxy Setting，设置端口为8888
    2. Proxy → SSL Proxying Settings，开启SSL代理
    3. Help → SSL Proxying → Install Charles Root Certificate，给本机安装SSL证书
2. 配置IOS
    1. 连接局域网，为该网络手动设置代理，代理地址为PC的局域网地址，端口为8888
    2. 电脑端：Help → SSL Proxying → Install Charles Root Certificate on a Mobile or Remote Server

        此时弹出一个框，按照其指示为手机安装证书

3. 抓包

    在需要抓包的链接单击右键 → Enable SSL Proxying

然后，就可以快乐滴抓包了。

## 坑点

这是本文的重点。上面基本步骤网上一搜一大把，因此文字描述足矣。

### 要怎么看mac本机地址

要么ifconfig | grep 192.168

要么Help → Local IP Adress

### mac端安装根证书

安装是比较好安装，但别忘了还要手动设置信任证书，否则不能用。

![macrootcertificate.png](https://gdz.oss-cn-shenzhen.aliyuncs.com/halo/mac-root-certificate_1629125032475.png)

### ios端安装根证书

手机端有两个注意事项

- 证书下载地址一定要用safari打开，否则IOS不会将其当做描述文件添加到设置中
- 描述文件安装后，还要在 通用 → 关于本机 → 证书信任设置。手动开启对Charles证书的信任，否则不能使用

    ![iosrootcertificate.png](https://gdz.oss-cn-shenzhen.aliyuncs.com/halo/ios-root-certificate_1629125032475.png)

### charles反复打开几次后代理失效

这一点不知道是不是Charles本身的问题，在Charles自动退出再进入之后，iOS端就无法再使用，也无法连接上网络。

解决方案——重启电脑。

## 初步感受到Charles比Fiddler好的地方

会按路径将所有请求进行归类，看起来清楚明了。

比如我抓幕布的包，就很明晰

![charesfolder.png](https://gdz.oss-cn-shenzhen.aliyuncs.com/halo/chares-folder_1629125032474.png)