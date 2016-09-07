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

arr = np.genfromtxt("data.out")
x_Pot3 = [row[0] for row in arr]
y_Pot3 = [row[1] for row in arr]

arr2 = np.genfromtxt("dataPot.out")
x_Pot = [row[0] for row in arr2]
y_Pot = [row[1] for row in arr2]


constante = 80
x_Log = np.linspace(1, 3**33, 100)
y_Log = constante * np.log(x_Log)

fig = plt.figure()
fig.patch.set_facecolor('white')

ax1 = fig.add_subplot(111)
pylab.plot(x_Log, y_Log, c='b', label= 'Teorico - Logaritmico')
pylab.plot(x_Pot, y_Pot, c='g', marker= 'o', markersize = 5,  label= 'Potencias de 3 - 1')
pylab.plot(x_Pot3, y_Pot3, c='r', marker= 'o', markersize = 5,  label= 'Potencias de 3')

ax1.set_xlabel('Peso de la llave (P = 3^x)')
ax1.set_ylabel('Tiempo de ejecucion (nanosegundos)')
ax1.set_xscale('log', basex=3)

leg = ax1.legend()

leg = plt.legend( loc = 'upper left')

#plt.savefig('grafico.eps', format='eps', bbox_inches = 'tight')
plt.savefig('grafico.png', format='png', bbox_inches = 'tight')


plt.close(fig)