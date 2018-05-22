#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

# brif is a faster method feature descriptor calculation and matching

img=cv2.imread("threshold2.png", 0)
# Initiate STAR detector
star = cv2.xfeatures2d.StarDetector_create()

# Initiate BRIEF extractor
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

# find the keypoints with STAR
kp = star.detect(img,None)
# compute the descriptors with BRIEF
kp, des = brief.compute(img, kp)

print kp
print des.shape