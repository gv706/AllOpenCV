import cv2
import matplotlib.pyplot as plt

img=cv2.imread("MyPicture.png",-1)
cv2.imshow("Image",img)
print(img.shape)
# Generally opencv reads the image in bgr format while the matplotlib reads the image in rgb format
# so we need to convert the bgr to rgb
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.xticks([]),plt.yticks([])
# above is to hide the ticks
plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
