import os
import sys
from sklearn.pipeline import Pipeline
from sklearn.lda import LDA
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV
from sklearn.mixture import GMM
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

import numpy as np
import cv2
import openface
import pickle

def classify(alignedFace, net, classifierModel):
    r = net.forward(alignedFace)
    rep = r[1].reshape(1, -1)
    bbx = r[0]
    predictions = clf.predict_proba(rep).ravel()
    maxI = np.argmax(predictions)
    person = le.inverse_transform(maxI)
    confidence = predictions[maxI]
    print("Predict {} with {:.2f} confidence.".format(person, confidence))
            
        
if __name__ == "__main__":
    dlib_predictor = "./.resources/shape_predictor_68_face_landmarks.dat"
    align = openface.AlignDlib(dlib_predictor)
    network_model = "./.resources/nn4.small2.v1.t7"
    net = openface.TorchNeuralNet(network_model, 96)
    classifierModel = "./svm.pkl"

    with open(classifierModel, 'r') as f:
        (le, clf) = pickle.load(f)
    
        bgrImg = cv2.imread(sys.argv[1])
        if bgrImg is None:
            raise Exception("Unable to load image: {}".format(imgPath))

        rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

        bb = align.getLargestFaceBoundingBox(rgbImg)
        
        alignedFace = align.align(
            96,
            rgbImg,
            bb,
            landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
        
        classify(alignedFace, net)
