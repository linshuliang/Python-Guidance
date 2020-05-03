# Linux grep 命令

## 简介

Linux grep 命令用于查找文件中的字符串。

## 语法

```
grep [-rv] 文件或目录
```

* -r : 递归地查找目录中的所有文件
* -v : 显示不包含匹配字符串的所有行

## 实例

1. 在当前目录中，查找后缀为 .py 的文件中包含字符串"torch"的文件，并打印出该字符串的行。

```
grep torch *.py
```

2. 以递归的方式查找符合条件的文件。例如，查找指定目录/etc/api 及其
子目录下所有文件中包含字符串"update"的文件，并打印出该字符串所在行的内容。

```
grep -r update /etc/api
```

3. 反向查找。将.py 文件中不包含字符串"torch"的行打印出来。

```
grep -v torch *.py
```

## 参考

[Linux grep 命令详解](https://www.runoob.com/linux/linux-comm-grep.html)
