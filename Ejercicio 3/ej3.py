class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))

knapsackWeight = [3,3,0];
weights = [2,1,3,4,5];
values = [2,1,5,10,10];

def maximoYElementos(options, items, weight, value):
	# AGREGAR los w_i como parametros, Ni idea porque carajo anda asi...
	maximo = 0
	elementos = []
	for x in options:
		while switch(x[0]):
			if case(0):
				elementos = items[w1][w2][w3]
				maximo = x[1]
				break
			if case(1):
				if maximo < x[1]:
					maximo = x[1]
					elementos = items[w1-weight][w2][w3]+[('M1',weight,value)]
				break
			if case(2):
				if maximo < x[1]:
					maximo = x[1]
					elementos = items[w1][w2-weight][w3]+[('M2',weight,value)]
				break
			if case(3):
				if maximo < x[1]:
					maximo = x[1]
					elementos = items[w1][w2][w3-weight]+[('M3',weight,value)]
				break
			
	return maximo, elementos

dp = [[[0]*(knapsackWeight[2]+1) for i in xrange(knapsackWeight[1]+1)] for i in xrange(knapsackWeight[0]+1)]
items = [[[[]]*(knapsackWeight[2]+1) for i in xrange(knapsackWeight[1]+1)] for i in xrange(knapsackWeight[0]+1)]

for i in xrange(0, len(weights)):
	for w1 in xrange(knapsackWeight[0], -1, -1): 								# [Peso mochila1 restando hasta 0]
		for w2 in xrange(knapsackWeight[1], -1, -1):							# [Peso mochila2 restando hasta 0]
			for w3 in xrange(knapsackWeight[2], -1, -1):						# [Peso mochila3 restando hasta 0]
				options = []													# options: [(option, value)]
				options.append((0,dp[w1][w2][w3]))								# 0 -> Peso anterior
				if weights[i] <= w1:
					options.append((1,dp[w1-weights[i]][w2][w3]+values[i]))		# 1 -> Agregandolo en la mochila 1
				if weights[i] <= w2:
					options.append((2,dp[w1][w2-weights[i]][w3]+values[i]))		# 2 -> Agregandolo en la mochila 2
				if weights[i] <= w3:
					options.append((3,dp[w1][w2][w3-weights[i]]+values[i]))		# 3 -> Agregandolo en la mochila 3

				dp[w1][w2][w3], items[w1][w2][w3] = maximoYElementos(options, items, weights[i], values[i])

# imprimirM(dp)
# imprimirM(items)

print "Peso total: " + str(dp[knapsackWeight[0]][knapsackWeight[1]][knapsackWeight[2]])
# print items[knapsackWeight[0]][knapsackWeight[1]][knapsackWeight[2]]

def imprimirLindo(tuplas, knapsackWeight):
	m1 = ""
	m2 = ""
	m3 = ""
	for t in tuplas:
		if t[0] == "M1":
			m1 = m1 + "[P=" + str(t[1]) + ", V=" + str(t[2]) + "]"
		if t[0] == "M2":
			m2 = m2 + "[P=" + str(t[1]) + ", V=" + str(t[2]) + "]"
		if t[0] == "M3":
			m3 = m3 + "[P=" + str(t[1]) + ", V=" + str(t[2]) + "]"

	print "Mochila 1[Capacidad=" + str(knapsackWeight[0]) + "]: " + m1
	print "Mochila 2[Capacidad=" + str(knapsackWeight[1]) + "]: " + m2
	print "Mochila 3[Capacidad=" + str(knapsackWeight[2]) + "]: " + m3

def imprimirM(matriz):
	for row in matriz:
		print row
	print ""

imprimirM(dp)
imprimirLindo(items[knapsackWeight[0]][knapsackWeight[1]][knapsackWeight[2]], knapsackWeight)
