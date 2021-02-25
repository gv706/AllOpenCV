import cv2
import numpy as np

img = cv2.imread("half_b_half_w.png", -1)
img2 = np.zeros([183, 275, 3], dtype=np.uint8)
img2 = cv2.rectangle(img2, (77, 20), (197, 90), (255, 255, 255), -1)
print(img.shape)
print(img2.shape)
cv2.imshow("image", img)
cv2.imshow("zerosimage", img2)

# bitAnd = cv2.bitwise_and(img2, img)
# bitOr = cv2.bitwise_or(img2, img)
# bitXor = cv2.bitwise_xor(img2, img)
bitNot = cv2.bitwise_not(img)

# cv2.imshow("bitOr", bitOr)
# cv2.imshow("bitAnd", bitAnd)
# cv2.imshow("bitXor", bitXor)
cv2.imshow("bitNot",bitNot)

cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2 as cv
import numpy as np
zeroes=np.zeros((512,512,3))