import cv2
img = cv2.imread('circle.bmp') 

KSIZE_NOISE = 5
threshold1 = 10.0
threshold2 = 80.0

grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
grayscale = cv2.medianBlur(grayscale,KSIZE_NOISE)


edges= cv2.Canny(grayscale,threshold1,threshold2,apertureSize=3,L2gradient=True)

cv2.imwrite('resultado1.bmp',edges)




