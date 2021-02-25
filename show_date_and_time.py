import cv2,datetime

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width:' + str(cap.get(3)) + " " + "Height:" + str(cap.get(4))
        date=str(datetime.datetime.now())
        frame = cv2.putText(frame, date, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) == ord("q"):
            break
cap.release()
cv2.destroyAllWindows()
