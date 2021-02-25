import cv2
import numpy as np


def listener(x):
    pass


cv2.namedWindow("Trackbar")
cv2.createTrackbar("LH", "Trackbar", 0, 255, listener)
cv2.createTrackbar("LS", "Trackbar", 0, 255, listener)
cv2.createTrackbar("LV", "Trackbar", 0, 255, listener)
cv2.createTrackbar("UH", "Trackbar", 255, 255, listener)
cv2.createTrackbar("US", "Trackbar", 255, 255, listener)
cv2.createTrackbar("UV", "Trackbar", 255, 255, listener)
cap = cv2.VideoCapture(0)
while 1:
    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lh = cv2.getTrackbarPos("LH", "Trackbar")
        ls = cv2.getTrackbarPos("LS", "Trackbar")
        lv = cv2.getTrackbarPos("LV", "Trackbar")
        uh = cv2.getTrackbarPos("UH", "Trackbar")
        us = cv2.getTrackbarPos("US", "Trackbar")
        uv = cv2.getTrackbarPos("UV", "Trackbar")
        lb = np.array([lh, ls, lv])
        ub = np.array([uh, us, uv])
        mask = cv2.inRange(hsv, lb, ub)
        if cv2.waitKey(1) == 27:
            break
cap.release()
cv2.destroyAllWindows()
