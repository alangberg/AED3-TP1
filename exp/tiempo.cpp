#include "ej2.h"
#include <chrono>
#include <stdlib.h>
#include <vector>
#include <math.h>
#include <utility>
#include <iostream>
#include <fstream>
#include <time.h>

#define ya chrono::high_resolution_clock::now
using namespace std;

template<typename S, typename T>
struct tupla{
	S primero;
	T segundo;
	tupla(S p, T s) : primero(p), segundo(s){}
};

clock_t tStart;
clock_t tFinish;

// parametros de entrada
// 1-repeticiones, 2-desde, 3-hasta, 4-incremento, 5-salida
// $ ./tiempo 100 0 33 1 data.out
int main(int argc, char const *argv[]){
	int repeticiones = atoi(argv[1]);
	unsigned long long pMin = atoll(argv[2]);
	unsigned long long pMax = atoll(argv[3]);
	int inc = atoi(argv[4]);

	vector< tupla<unsigned long long, double> > mediciones;

	for(unsigned long long p = pMin; p <= pMax; p+=inc){
		unsigned long long n = pow(3,p);
		// cout << p << ' ' << n << endl;
		vector<int> solucion;
		double medicion = 0;
		auto inicio_medicion = ya();
		for(int i = 0; i < repeticiones; i++){
			solucion = balancear(toBase3(n));
		}
		auto fin_medicion = ya();
		tupla<unsigned long long, double> t(p, (double) chrono::duration_cast<std::chrono::nanoseconds>(fin_medicion - inicio_medicion).count()/repeticiones);
		mediciones.push_back(t);
	}
	ofstream salida;
	salida.open(argv[5]);
	for(int i = 0; i < mediciones.size(); i++){
		salida << mediciones[i].primero << " "
			<< mediciones[i].segundo << endl;
	}
}


