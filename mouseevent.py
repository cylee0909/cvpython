import cv2
import numpy as np

def drawCircle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img,(x,y),10, (255,0,0), 1)
img = np.zeros((400,400,3), np.uint8)
win = cv2.namedWindow('win')
cv2.setMouseCallback('win', drawCircle)
while True:
    cv2.imshow('win', img)
    key = cv2.waitKey(50)
    print("in drawing...")
    if (key == 27):
        break
cv2.destroyAllWindows()