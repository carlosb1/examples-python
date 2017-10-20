import cv2
import numpy as np




img = cv2.imread('circle.bmp',0)

current_param1 = 50
step_current_param1=10

current_param2 = 70
step_current_param2=10
thres_near=1


ksize_noise = 5
threshold_canny1 = 10.0
step_threshold_canny1=10.0
threshold_canny2 = 80.0
step_threshold_canny2=10.0


import glob 

images = glob.glob("circles/*.bmp")

index_image = 0
img = cv2.imread(images[index_image])
canny_img = cv2.medianBlur(img,ksize_noise)
while (True):
    cimg = cv2.cvtColor(canny_img,cv2.COLOR_BGR2GRAY)

    canned = cv2.Canny(img,current_param1,threshold_canny1,threshold_canny2)
    #cv2.imshow('canned.bmp',canned)
    circles = cv2.HoughCircles(canned,cv2.HOUGH_GRADIENT,1,thres_near,
                            param1=1,param2=current_param2,minRadius=0,maxRadius=0)

    canned= cv2.cvtColor(canned,cv2.COLOR_GRAY2RGB)
    if circles !=None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(canned,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(canned,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('detected circles',canned)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('w'):
        current_param1+=step_current_param1
        print "Incr param1 ",current_param1
    elif key == ord('s') and current_param1 > 0:
        current_param1-=step_current_param1
        print "Decr param1 ",current_param1

    elif key == ord('e'):
        current_param2+=step_current_param2
        print "Incr param2 ",current_param2
    elif key == ord('d'):
        current_param2-=step_current_param2
        print "Decr param2 ",current_param2

    elif key == ord('r'):
        threshold_canny1+=step_threshold_canny1
        print "Incr threshold_canny1 ",threshold_canny1
    elif key == ord('f') and threshold_canny1 > 0:
        threshold_canny1-=step_threshold_canny1
        print "Decr threshold_canny1 ",threshold_canny1

    elif key == ord('t'):
        threshold_canny2+=step_threshold_canny2
        print "Incr threshold_canny2 ",threshold_canny2
    elif key == ord('g') and threshold_canny2 > 0:
        threshold_canny2-=step_threshold_canny2
        print "Decr threshold_canny2 ",threshold_canny2
    elif key == ord('y') and index_image < len(images) :
        index_image +=1
        img = cv2.imread(images[index_image])
        canny_img = cv2.medianBlur(img,ksize_noise)
    elif key == ord('y') and index_image >0 :
        index_image -=1
        img = cv2.imread(images[index_image])
        canny_img = cv2.medianBlur(img,ksize_noise)



cv2.destroyAllWindows()
