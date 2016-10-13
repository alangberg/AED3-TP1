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


constante = 1500
x_Cuad = x
y_Cuad = [constante * 30 * 24 for i in x_Cuad]

fig = plt.figure()
fig.patch.set_facecolor('white')

my_xticks = ["[2, 12]","[12, 2]","[4, 6]","[6, 4]","[3, 8]","[8, 3]"]
plt.xticks(x, my_xticks)

ax1 = fig.add_subplot(111)
pylab.plot(x_Cuad, y_Cuad, c='black', label= u'Cota teórica: cte * cantTesoros * capM1 * capM2')
pylab.plot(x, y, c='b', marker= 'o', markersize = 5,  label= u'Tiempo de ejecución')

ax1.set_xlabel('Capacidad [Mochila 1, Mochila 2]')
ax1.set_ylabel(u'Tiempo de ejecución [nanosegundos]')

leg = ax1.legend()

leg = plt.legend( loc = 'upper left')

plt.axis((1-0.2,len(my_xticks)+0.2,0,2000000))

plt.savefig(sys.argv[2], format='eps', bbox_inches = 'tight')
# plt.savefig(sys.argv[2], format='png', bbox_inches = 'tight')

plt.close(fig)