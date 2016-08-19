import sys

def toBase3(n):
	if n < 3:
		res = []
		res.append(n)
		return res
	else:
		res = toBase3(int(n/3))
		res.append(n%3)
		return res


ls = toBase3(int(sys.argv[1]))
ls.reverse()
res = [0] * (len(ls) + 1) #arreglo de 0s
i = 0
for d in ls:
	if d == 2:
		# si tiene un 2 lo puedo reemplazar sumando la potencia que sigue y restando la potencia acutal
		# ej: (6)_10 == (20)_3 <==> 2*3^1 + 0*3^0 <==> 1*3^2 - 1*3^1 + 0*3^0  
		res[i] = res[i] - 1
		res[i+1] = res[i+1] + 1
	elif d == 1:
		if res[i] == 1:
			# entonces tendria un 2, tengo que dejar -1
			res[i] = -1
			res[i+1] = res[i+1] + 1
		else:
			res[i] = 1
	i = i + 1

# res.reverse()
# print res

i = 0
left = []
right = []
for d in res:
	if d == 1:
		left.append(3**i)
	elif d == -1:
		right.append(3**i)
	i = i + 1

left.reverse()
right.reverse()
print str(len(left)) + " " + str(len(right))
print left
print right


		

