import cv2
import numpy as np
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #
while True:
    ret,frame=cap.read()
    frame = cv2.flip(frame, 2) 
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    edges=cv2.Canny(grey,50,50)
    cv2.imshow("face Detection ", frame)
    cv2.imshow("edges", edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()