#encoding:utf-8
#模板匹配
import cv2
import numpy as np
from matplotlib import pyplot as plt
#模板匹配采用窗口滑动机制来进行目标匹配，cv2.matchTemplate() 返回滑动匹配的匹配度
#采用cv2.minMaxLoc()方法可以得到最大值或者最小值

img = cv2.imread('dog.jpg',0)
img2 = img.copy()
template = cv2.imread('dog_clip.jpg',0)
w, h = template.shape[::-1]

# CV_TM_SQDIFF 平方差匹配法：该方法采用平方差来进行匹配；最好的匹配值为0；匹配越差，匹配值越大。
# CV_TM_CCORR 相关匹配法：该方法采用乘法操作；数值越大表明匹配程度越好。
# CV_TM_CCOEFF 相关系数匹配法：1表示完美的匹配；-1表示最差的匹配。
# CV_TM_SQDIFF_NORMED 归一化平方差匹配法
# CV_TM_CCORR_NORMED 归一化相关匹配法
# CV_TM_CCOEFF_NORMED 归一化相关系数匹配法

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()


#多个匹配
# img_rgb = cv2.imread('mario.png')
# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# template = cv2.imread('mario_coin.png',0)
# w, h = template.shape[::-1]

# res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# threshold = 0.8
# loc = np.where( res >= threshold)
# for pt in zip(*loc[::-1]):
#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

# cv2.imwrite('res.png',img_rgb)