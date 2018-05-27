#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

#svm 算法是通过一定策略找出数据的支持平面对数据进行分类的一种算法
# 对于非线性分类的数据，一般可以通过提升维度来达到转换为线性分类的目的
# 一般而言，我们可以在现有的维度内通过一定的运算逻辑，来计算高维的一些特征值
#  为了降低误分类的数据，\xi_i 被定义成 其位置点与支持平面的距离，所以各个点\xi_i的和越小，误分类的几率越低

# 手写识别
# 图像透视矫正
# def deskew(img):
#     m = cv2.moments(img)
#     if abs(m['mu02']) < 1e-2:
#         return img.copy()
#     skew = m['mu11']/m['mu02']
#     M = np.float32([[1, skew, -0.5*SZ*skew], [0, 1, 0]])
#     img = cv2.warpAffine(img,M,(SZ, SZ),flags=affine_flags)
#     return img
# 使用  Histogram of Oriented Gradients (HOG) 作为特征向量
# def hog(img):
#     gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
#     gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
#     # 计算大小方向
#     mag, ang = cv2.cartToPolar(gx, gy)

#     # quantizing binvalues in (0...16)
#     bins = np.int32(bin_n*ang/(2*np.pi))

#     # Divide to 4 sub-squares
#     bin_cells = bins[:10,:10], bins[10:,:10], bins[:10,10:], bins[10:,10:]
#     mag_cells = mag[:10,:10], mag[10:,:10], mag[:10,10:], mag[10:,10:]
#     hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
#     hist = np.hstack(hists)
#     return hist


SZ=20
bin_n = 16 # Number of bins

affine_flags = cv2.WARP_INVERSE_MAP|cv2.INTER_LINEAR

def deskew(img):
    m = cv2.moments(img)
    if abs(m['mu02']) < 1e-2:
        return img.copy()
    skew = m['mu11']/m['mu02']
    M = np.float32([[1, skew, -0.5*SZ*skew], [0, 1, 0]])
    img = cv2.warpAffine(img,M,(SZ, SZ),flags=affine_flags)
    return img

def hog(img):
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
    mag, ang = cv2.cartToPolar(gx, gy)
    bins = np.int32(bin_n*ang/(2*np.pi))    # quantizing binvalues in (0...16)
    bin_cells = bins[:10,:10], bins[10:,:10], bins[:10,10:], bins[10:,10:]
    mag_cells = mag[:10,:10], mag[10:,:10], mag[:10,10:], mag[10:,10:]
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists)     # hist is a 64 bit vector
    return hist

img = cv2.imread('digits.png',0)

cells = [np.hsplit(row,100) for row in np.vsplit(img,50)]

# First half is trainData, remaining is testData
train_cells = [ i[:50] for i in cells ]
test_cells = [ i[50:] for i in cells]

######     Now training      ########################

deskewed = [map(deskew,row) for row in train_cells]
hogdata = [map(hog,row) for row in deskewed]
trainData = np.float32(hogdata).reshape(-1,64)
responses = np.float32(np.repeat(np.arange(10),250)[:,np.newaxis])

trainingDataMat = np.array(trainData, np.float32)
labelsMat = np.array([responses], np.int32)


# svm_params = dict( kernel_type = cv2.ml.SVM_LINEAR,
#                     svm_type = cv2.ml.SVM_C_SVC,
#                     C=2.67, gamma=5.383 )
svm = cv2.ml.SVM_create()
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setC(2.67)
svm.setGamma(5.383)
svm.train(trainingDataMat,cv2.ml.ROW_SAMPLE,labelsMat)
svm.save('svm_data.dat')

######     Now testing      ########################

deskewed = [map(deskew,row) for row in test_cells]
hogdata = [map(hog,row) for row in deskewed]
testData = np.float32(hogdata).reshape(-1,bin_n*4)
# print dir(svm)
result = svm.predict(testData)[1]

print result
#######   Check Accuracy   ########################
mask = result == responses
correct = np.count_nonzero(mask)
print correct*100.0/len(result)

