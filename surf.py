#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
#surf 算法，对sift算法进行改进，优化计算速度, 实验证明，SURF算法较SIFT在运算速度上要快3倍左右
# 使用box filter替代dog
# 使用hessian矩阵进行缩放和关键点定位
# 主角度计算上，surf算法采用水平竖直方向的wavelet responses