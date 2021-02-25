import cv2
import datetime

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Every property has a number associated with it.
# so for the cv2.CAP_PROP_FRAME_WIDTH it is 3 and cv2.CAP_PROP_FRAME_HEIGHT it is 4

# setting the width and height through  constants
cap.set(3, 700)
cap.set(4, 700)
print(cap.get(3))
print(cap.get(4))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        font = cv2.FONT_HERSHEY_SIMPLEX

        dateandtime = str(datetime.datetime.now())
        text = "Width:" + str(cap.get(3)) + " Height:" + str(cap.get(4))
        print(text)

        cv2.putText(frame, dateandtime, (50, 400), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cap.release()
cv2.destroyAllWindows()
