# coding=utf-8
import cv2
import numpy as np
from PIL import Image


def PILImageToCV(img):
    """
    Transfer PIL Image to cv2 image.

    Args:
        img (PIL.PngImagePlugin.PngImageFile): input image

    Returns:
        im_arr (numpy.ndarray): output image.
    """
    im_arr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    return im_arr


def CVToPILImage(im):
    """
    Tranfer cv2 image to PIL Image.

    Args:
        im (numpy.ndarray): input image.

    Returns:
        img (PIL.PngImagePlugin.PngImageFile): output image.
    """
    img = Image.fromarray(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
    return img


im_path = '../../dataset/image/cat.jpeg'
im_arr = cv2.imread(im_path)
img = Image.open(im_path)

im_trans_arr = PILImageToCV(img)
img_trans = CVToPILImage(im_arr)
