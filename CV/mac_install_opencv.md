# mac 安装 opencv



# 安装 opencv

```shell
brew install pkg-config
brew install opencv
pkg-config --cflags --libs /usr/local/Cellar/opencv/4.3.0_4/lib/pkgconfig/opencv4.pc
pkg-config --cflags --libs opencv4
```



## 使用 opencv

```c++
#include <opencv2/opencv.hpp>
```

编译选项:

```shell
g++ $(pkg-config --cflags --libs opencv4) *.cpp
```

## bug 解决

(1) fatal error: 'opencv2/opencv.hpp' not found.

```shell
cd /usr/local/include
ln -sf /usr/local/include/opencv4/opencv2/ opencv2
```
