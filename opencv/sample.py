import cv2

# VideoCapture オブジェクトを取得します
capture = cv2.VideoCapture(1)

while(True):
    ret, frame = capture.read()
    # resize the window
    windowsize = (800, 600)
    frame = cv2.resize(frame, windowsize)

    cv2.imshow('title',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()