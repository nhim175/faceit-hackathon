import openface
import numpy as np
import os
import cv2

fileDir = os.path.dirname("~/openface")
modelDir = os.path.join(fileDir, 'models')
dlibModelDir = os.path.join(modelDir, 'dlib')
openfaceModelDir = os.path.join(modelDir, 'openface')

# `args` are parsed command-line arguments.
dlib_predictor = "./.resources/shape_predictor_68_face_landmarks.dat"
align = openface.AlignDlib(dlib_predictor)
network_model = "./.resources/nn4.small2.v1.t7"

net = openface.TorchNeuralNet(network_model, 96)

# `img` is a numpy matrix containing the RGB pixels of the image.
img1 = cv2.imread("./.resources/Phong/Phong0.png")
img2 = cv2.imread("./.resources/Phong/Phong1.png")
bb1 = align.getLargestFaceBoundingBox(img1)
bb2 = align.getLargestFaceBoundingBox(img2)
alignedFace1 = align.align(96, img1, bb1,
                                  landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)

alignedFace2 = align.align(96, img2, bb2,
                           landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)

rep1 = net.forward(alignedFace1)
rep2 = net.forward(alignedFace2)

# `rep2` obtained similarly.
d = rep1 - rep2
distance = np.dot(d, d)

print distance
