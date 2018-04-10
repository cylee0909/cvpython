#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('otsubinary.png', 0)
gaussian=cv2.GaussianBlur(img,(5,5), 0)
_,th1=cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_,th2=cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_,th3=cv2.threshold(gaussian, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
imgs=[img, 0, th1,
        img, 0, th2,
        gaussian, 0, th3]

for i in xrange(3):
    plt.subplot(3,3, i * 3 + 1)
    plt.imshow(imgs[i*3], 'gray')
    plt.xticks([]),plt.yticks([])
    plt.subplot(3,3, i * 3 + 2)
    plt.hist(imgs[i*3].ravel(), 256) 
    plt.xticks([]),plt.yticks([])
    plt.subplot(3,3, i * 3 + 3)
    plt.imshow(imgs[i*3+2], 'gray')
    plt.xticks([]),plt.yticks([])
plt.show()