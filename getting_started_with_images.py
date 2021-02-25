import cv2

img = cv2.imread("MyPicture.png", -1)
# 0 is for reading the image in grayscale mode
# 1 is for reading the image in colored image
print(img)

cv2.imshow("image", img)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("MyPictureCopy.png", img)
    cv2.destroyAllWindows()




