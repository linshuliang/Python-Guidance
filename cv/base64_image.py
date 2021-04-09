# coding=utf-8
import base64
import cv2

# 图片转 base64 字符串
with open("girl1.jpeg", "rb") as fr:
    base64_data = base64.b64encode(fr.read())

# base64 字符串转图片
with open("girl_decode.jpeg", "wb") as fw:
    img_data = base64.b64decode(base64_data)
    fw.write(img_data)
