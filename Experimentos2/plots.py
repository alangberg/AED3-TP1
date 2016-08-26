#encoding: utf-8

"""modo de uso: python plots.py dataFile1 dataFile2 ... dataFileN outputFile"""

import numpy as np
import os, sys
import matplotlib.pyplot as pplot

def parse(f):
	"""
	Espera un archivo que en cada línea tenga: n t1 t2 t3 ... tk & FRUTA
		n debería ser el tamaño de la entrada (en nuestro caso, el tamaño del tablero)
		t1 ... tk son los tiempos de k mediciones (nosotros las vamos a promediar después)
		Ignora lo que venga después del & (aprovechamos esto para imprimir la solución en algún lado)
	Devuelve una lista con un par (n, [t1, ..., tk]) por cada línea.
	"""
	tiempos = []
	for l in f:
		l = l.strip()
		if l :
			#separmos solución de tiempos
			resto, sol = l.split('&', 2)
			#partimos los tiempos por espacios
			resto = resto.split()
			#parseamos el n del caso
			n = int(resto[0])
			#convertimos a int los tiempos
			ts = map(int, resto[1:])
			tiempos.append((n, ts))
	return tiempos

def main(dataFiles, output, show=False, labels=None):
	labels = labels if labels else dataFiles #si no me pasaste labels, ploteo con nombre de archivo
	
	#para cada archivo, vamos a plotear sus datos como una serie diferente
	Xs, Ys = [], []
	for f in dataFiles:
		#abrimos el archivo de datos con with...: para que no quede abierto innecesariamente
		#lo abrimos para lectura (no pasamos argumentos extra a open)
		with open(f) as dataFile:
			tiempos = parse(dataFile)
		#print tiempos
		ns, ts = [], []
		for (n, t) in tiempos:
			ns.append(n)
			#calculamos el promedio usando np.mean ya que lo tenemos
			ts.append(np.mean(t))

		#guardamos una COPIA de ns y ts para plotear
		Xs.append(list(ns))
		Ys.append(list(ts))
		
	plot = myPlot(Xs, Ys, 
		labels=labels,
		xlabel= u"Tamaño del lado del tablero", 	#rotulamos los ejes
		ylabel=u"TIempo de ejecución (ns)", 	#empezamos los stings con u" para que use unicode y podamos poner ó, ñ...	
		title = u"Tiempo de ejecución para distintos tamaños de tablero",		#ponemos título!
		plotter = pplot, 		#usamos el pplot
		ylog = False				#ploteamos en log
		)
	# plot = plotNBars(Xs, Ys, 
	# 	labels=dataFiles, 
	# 	xlabel= u"Tamaño del lado del tablero",
	# 	ylabel=u"TIempo de ejecución (ns)",
	# 	title = u"Tiempo de ejecución para distintos tamaños de tablero",
	# 	plotter = pplot,
	# 	ylog = True
	# 	)

	plot.savefig(output)
	if show:
		plot.show()

def myPlot(Xs, Ys, labels, xlabel, ylabel, title, plotter, ylog=False):
	"""Plotea una curva para cada x, y, tomándolos en orden de Xs e Ys"""
	for (x, y, l) in zip(Xs, Ys, labels):
		if ylog:
			plotter.yscale('log')
		plotter.plot(x, y, label= l, marker='o', linestyle = ':')
		plotter.xlabel(xlabel)
		plotter.ylabel(ylabel)
		plotter.title(title)
		plotter.legend()
	return plotter

def plotNBars(Xs, Ys, labels, xlabel, ylabel, title, plotter, ylog = False, horizontalLine = None, verticalLine = None):
	"""Como myPlot, pero en vez de curvas, barras."""
	import numpy.numarray as na
	maxData = max(map(len, Xs))
	minVal = min(map(min, Xs))
	xlocations = na.array(range(maxData))
	width = 0.7
	i = 0
	colores = ['b','g','r','c','m','y','k','w','#610b0b']
	bar_width = float(width/len(Xs))
	for (x, y, l) in zip(Xs, Ys, labels):
		plotter.bar(map(lambda t: t+bar_width*i, x), y, bar_width, label= l, color = colores[i], log=ylog)
		i += 1

	plotter.ylabel(ylabel)
	plotter.xlabel(xlabel)
	plotter.title(title)
	if horizontalLine:
		hline = plotter.axhline(linewidth=2, color='r', y = horizontalLine, linestyle='dashed') 
		bars.append(hline)
	if verticalLine:
		plotter.axvline(linewidth=2, color='r', x = verticalLine) 
	plotter.legend()
	plotter.xticks(xlocations+width/2+minVal, xlocations+minVal, fontsize = 12) #, rotation = 30
	
	return plotter


if __name__ == '__main__':
	main(dataFiles = sys.argv[1:-1], output = sys.argv[-1], show = True)	