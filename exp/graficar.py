# -*- coding: utf-8 -*-

import sys
import matplotlib.pyplot as plt
import math
from math import log
from math import ceil
import pylab
import numpy as np

arr = np.genfromtxt("./Resultados/data_3_Alt")
x_Pot3_Alt = [row[0] for row in arr]
y_Pot3_Alt = [row[1] for row in arr]

arr1 = np.genfromtxt("./Resultados/data_3Menos1_Alt")
x_Pot3Menos1_Alt = [row[0] for row in arr1]
y_Pot3Menos1_Alt = [row[1] for row in arr1]

arr2 = np.genfromtxt("./Resultados/data_3_original")
x_Pot3_Original = [row[0] for row in arr2]
y_Pot3_Original = [row[1] for row in arr2]

arr3 = np.genfromtxt("./Resultados/data_3Menos1_original")
x_Pot3Menos1_Original = [row[0] for row in arr3]
y_Pot3Menos1_Original = [row[1] for row in arr3]

constante = 150
x_Log = np.linspace(1, 3**33, 100)
y_Log = constante * np.log(x_Log)

fig = plt.figure()
fig.patch.set_facecolor('white')

ax1 = fig.add_subplot(111)
pylab.plot(x_Log, y_Log, label= 'Teorica - Log(P)')
# pylab.plot(x_Pot3_Alt, y_Pot3_Alt, c='g', marker= 'o', markersize = 5,  label= 'Potencias de 3 (Estatico)')
# pylab.plot(x_Pot3Menos1_Alt, y_Pot3Menos1_Alt, c='r', marker= 'o', markersize = 5,  label= 'Potencias de 3 - 1 (Estatico)')
pylab.plot(x_Pot3_Original, y_Pot3_Original, c='c', marker= 'o', markersize = 5,  label= 'Potencias de 3')
pylab.plot(x_Pot3Menos1_Original, y_Pot3Menos1_Original, c='m', marker= 'o', markersize = 5,  label= 'Potencias de 3 - 1')

ax1.set_xlabel('Peso de la llave')
ax1.set_ylabel('Tiempo de ejecucion (nanosegundos)')
ax1.set_xscale('log', basex=3)

leg = ax1.legend()

leg = plt.legend(loc= 'upper left')

plt.savefig('grafico.eps', format='eps', bbox_inches = 'tight')
# plt.savefig('grafico.png', format='png', bbox_inches = 'tight')


plt.close(fig)