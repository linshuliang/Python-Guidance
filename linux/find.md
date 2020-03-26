# Linux find 命令

Linux find命令用来在指定目录下查找文件。任何位于参数之前的字符串都将被视为欲查找的目录名。
如果使用该命令时，不设置任何参数，则find命令将在当前目录下查找子目录与文件。并且将查找到的子目录和文件全部进行显示。

## 语法

```
find   path   -option   [   -print ]   [ -exec   -ok   command ]   {} \;
```

参数说明：

find 根据下列规则判断 path 和 expression，在命令列上第一个 `-` `(` `)` `,` `!` 之前的部份为 path，
之后的是 expression。如果 path 是空字串则使用目前路径，
如果 expression 是空字串则使用 -print 为预设 expression。


## 示例

### 删除指定文件夹(dir) 中所有名为 filename 的文件/子目录

```
find dir -name filename |xargs rm -rf
```
