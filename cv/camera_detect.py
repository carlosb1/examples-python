import numpy as np
import cv2


class VideoCam:

    def __init__(self,autofocus=0):
        self.cap = cv2.VideoCapture(-1)
        self.cap.set(cv2.CAP_PROP_AUTOFOCUS, autofocus) # turn the autofocus off

    def run(self,detector=None):
        while (True):
            ret, frame = self.cap.read()
            if detector != None:
                print detector.run(frame) + " num keypoints: "+str(len(detector.current_kp))
                cv2.drawKeypoints(frame,detector.current_kp,frame)
                cv2.imshow('frame',frame)
            else:
                cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()




