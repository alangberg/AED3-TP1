#include "ej2_alternativo.h"
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
	int pot_max;

	for(unsigned long long p = pMin; p <= pow(10,pMax); p+=(pow(10,pMax)/100)){
		unsigned long long n = p;
		// cout << p << ' ' << n << endl;
		vector<int> solucion;
		double medicion = 0;
		auto inicio_medicion = ya();
		for(int i = 0; i < repeticiones; i++){
			vector<int> v = toBase3(n,pot_max);
			solucion = balancear(v,pot_max);
		}
		auto fin_medicion = ya();
		tupla<unsigned long long, double> t(n/(log(n)/log(3)), (double) chrono::duration_cast<std::chrono::nanoseconds>(fin_medicion - inicio_medicion).count()/repeticiones);
		mediciones.push_back(t);
	}
	ofstream salida;
	salida.open(argv[5]);
	for(int i = 0; i < mediciones.size(); i++){
		salida << mediciones[i].primero << " "
			<< mediciones[i].segundo << endl;
	}
}


