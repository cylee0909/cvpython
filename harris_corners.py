#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

imgs=[]
img=cv2.imread("threshold2.png")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

imgs.append(gray)
harris = cv2.cornerHarris(gray,2,3,0.04)
imgs.append(harris)
#result is dilated for marking the corners, not important
dilate = cv2.dilate(harris,None)
imgs.append(dilate)

#如果对精度有更高的要求，可以使用cornerSubPix进行亚像素级别的角点检测
ret, threshold = cv2.threshold(dilate,0.01*dilate.max(),255,0)
threshold_raw = np.uint8(threshold)

imgs.append(threshold_raw)
# find centroids
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(threshold_raw)

# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

# Now draw them
res = np.hstack((centroids,corners))
res = np.int0(res)
print res
img[res[:,1],res[:,0]]=[0,0,255]
img[res[:,3],res[:,2]] = [0,255,0]


# # Threshold for an optimal value, it may vary depending on the image.
# img[dst>0.01*dst.max()]=[0,0,255]
# cv2.imshow('dst',img)
imgLen = len(imgs)
for i in range(0, imgLen) :
    plt.subplot(1, imgLen, i + 1),plt.imshow(imgs[i], 'gray')
plt.show()