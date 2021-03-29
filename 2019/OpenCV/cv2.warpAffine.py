# coding=utf-8
"""
Help on built-in function warpAffine:

def warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) -> dst
    @brief Applies an affine transformation to an image.

    The function warpAffine transforms the source image using the specified matrix:

        dst(x,y) = src(M_{11} * x + M_{12} * y + M_{13}, M_{21} * x + M_{22} * y + M_{23})

    设变换后的图的某个像素点为 (dx, dy)，是由原图的 (sx, sy) 经仿射变换得到的，也即：

        (dx dy).T = M * (sx sy).T

    也即：
        dx = M_{11} * sx + M_{12} * sy + M_{13}
        dy = M_{21} * sx + M_{22} * sy + M_{13}


    when the flag #WARP_INVERSE_MAP is set. Otherwise, the transformation is first inverted
    with #invertAffineTransform and then put in the formula above instead of M. The function cannot
    operate in-place.

    Args:
        * src   : input image.
        * dst   : output image that has the size dsize and the same type as src.
        * M     : transformation matrix with shape `2 * 3`
        * dsize : size of the output image.
        * flags : combination of interpolation methods and the optional
                  flag `WARP_INVERSE_MAP` that means that `M` is the inverse transformation (dst --> src)
"""
import cv2
import numpy as np

im_path = '../../dataset/image/cat.jpeg'
im = cv2.imread(im_path)

# 图像平移
x_shift = 50
y_shift = 100
horizontal_moving_matrix = np.array([[1, 0, x_shift],
                                     [0, 1, y_shift]]).astype(np.float32)

im_height, im_width, _ = im.shape
hm_im = cv2.warpAffine(im, horizontal_moving_matrix, (im_height, im_width))
cv2.imwrite('horizontal_moving.jpg', hm_im)
