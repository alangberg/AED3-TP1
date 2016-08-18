import sys


indysA = [1, 2]
caverA = [3, 4]

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

def ida(indysA, indysB, caverA, caverB, idab, movimientos, vel):

	if (len(indysA) > 0 and (len(indysA) < len(caverA))) or (len(indysB) > 0 and (len(indysB) < len(caverB))):
		# print 'perdi', idab, indysA, '--', caverA, indysB, caverB
		return (False, Nodo())
	elif len(indysA) == 0 and len(caverA) == 0:
		# print 'gane', idab, indysA, caverA, '--', indysB, caverB
		print movimientos, vel
		return (True, Nodo())

	# print idab, indysA, caverA, '--', indysB, caverB

	if idab == 1:
		nodo = Nodo()
		if len(indysA) > 1:
			movimientos.append('AA')
			movimientos.pop()
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

					res = ida(iA, iB, cA, cB, 1 - idab, movimientos, newVel)
					movimientos.pop()

					nodos.append(res)
					pass
				pass

			for res in nodos:
				if res[0] == 1:
					nodo.aa.append(res[1])
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
					res = ida(iA, iB, cA, cB, 1 - idab, movimientos, newVel)
					movimientos.pop()

					nodos.append(res)
					pass
				pass

			for res in nodos:
				if res[0] == 1:
					nodo.cc.append(res[1])
				pass

		if len(indysA) > 0 and len(caverA) > 0:
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
					res = ida(iA, iB, cA, cB, 1 - idab, movimientos, newVel)
					movimientos.pop()

					nodos.append(res)
					pass
				pass

			for res in nodos:
				if res[0] == 1:
					nodo.ac.append(res[1])
				pass
		if nodo.aa != [] or nodo.ac != [] or  nodo.cc != []:
			return (True, nodo)
		else:
			return (False, nodo)
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
				res = ida(iA, iB, caverA, caverB, 1 - idab, movimientos, newVel)
				movimientos.pop()
				
				nodos.append(res)
				pass

			for res in nodos:
				if res[0] == 1:
					nodo.a.append(res[1])
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
				res = ida(indysA, indysB, cA, cB, 1 - idab, movimientos, newVel)
				movimientos.pop()
				
				nodos.append(res)
				pass

			for res in nodos:
				if res[0] == 1:
					nodo.c.append(res[1])
				pass
		

		if nodo.c != [] or nodo.a != []:
			return (True, nodo)
		else:
			return (False, nodo)
		

idab = 1
mov = []
nodo = ida(indysA, indysB, caverA, caverB, idab, mov, 0)

print nodo
