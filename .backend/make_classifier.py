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
    # load the image from the path
    bgrImg = cv2.imread(imgPath)
    
    if bgrImg is None:
        raise Exception("Unable to load image: {}".format(imgPath))

    # convert to rgb
    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

    # there could be possible multiple images in the face
    if multiple:
        bbs = align.getAllFaceBoundingBoxes(rgbImg)
    else:
        bb1 = align.getLargestFaceBoundingBox(rgbImg)
        bbs = [bb1]
        
    if len(bbs) == 0 or (not multiple and bb1 is None):
        raise Exception("Unable to find a face: {}".format(imgPath))

    # array to hold the feature representations of the faces
    reps = []
    
    # iterate over the faces we found
    for bb in bbs:
        # align the face before feature calculation
        alignedFace = align.align(
            96,
            rgbImg,
            bb,
            landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
        if alignedFace is None:
            raise Exception("Unable to align image: {}".format(imgPath))
        
        # get the feature representation from the deep learning network
        rep = net.forward(alignedFace)
        # append this representation to the array
        reps.append(rep)
    
    # cast everything to a proper numpy array
    sreps = np.array(reps)
    #print(sreps.shape)
    return sreps


# train the classifier
def train(features, labels):
    # prepare the labels for a training process
    le = LabelEncoder().fit(labels)
    labelsNum = le.transform(labels)
    # some parameters for the trained model
    param_grid = [
        {'C': [1, 10, 100, 1000],
         'kernel': ['linear']},
        {'C': [1, 10, 100, 1000],
         'gamma': [0.001, 0.0001],
         'kernel': ['rbf']}
    ]
    
    # construct the model
    clf = GridSearchCV(SVC(C=1, probability=True), param_grid, cv=5)

    # train the model
    clf.fit(features, labelsNum)

    # store the model
    fName = "{}/svm.pkl".format(".")
    print("Saving classifier to '{}'".format(fName))
    with open(fName, 'w') as f:
        pickle.dump((le, clf), f)

# training the classifier to make the prediction for a face
def makeClassifier(allfacesdir, align, net):

    # get all the folders in the resources
    facesdir = [o for o in os.listdir(allfacesdir) if os.path.isdir(os.path.join(allfacesdir,o))]
    
    features = None
    labels = []
    
    # iterate over all folders containing images
    for facedir in facesdir:
        name = facedir # the folder name is also the persons name
        id_counter = id_name.index(name) # for training the classifier we can only use integer
        
        # build the folder path
        facedir_path = os.path.join(allfacesdir, facedir)
        # and get the images in this folder
        facesdir_images = [o for o in os.listdir(facedir_path) if os.path.isfile(os.path.join(facedir_path,o))]
        
        # iterate over all images in the folder of one person
        for facesdir_image in facesdir_images:
            # build the proper image path
            facesdir_image_path = os.path.join(facedir_path, facesdir_image)
            print facesdir_image_path
            
            # get the feature representations for this image
            reps = getRep(facesdir_image_path, align, net)
            
            # append the feature of the array going to be returned
            if features == None:
                features = reps
            else:
                features = np.concatenate([features, reps])
            
            # same for the labels
            labels.append(id_counter)
                
    # pass everything to the train function
    train(features, labels)

if __name__ == "__main__":
    # path to the face alignment model
    dlib_predictor = "./resources/shape_predictor_68_face_landmarks.dat"
    # construct the face alignment model
    align = openface.AlignDlib(dlib_predictor)
    # path to the deep neural network for feature representation
    network_model = "./resources/nn4.small2.v1.t7"
    # construct the network for feature representation
    net = openface.TorchNeuralNet(network_model, 96)
    
    # make a classifier
    makeClassifier("./resources/", align, net)
