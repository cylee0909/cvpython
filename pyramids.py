#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
#图像金字塔，图像搜寻的过程中有时我们并不知道目标物体在图像中的大小，这时我们需要为图像创建一系列
#不同尺寸的图像，然后在这个图像集合里搜寻目标物体

#laplacian 金字塔来源于高斯金字塔，laplacian金字塔是由同层高斯金字塔图像和其上一层的金字塔图像相减得到的
#

# img=cv2.imread('dog.jpg',0)
# lower_reso=cv2.pyrDown(img)
# lower_reso = cv2.pyrUp(lower_reso)
# cv2.imshow('win', lower_reso)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

A = cv2.imread('apple.png')
B = cv2.imread('orange.png')

A=cv2.resize(A,(256,256))
B=cv2.resize(B,(256,256))

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in xrange(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate laplacian pyramid for A
lpa = [gpA[5]]
for i in xrange(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    print gpA[i-1].shape, GE.shape
    L = cv2.subtract(gpA[i-1], GE)
    lpa.append(L)

# generate laplacian pyramid for B
lpb = [gpB[5]]
for i in xrange(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1], GE)
    lpb.append(L)

L=[]
i=0
for a,b in zip(lpa, lpb):
    rows,cols,dpt=a.shape
    ls=np.hstack((a[:,0:cols/2],b[:,cols/2:]))
    i+=1
    cv2.imwrite(str(i)+".jpg",ls)
    L.append(ls)
# now reconstruct
ls_ = L[0]
for i in xrange(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, L[i])
# image with direct connecting each half
real = np.hstack((A[:,:cols/2],B[:,cols/2:]))

# cv2.imwrite('1.jpg',ls_)
# cv2.imwrite('2.jpg',real)