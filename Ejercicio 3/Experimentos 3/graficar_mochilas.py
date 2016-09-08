# -*- coding: utf-8 -*-
# argumentos: <input.file> <graph.png>

import sys
import matplotlib.pyplot as plt
import math
from math import log
from math import ceil
import pylab
import numpy as np


arr = np.genfromtxt(sys.argv[1])
x = [row[0] for row in arr]
y = [row[1] for row in arr]

constante = 32000 
x_Cuad = np.linspace(0, len(x), 100)
y_Cuad = constante * np.power(x_Cuad,2)

fig = plt.figure()
fig.patch.set_facecolor('white')

ax1 = fig.add_subplot(111)
pylab.plot(x_Cuad, y_Cuad, c='black', label= u'Cota teórica')
pylab.plot(x, y, c='b', marker= 'o', markersize = 5,  label= u'Tiempo de ejecución')

ax1.set_xlabel('Capacidad Mochila 1 y Mochila 2')
ax1.set_ylabel(u'Tiempo de ejecución [nanosegundos]')

leg = ax1.legend()

leg = plt.legend( loc = 'upper left')

#plt.savefig('grafico.eps', format='eps', bbox_inches = 'tight')
plt.savefig(sys.argv[2], format='png', bbox_inches = 'tight')


plt.close(fig)