#include "ej1.h"
#include "nodo.h"
#include <chrono>
#include <stdlib.h>
#include <vector>
#include <utility>
#include <iostream>
#include <cassert>
#include <vector>

#define ya chrono::high_resolution_clock::now

using namespace std;

// ./tiempo repeticiones P(puro)/_(poda) n1 n2 n3 ...

int main(int argc, char const *argv[])
{
	assert(argc > 1);
	int repes = atoi(argv[1]);

	unsigned int cantidad_arqueologos =  atoi(argv[2]);
	unsigned int cantidad_canibales = atoi(argv[3]);
	std::vector<double> solucion;
	for (int t = 0; t < repes; t++) {		

		vector<unsigned int> indysB;
		vector<unsigned int> canibB;

		vector<unsigned int> canibA (cantidad_canibales, 1);
		vector<unsigned int> indysA (cantidad_arqueologos, 1);

		auto start = ya();
		Nodo* res = ida(indysA, canibA, indysB, canibB, 0, false); // Where the magic happens!!
		auto end = ya();
		
		delete res; // no hay que olvidar de deletear que si no perdemos memoria
		solucion.push_back(chrono::duration_cast<chrono::duration<double, std::nano>>(end-start).count());
	}

	double promedio;
	for(std::vector<double>::iterator it = solucion.begin(); it != solucion.end(); ++it) promedio += (*it);
	cout << cantidad_arqueologos << ' ' << promedio / repes << endl;
}


