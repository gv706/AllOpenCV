import cv2

cap = cv2.VideoCapture(0)
fourcccode = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
# or we can write fourcccode =cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter("myvideo4.avi", fourcccode, 20.0, (640, 480))
print(cap.isOpened())
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("videoframe", gray)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

'''fourcccode = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter("output.mp4", fourcccode,20.0,(640,480))
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Video", gray)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cap.release()
out.release()
cv2.destroyAllWindows()'''





