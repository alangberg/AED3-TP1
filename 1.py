entrada = [('A', 8), ('A', 4), ('C', 1)]

# entrada = [('A', 1), ('A', 2), ('A', 3), ('C', 1), ('C', 2)]

combinacion = ['AA','A','AC']

def armarPasadas(partida, llegada, c):
	if len(c) == 0:
		res = []
		return res

	if len(c[0]) == 2:
		# tengo que elegir 2 => estoy en la partida
		for x in filtrar(tomadosDeA2(partida), c[0]):
			aux = c
			aux.pop(0)
			res = armarPasadas(list(set(partida) - set(x)), llegada + x, aux)
			if len(res) == 0:
				res.insert(0, x)
			else:
				esta = []
				for elem in res:
					esta.append(x + elem)
				return esta
			return res 
			# tratar de sacar el return afuera sino me devuelve solo una combinacion...
	else:
		# elijo 1 para volver
		for x in filtrar(llegada, c[0]):
			aux = c
			aux.pop(0)
			res = armarPasadas(partida + x, list(set(llegada) - set(x)), aux)
			if len(res) == 0:
				res.insert(0, x)
			else:
				esta = []
				for elem in res:
					esta.append(x + elem)
				return esta
			return res 
	

def tomadosDeA2(conjunto):
	# k == 2
	res = []
	for i in xrange(0, len(conjunto)-1):
		for j in xrange(i+1, len(conjunto)):
			aux = []
			aux.append(conjunto[i])
			aux.append(conjunto[j])
			res.append(aux)
	return res

def filtrar(conjunto, criterio):
	k = len(criterio)
	if k == 1:
		# k == 1
		res = []
		for x in conjunto:
			# x == ('A', 4)
			comp = x[0]
			if comp == criterio:
				# para que quede con el mismo formato que el otro caso
				aux = []
				aux.append(x)
				res.append(aux)

		return res
	elif k == 2:
		# k == 2
		res = []
		for x in conjunto:
			# x == [('A', 4), ('C', 1)]
			comp = x[0][0] + x[1][0]
			# No importa el orden: 'AC' == 'CA' tiene que dar true
			if comp == criterio or comp[::-1] == criterio:
				res.append(x)

		return res

print tomadosDeA2(entrada)
# print armarPasadas(entrada, [], combinacion)
		