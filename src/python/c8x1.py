import sys

with open(sys.argv[1],"rb") as inp:
	dados = inp.read()

with open(sys.argv[2],"wb") as out:
	out.write(dados[:6144])
	atributos = [b'0'] * 6144
	i = 6144
	for f in range(3):
		for b in range(8):
			for g in range(8):
				for x in range(32):
					atributos[x + g*256 + b*32 + f*2048] = dados[i]
					i += 1
	out.write(bytes(atributos))