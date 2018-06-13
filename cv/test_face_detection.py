import glob
import cv2 as cv
import numpy as np

path_images = './output/images'
images = glob.glob(path_images+"/*.jpg")

for path_image in images:
    print(path_image)
    path_fil = "/".join(path_image.split('/')[:-1])
    name_image_with_ext = path_image.split('/')[-1:][0]
    name_extension = name_image_with_ext.split('.')[1]
    name_image = name_image_with_ext.split('.')[0]
    print("name_image_with_ext="+str(name_image_with_ext))
    print("path_fil="+str(path_fil))
    print("name_extension="+str(name_extension))
    print("name_image="+str(name_image))

    image = cv.imread(path_image)
    height, width, channel = image.shape
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    #TODO check parameters and function
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        padh = (int)(h * .40)
        padw = (int)(w * .20)
        y0 = y - padh
        x0 = x - padw
        yh1 = y+h + padh
        xw1 = x+w + padw
        if y0 < 0:
            y0 = 0
        if x0 < 0:
            x0 = 0
        if yh1 >=height:
            yh1=height-1
        if xw1>=width:
            xw1=width-1

        cv.rectangle(image,(x0,y0),(xw1,yh1),(0,255,0),2)
        cv.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        
        #roi_img = image[y:y+h, x:x+w] 
        #roi_gray = gray[y:y+h, x:x+w]
        cv.imshow('img',image)
    key = cv.waitKey()
    if key == ord('q'):
        break

cv.destroyAllWindows()



