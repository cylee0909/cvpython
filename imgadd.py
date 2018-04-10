#encoding:utf-8
import cv2
import numpy as np
cat=cv2.imread('cat.jpg')
dog=cv2.imread('dog.jpg')

#get the gray img
grayCat = cv2.cvtColor(cat, cv2.COLOR_BGR2GRAY)
#阈值处理 http://www.opencv.org.cn/opencvdoc/2.3.2/html/doc/tutorials/imgproc/threshold/threshold.html
ret, mask = cv2.threshold(grayCat, 100, 255, cv2.THRESH_BINARY)
# print ret
# cv2.imshow('grayCat',mask)
maskInv = cv2.bitwise_not(mask)
result = cv2.bitwise_and(grayCat,grayCat,mask = maskInv)
cv2.imshow('maskInv',result)

# rows,cols,channel=cat.shape
# roi = dog[0:rows, 0:cols ]
# result=cv2.addWeighted(cat, 0.2, roi, 0.8, 0)
# cv2.imshow('win', result)
#performance measure
#python scalar operate are fast than np, opencv function are fast than np
cv2.waitKey(0)
cv2.destroyAllWindows()