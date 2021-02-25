import cv2

img = cv2.imread("gradient.png")

cv2.namedWindow("Threshold")


def listener(x):
    # the pixel values values lower than the threshold value specified are valued as zero and higher values are
    # valued as one
    ret1, th1 = cv2.threshold(img, x, 255, cv2.THRESH_BINARY)
    # Binary inverse is opposite to the binary
    ret2, th2 = cv2.threshold(img, x, 255, cv2.THRESH_BINARY_INV)
    # within the threshold all the values are remained same
    # and after that the values remains the same as of the 125th pixel
    ret3, th3 = cv2.threshold(img, x, 255, cv2.THRESH_TRUNC)
    # contrary to the tozero
    ret5, th5 = cv2.threshold(img, x, 255, cv2.THRESH_TOZERO_INV)
    # In tozero, the values of pixels will be zeroes within the threshold and after that the values are remain same
    ret4, th4 = cv2.threshold(img, x, 255, cv2.THRESH_TOZERO)
    cv2.imshow("th1", th1)
    cv2.imshow("th2", th2)
    cv2.imshow("th3", th3)
    cv2.imshow("th4", th4)
    cv2.imshow("th5", th5)


cv2.createTrackbar("Value", "Threshold", 0, 255, listener)

while 1:
    cv2.imshow("Image", img)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
