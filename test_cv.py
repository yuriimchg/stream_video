import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    s, frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2.imshow('caption',frame)
    cv2.waitKey(1)



cap.release()
cv2.destroyAllWindows()
