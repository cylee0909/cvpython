import cv2
import numpy as np

img=np.zeros((400,400,3), np.uint8)
cv2.namedWindow('win')

def onTrack(value):
    pass

cv2.createTrackbar('R', 'win', 0, 255, onTrack)
cv2.createTrackbar('G', 'win', 0, 255, onTrack)
cv2.createTrackbar('B', 'win', 0, 255, onTrack)
switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch, 'win', 0, 1, onTrack)

while True:
    cv2.imshow('win', img)
    if (cv2.waitKey(1) == 27) :
        break
    r = cv2.getTrackbarPos('R', 'win')
    g = cv2.getTrackbarPos('G', 'win')
    b = cv2.getTrackbarPos('B', 'win')
    s = cv2.getTrackbarPos(switch, 'win')
    if (s == 0):
        img[:]=0
    else:
        img[:]=[b,g,r]
cv2.destroyAllWindows()