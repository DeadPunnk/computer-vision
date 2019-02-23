import cv2 

# Carregando imagem RGB e segmentando canais 

img = cv2 .imread('frutas.jpg')
azul, verde, vermelho = cv2.split(img)


# Exibindo imagens dos canais separados

cv2.imshow('Canal R', vermelho)
cv2.imshow('Canal G', verde)
cv2.imshow('Cana B', azul)


# Salando imagens dos canais separados

cv2.imwrite('frutas-canal-vermelho.jpg', vermelho)
cv2.imwrite('frutas-canal-verde.jpg', verde)
cv2.imwrite('frutas-canal-azul.jpg', azul)

cv2.waitKey(0)
cv2.destroyAllWindows()

