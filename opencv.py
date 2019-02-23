import cv2

img = cv2.imread('hidrante.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Hidrante', img)
cv2.waitKey(0)
cv2.DestroyAllWindows()