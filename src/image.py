"""
@Autor: Márcio Moda
Data: 23-05-2025
## O que esse código faz? ##
Este código é um exemplo de como carregar e exibir uma imagem usando OpenCV.
    - Importa a biblioteca OpenCV.
    - Carrega uma imagem do disco usando cv2.imread().
    - Exibe a imagem em uma janela usando cv2.imshow().
    - Aguarda uma tecla ser pressionada usando cv2.waitKey().

aula 23
"""

import cv2

image = cv2.imread('image.jpg')

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


