---
created_at: 2018-02-15 22:31:33.0
updated_at: 2021-02-16 23:27:57.129
slug: git-introduction
---

## GIT简介
1. 版本控制系统：即记录同一个文档在不同人和不同时间修改的各版本的系统，对于恢复文档、差异对比、协同工作有非常大的帮助。
2. GIT是由linux创始人linus花费两周时间写成的，用于托管linux系统。目前已经有众多开源项目，如jQuery、PHP、Ruby等。
<!-- more -->
3. 集中式版本控制系统：以CVS、SVN为代表，版本库是集中存放在中央服务器的，在使用时候要先从服务器中取得最新版本，本地操作完成后还要上传给服务器，非常不方便，而且不安全。
4. 分布式版本控制系统：以GIT为代表，没有集中式的中央服务器，每个人的电脑上都是一个完整的版本库，在工作完成之后只需要和其他同事交换修改的部分即可。具体工作方式还要实际体会。
分布式在本地维护一个完整的库，因此不需要联网也可以工作，等有网络时再把本地库推送到远程库即可。

## 基础知识
1. 所有的版本控制系统只能跟踪文本文件的改动，如txt文件、网页、程序代码等，并且可以明确告诉你在什么地方改了什么。而图片、视频等二进制文件则没有办法跟踪其变化，只能告知文件的大小改变情况，但是不知道具体改了什么。而微软的word就是二进制格式，因此不能详细跟踪。
基于以上原因，使用GIT时，就要以纯文本方式编写文件。
2. 为了长久性和通用性考虑，编写文本时一定要通通使用UTF-8编码。
3. 老司机寄语：千万不要用windows自带的记事本编辑任何文本文件。
原因：记事本团队使用了一个非常弱智的行为来保存UTF-8编码的文件，他们自作聪明地在每个文件开头添加了0xefbbbf字符，对程序的编译之类的会造成错误。推荐使用Ntepad++
4. Git的版本会退速度很快，因为其内部有个指向当前版本的指针HEAD，回退或前进时只是改变了HEAD指向的位置。
5. 工作区和暂存区
工作区：就是电脑上能够看到的目录（working directory）
版本库：工作区内有一个隐藏目录 .git，这是Gti的版本库
暂存区：Git的版本库中存了很多东西，最重要的就是成为stage（或者叫index）的缓存区。还有自动创建的第一个分支master，以及指向master的一个指针HEAD，如下图所示：

    ![工作区、缓存区、版本库的关系](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTgwMjE1MTU0OTA5ODgy?x-oss-process=image/format,png)

    执行git add时，就是把文件修改添加到了缓存区；

    执行git commit时，就是把缓存区的所有内容提交到当前分支。

6. git每次提交的是修改，不是整个文件，因此执行“第一次修改 -> git add -> 第二次修改 -> git add -> git commit”这样的操作后，第二次修改是不会被提交的，因为第二次修改没有添加到暂存区。
7. 在创建远程仓库之前，由于git和github之间是通过SSH加密传输的，因此要先创建SSH Key
<font color=#0000ff><i>ssh-keygen -t rsa -C "youremail@example.com"</i></font>
创建之后在用户主目录下面会生成两个文件：id_rsa、id_rsa.pub，其中id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，可以告诉任何人。
为什么要SSH Key?
因为github需要识别你推送的文件确实是你推送的，而不是别人冒充的，因此需要身份验证。也可任意添加多个Key，每个Key对应不同的电脑，添加之后你可以使用不同的电脑推送文件。
本地生成SSH Key后，需要在github的个人账户中添加该公钥，这样才能正常使用。
8. 添加远程库时，在创建一个repository后github会提示进行本地库的添加，按照提示来就好。
9. 本地库在推送或从远程库提取东西时，支持两种协议：https和ssh，相比而言，ssh的速度更快。
10. **分支的概念**
分支就是科幻电影中的平行宇宙，当你在学习Git时，另一个你在另一个平行宇宙学习SVN，正常时两个宇宙互不干扰，但在某一个时间点，两个宇宙合并了，你就及学会了Git，又会了SVN。
实际用途：开发新功能，需要两周，第一周写了50%，如果立刻提交，会导致代码库不完整，致使别人不能干活，如果等写完了再一起上传，又存在丢失每天进度的风险。有了分支后，可以创建一个专属于你的分支，别人看不到，你在自己的分支上工作，等工作完成后，再把你自己的分支一次性合并到原来的分支上。
git中维护方式：默认创建一个master分支，master分支指向提交，HEAD指向当前分支，默认是master，每次提交，master就向前移一步，随着不断提交，master分支的线越来越长。
    ![这里写图片描述](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTgwMjE1MTYwNTA3OTcx?x-oss-process=image/format,png)
    当创建新的分支时，Git新建一个指针dev，指向master相同指向的提交，再把HEAD指向dev，就表示当前分支在dev上。之后对工作区的修改和提交就是针对dev分支了，重新提交一次后，dev指针往前移动一步，而master指针不变。
    ![这里写图片描述](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTgwMjE1MTYwNjExNzA5?x-oss-process=image/format,png)
    此时要把dev合并到master上，最简单的方法就是将master指向dev的当前提交，完成合并。
    ![这里写图片描述](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTgwMjE1MTYwNjUzMjM2?x-oss-process=image/format,png)
    由于git的分支管理使用的是指针的方式，因此切换和合并起来操作非常快捷。同时<font color=red>鼓励使用分支进行工作</font>，工作完成后再合并到master上，这样有助于提升master的安全性。
11. **分支冲突**
当创建一个分支dev，并且提交了一个修改，同时切换到master上对同一文件进行了修改并提交，在合并分支时很可能会发生冲突，无法完成自动合并，此时只有手动解决冲突再提交才能继续合并。合并后时间线就变成如下。
    ![这里写图片描述](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTgwMjE1MTYwODM4ODg1?x-oss-process=image/format,png)
12. **分支的非快速合并方式**
分支合并时，会默认使用ff(fast forward)模式进行合并，但这样带来的坏处是会丢掉分支信息。此时可以禁用ff模式，在merge时生成新的提交。
如下是ff模式
    ![这里写图片描述](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTgwMjE1MTYxMDAwMzg1?x-oss-process=image/format,png)
    如下是非ff模式
    ![这里写图片描述](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTgwMjE1MTYxMTM0Mzg5?x-oss-process=image/format,png)
13. **分支策略**
实际开发中管理分支的几个基本原则（还是要开发中实际应用才会有体会，现在体会不深）
（1）master分支应该是稳定的，仅用来发布新版本，平时不能在上面干活
（2）干活都在新建的dev分支上，dev是不稳定的，到版本发布时再将dev分支合并到master上
（3）每个工作人员建立一个自己的分支，时不时在dev上进行合并就可以了。
    ![这里写图片描述](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTgwMjE1MTYxMTA5MjMw?x-oss-process=image/format,png)
14. **BUG分支和feature分支**
当我们临时解决一个BUG，或者增加一个新功能时，最好新建一个分支，待完成工作后再将该分支合并到工作分支中。
15. 当你从远程仓库克隆时，Git自动把本地master分支和远程的master分支对应起来，并且远程仓库的默认名称是origin。可以把本地的分支往远程推送，推送完成后远程库的分支结构就基本和本地一样了，但是也可以不必把所有的分支推送，这个要看实际需求。
16. **多人协作的情况（需要实际体会）**
（1）首先，可以试图用<font color=green><i>git push origin branch-name</i></font>推送自己的修改；
（2）如果推送失败，则因为远程分支比你的本地更新，需要先用<font color=green><i>git pull</i></font>抓取到本地试图合并；
（3）如果合并有冲突，则解决冲突，并在本地提交；
（4）没有冲突或者解决掉冲突后，再用<font color=green><i>git push origin branch-name</i></font>推送就能成功！
注意：如果git pull提示“no tracking information”，则说明本地分支和远程分支的链接关系没有创建，用命令<font color=green><i>git branch --set-upstream branch-name origin/branch-name。</i></font>
17. 标签
通常在版本库中打一个标签（tag），将来任何时候都可以按照标签名称来取某个时刻的历史版本。tag实际上是指向某个commit的指针，与分支不同的是，标签不能移动。可以理解为标签是固定在某一时刻的commit的指针。目的是能够很快地找到某一时刻的commit，而不用记复杂的commit id
18. 在github上参与别人的开源项目
    - 访问项目主页，点击fork，在自己的账号下克隆一个相同的仓库。
    - 按照正常克隆的方式从自己的账号下克隆到本地，此时开源项目、你的远程库和本地库关系如下。
    ![这里写图片描述](https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTgwMjE1MTYxODA4NDk0?x-oss-process=image/format,png)

    - 本地修改后推送到自己账号的远程库
    - 要想把自己修改的点推送给开源项目，可以在自己账号发起pull request。
19. 忽略特殊文件
有不想提交的文件时候，可以编写.gitignore文件，将不想提交的文件写到.gitignore文件中，这样在提交时候就会忽略该文件。注意文件名就是“.gitignore”，前面没有东西的。
20. 添加.gitignore文件后没有效果解决办法
原因：.gitignore只能忽略那些原来没有被track的文件，如果某些文件已经被纳入了版本管理中，则修改.gitignore是无效的。解决的办法就是先把本地缓存删除，改成未track状态，然后提交。
（1）先将所有文件提交到Git
（2）在Git根目录执行以下命令
<font color=green><i>git rm -r --cached .</i></font>
<font color=green><i>git add .</i></font>
<font color=green><i>git commit -m "fixed untracked files".</i></font>
1. 配置
配置git时，加上--global是针对当前用户起作用的，如果不加就只对当前仓库起作用。
每个仓库的配置文件都放在.git/config中，对整个仓库起作用。
用户的配置恩见放在用户主目录下的一个隐藏文件/gitconfig中，对用户的所有仓库起作用
可以直接修改配置文件，如果改错了可以删掉文件重新通过命令进行配置。
<font color=red>鼓励进行别名的配置。</font>
2. 自己搭建Git服务器
Git功能强大，但是github并不是必须的，他只是作为一个一直开着的服务器而已，且兼有社区的作用。如果想要自己的代码不开源，又要用Git，那么可以自己搭建一个Git服务器。搭建方式[看这里](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/00137583770360579bc4b458f044ce7afed3df579123eca000)
3. 其它
[Git官方网站](http://git-scm.com)
[Git cheat sheet](https://pan.baidu.com/s/1kU5OCOB#list/path=%2Fpub%2Fgit)