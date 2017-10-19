import cv2
import numpy as np
import glob
import cPickle as pickle
import os
import shutil

def pickle_keypoints(keypoints, descriptors, img):
  i = 0
  array = []
  array.append(img)
  temp_array = []
  for point in keypoints:
    temp = (point.pt, point.size, point.angle, point.response, point.octave,
    point.class_id, descriptors[i])
    i+=1
    temp_array.append(temp)
  array.append(temp_array)
  return array

def unpickle_keypoints(array):
  keypoints = []
  descriptors = []
  img = array[0]
  for point in array[1]:
    temp_feature = cv2.KeyPoint(x=point[0][0],y=point[0][1],_size=point[1],
      _angle=point[2], _response=point[3], _octave=point[4], _class_id=point[5])
    temp_descriptor = point[6]
    keypoints.append(temp_feature)
    descriptors.append(temp_descriptor)
  return keypoints, np.array(descriptors), img


class ORBFeature:
    def __init__(self):
        self.orb = cv2.ORB_create()
    def apply(self,gray):
        return self.orb.detectAndCompute(gray,None)

class SIFTFeature:
    def __init__(self):
        self.sift = cv2.xfeatures2d.SIFT_create()
    def apply(self,gray):
        return self.sift.detectAndCompute(gray,None)


class BFMatcher:
    def __init__(self,model):
        self.model = model
        self.matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
    def bestMatches(self,des,threshold):
        #reset counts
        for key in self.model.mod:
            (kp_model,des_model,points) = self.model.mod[key]
            self.model.mod[key] = (kp_model, des_model,0)

        for key in self.model.mod:
            (kp_model,des_model,points) = self.model.mod[key]
            matches = self.matcher.knnMatch(des,trainDescriptors=des_model,k=2)
            good = []
            for (m,n) in matches:
                if (n.distance == 0):
                    continue
                if m.distance <threshold*n.distance:
                    good.append(m)
            self.model.mod[key] = (kp_model, des_model, len(good))   
   

class FlannMatcher:
    def __init__(self, model, FLANN_INDEX_KDTREE = 1, n_trees = 5, n_checks = 50):
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = n_trees)
        search_params = dict(checks = n_checks)   # or pass empty dictionary
        self.flann = cv2.FlannBasedMatcher(index_params,search_params)
        self.model = model
    def bestMatches(self,des,threshold):
        #reset counts
        for key in self.model.mod:
            (kp_model,des_model,points) = self.model.mod[key]
            self.model.mod[key] = (kp_model, des_model,0)

        for key in self.model.mod:
            (kp_model,des_model,points) = self.model.mod[key]
            matches = self.flann.knnMatch(des,des_model, k = 2)
    
            good = []
            for m,n in matches:
                if (n.distance == 0):
                    continue
                if m.distance <threshold*n.distance:
                    good.append(m)
            self.model.mod[key] = (kp_model, des_model, len(good))


class Model:
    def __init__(self,directory):
        self.mod = {}
        self.directory = os.path.join(os.getcwd(),directory)
        #TODO refactor
        if not os.path.exists(self.directory):
            print "trying to create :" +str(self.directory)+ "or will not work"
            #supermarkerdirs(self.directory,777)

    def reset(self):
        self.mod = {}
        #shutil.rmtree(self.directory,ignore_errors=True)

    def load(self):
        model_images = glob.glob(self.directory+"/*.txt")
        for model_image in  model_images:
            keypoints_database = pickle.load(open(model_image,"rb"))
            (kp,des,img_url) = unpickle_keypoints(keypoints_database)
            self.mod[str(img_url)] = (kp,des,0)
    def save(self, kp, des, image_url):
        self.mod[str(image_url)]=(kp,des,0)
        
        temp = pickle_keypoints(kp, des, image_url)
        name = image_url.split("/")[2].split(".")[0]
        file = self.directory+"/" + name + ".txt"
        pickle.dump(temp, open(file, "wb"))


class Detector():
    def __init__(self,feature,matcher,model,threshold=0.7):
        self.feature = feature
        self.matcher = matcher
        self.model = model
        self.threshold = threshold

    def train(self, directory):
        database_images = glob.glob(directory+"/*.jpg")
        
        self.model.reset()
        # Load each image
        for image_url in database_images:
            number = image_url.split("/")[2].split(".")[0]
            img = cv2.imread(image_url)
            # Convert them to greyscale
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            kp,des = self.feature.apply(gray)
            self.model.save(kp,des,image_url)
    def run(self,image):
            gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            kp, des = self.feature.apply(gray)
            self.matcher.bestMatches(des,self.threshold)
            sorted_votes = sorted(self.model.mod.keys(),key=lambda x: self.model.mod[x][2], reverse=True)
            #TODO check if it exists
            return sorted_votes[0]


#feature = SIFTFeature()
#feature = ORBFeature()
#model = Model('model_test1')
#matcher = FlannMatcher(model)
#matcher = BFMatcher(model)
#detector = Detector(feature,matcher,model)

#detector.train("./database")
#image = cv2.imread("./database/2.jpg")
#print str(detector.run(image))
