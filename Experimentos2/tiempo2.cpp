
#include "ej2.h"
#include <chrono>
#include <stdlib.h>
#include <vector>
#include <utility>
#include <iostream>


#define ya chrono::high_resolution_clock::now

using namespace std;

// ./tiempo repeticiones P(puro)/_(poda) n1 n2 n3 ...

int main(int argc, char const *argv[])
{
	int repes = atoi(argv[1]);
	//bool puro = argv[2][0] == 'P';
	vector<int> ns(argc-3);
	for (int i = 0; i < ns.size(); i++) {
		ns[i] = atoi(argv[i+3]);
	}
	for (auto n : ns) {
		vector<long long int> solucion(n);
		cout << n << ' ';
		for (int t = 0; t < repes; t++) {
			cerr << "Empezando medicion nro "<< t+1 << " para n = " << n << endl;
			auto start = ya();
			solucion = balancear(toBase3(n));
			auto end = ya();
			cout << chrono::duration_cast<std::chrono::nanoseconds>(end-start).count() << "\t";
		}
		cout << "& ";
		for (int i = 0; i < solucion.size(); ++i)
				cout << solucion[i];
		cout << "\n";
	}
}


