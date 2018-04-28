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
_,contours,hierarchy=cv2.findContours(thresh,1,2)
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
img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

cv2.imshow("win", img)
cv2.waitKey(0)
cv2.destroyAllWindows()