import cv2
import numpy as np

# Carrega a imagem do produto
img = cv2.imread("C:\workspace\cadastro-aton\mordomo\programas\product.jpg")

# convertendo a imagem para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# aplicando threshold para remover o fundo branco
_, thresh = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY_INV)

# encontrar os contornos na imagem
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# encontrar o contorno com a maior área
c = max(contours, key = cv2.contourArea)

# encontrar o retângulo de bounding box para o contorno
x, y, w, h = cv2.boundingRect(c)

# cortar o produto da imagem original
crop = img[y:y+h, x:x+w]

# redimensionar a imagem cortada para 1000x1000
crop = cv2.resize(crop, (1000, 1000))

# Salva a imagem resultante
cv2.imwrite("C:\workspace\cadastro-aton\mordomo\programas\Result2.jpg", crop)