import sys


indysA = [1, 2, 3]
caverA = ['A', 'B']

indysB = []
caverB = []

class Nodo():
	"""docstring for Nodo"""
	def __init__(self):
		self.aa = None
		self.cc = None
		self.ac = None
		self.a = None
		self.c = None

def ida(indysA, indysB, caverA, caverB, idab, movimientos):

	iA = indysA
	iB = indysB
	cA = caverA
	cB = caverB

	if (len(iA) > 0 and (len(iA) < len(cA))) or (len(iB) > 0 and (len(iB) < len(cB))):
		# print 'perdi', idab, indysA, '--', caverA, indysB, caverB
		return (False, Nodo())
	elif len(iA) == 0 and len(cA) == 0:
		# print 'gane', idab, indysA, caverA, '--', indysB, caverB
		print movimientos
		return (True, Nodo())

	# print idab, indysA, caverA, '--', indysB, caverB

	if idab == 1:
		nodo = Nodo()
		if len(iA) > 1:
			movimientos.append('AA')
			res = ida(iA[:len(iA) - 2], iB + iA[len(iA) - 2:], cA, cB, 1 - idab, movimientos)
			movimientos.pop()
			if res[0] == True:
				nodo.aa = res[1]

		if len(cA) > 1:
			movimientos.append('CC')
			res = ida(iA, iB, cA[:len(cA) - 2], cB + cA[len(cA) - 2:], 1 - idab, movimientos)
			movimientos.pop()

			if res[0] == True:
				nodo.cc = res[1]

		if len(iA) > 0 and len(cA) > 0:
			movimientos.append('AC')
			res = ida(iA[:len(iA) - 1], iB + iA[len(iA) - 1:], cA[:len(cA) - 1], cB + cA[len(cA) - 1:], 1 - idab, movimientos)
			movimientos.pop()

			if res[0] == True:
				nodo.ac = res[1]

		if nodo.aa != None or nodo.ac != None or  nodo.cc != None:
			return (True, nodo)
		else:
			return (False, nodo)
	else:
		nodo = Nodo()
		if len(iB) > 0:
			movimientos.append('A')
			res = ida(iA + iB[len(iB) - 1:], iB[:len(iB) - 1], cA, cB, 1 - idab, movimientos)
			movimientos.pop()

			if res[0] == True:
				nodo.a = res[1]

		if len(cB) > 0:
			movimientos.append('C')
			res = ida(iA, iB, cA + cB[len(cB) - 1:], cB[:len(cB) - 1], 1 - idab, movimientos)
			movimientos.pop()

			if res[0] == True:
				nodo.c = res[1]
		

		if nodo.c != None or nodo.a != None:
			return (True, nodo)
		else:
			return (False, nodo)
		

idab = 1
mov = []
nodo = ida(indysA, indysB, caverA, caverB, idab, mov)



print nodo