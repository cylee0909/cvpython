import cv2
import numpy as np
img=cv2.imread('cat.jpg')
BLUE = [255,0,0]
print img.shape
newImg = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
print newImg.shape
cv2.imshow('win', newImg)
cv2.waitKey(0)