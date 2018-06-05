#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

def showImgs(imgs):
    imgLen = len(imgs)
    for i in range(0, imgLen) :
        plt.subplot(1, imgLen, i + 1),plt.imshow(imgs[i], 'gray')
    plt.show()