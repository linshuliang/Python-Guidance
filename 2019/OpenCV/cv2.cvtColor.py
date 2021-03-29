# coding=utf-8
# cv2.cvtColor() method is used to convert an image from one color space to another.
# There are more than 150 color-space conversion methods available in OpenCV.
#
# opencv 中有多种色彩空间，包括 RGB、BGR、HSI、HSL、HSV、HSB、YCrCb、CIE XYZ、CIE Lab 等多种，
# 使用中经常要遇到色彩空间的转化。函数 cv2.cvtColor的作用是将一个图像从一个颜色空间转换到另一个颜色空间，
# 在opencv中，其默认的颜色排列是 BGR 而非 RGB。
# 对于24位颜色图像来说，前8-bit是蓝色，中间8-bit是绿色，最后8-bit是红色。常见的R, G, B通道的取值范围为：
#     0-255 :CV_8U类型图
#     0-65535: CV_16U类型图片
#     0-1: CV_32F类型图片
#
# Syntax:
#     cvtColor(src, code[, dst[, dstCn]]) -> dst
#
# Parameters:
#     src: It is the image whose color space is to be changed.
#     code: It is the color space conversion code.
#     dst (OPTIONAL): It is the output image of the same size and depth as src image.
#     dstCn (OPTIONAL): It is the number of channels in the destination image.
#
# PIL.Image.open 读入的是 RGB, cv2.imread 读入的是 BGR, cv2.imread 会显示图片更蓝一些。
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import cv2
import numpy as np
from PIL import Image

im_path = '../../dataset/image/road_mark.jpeg'
img_1 = cv2.imread(im_path)
img_2 = Image.open(im_path)
img_2 = np.array(img_2)

plt.subplot(121)
plt.imshow(img_1)
plt.subplot(122)
plt.imshow(img_2)
plt.show()
