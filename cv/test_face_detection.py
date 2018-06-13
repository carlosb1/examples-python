import glob
import cv2 as cv
import numpy as np

path_images = './output/images'
images = glob.glob(path_images+"/*.jpg")

for path_image in images:
    print(path_image)
    image = cv.imread(path_image)
    print(image.shape)
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    #TODO check parameters and function
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        cv.imshow('img',image)
    key = cv.waitKey()
    if key == ord('q'):
        break

cv.destroyAllWindows()



