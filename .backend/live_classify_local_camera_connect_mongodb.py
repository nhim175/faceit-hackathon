import openface
import numpy as np
import os
import cv2
import pickle
from pymongo import MongoClient
import time


id_name = ["Eric", "Martin","Neil","Phong","Thinh","Xanta_Klause", "Fanta_Klauss"]

def classify(alignedFace, net, clf, le):
    rep = net.forward(alignedFace)
    predictions = clf.predict_proba(rep).ravel()
    maxI = np.argmax(predictions)
    person = le.inverse_transform(maxI)
    confidence = predictions[maxI]
    print("Predict {} with {:.2f} confidence.".format(person, confidence))
    return person, confidence

def push_to_db(person_id):
    client = MongoClient('mongodb://47.91.16.198:27017')
    db = client['faceit']
    # Get the userId for the classifyID
    db_id = db['UserClassifyId']
    record = db_id.find_one({"classifyId": person_id})
    user_id = record['userId']

    # Content to push
    event_id = "pHJ9fGNMxNMh88pGH"
    type = "in"
    created_at = time.time()
    post = {"userId": user_id,
            "eventId": event_id,
            "type": type,
            "createdAt": created_at}

    db_to_push = db['CheckInOutQueue']
    post_id = db_to_push.insert_one(post).inserted_id
    print(post_id)

if __name__ == "__main__":

    show_video = False
    CONFIDENCE_THRESHOLD = 0.5

    fileDir = os.path.dirname("~/openface")
    modelDir = os.path.join(fileDir, 'models')
    dlibModelDir = os.path.join(modelDir, 'dlib')
    openfaceModelDir = os.path.join(modelDir, 'openface')

    # `args` are parsed command-line arguments.
    dlib_predictor = "./resources/shape_predictor_68_face_landmarks.dat"
    align = openface.AlignDlib(dlib_predictor)
    network_model = "./resources/nn4.small2.v1.t7"

    net = openface.TorchNeuralNet(network_model, 96)

    # `img` is a numpy matrix containing the RGB pixels of the image.
    classifierModel = "./svm.pkl"

    with open(classifierModel, 'r') as f:
        (le, clf) = pickle.load(f)

        video = cv2.VideoCapture(0)
        if(video is None):
            exit()

        while True:
            # Grab image
            ret, cameraFrame = video.read()
            if (not ret):
                exit()
            try:

                bbs = align.getAllFaceBoundingBoxes(cameraFrame)
                for bb2 in bbs:
                    alignedFace2 = align.align(96, cameraFrame, bb2,
                                            landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
                    id, confidence = classify(alignedFace2, net, clf, le)
                    if float(confidence) >= CONFIDENCE_THRESHOLD:
                        push_to_db(id)
                        print("Pushed to DB.")

                    if show_video:
                        person_name = id_name[id]
                        frameSleep = 50
                        rectColor = (0, 255, 0)
                        textColor = (255, 0, 0)
                        face_top_left = (bb2.left(), bb2.top())
                        face_bottom_right = (bb2.right(), bb2.bottom())
                        cv2.rectangle(cameraFrame, face_top_left, face_bottom_right,rectColor)
                        cv2.putText(cameraFrame, str(person_name), face_top_left,
                                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=textColor, thickness=2)

                if show_video:
                    cv2.imshow('FaceRecognizer', cameraFrame)
                if (cv2.waitKey(frameSleep) >= 0):
                    break

            except:
                cv2.imshow('FaceRecognizer', cameraFrame)
                continue




