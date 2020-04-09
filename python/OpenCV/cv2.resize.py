# coding=utf-8
# Syntax:
#     resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
#
# Parameters:
#     src: source/input image.
#     dsize: desired size for the output image. (out_width, out_height)
#     fx (optional): scale factor along the horizontal axis.
#     fy (optional): scale factor along the vertical axis.
#     interpolation	(optional):
#         * cv2.INTER_NEAREST - a nearest-neighbor interpolation.
#         * cv2.INTER_LINEAR - a bilinear interpolation (used by default).
#         * cv2.INTER_AREA – resampling using pixel area relation.
#         * cv2.INTER_CUBIC – a bicubic interpolation over 4×4 pixel neighborhood.
#         * cv2.INTER_LANCZOS4 – a Lanczos interpolation over 8×8 pixel neighborhood.
import cv2
im_path = '../../dataset/image/cat.jpeg'
im = cv2.imread(im_path)
out_width = 256
out_height = 512
out_size = (out_width, out_height)
im_rs = cv2.resize(im, dsize=out_size, interpolation=cv2.INTER_LINEAR)
cv2.imwrite('resized_image.jpeg', im_rs)
