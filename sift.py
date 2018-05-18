#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
#sift 算法
#sift具有空间不变性
#此算法在高斯金字塔上计算dog代替log
#在不同层的dog上计算关键点（领域极大值），并计算其精确值（泰勒展开并差值），移除边缘点
#利用关键点邻域方向并使用直方图统计获得主方向
#关键点特征值使用16个领域4x4大小区域的8特征值来描述
#关键点匹配，关键点匹配中舍去第二相似度与最相似比值大于0.8的点，这样会舍去90%的错误匹配点和5%正确点
#由于sift算法是有专利的，其并不在opencv的核心模块中实现，需要安装contrib (python -m pip install opencv-contrib-python --user)
img = cv2.imread('threshold2.png')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)
# 计算特征向量
# kp,des = sift.compute(gray,kp)
# kp, des = sift.detectAndCompute(gray,None)

img=cv2.drawKeypoints(gray,kp,img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# it will draw a circle with size of keypoint and it will even show its orientation
# img=cv2.drawKeypoints(gray,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.plot(),plt.imshow(img, 'gray')
plt.show()
