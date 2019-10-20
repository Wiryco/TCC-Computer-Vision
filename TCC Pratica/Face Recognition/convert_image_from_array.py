from PIL import Image, ImageDraw
import numpy as np

imagem = Image.open("jogador_de_futebol_americano.png")
arrayImagem = np.asarray(imagem)
resultArrayImagem = Image.fromarray(arrayImagem)
print("Teste: ", arrayImagem)

arquivo = open('imagem_jogador_convertida.txt', 'r')
conteudo = arquivo.readlines()


conteudo.append(arrayImagem)

arquivo = open('imagem_jogador_convertida.tx', 'w')

arquivo.write(str(conteudo))
arquivo.close()
