import cv2

# Carregando imagem RGB e segmentando canais

img = cv2.imread('frutas.jpg')
azul, verde, vermelho = cv2.split(img)


# Combinando os três canais em uma única imagem 

img = cv2.merge((azul, verde, vermelho))
cv2.imshow('Imagem', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

