#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
# img=cv2.imread('cat.jpg',0)
#calc histogram cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
# channels 图像channelindex
# print img.shape
# hist = cv2.calcHist([img],[0],None,[256],[0,256])
# calc histogram use numpy
# hist,bins = np.histogram(img.ravel(),256,[0,256])
#hist = np.bincount(img.ravel(),minlength=256)会更快一点
# plt.hist(img.ravel(),256,[0,256]); plt.show()

# img = cv2.imread('dog.jpg')
# color = ('b','g','r')
# for i,col in enumerate(color):
#     histr = cv2.calcHist([img],[i],None,[256],[0,256])
#     plt.plot(histr,color = col)
#     plt.xlim([0,256])
# plt.show()


img = cv2.imread('dog.jpg',0)
hist,bins=np.histogram(img.flatten(),256, [0,256])
cdf = hist.cumsum() #计算累加值
# cdf_normalized = cdf * hist.max()/ cdf.max() #计算累加灰度分布
# plt.plot(cdf_normalized, color = 'b')
# plt.hist(img.flatten(), 256, [0,256], color='r')
# plt.xlim([0,256])
# plt.legend(('cdf','histogram'), loc = 'upper left')
# plt.show()

#直方图均衡 使用numpy来计算
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_equalization/py_histogram_equalization.html#histogram-equalization 直方图均衡
# cdf_m=np.ma.masked_equal(cdf, 0) #get the masked array
# cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min()) #get the map
# cdf = np.ma.filled(cdf_m,0).astype('uint8') #fill the masked
# img2=cdf[img]

# cdf_m=np.ma.masked_equal(cdf, 0)
# imgW=img.shape[0]
# imgH=img.shape[1]
# area=imgW * imgH
# cdf_m = ((cdf_m)*255./area).astype('uint8') # 按照《数字图像处理第三版》直方图均衡定义来处理

# img2=cdf_m[img]
# hist,bins=np.histogram(img2.flatten(),256, [0,256])
# cdf = hist.cumsum() #计算累加值
# cdf_normalized = cdf * hist.max()/ cdf.max() #计算累加灰度分布
# plt.plot(cdf_normalized, color = 'b')
# plt.hist(img2.flatten(), 256, [0,256], color='r')
# plt.xlim([0,256])
# plt.legend(('cdf','histogram'), loc = 'upper left')
# plt.show()

equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))

#限制对比度自适应直方图均衡化
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

result=np.hstack((res,cl1))
plt.imshow(result,'gray')

plt.show()


