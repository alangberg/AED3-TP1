# -*- coding: utf-8 -*-
# argumentos: <mejor_caso.file> <peor_caso.file> <caso_rnd.file> <graph.png>

import sys
import matplotlib.pyplot as plt
import math
from math import log
from math import ceil
import pylab
import numpy as np


arr = np.genfromtxt(sys.argv[1])
xMejorCaso = [row[0] for row in arr]
yMejorCaso = [row[1] for row in arr]

arr = np.genfromtxt(sys.argv[2])
xPeorCaso = [row[0] for row in arr]
yPeorCaso = [row[1] for row in arr]

arr = np.genfromtxt(sys.argv[3])
xCasoRnd = [row[0] for row in arr]
yCasoRnd = [row[1] for row in arr]

constante = 240000
x_Lin = np.linspace(0, len(xMejorCaso), 100)
y_Lin = constante * x_Lin

fig = plt.figure()
fig.patch.set_facecolor('white')

ax1 = fig.add_subplot(111)
pylab.plot(x_Lin, y_Lin, c='black', label= u'Cota teórica')
pylab.plot(xMejorCaso, yMejorCaso, c='r', marker= 'o', markersize = 5,  label= u'Ningún tesoro entra')
pylab.plot(xPeorCaso, yPeorCaso, c='b', marker= 'o', markersize = 5,  label= u'Todos los tesoros entran')
pylab.plot(xCasoRnd, yCasoRnd, c='g', marker= 'o', markersize = 5,  label= u'Caso random')

ax1.set_xlabel('Cantidad de tesoros')
ax1.set_ylabel(u'Tiempo de ejecución [nanosegundos]')

leg = ax1.legend()

leg = plt.legend( loc = 'upper left')

plt.savefig(sys.argv[4], format='eps', bbox_inches = 'tight')
# plt.savefig(sys.argv[4], format='png', bbox_inches = 'tight')


plt.close(fig)