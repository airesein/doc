import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = cv2.imread("./1.png")

def arnold_encode(image, shuffle_times, a, b):
    arnold_image = np.zeros(shape=image.shape)  # 注意缩进！
    h, w = image.shape[0], image.shape[1]
    N = h  # 或N=w
    for time in range(shuffle_times):
        for ori_x in range(h):
            for ori_y in range(w):
                new_x = (1*ori_x + b*ori_y) % N
                new_y = (a*ori_x + (a*b+1)*ori_y) % N
                arnold_image[new_x, new_y, :] = image[ori_x, ori_y, :]
    image = np.copy(arnold_image)
    cv2.imwrite('flag_arnold_encode.png', arnold_image, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
    return arnold_image

def arnold_decode(image, shuffle_times, a, b):
    decode_image = np.zeros(shape=image.shape)  # 注意缩进！
    h, w = image.shape[0], image.shape[1]
    N = h  # 或N=w
    for time in range(shuffle_times):
        for ori_x in range(h):
            for ori_y in range(w):
                new_x = ((a * b + 1) * ori_x + (-b) * ori_y) % N
                new_y = ((-a) * ori_x + ori_y) % N
                decode_image[new_x, new_y, :] = image[ori_x, ori_y, :]
    cv2.imwrite('flag.png', decode_image, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
    return decode_image

# 调用示例
# arnold_encode(img, 1, 2, 3)
arnold_decode(img, 1, 1, -2)
