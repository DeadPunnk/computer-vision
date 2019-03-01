import cv2
import numpy as np 
from matplotlib import pyplot as graf

imgorigin = cv2.imread('maquina.jpg', 0)
imgequalize = cv2.equalizeHist(imgorigin)

cv2.imshow('Imagem Original', imgorigin)
cv2.imshow('Imagem Equalizada', imgequalize)

graf.hist(imgorigin.ravel(), 256, [0,256])

graf.figure()
graf.hist(imgequalize.ravel(), 256, [0,256])

graf.show()
