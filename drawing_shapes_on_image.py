import numpy as np
# importing the opencv package
import cv2

# reading the image in colored mode
# img = cv2.imread("MyPicture.png", 1)
img=np.zeros([512,512,3],dtype=np.uint8)  # this gives a black image
# uint8 is an unsigned 8-bit integer that can represent values 0.. 255.
# int on the other hand is usually a 32-bit signed integer.
# When you create array using dtype=int, each element in that array takes 4 bytes.
# OpenCV apparently expect array to be made of 8-bit tuples representing red, green and blue.

# drawing line on he image
# parameters are image,startingcoordinates,endingcoordinates,color,thickness
img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), thickness=5)

# drawing the arrowed line on the image
img = cv2.arrowedLine(img, (0, 255), (255, 255), (0, 255, 0), thickness=5)

# drawing rectangle
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255),10)  # if we mention thickness as -1 then the particular rectangle will be filled with the specified color

# drawing circle
img = cv2.circle(img, (200, 200), 100, (0, 255, 0), 10)

# specifying the font
font=cv2.FONT_HERSHEY_SIMPLEX
text_to_be_displayed="Chandra"
img=cv2.putText(img,text_to_be_displayed,(100,500),font,1,(0,0,255),2,cv2.LINE_AA)
cv2.imshow("MyImage", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


