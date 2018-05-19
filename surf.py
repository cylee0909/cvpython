#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
#surf 算法，对sift算法进行改进，优化计算速度, 实验证明，SURF算法较SIFT在运算速度上要快3倍左右
# 使用box filter替代dog
# 采用改变滤波sigma而不改变图像尺寸来计算图像金字塔
# 主角度计算上，统计特征点领域内的Harr小波特征
# 特征描述子 使用16 x haar小波特征为水平方向值之和，水平方向绝对值之和，垂直方向之和，垂直方向绝对值之和
img = cv2.imread("threshold2.png", 0)
surf = cv2.xfeatures2d.SURF_create(400)
print surf.getUpright()
# set the up right 不再检测方向，加快速度
surf.setUpright(True) 
kp, des = surf.detectAndCompute(img,None)
print len(kp), des.shape

img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()