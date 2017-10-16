import numpy as np
import cv2
import glob
import cPickle as pickle

path='./data/1.jpg'
voc = pickle.load(voc,open("keypoints_kmeans.p","wb"))

NUMBER_TYPES=5
size_small= (89,40)

dictionarySize=5
i=0

SIFT=np.zeros([NUMBER_TYPES,dictionarySize])
NoDes=[]

gray = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2GRAY)
kp = []
kp, dsc = sift.detectAndCompute(cv2.resize(gray, size_small), None)
if len(kp) > 0:
print dsc.shape
hist=np.zeros([1,dictionarySize])
for k in range(dsc.shape[0]):

    d=[]

    for j in range(dictionarySize):
        x=voc[j,:]-dsc[k,:]
        sum=0
        for ii in range(x.shape[0]):
            sum+=x[ii]*x[ii]
        d.append(math.sqrt(sum))

    val, idx = min((val, idx) for (idx, val) in enumerate(d))
    SIFT[i,idx]+=1
# HIST[i,:]=HIST[i,:]/np.sum(HIST[i,:])

else:
# sometimes we cannot detect any keypoints. Let's keep track of it
	NoDes.append(i)



if len(NoDes)>0:
    SIFT=np.delete(SIFT,tuple(NoDes),0)


