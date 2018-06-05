#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

#No-local Means Denoising 算法，基本思想是先寻找相似的窗口，对相似的窗口取均值替换原来窗口的数据
img=cv2.imread("nldenoise.png")
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
plt.show()