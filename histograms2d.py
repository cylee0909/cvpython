#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cat.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
# histogram in numpy
# hist, xbins, ybins = np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])
print len(hist) ,len(hist[0])
plt.imshow(hist,interpolation = 'nearest')
plt.show()