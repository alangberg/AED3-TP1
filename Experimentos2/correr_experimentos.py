#encoding: utf-8
from math import log
from math import ceil

"""modo de uso: python correr_experimentos.py 1(repetir experimentos)/0(no repetir experimentos)"""

ejecutable = "./tiempo"
datoslog = "tiempoteorica.dat"
datospotencia = 'tiempopotencia.dat'
datospotmenos = 'tiempopotmenos.dat'
outputGrafico = 'ej2.png'
#rango = range(0, 10**10, (10**10)/50)
repes = 100
labellog = u"log3(P)"
labelpotmenos = u"P= 3^i - 1"
labelpotencia=u"P= 3^i"

rango= [(3**i) for i in xrange(0,20)] 
rango2 = [(3**i)-1 for i in xrange(0,20)]
#rango= [3**13-1, 3**14-1]
def funcion(a, rango):
		return []+ map(str,map(a, rango))

def armarArgumentos(ejecutable, repes, rango):
	# Esto arma los argumentos para call:
	# 	El primer elemento de la lista es el programa que se va a correr
	# 	El resto son los argumentos para este programa.
	#	O sea, si tenemos la lista l = [exec, a1, a2, a3] y hacemos call(l)
	#   es como si escribiéramos en la terminal exec a1 a2 a3 y apretáramos enter.
	#	Obs: todos tienen que ser strings.
	return [ejecutable, str(repes)] + map(str, rango)

if __name__ == '__main__':
	from sys import argv
	repetirExperimentos = bool(int(argv[1]))
	if repetirExperimentos :
		from subprocess import call

		#'w' indica que el archivo se abre en modo escritura
		#	Esto significa que si ya existe un archivo con el mismo nombre,
		#  	éste SE SOBREESCRIBE CON UN ARCHIVO VACÍO.
		#	Si no existe, se crea.
		with open(datospotencia, 'w') as f:
			args =  armarArgumentos(ejecutable, repes, rango)
			print args
			#los parámetros de call son: 
			#	args: una lista con los argumentos del programa, como si fuera la terminal (ver armarArgumentos)
			#	tiene parámetros opcionales stdout, stdin, stderr para redirigirlos a archivos. 
			#	Ojo con hacer pipes, ver documentación. 
		 	call(args, stdout=f)

		with open(datospotmenos, 'w') as f:
			args =  armarArgumentos(ejecutable, repes, rango2)
			print args
			#los parámetros de call son: 
			#	args: una lista con los argumentos del programa, como si fuera la terminal (ver armarArgumentos)
			#	tiene parámetros opcionales stdout, stdin, stderr para redirigirlos a archivos. 
			#	Ojo con hacer pipes, ver documentación. 
		 	call(args, stdout=f)

		with open(datoslog, 'w') as f:
			args =  [(y,log(y,3)) for y in rango]
			#args = map(str,map(int,args))
			print args
			for x in args:
				#x[0]=str(int(x[0]))
				#x[1]=str(int(x[1]))
				f.write(str(long(x[0])))
				f.write(" ")
				f.write(str(800*long(ceil(x[1]))))
				f.write('&')
				f.write("\n")
			#los parámetros de call son: 
			#	args: una lista con los argumentos del programa, como si fuera la terminal (ver armarArgumentos)
			#	tiene parámetros opcionales stdout, stdin, stderr para redirigirlos a archivos. 
			#	Ojo con hacer pipes, ver documentación. 
		 	#call(args, stdout=f)


		# with open(datoslog, 'w') as f:
		#  	caca= []
		#  	for x in rango:
		#  		caca+ [log(x,3)]
		#  	map(str,caca)

		#  	print caca
		#  	call(caca, stdout=f)
		
		
		#Acá se cierra f, así si lo interrumpimos mientras mide para 8,
		#los datos anteriores están escritos en el archivo
		
		#'a' indica que el archivo se abre en modo append (agregar)
		#	Esto significa que si no existe un archivo con ese nombre, se crea.
		#	Si ya existe, se conserva y se le agrega  al final lo que se vaya a escribir.		
	from plots import main
	main(dataFiles=[datospotencia, datoslog, datospotmenos], output = outputGrafico, labels = [labelpotencia, labellog,labelpotmenos], show = True)
