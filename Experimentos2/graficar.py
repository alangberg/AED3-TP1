# -*- coding: utf-8 -*-

import sys
import matplotlib.pyplot as plt
import math
from math import log
from math import ceil
import pylab
import numpy as np


with open("data.out") as file:
	lineas = file.readlines()

rango = xrange(1,33)
with open('datosLog', 'w') as file:
	for x in xrange(0, 33):
		file.write(str(long(x)) + " " + str(long(ceil(log(3**x,3)))) + "\n")


arr = np.genfromtxt("data.out")
x_pot3 = [row[0] for row in arr]
y_pot3 = [row[1] for row in arr]

arr = np.genfromtxt("datosLog")
x_log = [row[0] for row in arr]
y_log = [row[1] for row in arr]

fig = plt.figure()
fig.patch.set_facecolor('white')

ax1 = fig.add_subplot(111)
pylab.plot(x_log, y_log, c='g', label= 'Teorico - Logaritmico')
pylab.plot(x_pot3, y_pot3, c='b', label= 'Potencias de 3')


ax1.set_xlabel('Peso de la llave (P = 3^x)')
ax1.set_ylabel('Tiempo de ejecucion (segundos)')

leg = ax1.legend()

leg = plt.legend( loc = 'upper left')

plt.savefig('grafico.eps', format='eps', bbox_inches = 'tight')
# plt.savefig('grafico.png', format='png', bbox_inches = 'tight')


plt.close(fig)