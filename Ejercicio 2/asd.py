import sys

def abs(num):
    return -num if num < 0 else num

# Dado un numero busco la siguiente potencia de 3 mas grande.
# Ej: numero = 7 -> res = 9
def siguiente(numero):
	i = 0
	k = len(potencias) - 1
	med = 0

	while i + 1 < k:
		med = (i + k) / 2

		if potencias[med] <= abs(numero):
			i = med
		else:
			k = med
		pass
	
	if potencias[i] == abs(numero):
		return potencias[i]
	else:
		return potencias[k]


# Dado un numero busco la anterior potencia de 3 mas grande.
# Ej: numero = 7 -> res = 3
def anterior(numero):
	i = 0
	k = len(potencias) - 1
	med = 0

	while i + 1 < k:
		med = (i + k) / 2

		if potencias[med] < abs(numero):
			i = med
		else:
			k = med
		pass

	if potencias[k] == abs(numero):
		return potencias[k]
	else:
		return potencias[i]


# Esto es medio magico, surgio de mirar los resultados de varios numeros.
# 
def siguiente_a_usar(numero):
	ant = anterior(numero)
	if abs(ant - abs(numero)) < (ant / 2.0): # la magia esta aca
		# print 'anterior: ' + str(anterior(numero))
		if numero > 0:
			return -1*ant
		else:
			return ant
	else:
		# print 'siguiente: ' + str(siguiente(numero))
		sig = siguiente(numero)
		if numero > 0:
			return -1*sig
		else:
			return sig



# #
# Aca arranca 'main'
# #

global potencias
potencias = []


# ----------------
# calculo todas las potencias de 3
# for x in xrange(1,10000000000000000):
	
numero = int(sys.argv[1])
aux = numero

n = 0
i = 0
while n < numero:
	n = 3**i
	potencias.append(n)
	i += 1
	pass
# ----------------

# resuelvo
pesaIzq = []
pesaDer = []
izq = 0
der = 0
while numero != 0:
	n = siguiente_a_usar(numero)
	if n < 0:
		pesaIzq.append(abs(n))
		izq += 1
	else:
		pesaDer.append(n)
		der += 1
	pass

	numero += n

	pass
# pesaIzq.reverse()
# pesaDer.reverse()
# print izq, der
# print "{} \n{}".format(pesaIzq, pesaDer)

# if not (aux == (sum(pesaIzq) - sum(pesaDer))):
# print str(aux) + ': ' + str(aux == (sum(pesaIzq) - sum(pesaDer)))
