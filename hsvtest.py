#encoding:utf-8
import cv2
import numpy as np
raw=cv2.imread('frame.jpg')
hsv = cv2.cvtColor(raw, cv2.COLOR_BGR2HSV)
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
mask=cv2.inRange(hsv, lower_blue, upper_blue)
cv2.imshow('win', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()