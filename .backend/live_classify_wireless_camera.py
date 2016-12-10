import openface
import numpy as np
import os
import cv2
import pickle
import vlc

def classify(alignedFace, net, clf, le):
    rep = net.forward(alignedFace)
    predictions = clf.predict_proba(rep).ravel()
    maxI = np.argmax(predictions)
    person = le.inverse_transform(maxI)
    confidence = predictions[maxI]
    print("Predict {} with {:.2f} confidence.".format(person, confidence))
    return person

if __name__ == "__main__":

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

        player = vlc.MediaPlayer("rtsp://10.201.120.92:554/onvif2")
        player.play()

        while True:
            # Grab image
            player.video_take_snapshot(0, './snapshot.tmp.png', 0, 0)
            cameraFrame = cv2.imread("./snapshot.tmp.png")

            try:
                bb2 = align.getLargestFaceBoundingBox(cameraFrame)
                alignedFace2 = align.align(96, cameraFrame, bb2,
                                           landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
                id = classify(alignedFace2, net, clf, le)

                if id == 0:
                    person_name = "Martin"
                elif id == 1:
                    person_name = "Neil"
                elif id == 2:
                    person_name = "Phong"
                elif id == 3:
                    person_name = "Thinh"

                frameSleep = 50
                rectColor = (0, 255, 0)
                textColor = (255, 0, 0)
                face_top_left = (bb2.left(), bb2.top())
                face_bottom_right = (bb2.right(), bb2.bottom())
                cv2.rectangle(cameraFrame, face_top_left, face_bottom_right,rectColor)
                cv2.putText(cameraFrame, str(person_name), face_top_left,
                            fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=textColor, thickness=2)
                cv2.imshow('FaceRecognizer', cameraFrame)
                if (cv2.waitKey(frameSleep) >= 0):
                    break

            except:
                cv2.imshow('FaceRecognizer', cameraFrame)
                continue



