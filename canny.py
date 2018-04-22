#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
#canny 算法的主要思想如下：
# 1、 采用高斯滤波平滑图像，去除噪点
# 2、分别计算图像两个方向的一阶差分，然后求出图像梯度幅值和方位角
# 3、对幅值进行非极大值抑制
# 4、双阈值（a,b）排除边缘（只有大于a（强边缘）和介于ab之间且和强边缘相连的像素会被保留）
img = cv2.imread('threshold2.png',0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()