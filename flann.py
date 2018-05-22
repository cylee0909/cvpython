#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

#flann 在匹配更大维度或者更大的数据集时速度会更快
# 第一个参数SIFT, SURF 一般传index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
# 对于orb 一般传index_params= dict(algorithm = FLANN_INDEX_LSH,
                #    table_number = 6, # 12
                #    key_size = 12,     # 20
                #    multi_probe_level = 1) #2
# 第二个参数指定递归的次数，越大越精确，速度也越慢 search_params = dict(checks=100)

img1=cv2.imread("cat.jpg",0)
img2=cv2.imread("cat_search.png", 0)
orb=cv2.xfeatures2d.SIFT_create()
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary

flann = cv2.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des1,des2,k=2)

# Need to draw only good matches, so create a mask
matchesMask = [[0,0] for i in xrange(len(matches))]

# ratio test as per Lowe's paper
for i,(m,n) in enumerate(matches):
    if m.distance < 0.6*n.distance:
        matchesMask[i]=[1,0]

draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = 0)

# img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)

g=[]
for a , b in matches:
    if (a.distance < 0.5 * b.distance):
        g.append([a])
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,g,None,flags=2)

plt.imshow(img3,),plt.show()