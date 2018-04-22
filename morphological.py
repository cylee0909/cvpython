#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('j.png')
#erosion腐蚀算法,通常用一个kernal滑过整张图片，只有整个kernel下的图像都是非零的时候才设置中心点图像非零。
#主要用于移除小的白色噪点，切断相连的物体等
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
#Dilation 膨胀算法，与腐蚀相反
dilation = cv2.dilate(img,kernel,iterations = 1)
#open 开运算，先腐蚀后膨胀，消除噪点
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#close 闭运算，先膨胀后腐蚀，用于消除图像中小黑洞
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#MORPH_GRADIENT 形态学梯度运算，膨胀图和腐蚀图相减，用于突出轮廓
gradient=cv2.morphologyEx(img, cv2.MORPH_GRADIENT,kernel)
#top hat 原图像减去开运算的过程，主要用于矫正不均匀光照的影响
topHat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT, kernel)
#black hat 闭运算的图像减去原图像，主要用于突出比原图轮廓周围更暗的区域
blackHat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
#getStructuringElement方法创建特定形状的kernal
mat = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
print mat
cv2.imshow('win', blackHat)
cv2.waitKey(0)
cv2.destroyAllWindow()