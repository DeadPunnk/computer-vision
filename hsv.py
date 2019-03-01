import cv2

img = cv2.imread('frutas.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
matiz, saturacao, valor = cv2.split(img)

cv2.imshow('Canal H', matiz)
cv2.imshow('Canal S', saturacao)
cv2.imshow('Canal V', valor)

img = cv2.merge((matiz, saturacao, valor))
img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)


cv2.imshow('Imagem', img)


cv2.waitKey(0)
cv2.destroyAllWindows()
