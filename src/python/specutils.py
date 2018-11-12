import collections
import itertools
import operator


def contar_cores(bl):
	estat_cores = collections.Counter(itertools.chain.from_iterable(bl))
	return sorted(estat_cores.items(), key=operator.itemgetter(1), reverse=True)

def conv_baites(item_bloco):
	return int(''.join((str(d) for d in item_bloco)),2)

def gera_blocos(img, tc = 8):
	w = img.width
	h = img.height

	cores = [[img.getpixel((i,j)) for i in range(w)] for j in range(h)]
	return [[[cores[j+k*tc][i*8:i*8+8] for j in range(tc)] for i in range(w // 8)] for k in range(h // tc)]


def gera_cores(img, default=121):
	cores = [default] * 768;
	blocos_cores = gera_blocos(img) 
	#for a in blocos_cores:
	#	for b in a:
	#		w = contar_cores(b)
	#		for p,q in w:
	#			qt[p] = qt.get(p,0) + q
	#	if len(w) > 2:
	#		print(contar_cores(b),end=" ")
	#print()
	#geral = sorted(qt.items(), key=operator.itemgetter(1), reverse=True)
	border = (256 - img.width) >> 4
	offset = border
	for a in blocos_cores:
		for b in a:
			w = contar_cores(b)
			s = 7
			if len(w) > 1:
				s = w[1][0] % 7
			cores[offset] = ((w[0][0] % 7) << 3) + s
			offset += 1
		offset += border + border
	return cores

def salva_scr(imagem, cores):
	pass