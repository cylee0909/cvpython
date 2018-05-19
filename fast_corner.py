#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

# fast算法 认为在某个像素(值为lp)大小为16的圆山有连续n个像素点，他们的值 >= lp + t或者 <= lp - t, 那么它是一个角点，一般n取9效果比较好
# 为进一步优化算法速度 一般检测1 9 5 13四个位置，如果p为角点那么一般会有至少3个点满足1
# 为解决 n < 12时无法用快速算法、检测的角点有可能不是最优的，因为他的效率取决于问题的排序和角点的分布、快速检测的结果被丢弃，我们通常使用机器学习实现一个角点分类器
    # 角点分类器
    # 搜集测试图片
    # 运行fast角点检测来获取测试图片上的所有角点特征
    # 对于每个角点 将邻域圆上16个点存储下来保存在一个vector中，对于邻域圆上点进行分类，darker similar brighter（pb, ps, pd）,并将其存储在P中
    # 定义kp 如果p为角点 kp为true
    # 使用ID3算法（决策树分类器）来查询每一个子集
    # 递归计算所有的子集直到Kp的熵为0
    # 被创建的决策树就用于于其他图片的FAST检测

img = cv2.imread('threshold2.png',0)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()
# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2)
plt.show()
