#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
#静态迭代图割算法
#给定一个矩形 矩形外部为背景区域，内部不确定区域
#使用高斯混合模型（GMM）对前景背景进行分类
#GMM会对矩形内部的不确定区域进行分类，依据每个点和已确定标记点的关系给出每个点属于背景或者前景的几率
#根据GMM结果绘制图结构，每个不确定点都是树的叶子，另外会添加两个特殊的节点（Source node and Sink node）forgound 节点与source node相连，backgraound与sink node相连
#与 source node或者 sink node相连的边的权重用于标识改点属于前景或者背景可信度，叶子之间边表达两像素点的相似度
#使用 mincut算法来分割图为背景与前景，mincut算法保证分割边界weight和最小，分割后与source node相连的为前景，与sink相连的为背景
#重复上述步骤直至收敛

img=cv2.imread('dog.jpg')
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
# print img.shape
rect = (57,32,330,240)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8') #将背景或者可能为背景的区域置为0
imgresult = img*mask2[:,:,np.newaxis]


newmask = np.zeros(img.shape[:2],np.uint8)
for i in range(247, 280):
    for j in range(226, 311):
        newmask[i,j] = 1
cv2.grabCut(img,newmask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
newmask = np.where((newmask==2)|(newmask==0),0,1).astype('uint8') #将背景或者可能为背景的区域置为0
imgresult2 = img*newmask[:,:,np.newaxis]

plt.subplot(131),plt.imshow(img)
plt.subplot(132),plt.imshow(imgresult)
plt.subplot(133),plt.imshow(imgresult2)
plt.show()