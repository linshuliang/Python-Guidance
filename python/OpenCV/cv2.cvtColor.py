# coding=utf-8
# cv2.cvtColor() method is used to convert an image from one color space to another.
# There are more than 150 color-space conversion methods available in OpenCV.
# Syntax:
#     cv2.cvtColor(src, code[, dst[, dstCn]])
#
# Parameters:
#     src: It is the image whose color space is to be changed.
#     code: It is the color space conversion code.
#     dst (OPTIONAL): It is the output image of the same size and depth as src image.
#     dstCn (OPTIONAL): It is the number of channels in the destination image.

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
