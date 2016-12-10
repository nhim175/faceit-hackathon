import openface
import numpy as np
import os
import cv2
import vlc
import time

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
img1 = cv2.imread("./resources/Phong/Phong0.png")
bb1 = align.getLargestFaceBoundingBox(img1)
alignedFace1 = align.align(96, img1, bb1,
                           landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)


# video = cv2.VideoCapture("rtsp://10.201.120.92:554/onvif2")
# if(video is None):
#     print("There is no video!")
#     exit
player = vlc.MediaPlayer("rtsp://10.201.120.92:554/onvif2")
player.play()

while True:
    time.sleep(1)
    player.video_take_snapshot(0, './snapshot.tmp.png', 0, 0)
    cameraFrame = cv2.imread("./snapshot.tmp.png")
    bb2 = align.getLargestFaceBoundingBox(cameraFrame)
    alignedFace2 = align.align(96, cameraFrame, bb2,
                               landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)

    rep1 = net.forward(alignedFace1)
    try:
        rep2 = net.forward(alignedFace2)
    except:
        print("No face captured.")
        continue

    # `rep2` obtained similarly.
    d = rep1 - rep2
    distance = np.dot(d, d)

    frameSleep = 50
    rectColor = (0, 255, 0)
    textColor = (255, 0, 0)
    face_top_left = (bb2.left(), bb2.top())
    face_bottom_right = (bb2.right(), bb2.bottom())
    cv2.rectangle(cameraFrame, face_top_left, face_bottom_right,rectColor)
    cv2.putText(cameraFrame, str(distance), face_top_left,
                fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=textColor, thickness=2)
    cv2.imshow('FaceRecognizer', cameraFrame)
    if (cv2.waitKey(frameSleep) >= 0):
        break
