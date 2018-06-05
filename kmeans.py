#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

# kmeans算法
# 1选取n个初始点，将数据根据距离初始点的距离分成n份
# 计算这n份数据的中心点，作为初始点迭代
# 直至稳定

# x = np.random.randint(25,100,25)
# y = np.random.randint(175,255,25)
# z = np.hstack((x,y))
# z = z.reshape((50,1))
# z = np.float32(z)

# # Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# # Set flags (Just to avoid line break in the code)
# flags = cv2.KMEANS_RANDOM_CENTERS
# # Apply KMeans
# compactness,labels,centers = cv2.kmeans(z,2,None,criteria,10,flags)
# # 1p data, 2p group count, 3p bestLabels,
# # 4p criteria, (type, max_iter(最大迭代次数), epsilon（精度）)
# # 5p attempts, 6p flags(cv2.KMEANS_PP_CENTERS and cv2.KMEANS_RANDOM_CENTERS)
# print centers
# A = z[labels==0]
# B = z[labels==1]

# # Now plot 'A' in red, 'B' in blue, 'centers' in yellow
# plt.hist(A,256,[0,256],color = 'r')
# plt.hist(B,256,[0,256],color = 'b')
# plt.hist(centers,256,[0,256],color = 'y')
# plt.show()

img = cv2.imread('cat.jpg')
Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 3
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
print center
print label
res = center[label.flatten()]
res2 = res.reshape((img.shape))

img_bgr = res2
img_rgb = np.zeros(img_bgr.shape, img_bgr.dtype)
img_rgb[:,:,0] = img_bgr[:,:,2]
img_rgb[:,:,1] = img_bgr[:,:,1]
img_rgb[:,:,2] = img_bgr[:,:,0]

plt.imshow(img_rgb)
plt.show()