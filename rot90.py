import cv2 
import numpy as np 

imgOrigin = cv2.imread('hidrante.jpg', 0)
totalLinhas, totalColunas = imgOrigin.shape

matrix = cv2.getRotationMatrix2D((totalColunas / 2,
			totalLinhas / 2), 90, 1)

imgRotacionada =  cv2.warpAffine(
		imgOrigin, matrix, (totalColunas, totalLinhas))

cv2.imshow('Resultado', imgRotacionada)

cv2.waitKey(0)
cv2.destroyAllWindows()