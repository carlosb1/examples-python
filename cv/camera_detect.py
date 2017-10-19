import numpy as np
import cv2


class VideoCam:

    def __init__(self):
        self.cap = cv2.VideoCapture(-1)

    def run(self,detector=None):
        while (True):
            ret, frame = self.cap.read()
            cv2.imshow('frame',frame)
            if detector != None:
                print detector.run(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()




