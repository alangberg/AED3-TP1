#encoding: utf-8

"""modo de uso: python correr_experimentos.py 1(repetir experimentos)/0(no repetir experimentos)"""

ejecutable = "./tiempo"
datosPuro = "tiemposPuroPython.dat"
datosPoda = 'tiempoPodaPython.dat'
outputGrafico = 'ej2.png'
rango = range(1, 5000)
repes = 9999
labelPuro = u"Sin podas"
labelPoda = u"Con podas"

def armarArgumentos(ejecutable, repes, rango, puro = True):
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
		with open(datosPoda, 'w') as f:
			args =  armarArgumentos(ejecutable, repes, rango, puro = False)
			print args
			#los parámetros de call son: 
			#	args: una lista con los argumentos del programa, como si fuera la terminal (ver armarArgumentos)
			#	tiene parámetros opcionales stdout, stdin, stderr para redirigirlos a archivos. 
			#	Ojo con hacer pipes, ver documentación. 
		 	call(args, stdout=f)

		
		with open(datosPuro, 'w') as f:
			args =  armarArgumentos(ejecutable, 3, range(2, 8), puro = True)
			print args
		 	call(args, stdout=f)
		
		#Acá se cierra f, así si lo interrumpimos mientras mide para 8,
		#los datos anteriores están escritos en el archivo
		
		#'a' indica que el archivo se abre en modo append (agregar)
		#	Esto significa que si no existe un archivo con ese nombre, se crea.
		#	Si ya existe, se conserva y se le agrega  al final lo que se vaya a escribir.		
		with open(datosPuro, 'a') as f:
			args =  armarArgumentos(ejecutable, 3, [8], puro = True)
			print args
		 	call(args, stdout=f)

	from plots import main
	main(dataFiles=[datosPuro, datosPoda], output = outputGrafico, labels = [labelPuro, labelPoda], show = True)
