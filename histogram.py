#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('cat.jpg',0)
hist,bins = np.histogram(img.flatten(),256,  [0,256])
print hist
print bins
