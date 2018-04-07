#encoding:utf-8
import cv2
import numpy as np
img=cv2.imread('cat.jpg')
#simply accessing each and every pixel values and modifying it will be very slow and it is discouraged.
print img[0,0]
print len(img), len(img[0])

#use item/itemset
print img.item(0,0,0) 
img.itemset((10,10,2),0)

#access img shape
print "img shape {}".format(img.shape)
print "img dtype %s"%img.dtype

smallImg=img[0:100, 50:100]
# print img
# print smallImg
# img[50:100, 50:100]=smallImg
#modify one point

img[0,0]=[0,0,0]
cv2.imshow('raw', img)
cv2.imshow('win', smallImg)

b,g,r=cv2.split(img)
print b.shape
cv2.imshow('b', b)
img2 = cv2.merge((b,g,r))
cv2.imshow('im2', img2)

cv2.waitKey(0)
