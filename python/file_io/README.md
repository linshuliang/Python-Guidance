# Python 文件和目录访问

Python 标准库中，用于文件和目录访问的模块包括:

* os.path --- 常用路径操作
* shutil --- 高阶文件操作
* glob --- Unix 风格路径名模式扩展
* pathlib --- 面向对象的文件系统路径
* fileinput --- 迭代来自多个输入流的行
* stat --- 解析 stat() 结果
* filecmp --- 文件及目录的比较
* tempfile --- 生成临时文件和目录
* fnmatch --- Unix 文件名模式匹配
* linecache --- 随机读写文本行

# os 模块中的文件系统函数

| 函数名称                 | 功能                                                                   |
|:------------------------ | :----------------------------------------------------------------------|
| os.getcwd()              | 返回当前的工作目录                                                     |
| os.listdir(path)         | 用于返回指定的文件夹(path)包含的文件或文件夹的名字的列表               |
| os.walk                  | 是一个简单易用的文件、目录遍历器.                                      |
| os.chdir(path)           | 用于改变当前工作目录到指定的路径(path)                                 |
| os.makedirs(path, mode)  | 用于递归创建目录，创建的所有 intermediate-level 文件夹需要包含子目录。 |
| os.removedirs(path)      | 用于删除目录，如果此目录中存在子目录，则不能直接删除此目录。           |
| os.rename(src, dst)      | 重命名文件或者目录，如果 dst 已经存在，将 raise OSError。              |

## os.path 模块

| 函数名称                        | 功能                                                             |
|:--------------------------      | :----------------------------------------------------------------|
| os.path.exists(path)            | 如果路径 path 存在，返回 True；如果路径 path 不存在，返回 False。|
| os.path.isfile(path)            | 判断路径是否为文件。                                             |
| os.path.isdir(path)             | 判断路径是否为目录。                                             |
| os.path.join(path1, path2, ...) | 合并路径                                                         |
| os.path.basename(path)          | 返回文件名。                                                     |
| os.path.dirname(path)           | 返回文件的目录路径。                                             |
| os.path.split(path)             | 将路径分割为 dirname 和 basename，返回一个元组。                 |
| os.path.splitext(path)          | 返回路径名和文件扩展名的元组。                                   |  

## shutil 模块

| 函数名称                     | 功能             |
|:-----------------------------| :----------------|
| shutil.rmtree                | 递归地删除目录   |


## glob

glob 模块，用于查找符合特定规则的文件路径名，也即从目录通配符搜索中生成文件列表。

| 函数名称                      | 功能                                                                                           |
|:----------------------------- | :--------------------------------------------------------------------------------------------- |
| glob.glob(pathname)           | 返回与路径名模型匹配的路径列表。pathname 中定义了文件路径匹配规则，三个匹配符 `*`, `?`, `[]`。 |
| glob.iglob(pathname)          | 返回一个迭代器，该迭代器生成与路径名规则匹配的路径。                                           |
