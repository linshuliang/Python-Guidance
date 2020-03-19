# coding=utf-8
# help(cv2.rectangle)
# Syntax:
#     rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
#     .   @brief Draws a simple, thick, or filled up-right rectangle.
#     .
#     .   The function cv::rectangle draws a rectangle outline or a filled rectangle
#     .   whose two opposite corners are pt1 and pt2.
#     .
#     .   @param img Image.
#     .   @param pt1 Vertex of the rectangle.
#     .   @param pt2 Vertex of the rectangle opposite to pt1.
#     .   @param color Rectangle color or brightness (grayscale image).
#     .   @param thickness Thickness of lines that make up the rectangle.
#     .   Negative values, like #FILLED, mean that the function has to draw a filled rectangle.
#     .   @param lineType Type of the line. See #LineTypes
#     .   @param shift Number of fractional bits in the point coordinates.
import cv2

im_path = '../../dataset/image/cat.jpeg'
org_im = cv2.imread(im_path)
im = cv2.rectangle(img=org_im,
                   pt2=(5, 20),
                   pt1=(100, 200),
                   color=(255, 0, 0),
                   thickness=2)

cv2.imwrite('im_rectangle.jpg', im)
