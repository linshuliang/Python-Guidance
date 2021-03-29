# coding=utf-8
# Syntax
#     cv2.meanStdDev(src[, mean[, stddev[, mask]]]) -> mean, stddev
#     .   Calculates a mean and standard deviation of array elements.
#     .
#     .   The function cv::meanStdDev calculates the mean and the standard deviation M
#     .   of array elements independently for each channel and returns it via the
#     .   output parameters:
#     .   When all the mask elements are 0's, the function returns
#     .   mean=stddev=Scalar::all(0).
#     .   @note The calculated standard deviation is only the diagonal of the
#     .   complete normalized covariance matrix. If the full matrix is needed, you
#     .   can reshape the multi-channel array M x N to the single-channel array
#     .   M\*N x mtx.channels() (only possible when the matrix is continuous) and
#     .   then pass the matrix to calcCovarMatrix .
#     .   @param src input array that should have from 1 to 4 channels so that the results can be stored in
#     .   Scalar_ 's.
#     .   @param mean output parameter: calculated mean value.
#     .   @param stddev output parameter: calculated standard deviation.
#     .   @param mask optional operation mask.
import cv2

im = cv2.imread('../../dataset/image/cat.jpeg')
im_mean, im_stddev = cv2.meanStdDev(im)

print('im_mean=\n{}\n'.format(im_mean))
'''
[[146.27405614]
 [147.0985108 ]
 [150.8452228 ]]
'''

print('im_stddev=\n{}\n'.format(im_stddev))
'''
[[66.87040978]
 [64.36625361]
 [61.33287371]]
'''
