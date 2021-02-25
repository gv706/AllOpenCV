import cv2
import matplotlib.pyplot as plt

img=cv2.imread("MyPicture.png",-1)
cv2.imshow("Image",img)

plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
