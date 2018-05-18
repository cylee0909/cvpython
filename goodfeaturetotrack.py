#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

imgs=[]
img=cv2.imread("threshold2.png")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#goodfeaturetotrack函数返回 指定数目的角点，可以指定一个quality level（0-1）低于此quality的角点会直接被丢弃掉, 在指定范围内只会返回quality最高的角点
corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

plt.imshow(img),plt.show()