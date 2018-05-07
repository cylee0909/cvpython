#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('coins.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

#使用形态学开运算 移除图片的白色噪点
#使用形态学闭运算 移除物体上小的洞
# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

# sure background area 膨胀算法，膨胀后黑色区域肯定是背景色
sure_bg = cv2.dilate(opening,kernel,iterations=3)

#如果只是需要对前景物体进行分隔，使用图像腐蚀就可以了
# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5) # 用于计算图像中每一个非零点像素与其最近的零点像素之间的距离
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)

print markers

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0
# markers[sure_bg == 0] = 0


markers = cv2.watershed(img, markers)
img[markers == -1] = [255,0,0]

# plt.subplot(141),plt.imshow(thresh, 'gray')
# plt.subplot(142),plt.imshow(opening, 'gray')
# plt.subplot(143),plt.imshow(sure_fg, 'gray')
# plt.subplot(144),plt.imshow(markers, 'gray')
plt.imshow(img)
plt.show()