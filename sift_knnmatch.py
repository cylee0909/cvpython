#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

#basics of brute-force mathcher
# cv2.BFMatcher 第一个参数是计算距离的方法 一般SIFT, SUR 采用 cv2.NORM_L2(欧氏距离) ORB, BRIEF, BRISK采用cv2.NORM_HAMMING(海明距离)
# 第二个参数是crossCheck 如果为true 只会返回相互匹配的特征点
# BFMatcher.match返回最佳匹配，knnMatch返回k个最佳匹配

img1=cv2.imread("cat.jpg",0)
img2=cv2.imread("cat_search.png", 0)
orb=cv2.xfeatures2d.SIFT_create()
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=False)
# Match descriptors.
matches = bf.knnMatch(des1,des2, 2)
# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.65*n.distance:
        good.append([m])
# Draw first 10 matches.
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good, None, flags=2)

plt.imshow(img3),plt.show()