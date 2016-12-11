import openface
import numpy as np
import os
import cv2
import pickle
from pymongo import MongoClient
import time

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
    return person, confidence

# A function to push to MongoDB
# pram: person_id: id from classifying result.
#       type: "in" or "out"

def push_to_db(db_id, db_to_push, person_id, type):
    # Get the userId for the classifyID
    record = db_id.find_one({"classifyId": person_id})
    user_id = record['userId']

    # Content to push
    event_id = "pHJ9fGNMxNMh88pGH"
    created_at = time.time()
    post = {"userId": user_id,
            "eventId": event_id,
            "type": type,
            "createdAt": created_at}

    post_id = db_to_push.insert_one(post).inserted_id
    print(post_id)


if __name__ == "__main__":
    
    frameSleep = 10
    
    # the path to our deep learning model

    dlib_predictor = "./resources/shape_predictor_68_face_landmarks.dat" # the library to find and align a face
    align = openface.AlignDlib(dlib_predictor) # the object doing the alignment
    network_model = "./resources/nn4.small2.v1.t7" # the deep learning model to calculate the features of a face

    net = openface.TorchNeuralNet(network_model, 96) # the object to calculate the features of a face

    # `img` is a numpy matrix containing the RGB pixels of the image.
    classifierModel = "./svm.pkl" # our trained classifier to receive a persons id

    client = MongoClient('mongodb://47.91.16.198:27017')
    db = client['faceit']
    db_id = db['UserClassifyId']
    db_to_push = db['CheckInOutQueue']
    print("Connection to DB done")

    with open(classifierModel, 'r') as f: # try to open the classifier
        (le, clf) = pickle.load(f) # open the classifier

        # open the two video streams from the local ports
        video1 = cv2.VideoCapture("udp://127.0.0.1:6000")
        video2 = cv2.VideoCapture("udp://127.0.0.1:6001")
        
        video1.set(cv2.CAP_PROP_BUFFERSIZE, 3);
        video2.set(cv2.CAP_PROP_BUFFERSIZE, 3);
        
        # stop if we have no video
        if(video1 is None or video2 is None):
            print("There is no video!")
            exit()
            
        video_steams = [video1, video2]
        
        counter = 0
        
        # loop forever
        while True:
            # catch the two streams
            for video in video_steams:
                counter += 1;
                video_id = video_steams.index(video)

                # Video id 0 for going in, and the rest are going out.
                if video_id == 0:
                    type = "in"
                else:
                    type = "out"
                
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
                    
                    to_push = []
                    # iterate over all faces
                    for bb2 in bbs:
                        # align the face before calculating features
                        alignedFace2 = align.align(96, cameraFrame, bb2,
                                                landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
                        
                        # get the user id for this face
                        id, confidence = classify(alignedFace2, net, clf, le)
                        to_push.append((id, confidence))
                        if float(confidence) >= 0.5:
                            # the persons name
                            person_name = id_name[id]

                            # draw some region and the name in the image
                            rectColor = (0, 255, 0)
                            textColor = (255, 0, 0)
                            face_top_left = (bb2.left(), bb2.top())
                            face_bottom_right = (bb2.right(), bb2.bottom())
                            cv2.rectangle(cameraFrame, face_top_left, face_bottom_right,rectColor)
                            cv2.putText(cameraFrame, str(counter) + " (" + str(type) + ")", face_top_left,
                                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=textColor, thickness=2)

                    # show the image
                    cv2.imshow('FaceRecognizer ' + str(video_id), cameraFrame)
                    # push the results to DB
                    
                    for (id, confidence) in to_push:
                        push_to_db(db_id, db_to_push, id, type)
                        
                    if (cv2.waitKey(frameSleep) >= 0):
                        exit()
                    
                        

                except:
                    #cv2.imshow('FaceRecognizer ' + str(video_id), cameraFrame)
                    pass




