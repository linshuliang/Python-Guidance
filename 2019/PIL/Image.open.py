# coding=utf-8
# PIL.Image.open(fp, mode='r')
from PIL import Image

im_path = '../../dataset/image/cat.jpeg'
im = Image.open(im_path)
im_width, im_height = im.size  # 图片的宽,高
print(im_width, im_height)

import numpy as np
im_arr = np.array(im)
print(im_arr.shape)  # height, width, channel
