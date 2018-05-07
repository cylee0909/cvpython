#encoding:utf-8
import cv2
import numpy as np
#图像轮廓
img=cv2.imread('cat.jpg')
#灰度化
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#二值化
ret,thresh=cv2.threshold(imgray,127,255,0)
#查找所有轮廓，查找轮廓需要在二值化图像中进行，从黑色背景中找出白色元素的轮廓
# Contour Retrieval Mode  cv2.RETR_LIST, cv2.RETR_TREE, cv2.RETR_CCOMP, cv2.RETR_EXTERNAL
_,contours,hierarchy=cv2.findContours(thresh,1,2)
# 其中 RETR_LIST 代表轮廓间无层级关系 RETR_EXTERNAL 只返回外部轮廓，内部轮廓被忽略 
# RETR_CCOMP 这个会将轮廓分为两级 最外层的轮廓为h1 其子轮廓为h2 h2的子轮廓为h1
# RETR_TREE 树形结构

#轮廓相关参数
cnt = contours[0]
#计算轮廓的矩
M = cv2.moments(cnt)
#计算轮廓的中心点
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
#计算轮廓的面积
area = cv2.contourArea(cnt) #or M['m00']
#计算轮廓的周长
perimeter = cv2.arcLength(cnt,True)
#轮廓的近似，Douglas–Peucker algorithm算法，采用多段直线逼近轮廓，其中epsilon为最大边距，用于控制逼近精度
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
#凸包 convex hull
# hull = cv2.convexHull(points[, hull[, clockwise[, returnPoints]]
hull = cv2.convexHull(cnt)
#检查一个轮廓是否为凸包
k = cv2.isContourConvex(cnt)
#查找外接矩形，此方法不考虑旋转，因此可能不是最小矩形
x,y,w,h = cv2.boundingRect(cnt)
#查找最小矩形，cv2.minAreaRect()，此方法返回一个Box2d的结构，（(x,y),(w,h),rotation）,因此我们可以通过cv2.boxPoints()将此结构转换为4个顶点的矩形
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
print box

#计算点到轮廓的距离,当点在轮廓外部时返回负数，内部时返回正数，最后一个参数是否计算距离，false时只检测相对位置 返回 +1 -1 0
dist = cv2.pointPolygonTest(cnt,(50,50),True)
#计算轮廓的相似度，值越小越相似 cv2.matchShapes,算法基于hu-moment, 这些矩具有位移旋转缩放不变的性质
ret = cv2.matchShapes(cnt,cnt,1,0.0)


#计算宽长比
aspect_ratio = float(w)/h
#计算extent
rect_area = w * h
extent = float(area) / rect_area
#计算solidity
hull_area = cv2.contourArea(hull)
solidity=float(area)/hull_area
#计算当量直径 Equivalent Diameter 面积等于已知轮廓面积圆的半径
equi_diameter = np.sqrt(4*area/np.pi)
# 计算轮廓方向 
(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)
#获取mask
mask = np.zeros(imgray.shape,np.uint8)
cv2.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
#pixelpoints = cv2.findNonZero(mask)
# print "mask-->", pixelpoints
#获取最大值最小值及他们的位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imgray,mask = mask)
#获取平均色值
mean_val = cv2.mean(im,mask = mask)
#获取边界点
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

img = cv2.drawContours(img,[box],0,(0,0,255),1)
print img.shape

#查找最小轮廓圆 cv2.minEnclosingCircle() 
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(0,255,0),2)

#查找最小轮廓椭圆 cv2.fitEllipse() 
ellipse = cv2.fitEllipse(cnt)
img = cv2.ellipse(img,ellipse,(0,255,0),2)

#查找匹配直线
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
# img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

cv2.imshow("win", img)
cv2.waitKey(0)
cv2.destroyAllWindows()