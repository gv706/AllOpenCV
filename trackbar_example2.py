import cv2 as cv
import numpy as np




def listener(x):
    global img
    img = np.zeros([512, 512, 3], dtype=np.uint8)
    img=cv.putText(img, str(x), (10, 100), font, 2, (255, 255, 255), 2, lineType=cv.LINE_AA)
    cv.imshow("image",img)



font = cv.FONT_HERSHEY_SIMPLEX
cv.namedWindow("image")
cv.createTrackbar("CP", "image", 100, 200, listener)

img = np.zeros([512, 512, 3], dtype=np.uint8)
while 1:
    cv.imshow("image", img)
    k = cv.waitKey(1)
    if k == 27:
        break

cv.destroyAllWindows()
