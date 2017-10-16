import numpy as np
import cv2
import glob
import cPickle as pickle

NUMBER_TYPES=5
size_small= (89,40)

def pickle_keypoints(keypoints, descriptors):
    i = 0
    temp_array = []
    for point in keypoints:
        temp = (point.pt, point.size, point.angle, point.response, point.octave,
        point.class_id, descriptors[i])     
        ++i
        temp_array.append(temp)
    return temp_array

def unpickle_keypoints(array):
    keypoints = []
    descriptors = []
    for point in array:
        temp_feature = cv2.KeyPoint(x=point[0][0],y=point[0][1],_size=point[1], _angle=point[2], _response=point[3], _octave=point[4], _class_id=point[5])
        temp_descriptor = point[6]
        keypoints.append(temp_feature)
        descriptors.append(temp_descriptor)
    return keypoints, np.array(descriptors)
  





sift = cv2.xfeatures2d.SIFT_create()

BOW = cv2.BOWKMeansTrainer(5)


for filename in sorted(glob.glob('data/*.jpg')):
    print "filename="+filename
    gray = cv2.cvtColor(cv2.imread(filename),cv2.COLOR_BGR2GRAY)
    kp = []

    kp, dsc = sift.detectAndCompute(cv2.resize(gray,size_small),None)
    
    print ("#kps: {}, descriptors {}".format(len(kp),dsc.shape))
    if len(kp) > 0: 
        BOW.add(dsc)

voc = BOW.cluster()

pickle.dump(voc,open("keypoints_kmeans.p","wb"))

print str(voc)



