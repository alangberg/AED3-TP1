import sys

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

def asd(numero):
	ant = anterior(numero)
	if abs(ant - abs(numero)) < (ant / 2.0):
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

global potencias
potencias = []

numero = int(sys.argv[1])
n = 0
i = 0
while n < numero:
	n = 3**i
	potencias.append(n)
	i += 1
	pass

print siguiente(numero)
print anterior(numero)


x = []
while numero != 0:
	n = asd(numero)
	x.append(n)
	numero += n
	pass

print x




