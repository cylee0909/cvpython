import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("cat.jpg",0)
print img.shape
smallImg = cv2.resize(img, None, fx=0.5,fy=0.5, interpolation=cv2.INTER_CUBIC)
print smallImg.shape

rows,cols = img.shape
#transform img
M = np.float32([[1,0,100],[0,1,50]])
trans = cv2.warpAffine(img,M,(cols,rows))

#rotate img
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
rotate=cv2.warpAffine(img, M,(cols, rows))

#use three point
# pts1 = np.float32([[50,50],[200,50],[50,200]])
# pts2 = np.float32([[10,100],[200,50],[100,250]])
# M = cv2.getAffineTransform(pts1,pts2)
# dst = cv2.warpAffine(img,M,(cols,rows))
# plt.subplot(121),plt.imshow(img, 'gray'),plt.title('Input')
# plt.subplot(122),plt.imshow(dst, 'gray'),plt.title('Output')
# plt.show()

#use four point 透视变换
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

# cv2.imshow('img',rotate)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

