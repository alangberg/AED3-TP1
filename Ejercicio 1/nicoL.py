import sys

indysA = [1,2,3,4,5,6]

caverA = []

indysB = []
caverB = []

class Nodo():
	"""docstring for Nodo"""
	def __init__(self):
		self.aa = []
		self.cc = []
		self.ac = []
		self.a = []
		self.c = []
		self.cantidad = 1
		self.altura = 1

def ida(indysA, indysB, caverA, caverB, idab, movimientos, vel, b):
	if (len(indysA) > 0 and (len(indysA) < len(caverA))) or (len(indysB) > 0 and (len(indysB) < len(caverB))):
		# print 'perdi', idab, indysA, '--', caverA, indysB, caverB
		return (False, Nodo(), vel)
	elif len(indysA) == 0 and len(caverA) == 0:
		# print 'gane', idab, indysA, caverA, '--', indysB, caverB
		# print movimientos, vel
		return (True, Nodo(), vel)

	velMin	= 9999999999
	altura = 0
	# print idab, indysA, caverA, '--', indysB, caverB
	if idab == 1:
		nodo = Nodo()
		if len(indysA) > 1:
			nodos = []

			for i in xrange(0,len(indysA)):
				for j in xrange(i+1,len(indysA)):

					iA = list(indysA)
					iB = list(indysB)
					cA = list(caverA)
					cB = list(caverB)

					newVel = vel + max(iA[i], iA[j])
					iB.append(iA[i])
					iB.append(iA[j])

					movimientos.append('A' + str(iA[i]) + ' A' + str(iA[j]))
					
					del iA[i]
					del iA[j - 1]

					res = ida(iA, iB, cA, cB, 1 - idab, movimientos, newVel, False)
					movimientos.pop()

					nodos.append(res)
					pass
				pass

			for res in nodos:
				if res[0] == 1:
					nodo.cantidad += res[1].cantidad
					nodo.aa.append(res[1])
					altura = max(res[1].altura, altura) 
					if res[2] < velMin:
						velMin = res[2]
				pass

		if len(caverA) > 1:
			nodos = []

			for i in xrange(0,len(caverA)):
				for j in xrange(i+1,len(caverA)):
					iA = list(indysA)
					iB = list(indysB)
					cA = list(caverA)
					cB = list(caverB)

					newVel = vel + max(cA[i], cA[j])
					cB.append(cA[i]) 
					cB.append(cA[j])

					movimientos.append('C' + str(cA[i]) + ' C' + str(cA[j]))
					del cA[i]
					del cA[j - 1]
					res = ida(iA, iB, cA, cB, 1 - idab, movimientos, newVel, False)
					movimientos.pop()

					nodos.append(res)
					pass
				pass

			for res in nodos:
				if res[0] == 1:
					nodo.cantidad += res[1].cantidad
					altura = max(res[1].altura, altura) 
					nodo.cc.append(res[1])
					if res[2] < velMin:
						velMin = res[2]
				pass

		if len(indysA) > 0 and len(caverA) > 0 and not b:
			nodos = []
			
			for i in xrange(0,len(indysA)):
				for j in xrange(0,len(caverA)):

					iA = list(indysA)
					iB = list(indysB)
					cA = list(caverA)
					cB = list(caverB)

					newVel = vel + max(iA[i], cA[j])
					iB.append(iA[i])
					cB.append(cA[j])

					movimientos.append('A' + str(iA[i]) + ' C' + str(cA[j]))
					del iA[i]
					del cA[j]
					res = ida(iA, iB, cA, cB, 1 - idab, movimientos, newVel, False)
					movimientos.pop()

					nodos.append(res)
					pass
				pass

			for res in nodos:
				if res[0] == 1:
					nodo.cantidad += res[1].cantidad
					altura = max(res[1].altura, altura) 
					nodo.ac.append(res[1])
					if res[2] < velMin:
						velMin = res[2]
				pass

		if nodo.aa != [] or nodo.ac != [] or  nodo.cc != []:
			nodo.altura += altura
			return (True, nodo, velMin)
		else:
			return (False, nodo, 999)
	else:
		nodo = Nodo()
		if len(indysB) > 0:
			nodos = []
			for i in xrange(0,len(indysB)):
				iA = list(indysA) # pasa por copia
				iB = list(indysB)

				newVel = vel + iB[i]
				iA.append(iB[i])

				# print 'A' + str(iB[i])
				movimientos.append('A' + str(iB[i]))
				
				del iB[i]
				res = ida(iA, iB, caverA, caverB, 1 - idab, movimientos, newVel, False)
				movimientos.pop()
				
				nodos.append(res)
				pass

			for res in nodos:
				if res[0] == 1:
					nodo.cantidad += res[1].cantidad
					altura = max(res[1].altura, altura) 
					nodo.a.append(res[1])
					if res[2] < velMin:
						velMin = res[2]
				pass

		if len(caverB) > 0:
			nodos = []
			for i in xrange(0,len(caverB)):
				cA = list(caverA)
				cB = list(caverB)

				newVel = vel + cB[i]
				cA.append(cB[i])

				movimientos.append('C' + str(cB[i]))
				del cB[i]
				res = ida(indysA, indysB, cA, cB, 1 - idab, movimientos, newVel, False)
				movimientos.pop()
				
				nodos.append(res)
				pass

			for res in nodos:
				if res[0] == 1:
					nodo.cantidad += res[1].cantidad
					altura = max(res[1].altura, altura) 
					nodo.c.append(res[1])
					if res[2] < velMin:
						velMin = res[2]
				pass
		
		if nodo.c == [] and nodo.a == []:

			if len(indysA) > 0 and len(caverA) > 0:
				nodos = []
			
				for i in xrange(0,len(indysB)):
					for j in xrange(0,len(caverB)):

						iA = list(indysA)
						iB = list(indysB)
						cA = list(caverA)
						cB = list(caverB)

						newVel = vel + max(iB[i], cB[j])
						iA.append(iB[i])
						cA.append(cB[j])

						movimientos.append('A' + str(iB[i]) + ' C' + str(cB[j]))
						del iB[i]
						del cB[j]
						res = ida(iA, iB, cA, cB, 1 - idab, movimientos, newVel, True)
						movimientos.pop()

						nodos.append(res)
						pass
					pass

				for res in nodos:
					if res[0] == 1:
						nodo.cantidad += res[1].cantidad
						altura = max(res[1].altura, altura)
						nodo.ac.append(res[1])
						if res[2] < velMin:
							velMin = res[2]
					pass

			if nodo.ac == []:
				return (False, nodo, 999)
			else:
				nodo.altura += altura
				return (True, nodo, velMin)
		else:
			nodo.altura += altura
			return (True, nodo, velMin)
		

idab = 1
mov = []
nodo = ida(indysA, indysB, caverA, caverB, idab, mov, 0, False)
# print nodo[1].altura
print nodo[2]
