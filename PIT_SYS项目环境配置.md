# 工具及环境
### python3.6
后端语言使用python3.6，所以需要先安装python3.6
1. 首先查看是否已安装python3.6环境
打开终端，输入	`python`或`python3`命令

```Shell
python
或
python3
```

如果启动成功则查看python版本，如果版本为2.x版本，或者显示没有python解释器，则进行安装

2. 如果没有安装python3则下载python3.6安装包

链接:https://pan.baidu.com/s/10ASpMfbFpOLzJ7qjFxpM_A  密码:hlli

3. 下载完成后，运行pkg安装包
点击继续一直到安装完成，然后再继续执行步骤1中的查看，看是否安装成功

4. 如果已经安装好了python3.6，那么就开始下载flask项目所需的功能模块
通过终端跳转到你的项目所在的根目录文件夹下
然后执行操作：

```shell
pip3 install -r ./requirements/packages.txt
```

### PyCharm
1. 下载pycharm安装包
	链接:https://pan.baidu.com/s/1ewgUhycZy0vKq_nVzaDYIQ  密码:hblw
2. 安装pycharm并首次启动
选择输入注册码，并去下面网址获取注册码
http://idea.lanyus.com
将注册码输入注册码框
之后找到前往文件夹/etc/下，修改hosts文件，在文件最后添加一行代码
```
0.0.0.0 account.jetbrains.com
```
之后保存退出，再点击pycharm注册后可以使用

### MySQL
1. 下载Mysql安装包
	链接:https://pan.baidu.com/s/1-B6TsVj7KYlifNwKdOhNUQ  密码:e5wu
2. 安装MySQL
3. 在偏好设置里查看是否安装成功，成功则启动mysql
4. 在终端中启动mysql
```
mysql -h localhost -u root
```
如果进不去，则
```
mysql -h localhost -u root -p
```
提示输入密码时直接回车

5. 进入后输入下面命令
```
show databases;
use mysql;
select Host,user,authentication_string from user where user='root';
update user set authentication)strinig=password('你的密码') where user='root' and Host='localhost';
```

### postman
postman不需要配置，直接下载安装使用
	链接:https://pan.baidu.com/s/1DLuLyJnWa5vclt1Utj7flA  密码:zk1g

### Navicat
Navicat下载安装后直接使用
	链接:https://pan.baidu.com/s/1a1TG466b4pi1WzLTT7iFBw  密码:bprn