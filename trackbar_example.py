import cv2 as cv
import numpy as np


def listener(x):
    if cv.getTrackbarPos("ON||OFF", "image") == 0:
        img[:] = 0
    else:
        b = cv.getTrackbarPos("B", "image")
        g = cv.getTrackbarPos("G", "image")
        r = cv.getTrackbarPos("R", "image")
        img[:] = [b, g, r]


img = np.zeros([512, 512, 3], dtype=np.uint8)
cv.namedWindow("image")
cv.createTrackbar("B", "image", 0, 255, listener)
cv.createTrackbar("G", "image", 0, 255, listener)
cv.createTrackbar("R", "image", 0, 255, listener)
cv.createTrackbar("ON||OFF", "image", 0, 1, listener)
while 1:
    cv.imshow("image", img)
    k = cv.waitKey(1)
    if k == 27:
        break

cv.destroyAllWindows()
