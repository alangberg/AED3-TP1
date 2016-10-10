import sys

global velocidad_minima
velocidad_minima = 999999999

class Nodo():
	def __init__(self):
		self.a = []
		self.c = []
		self.aa = []
		self.cc = []
		self.ac = []

class Estado():
	def __init__(self, iA, iB, cA, cB, ida):
		self.iA = set(iA)
		self.iB = set(iB)
		self.cA = set(cA)
		self.cB = set(cB)
		self.ida = ida

	def iguales(self, otro):
		return (self.iA == otro.iA and self.iB == otro.iB and self.cA == otro.cA and self.cB == otro.cB and self.ida == otro.ida)
		
def existe_estado(movimientos, iA, iB, cA, cB, ida):
	e = Estado(iA, iB, cA, cB, ida)
	for est in movimientos:
		if est.iguales(e): return True
	return False

def agregar_estado(movimientos, iA, iB, cA, cB, ida):
	movimientos.append(Estado(iA, iB, cA, cB, ida))

def ida(indysA, indysB, canivA, canivB, movimientos, mov, vel):
	global velocidad_minima
	
	if velocidad_minima < vel:
		return (False, Nodo(), -1)		

	if (len(indysA) > 0 and (len(indysA) < len(canivA))) or (len(indysB) > 0 and (len(indysB) < len(canivB))):
		return (False, Nodo(), -1)
	elif len(indysA) == 0 and len(canivA) == 0:
		# print movimientos, vel
		velocidad_minima = min(velocidad_minima, vel)
		print velocidad_minima
		return (True, Nodo(), vel)

	velMin	= 9999999999
	nodo = Nodo()

	for i in xrange(0,len(indysA)):
		iA = list(indysA) # pasa por copia
		iB = list(indysB)

		newVel = vel + iA[i]
		iB.append(iA[i])

		mov.append('A' + str(iA[i]))
		del iA[i]

		if not existe_estado(movimientos, iA, iB, canivA, canivB, 1):
			agregar_estado(movimientos, iA, iB, canivA, canivB, 1)
			res = vuelta(iA, iB, canivA, canivB, movimientos, mov, newVel)
			movimientos.pop()
			if res[0] == 1:
				nodo.a.append(res[1])
				velMin = min(velMin, res[2])
	
		mov.pop()

		for j in xrange(i+1, len(indysA)):
			iA = list(indysA) # pasa por copia
			iB = list(indysB)

			newVel = vel + max(iA[i], iA[j])
			iB.append(iA[i])
			iB.append(iA[j])

			mov.append('A' + str(iA[i]) + 'A' + str(iA[j]))
			del iA[i]
			del iA[j-1]

			if not existe_estado(movimientos, iA, iB, canivA, canivB, 1):
				agregar_estado(movimientos, iA, iB, canivA, canivB, 1)
				res = vuelta(iA, iB, canivA, canivB, movimientos, mov, newVel)
				movimientos.pop()
				if res[0] == 1:
					nodo.aa.append(res[1])
					velMin = min(velMin, res[2])
		
			mov.pop()
			pass
		
		pass

	for i in xrange(0,len(canivA)):
		cA = list(canivA) # pasa por copia
		cB = list(canivB)

		newVel = vel + cA[i]
		cB.append(cA[i])

		mov.append('C' + str(cA[i]))
		del cA[i]

		if not existe_estado(movimientos, indysA, indysB, cA, cB, 1):
			agregar_estado(movimientos, indysA, indysB, cA, cB, 1)
			res = vuelta(indysA, indysB, cA, cB, movimientos, mov, newVel)
			movimientos.pop()
			if res[0] == 1:
				nodo.c.append(res[1])
				velMin = min(velMin, res[2])
	
		mov.pop()

		for j in xrange(i+1, len(canivA)):
			cA = list(canivA) # pasa por copia
			cB = list(canivB)

			newVel = vel + max(cA[i], cA[j])
			cB.append(cA[i])
			cB.append(cA[j])

			mov.append('C' + str(cA[i]) + 'C' + str(cA[j]))
			del cA[i]
			del cA[j-1]

			if not existe_estado(movimientos, indysA, indysB, cA, cB, 1):
				agregar_estado(movimientos, indysA, indysB, cA, cB, 1)
				res = vuelta(indysA, indysB, cA, cB, movimientos, mov, newVel)
				movimientos.pop()
				if res[0] == 1:
					nodo.cc.append(res[1])
					velMin = min(velMin, res[2])
		
			mov.pop()
			pass
		pass


	if len(indysA) > 0 and len(canivA) > 0:		
		for i in xrange(0,len(indysA)):
			for j in xrange(0,len(canivA)):

				iA = list(indysA)
				iB = list(indysB)
				cA = list(canivA)
				cB = list(canivB)

				newVel = vel + max(iA[i], cA[j])
				iB.append(iA[i])
				cB.append(cA[j])

				mov.append('A' + str(iA[i]) + ' C' + str(cA[j]))
				del iA[i]
				del cA[j]
				if not existe_estado(movimientos, iA, iB, cA, cB, 1):
					agregar_estado(movimientos, iA, iB, cA, cB, 1)
					res = vuelta(iA, iB, cA, cB, movimientos, mov, newVel)
					movimientos.pop()
					if res[0] == 1:
						nodo.ac.append(res[1])
						velMin = min(velMin, res[2])
		
				mov.pop()
			pass
		pass

	valido = nodo.aa != [] or nodo.cc != [] or nodo.a != [] or nodo.c != [] or nodo.ac != []
	return (valido, nodo, velMin)



def vuelta(indysA, indysB, canivA, canivB, movimientos, mov, vel):
	global velocidad_minima
	
	if velocidad_minima < vel:
		return (False, Nodo(), -1)		

	if (len(indysA) > 0 and (len(indysA) < len(canivA))) or (len(indysB) > 0 and (len(indysB) < len(canivB))):
		return (False, Nodo(), vel)
	elif len(indysA) == 0 and len(canivA) == 0:
		# print mov, vel
		velocidad_minima = min(velocidad_minima, vel)
		return (True, Nodo(), vel)

	
	velMin	= 9999999999
	nodo = Nodo()

	for i in xrange(0,len(indysB)):
		iB = list(indysB) # pasa por copia
		iA = list(indysA)

		newVel = vel + iB[i]
		iA.append(iB[i])

		mov.append('A' + str(iB[i]))
		del iB[i]

		if not existe_estado(movimientos, iA, iB, canivA, canivB, 0):
			agregar_estado(movimientos, iA, iB, canivA, canivB, 0)
			res = ida(iA, iB, canivA, canivB, movimientos, mov, newVel)
			movimientos.pop()
			if res[0] == 1:
				nodo.a.append(res[1])
				velMin = min(velMin, res[2])
	
		mov.pop()

		for j in xrange(i+1, len(indysB)):
			iB = list(indysB) # pasa por copia
			iA = list(indysA)

			newVel = vel + max(iB[i], iB[j])
			iA.append(iB[i])
			iA.append(iB[j])

			mov.append('A' + str(iB[i]) + 'A' + str(iB[j]))
			del iB[i]
			del iB[j-1]

			if not existe_estado(movimientos, iA, iB, canivA, canivB, 0):
				agregar_estado(movimientos, iA, iB, canivA, canivB, 0)
				res = ida(iA, iB, canivA, canivB, movimientos, mov, newVel)
				movimientos.pop()
				if res[0] == 1:
					nodo.aa.append(res[1])
					velMin = min(velMin, res[2])
		
			mov.pop()
			pass
		
		pass

	for i in xrange(0,len(canivB)):
		cA = list(canivA) # pasa por copia
		cB = list(canivB)

		newVel = vel + cB[i]
		cA.append(cB[i])

		mov.append('C' + str(cB[i]))
		del cB[i]

		if not existe_estado(movimientos, indysA, indysB, cA, cB, 0):
			agregar_estado(movimientos, indysA, indysB, cA, cB, 0)
			res = ida(indysA, indysB, cA, cB, movimientos, mov, newVel)
			movimientos.pop()
			if res[0] == 1:
				nodo.c.append(res[1])
				velMin = min(velMin, res[2])
	
		mov.pop()

		for j in xrange(i+1, len(canivB)):
			cA = list(canivA) # pasa por copia
			cB = list(canivB)

			newVel = vel + max(cB[i], cB[j])
			cA.append(cB[i])
			cA.append(cB[j])

			mov.append('C' + str(cB[i]) + 'C' + str(cB[j]))
			del cB[i]
			del cB[j-1]

			if not existe_estado(movimientos, indysA, indysB, cA, cB, 0):
				agregar_estado(movimientos, indysA, indysB, cA, cB, 0)
				res = ida(indysA, indysB, cA, cB, movimientos, mov, newVel)
				movimientos.pop()
				if res[0] == 1:
					nodo.cc.append(res[1])
					velMin = min(velMin, res[2])
		
			mov.pop()
			pass
		pass


	if len(indysB) > 0 and len(canivB) > 0:		
		for i in xrange(0,len(indysB)):
			for j in xrange(0,len(canivB)):

				iA = list(indysA)
				iB = list(indysB)
				cA = list(canivA)
				cB = list(canivB)

				newVel = vel + max(iB[i], cB[j])
				iA.append(iB[i])
				cA.append(cB[j])

				mov.append('A' + str(iB[i]) + ' C' + str(cB[j]))
				del iB[i]
				del cB[j]
				if not existe_estado(movimientos, iA, iB, cA, cB, 0):
					agregar_estado(movimientos, iA, iB, cA, cB, 0)
					res = ida(iA, iB, cA, cB, movimientos, mov, newVel)
					movimientos.pop()
					if res[0] == 1:
						nodo.ac.append(res[1])
						velMin = min(velMin, res[2])
		
				mov.pop()
			pass
		pass

	valido = nodo.aa != [] or nodo.cc != [] or nodo.a != [] or nodo.c != [] or nodo.ac != []
	return (valido, nodo, velMin)


indysA = [1, 2, 3]
canivA = [4, 5, 6]

res = ida(indysA, [], canivA, [], [], [], 0)

print res[2], velocidad_minima