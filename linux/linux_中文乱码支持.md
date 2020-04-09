# ubuntu 中文支持

目标：使系统/服务器支持中文，能够正常显示

首先查看系统有没有安装中文语言包：

```
locale -a
```

看是否包含以下几项：

zh_CN.gb2312
zh_CN.gbk
zh_CN.utf8

## Step 1. 安装中文支持包 language-pack-zh-hans

```
sudo apt-get install language-pack-zh-hans
```

## Step 2. 修改/etc/environment，加上下面两行

```
LANG="zh_CN.UTF-8"
LANGUAGE="zh_CN:zh:en_US:en"
```

## Step 3. 修改文件 /var/lib/locales/supported.d/local

如果没有这个文件就新建，
如果存在就在末尾追加。

```
en_US.UTF-8 UTF-8
zh_CN.UTF-8 UTF-8
zh_CN.GBK GBK
zh_CN GB2312
```

## Step 4. 设置语言

```
sudo locale-gen
```

## Step 5. 安装中文字体

```
sudo apt-get install fonts-droid-fallback ttf-wqy-zenhei ttf-wqy-microhei fonts-arphic-ukai fonts-arphic-uming
```

## Stp 6. 修改 ~/.bashrc

在 `~/.bashrc` 中新增一行:

```
export LANG=zh_CN.UTF-8
```

## 参考

[centos 中文语言乱码解决方法](https://blog.csdn.net/hpf247/article/details/79981803)
