# cv2

## 基础 API

| API | 功能  |
|:----| :-----|
|[cv2.imread](cv2.imread.py) | 读取图片 |
|[cv2.imwrite](cv2.imwrite.py) | 保存图片 |
|[cv2.cvtColor](cv2.cvtColor.py) | 转换色域 |
|[cv2.resize](cv2.resize.py) | 调整大小 |
|[cv2.meanStdDev](cv2.meanStdDev.py) | 计算图片的均值和标准差 |

## 仿射变换

| API | 功能  |
|:----| :-----|
|[cv2.warpAffine](cv2.warpAffine.py) | 仿射变换的基础API，仿射变换包括平移，旋转，伸缩，本质是通过一个 2 \* 3 的仿射矩阵来计算变换关系 |
|[cv2.getRotationMatrix2D](cv2.getRotationMatrix2D.py) | 旋转图像 |
|[cv2.getAffineTransform](cv2.getAffineTransform.py) | 根据变换前后三个点的对应关系赖自动求解仿射矩阵 |
