import cv2
import numpy as np 
from matplotlib import pyplot as graf

img = cv2.imread('folha-cor.bmp')
azul, verde, vermelho = cv2.split(img)

graf.hist(azul.ravel(), 256, [0, 256])  #ravel() -> transforma a imagem em vetor 

graf.figure()
graf.hist(verde.ravel(), 256, [0, 256])

graf.figure()
graf.hist(vermelho.ravel(), 256, [0, 256])

graf.show()

