import cv2
import numpy as np 
from matplotlib import pyplot as grafico 

img = cv2.imread('folha-binaria.bmp', 0)
grafico.hist(img.ravel(), 256, [0, 256])
grafico.show()