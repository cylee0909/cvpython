import cv2
import numpy as np
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(r"test.mp4")
while True:
    rect,img=cap.read()
    if rect == True:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imshow("win", gray)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()