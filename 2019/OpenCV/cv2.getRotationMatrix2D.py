# coding=utf-8
"""
def getRotationMatrix2D(center, angle, scale) -> retval

    Args:
        * center : Center of the rotation in the source image.
        * angle  : Rotation angle in degrees. Positive values mean counter-clockwise rotation.
        * scale  : isotropic scale factor.

    Returns:
        * retval : matrix whose dimension is 2 * 3:
            [[alpha, beta, (1 - alpha) * center.x - beta * center.y],
             [-beta, alpha, beta*center.x + (1 - alpha) * center.y]]

          where:
            alpha = scale * cos(angle)
            beta = sclae * sin(angle)
"""
import cv2
import numpy as np

im_path = '../../dataset/image/cat.jpeg'
im = cv2.imread(im_path)

im_height, im_width, im_channel = im.shape

rotate_matrix = cv2.getRotationMatrix2D((im_height / 2, im_width / 2), 45, 1)

rotate_im = cv2.warpAffine(im, rotate_matrix, (im_height, im_width))
cv2.imwrite('rotate_image.png', rotate_im)
