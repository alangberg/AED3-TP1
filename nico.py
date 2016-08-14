import sys

def siguiente(numero):
	for x in xrange(0,100):
		n = 3**x
		if n >= abs(numero):
			return int(n)
		pass

def anterior(numero):
	for x in xrange(0,100):
		n = 3**x
		if n > abs(numero):
			return int(3**(x - 1))
		pass


def asd(numero):
	if abs(anterior(numero) - abs(numero)) < (anterior(numero) / 2.0):
		# print 'anterior: ' + str(anterior(numero))

		if numero > 0:
			return -1*anterior(numero)
		else:
			return anterior(numero)
	else:
		# print 'siguiente: ' + str(siguiente(numero))
		if numero > 0:
			return -1*siguiente(numero)
		else:
			return siguiente(numero)

x = []
numero = int(sys.argv[1])
while numero != 0:
	x.append(asd(numero))
	numero += asd(numero)
	pass

print x




