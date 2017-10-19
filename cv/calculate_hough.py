import cv2
import numpy as np




img = cv2.imread('circle.jpg',0)
img = cv2.medianBlur(img,5)

current_param1 = 50
step_current_param1=10

current_param2 = 30
step_current_param2=10
thres_near=1
while (True):
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,thres_near,
                            param1=current_param1,param2=current_param2,minRadius=0,maxRadius=0)

    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('detected circles',cimg)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('w'):
        current_param1+=step_current_param1
        print "Incr param1 ",current_param1
    elif key == ord('s') and current_param1 > 0:
        current_param1-=step_current_param1
        print "Decr param1 ",current_param1
    elif key == ord('x'):
        thres_near+=1
        print "Incr thres_near ",thres_near
    elif key == ord('e'):
        current_param2+=step_current_param2
        print "Incr param2 ",current_param2
    elif key == ord('c') and thres_near > 0:
        thres_near-=1
        print "Decr thres_near ",thres_near
    elif key == ord('d'):
        current_param2-=step_current_param2
        print "Decr param2 ",current_param2


cv2.destroyAllWindows()
