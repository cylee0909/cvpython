#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
#orb 算法结合 fast特征提取及brief特征描述算法，并做了改进
# 构造金字塔，采用fast特征提取特征点，采用harris角点相应函数选取前N个特征点
# 计算灰度质心的位置，中心位置到灰度质心位置向量的方向定义为特征点的方向
# 将特征点矩阵旋转到主方向steerBRIEF
#搜索计算rBRIEF

img=cv2.imread("threshold2.png", 0)
# Initiate STAR detector
orb = cv2.ORB_create(nfeatures=30)

# find the keypoints with ORB
kp = orb.detect(img,None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img,kp,img, color=(0,255,0), flags=0)
plt.imshow(img2),plt.show()