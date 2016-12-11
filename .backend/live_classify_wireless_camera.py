import openface
import numpy as np
import os
import cv2
import pickle

# those id to name mapping should come from the mangoDB server. However, the network is too slow to sufficiently do so.
id_name = ["Eric", "Martin","Neil","Phong","Thinh","Xanta_Klause", "Fanta_Klauss"]

# receives and aligned image, the deep neural network to calculate the features, the classifier+labels
def classify(alignedFace, net, clf, le):
    rep = net.forward(alignedFace) # get the feature representation of the face
    predictions = clf.predict_proba(rep.reshape(1, -1)).ravel() # make the prediction who it is
    maxI = np.argmax(predictions) # get the internal id with the highest confidence
    person = le.inverse_transform(maxI) # get the real persons id
    confidence = predictions[maxI] # the confidence how sure we are about this classification
    print("Predict {} with {:.2f} confidence.".format(person, confidence)) 
    return person

if __name__ == "__main__":
    
    # the path to our deep learning model

    dlib_predictor = "./resources/shape_predictor_68_face_landmarks.dat" # the library to find and align a face
    align = openface.AlignDlib(dlib_predictor) # the object doing the alignment
    network_model = "./resources/nn4.small2.v1.t7" # the deep learning model to calculate the features of a face

    net = openface.TorchNeuralNet(network_model, 96) # the object to calculate the features of a face

    # `img` is a numpy matrix containing the RGB pixels of the image.
    classifierModel = "./svm.pkl" # our trained classifier to receive a persons id

    with open(classifierModel, 'r') as f: # try to open the classifier
        (le, clf) = pickle.load(f) # open the classifier

        # open the two video streams from the local ports
        video1 = cv2.VideoCapture("udp://127.0.0.1:6000")
        video2 = cv2.VideoCapture("udp://127.0.0.1:6001")
        
        # stop if we have no video
        if(video1 is None or video2 is None):
            print("There is no video!")
            exit()
            
        video_steams = [video1, video2]
        
        # loop forever
        while True:
            # catch the two streams
            for video in video_steams:
                video_id = video_steams.index(video)
                
                # skip some frames as the network is too slow to process all frames
                for i in range(0,25):
                    video.grab()
                
                # receive a real from from the 
                ret, cameraFrame = video.read()
                
                # something went wrong while receiving the frame
                if (not ret):
                    exit()

                try:
                    # get the faces in the image
                    bbs = align.getAllFaceBoundingBoxes(cameraFrame)
                    
                    # iterate over all faces
                    for bb2 in bbs:
                        # align the face before calculating features
                        alignedFace2 = align.align(96, cameraFrame, bb2,
                                                landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
                        
                        # get the user id for this face
                        id = classify(alignedFace2, net, clf, le)

                        # the persons name
                        person_name = id_name[id]

                        frameSleep = 50
                        # draw some region and the name in the image
                        rectColor = (0, 255, 0)
                        textColor = (255, 0, 0)
                        face_top_left = (bb2.left(), bb2.top())
                        face_bottom_right = (bb2.right(), bb2.bottom())
                        cv2.rectangle(cameraFrame, face_top_left, face_bottom_right,rectColor)
                        cv2.putText(cameraFrame, str(person_name), face_top_left,
                                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=textColor, thickness=2)

                    # show the image
                    cv2.imshow('FaceRecognizer ' + str(video_id), cameraFrame)
                    if (cv2.waitKey(frameSleep) >= 0):
                        exit()
                                

                except:
                    cv2.imshow('FaceRecognizer ' + str(video_id), cameraFrame)
                    continue




