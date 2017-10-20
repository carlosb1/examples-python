from camera_detect import VideoCam
from feature_detect import Detector, ORBFeature, SIFTFeature, BFMatcher, FlannMatcher, Model

#feature = SIFTFeature()
feature = ORBFeature()
model = Model('model_test1')
#matcher = FlannMatcher(model)
matcher = BFMatcher(model)
detector = Detector(feature,matcher,model)

detector.train("./data")
#image = cv2.imread("./database/2.jpg")
#print str(detector.run(image))

videoCam = VideoCam(1)
videoCam.run(detector)

