import os
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


# currently hard mapped id to name, as network is too slow and no access to facebook as been granted
id_name = ["Eric", "Martin","Neil","Phong","Thinh"]

# function the calculate the feature representation of the face
def getRep(imgPath, align, net, multiple=False):
    bgrImg = cv2.imread(imgPath)
    if bgrImg is None:
        raise Exception("Unable to load image: {}".format(imgPath))

    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

    if multiple:
        bbs = align.getAllFaceBoundingBoxes(rgbImg)
    else:
        bb1 = align.getLargestFaceBoundingBox(rgbImg)
        bbs = [bb1]
    if len(bbs) == 0 or (not multiple and bb1 is None):
        raise Exception("Unable to find a face: {}".format(imgPath))

    reps = []
    for bb in bbs:
        alignedFace = align.align(
            96,
            rgbImg,
            bb,
            landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
        if alignedFace is None:
            raise Exception("Unable to align image: {}".format(imgPath))

        rep = net.forward(alignedFace)
        reps.append(rep)
    sreps = np.array(reps)
    #print(sreps.shape)
    return sreps


# train the classifier
def train(features, labels):
    le = LabelEncoder().fit(labels)
    labelsNum = le.transform(labels)
    param_grid = [
        {'C': [1, 10, 100, 1000],
         'kernel': ['linear']},
        {'C': [1, 10, 100, 1000],
         'gamma': [0.001, 0.0001],
         'kernel': ['rbf']}
    ]
    clf = GridSearchCV(SVC(C=1, probability=True), param_grid, cv=5)

    clf.fit(features, labelsNum)

    fName = "{}/svm.pkl".format(".")
    print("Saving classifier to '{}'".format(fName))
    # store the classifier
    with open(fName, 'w') as f:
        pickle.dump((le, clf), f)

# training the classifier to make the prediction for a face
def makeClassifier(allfacesdir, align, net):

    facesdir = [o for o in os.listdir(allfacesdir) if os.path.isdir(os.path.join(allfacesdir,o))]
    
    features = None
    labels = []
    
    for facedir in facesdir:
        name = facedir
        id_counter = id_name.index(name)
        facedir_path = os.path.join(allfacesdir, facedir)
        facesdir_images = [o for o in os.listdir(facedir_path) if os.path.isfile(os.path.join(facedir_path,o))]
        
        for facesdir_image in facesdir_images:
            facesdir_image_path = os.path.join(facedir_path, facesdir_image)
            print facesdir_image_path
            reps = getRep(facesdir_image_path, align, net)
            
            if features == None:
                features = reps
            else:
                features = np.concatenate([features, reps])
            
            labels.append(id_counter)
                
    
    print features
    train(features, labels)

if __name__ == "__main__":
    dlib_predictor = "./resources/shape_predictor_68_face_landmarks.dat"
    align = openface.AlignDlib(dlib_predictor)
    network_model = "./resources/nn4.small2.v1.t7"
    net = openface.TorchNeuralNet(network_model, 96)
    
    makeClassifier("./resources/", align, net)
