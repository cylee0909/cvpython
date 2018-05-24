#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

#knn 算法 又称为k-Nearest Neighbour算法， 是监督学习的一种，会计算待分类个体最邻近的k个邻居，最近的邻居的类别（数目最多的类别）作为自己的类别
# 由于 k为 偶数的时候可能出现无法分类的情况，所以计算类别分类的时候加上权重 又称为modified kNN算法
# knn 算法在数据量很大的时候计算量比较大，但几乎不需要训练数据

# Feature set containing (x,y) values of 25 known/training data
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)

# Labels each one either Red or Blue with numbers 0 and 1
responses = np.random.randint(0,2,(25,1)).astype(np.float32)

# Take Red families and plot them
red = trainData[responses.ravel()==0]
plt.scatter(red[:,0],red[:,1],80,'r','^')

# Take Blue families and plot them
blue = trainData[responses.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')

newcomer = np.random.randint(0,100,(10,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')

# create new knn instance
knn = cv2.ml.KNearest_create()
# print (dir(knn))
# train our data
knn.train(trainData,cv2.ml.ROW_SAMPLE, responses)

ret, results, neighbours ,dist = knn.findNearest(newcomer, 3)

print "result: ", results,"\n"
print "neighbours: ", neighbours,"\n"
print "distance: ", dist

plt.show()