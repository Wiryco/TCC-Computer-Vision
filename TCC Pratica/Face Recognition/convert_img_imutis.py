from PIL import Image, ImageDraw
import numpy as np
import imutils

imagem = Image.open("jogador_de_futebol_americano.png")
arrayImagem = imutils.translate(imagem, 25, -75)

print(arrayImagem)
