import cv2
import numpy as np


cam = cv2.VideoCapture(0)
cam.set(3,1280)
cam.set(4,1024)

ret, img = cam.read()
cv2.namedWindow('Display',0)
print ret

while True:
     ret, ima = cam.read()
     cv2.imshow('Display',ima)
     k=cv2.waitKey(10)
     if chr(k&255) == 'q':
         break
