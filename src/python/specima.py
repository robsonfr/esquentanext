from PIL import Image
import collections
import itertools
import operator
import sys


from specutils import *

if len(sys.argv) < 2:
	print("Sintaxe: %s <arquivo de imagem> [imagem colorida]" % sys.argv[0])
	sys.exit(1)

colorida = ""
if len(sys.argv) == 3:
	colorida = sys.argv[2]

imagem = Image.open(sys.argv[1])
#cores = [[imagem.getpixel((i,j)) for i in range(w)] for j in range(h)]
#blocos = [[[cores[j+k*tam_celula][i*8:i*8+8] for j in range(tam_celula)] for i in range(w // 8)] for k in range(h // tam_celula)]

qt = dict()
cores = [121] * 768;
if colorida != "":
	cores = gera_cores(Image.open(colorida))

w = imagem.width
h = imagem.height

with open("imagem.scr","wb") as out:
	bitmap = [0] * 6144 
	border = (256 - w) >> 4
	offset = border
	blocos = gera_blocos(imagem)
	for bloco in blocos:
		for item in bloco:
			row_offset =  0
			for sub_item in item:	
				bitmap[offset + row_offset]=conv_baites(sub_item)
				row_offset += 256
			offset += 1
		offset += border + border
		if (offset - border) % 256 == 0:
			offset += 1792		
		print(offset)
	out.write(bytes(bitmap))
	out.write(bytes(cores))
#for c in geral:
#	print("Cor %d: %d" % c)
#for j in range(imagem.height):
#	print(" ".join(("%02X" % imagem.getpixel((i,j)) for i in range(imagem.width))))


