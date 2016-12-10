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


def getRep(imgPath, align, net, multiple=False):
    start = time.time()
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
    if args.verbose:
        print("Face detection took {} seconds.".format(time.time() - start))

    reps = []
    for bb in bbs:
        start = time.time()
        alignedFace = align.align(
            args.imgDim,
            rgbImg,
            bb,
            landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
        if alignedFace is None:
            raise Exception("Unable to align image: {}".format(imgPath))
        if args.verbose:
            print("Alignment took {} seconds.".format(time.time() - start))
            print("This bbox is centered at {}, {}".format(bb.center().x, bb.center().y))

        rep = net.forward(alignedFace)
        if args.verbose:
            print("Neural network forward pass took {} seconds.".format(
                time.time() - start))
        reps.append((bb.center().x, rep))
    sreps = sorted(reps, key=lambda x: x[0])
    return sreps


def train(features, labels):
    
    from nolearn.dbn import DBN
    clf = DBN([len(features), 200, len(labels),
              learn_rates=0.3,
              # Smaller steps mean a possibly more accurate result, but the
              # training will take longer
              learn_rate_decays=0.9,
              # a factor the initial learning rate will be multiplied by
              # after each iteration of the training
              epochs=300,  # no of iternation
              # dropouts = 0.25, # Express the percentage of nodes that
              # will be randomly dropped as a decimal.
              verbose=1)

    clf.fit(features, labels)

    fName = "{}/dbn.pkl".format(".")
    print("Saving classifier to '{}'".format(fName))
    with open(fName, 'w') as f:
        pickle.dump((le, clf), f)

def makeClassifier(allfacesdir, align, net):

    facesdir = [o for o in os.listdir(allfacesdir) if os.path.isdir(os.path.join(allfacesdir,o))]
    id_counter = 0
    
    features = None
    labels = None
    
    for facedir in facesdir:
        name = facedir
        facedir_path = os.path.join(allfacesdir, facedir)
        facesdir_images = [o for o in os.listdir(facedir_path) if os.path.isfile(os.path.join(facedir_path,o))]
        
        for facesdir_image in facesdir_images:
            facesdir_image_path = os.path.join(facedir_path, facesdir_image)
            print facesdir_image_path
            reps = self.getRep(facesdir_image_path, align, net)
            
            print reps
            
            if features == None:
                features = reps
            else:
                np.append([features, reps], axis=0)
                
            if labels == None:
                labels = id_counter
                np.append([labels, reps], axis=0)
                
                
        id_counter += 1
    
    self.train(features, labels)

if __name__ == "__main__":
    dlib_predictor = "./.resources/shape_predictor_68_face_landmarks.dat"
    align = openface.AlignDlib(dlib_predictor)
    network_model = "./.resources/nn4.small2.v1.t7"
    net = openface.TorchNeuralNet(network_model, 96)
    
    self.makeClassifier("./.resources/")
