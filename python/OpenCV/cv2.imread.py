# coding=utf-8
# Syntax:
#     cv2.imread(path, flag)
# Parameters:
#     path: A string representing the path of image to be read.
#     flag: It specifies the way in which image should be read.
#           Its default value is cv2.IMREAD_COLOR.
#           Optional choices: cv2.IMREAD_GRAYSCALE, cv2.IMREAD_UNCHANGED.
import cv2
im_path = '../../dataset/image/cat.png'  # 原图 539KB

# The default value of flag is cv2.IMREAD_COLOR
img_color = cv2.imread(im_path)
cv2.imwrite('color.jpeg', img_color)  # 132 KB

# Loading an image in grayscale
img_grayscale = cv2.imread(im_path, cv2.IMREAD_GRAYSCALE)
cv2.imwrite('grayscale.jpeg', img_grayscale)  # 124KB

# Loading an image as such including alpha channel.
img_unchanged = cv2.imread(im_path, cv2.IMREAD_UNCHANGED)
cv2.imwrite('unchanged.png', img_unchanged)  # 741KB
