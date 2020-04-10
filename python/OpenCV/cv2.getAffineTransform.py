# coding=utf-8
"""
def cv2.getAffineTransform(src, dst) -> retval
    Args:
        * src : 原图中的三个点
        * dst : 变换后图中的三个对应点
    Results:
        retval : 一个 2 * 3 的仿射矩阵。
"""
import cv2
import numpy as np

im_path = '../../dataset/image/cat.jpeg'
im = cv2.imread(im_path)

im_height, im_width, im_channel = im.shape

src_three_points = np.array([[0, 0], [50, 50], [100, 200]]).astype(np.float32)
dst_three_points = np.array([[10, 100], [200, 60], [100,
                                                    260]]).astype(np.float32)

affine_matrix = cv2.getAffineTransform(src_three_points, dst_three_points)
trans_im = cv2.warpAffine(im, affine_matrix, (im_height, im_width))
cv2.imwrite('affine_image.png', trans_im)
