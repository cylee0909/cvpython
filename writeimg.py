import cv2
import numpy as np
img = cv2.imread("cat.jpg",0)
win = cv2.namedWindow('win',cv2.WINDOW_NORMAL)
cv2.imshow('win', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    # write an image
    cv2.imwrite("cat2.jpg", img)