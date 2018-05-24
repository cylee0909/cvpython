#encoding:utf-8
#直方图反向投影
import cv2
import numpy as np
from matplotlib import pyplot as plt

#roi is the object or region of object we need to find
roi = cv2.imread('dog_clip.jpg')
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

#target is the image we search in
target = cv2.imread('dog.jpg')
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

# Find the histograms using calcHist. Can be done with np.histogram2d also
M = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
I = cv2.calcHist([hsvt],[0, 1], None, [180, 256], [0, 180, 0, 256] )
print len(M), len(I), len(M[0]), len(I[0])
# print I
R=M/I #计算 h&s 目标图片和搜寻图片的比值
h,s,v = cv2.split(hsvt)
print len(h), len(h.ravel())
B = R[h.ravel(),s.ravel()]
print len(B)
B = np.minimum(B,1) #b(x,y) = min(b(x,y),1)
B = B.reshape(hsvt.shape[:2])

disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(B,-1,disc,B) #滤波
B = np.uint8(B)
cv2.normalize(B,B,0,255,cv2.NORM_MINMAX) #归一化，换算到0-255之间

ret,thresh = cv2.threshold(B,50,255,0) #二值化 

#使用opencv提供的函数
roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)

# Now convolute with circular disc
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(dst,-1,disc,dst)

# threshold and binary AND
ret,thresh = cv2.threshold(dst,50,255,0)
thresh = cv2.merge((thresh,thresh,thresh))
res = cv2.bitwise_and(target,thresh)

res = np.vstack((target,thresh,res))
plt.imshow(res)
plt.show()




