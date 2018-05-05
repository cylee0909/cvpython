#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
#霍夫变换，检测直线时可以看作是一种投票系统，将点转换为p=x*sin(a)+y*cos(a)的形式
#opencv 中 cv2.HoughLines() 
img = cv2.imread('threshold2.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #get the gray image

plt.subplot(131),plt.imshow(gray, 'gray')
edges = cv2.Canny(gray,50,150,apertureSize = 3) # get the edge image

plt.subplot(132),plt.imshow(edges, 'gray')
# first param is the image, we should pass the edge image
# second param is p accuracies
# third param is the a aacuracies
# fourth param is the vote threshold  
lines = cv2.HoughLines(edges,1,np.pi/180,120) # detect the lines
for line in lines:
    for rho,theta in line:
        print rho, theta
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)
plt.subplot(133)
plt.imshow(img, 'gray')
plt.show()


#Probabilistic Hough Transform
# 提高霍夫变换的计算速度，并不计算所有的点，而是计算一个随机集合的系列点
# img = cv2.imread('dave.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,50,150,apertureSize = 3)
# minLineLength = 100
# maxLineGap = 10
# lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
# for x1,y1,x2,y2 in lines[0]:
#     cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

# cv2.imwrite('houghlines5.jpg',img)


# 霍夫圆检测，
# img = cv2.imread('opencv_logo.png',0)
# img = cv2.medianBlur(img,5)
# cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

# circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
#                             param1=50,param2=30,minRadius=0,maxRadius=0)

# circles = np.uint16(np.around(circles))
# for i in circles[0,:]:
#     # draw the outer circle
#     cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
#     # draw the center of the circle
#     cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

# cv2.imshow('detected circles',cimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()