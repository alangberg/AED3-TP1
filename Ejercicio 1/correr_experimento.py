#encoding: utf-8

import math
import random
from subprocess import call, Popen, PIPE
from sys import argv
import time

data ="data"

ejecutable = "./tiempos"

repes = int(argv[1])

cantidad_canibales = int(argv[2])
data += '_' + str(cantidad_canibales)

a = 6 - (6 - cantidad_canibales)
n = 6 - cantidad_canibales

if a == 0: a = 1

# with open(data, 'w') as f:
# 	for x in xrange(a, n+1):
# 			call([ejecutable, str(repes), str(x), str(cantidad_canibales)], stdout=f)


import operator as op
def ncr(n, r):
	if n < r: 
		return 0
	r = min(r, n-r)
	if r == 0: return 1
	numer = reduce(op.mul, xrange(n, n-r, -1))
	denom = reduce(op.mul, xrange(1, r+1))
	return numer//denom

c = 100000
M = cantidad_canibales
with open('teorico', 'w') as f:
	for x in xrange(a, n+1):
		if x > 1:
			res = (3*x + 3*M + 2*x + 2*M) * (ncr(x, 2)+ncr(M,2)+x*M)**(2**(x+M))
			# res = (3*x + 3*M + 2*x + 2*M) * (ncr(x, 2)+ncr(M,2)+x*M)**(x)
		else:
			res = (3*x + 3*M + 2*x + 2*M) * (1+ncr(M,2)+x*M)**(2**(x+M))
			# res = (3*x + 3*M + 2*x + 2*M) * (1+ncr(M,2)+x*M)**(x)
		f.write(str(x) + ' ' + str(c*res)+'\n')

# import math
import numpy as np
import matplotlib.pyplot as plt
import pylab

arr = np.genfromtxt('data_0')
c0_x = [row[0] for row in arr]
c0_y = [row[1] for row in arr]
# err0 = [row[2] for row in arr]

arr = np.genfromtxt("data_1")
c1_x = [row[0] for row in arr]
c1_y = [row[1] for row in arr]
# err1 = [row[2] for row in arr]

arr = np.genfromtxt("data_2")
c2_x = [row[0] for row in arr]
c2_y = [row[1] for row in arr]
# err2 = [row[2] for row in arr]

arro3 = np.genfromtxt("teorico")
c3_x = [row[0] for row in arro3]
c3_y = [row[1] for row in arro3]
# err3 = [row[2] for row in arro3]

# arrr = np.genfromtxt("SEPIA_ASM")
# asm_x = [row[0] for row in arrr]
# asm_y = [row[1] for row in arrr]
# errASM = [row[2] for row in arrr]

# # a = np.arange(2048*2048)
# # b = 600*a


fig = plt.figure()
fig.patch.set_facecolor('white')

# plt.errorbar(c0_x, c0_y, err0)
# plt.errorbar(c3_x, c3_y, err1)
# plt.errorbar(c3_x, c3_y, err2)
# plt.errorbar(c3_x, c3_y, err3)
# plt.errorbar(asm_x, asm_y, errASM)

ax1 = fig.add_subplot(111)
pylab.plot(c0_x,c0_y,c='r', marker='o', markersize=5, label= 'M = 0')
pylab.plot(c1_x,c1_y,c='b', marker='s', markersize=5, label= 'M = 1')
pylab.plot(c2_x,c2_y,c='c', marker='D', markersize=5, label= 'M = 2')
pylab.plot(c3_x,c3_y,c='g', marker='^', markersize=5, label= 'f(n)')
# pylab.plot(asm_x,asm_y,c='m', label = 'ASM - SIMD')

# # pylab.plot((a),(b), c='r', label ='f(X)=1024x')
# # plt.errorbar(w, z, np.std(desvio))
# ax1.set_title("Ejercicio 1 - Tiempos de Ejecucion")
ax1.set_xlabel('Cantidad de arqueologos - N')
ax1.set_ylabel('Tiempo en nanosegundos')
ax1.set_yscale('log', basey=2)
# ax1.set_xscale('log', basex=2)


# #ax1.plot(np.log2(x),np.log2(y), c='r', label='EL CHACHO ARRIBAS')
# # pylab.plot((x),(y), c='r', label='ASM')
# # pylab.plot(w,z, c='b',label='C')
leg = ax1.legend()

leg = plt.legend( loc = 'upper left')

plt.show()