import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    s, frame = cap.read()
    frame = cv2.flip(frame,1)
    print(type(frame), len(frame))
    #gray = cv2.cvtColor(frame, cv2.COLOR_BRG2GRAY)
    cv2.imshow('caption',frame)
    cv2.waitKey(1)



cap.release()
cv2.destroyAllWindows()
