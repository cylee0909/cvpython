#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plot
img=cv2.imread('threshold.png', 0)
img2=cv2.imread('threshold2.png', 0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

ret,t8=cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)
t6=cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 6)
t7=cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 6)
titles=['original', 'binary', 'binary_inv', 'trunc', 'tozero', 'tozero_inv', 'binary2', 'adaptiveMean', 'adaptiveGaussian']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5, t8, t6, t7]
for i in xrange(9):
    plot.subplot(3, 3, i + 1)
    plot.imshow(images[i],cmap='gray')
    plot.title(titles[i])
    plot.xticks([])
    plot.yticks([])
plot.show()