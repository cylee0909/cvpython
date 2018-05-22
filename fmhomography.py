#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

imgs=[]

img1=cv2.imread("cat.jpg",0)
img2=cv2.imread("cat_search.png", 0)
orb=cv2.xfeatures2d.SIFT_create()
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1,des2,k=2)

# store all the good matches as per Lowe's ratio test.
good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)

# print type(kp1[0])
if (len(good) > 10):
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()
    h,w = img1.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    print len(pts), len(pts[0])
    print pts
    dst = cv2.perspectiveTransform(pts,M)

    print len(dst), len(dst[0])
    # print dst
    print np.int32(dst)
    cv2.polylines(img2,[np.int32(dst)],True,(0,255,255))
    # img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)
    # imgs.append(img2)
else:
    print "Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT)
    matchesMask = None

draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   matchesMask = matchesMask, # draw only inliers
                   flags = 2)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
imgs.append(img3)

imgLen = len(imgs)
for i in range(0, imgLen) :
    plt.subplot(1, imgLen, i + 1),plt.imshow(imgs[i], 'gray')
plt.show()