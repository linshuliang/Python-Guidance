# mac 安装 opencv



# 安装 opencv

```shell
brew install opencv
```



## 使用 opencv

```c++
#include <opencv2/opencv.hpp>
```



## bug 解决

(1) fatal error: 'opencv2/opencv.hpp' not found.

```shell
cd /usr/local/include
ln -sf /usr/local/include/opencv4/opencv2/ opencv2
```
