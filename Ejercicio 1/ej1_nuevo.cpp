#include <iostream>
#include <cassert>
#include <stdlib.h>
#include <stdio.h>
#include <sstream>
#include <string>
#include <set>

#include "nodo.h"
#include "ej1.h"

using namespace std;


void split(const string &s, char delim, vector<int> &elems) {
    stringstream ss;
    ss.str(s);
    string item;
    while (getline(ss, item, delim)) {
        elems.push_back(atoi(item.c_str()));
    }
}

struct Estado {
 	Estado();
 	Estado(vector<unsigned int>&a, vector<unsigned int>&b, vector<unsigned int>&c, vector<unsigned int>&d, bool i) {
 		ida = i;
 		if (i) {
 			iA = set<unsigned int>(a.begin(), a.end());
 			iB = set<unsigned int>(b.begin(), b.end());
 			cA = set<unsigned int>(c.begin(), c.end());
 			cB = set<unsigned int>(d.begin(), d.end());
 		} else {
 			iA = set<unsigned int>(b.begin(), b.end());
 			iB = set<unsigned int>(a.begin(), a.end());
 			cA = set<unsigned int>(d.begin(), d.end());
 			cB = set<unsigned int>(c.begin(), c.end());
 		}
 	}

 	set<unsigned int> iA;
 	set<unsigned int> iB;
 	set<unsigned int> cA;
 	set<unsigned int> cB;
 	bool ida;

 	bool iguales(Estado& otro) {
 		return (iA == otro.iA && iB == otro.iB && cA == otro.cA && cB == otro.cB && ida == otro.ida);
 	}

 };

bool nodo_visitado(vector<Estado>& movimientos, vector<unsigned int>& iA, vector<unsigned int>& iB, vector<unsigned int>& cA, vector<unsigned int>& cB, bool ida) {
	Estado e = Estado(iA, iB, cA, cB, ida);
	for (int i = 0; i < movimientos.size(); i++) {
		if (movimientos[i].iguales(e)) return true;
	}
	return false;
}

void agregar_nodo(vector<Estado>& movimientos, vector<unsigned int>& iA, vector<unsigned int>& iB, vector<unsigned int>& cA, vector<unsigned int>& cB, bool ida) {
	movimientos.push_back(Estado(iA, iB, cA, cB, ida));
}

// Lo declaro primero porque si no no compila. La funcion ida() la usa y si no esta arriba, no sabe que es.
Nodo* cruzar_puente(vector<unsigned int> indysA, vector<unsigned int> canibA, vector<unsigned int> indysB, vector<unsigned int> canibB, bool ida, vector<Estado> movimientos, int vel, int* velocidad_minima) {
	// No importa cual sea el escenario siempre voy a necesitar un nodo nuevo
	Nodo* new_nodo = new Nodo(); // Por default su vel = 0 y valido = true
	
	// Si hay mas canibales que arqueologos de algun lado (y cantidad de arqueologos != 0) perdi
	if ((!indysA.empty() and indysA.size() < canibA.size()) || (!indysB.empty() and indysB.size() < canibB.size())) {
		new_nodo->valido = false; // Marco en el nodo que NO es solucion
		return new_nodo;

	// Si no hay mas arqueologos ni canibales del lado A, gane
	} else if ((indysA.empty() && canibA.empty() && ida) || (indysB.empty() && canibB.empty() && !ida)) {
		if (*velocidad_minima != -1) *velocidad_minima = min(*velocidad_minima, vel); // Seteo su velocidad
		else *velocidad_minima = vel;
		return new_nodo;
	} else if (*velocidad_minima != -1 && vel > *velocidad_minima) {
		new_nodo->valido = false; // Marco en el nodo que NO es solucion
		return new_nodo;
	}

	for (unsigned int i = 0; i < indysA.size(); i++) {
		// copio los vectores para modificarlos sin perder los originales
		vector<unsigned int> iA (indysA);
		vector<unsigned int> iB (indysB);

		unsigned int new_vel = vel + iA[i]; // sumo a la velocidad actual el maximo entre los dos arqueologos

		// Los agrego al vector del otro lado
		iB.push_back(iA[i]);

		// los saco del vector
		iA.erase(iA.begin() + i);

		if (!nodo_visitado(movimientos, iA, iB, canibA, canibB, !ida)) {
			agregar_nodo(movimientos, iA, iB, canibA, canibB, !ida);
			Nodo* res = cruzar_puente(iB, canibB, iA, canibA, !ida, movimientos, new_vel, velocidad_minima); // hago la recursion
			movimientos.pop_back();
			if (res->valido) // si es solucion
				new_nodo->a.push_back(res); // lo guardo en el nodo nuevo que va a devolver la funcion
		}

		for (unsigned int j = i + 1; j < indysA.size(); j++) {

			// copio los vectores para modificarlos sin perder los originales
			vector<unsigned int> iA (indysA);
			vector<unsigned int> iB (indysB);

			unsigned int new_vel = vel + max(iA[i], iA[j]); // sumo a la velocidad actual el maximo entre los dos arqueologos

			// Los agrego al vector del otro lado
			iB.push_back(iA[i]);
			iB.push_back(iA[j]);

			// los saco del vector
			iA.erase(iA.begin() + i);
			iA.erase(iA.begin() + (j - 1)); // el -1 es porque ya sace el iA[i] entonces hay un elemento menos

			if (!nodo_visitado(movimientos, iA, iB, canibA, canibB, !ida)) {
				agregar_nodo(movimientos, iA, iB, canibA, canibB, !ida);
				Nodo* res = cruzar_puente(iB, canibB, iA, canibA, !ida, movimientos, new_vel, velocidad_minima); // hago la recursion
				movimientos.pop_back();
				if (res->valido) // si es solucion
					new_nodo->aa.push_back(res); // lo guardo en el nodo nuevo que va a devolver la funcion
			}
		}
	}

	for (unsigned int i = 0; i < canibA.size(); i++) {
		vector<unsigned int> cA (canibA);
		vector<unsigned int> cB (canibB);

		unsigned int new_vel = vel + cA[i]; // sumo a la velocidad actual el maximo entre los dos arqueologos

		// Los agrego al vector del otro lado
		cB.push_back(cA[i]);

		// los saco del vector
		cA.erase(cA.begin() + i);

		if (!nodo_visitado(movimientos, indysA, indysB, cA, cB, !ida)) {
			agregar_nodo(movimientos, indysA, indysB, cA, cB, !ida);
			Nodo* res = cruzar_puente(indysB, cB, indysA, cA, !ida, movimientos, new_vel, velocidad_minima); // hago la recursion
			movimientos.pop_back();
			if (res->valido) // si es solucion
				new_nodo->c.push_back(res); // lo guardo en el nodo nuevo que va a devolver la funcion
		}
		for (unsigned int j = i + 1; j < canibA.size(); j++) {
			vector<unsigned int> cA (canibA);
			vector<unsigned int> cB (canibB);

			unsigned int new_vel = vel + max(cA[i], cA[j]);

			cB.push_back(cA[i]);
			cB.push_back(cA[j]);

			cA.erase(cA.begin() + i);
			cA.erase(cA.begin() + (j - 1));

			if (!nodo_visitado(movimientos, indysA, indysB, cA, cB, !ida)) {
				agregar_nodo(movimientos, indysA, indysB, cA, cB, !ida);
				Nodo* res = cruzar_puente(indysB, cB, indysA, cA, !ida, movimientos, new_vel, velocidad_minima); // hago la recursion
				movimientos.pop_back();
				if (res->valido) // si es solucion
					new_nodo->cc.push_back(res); // lo guardo en el nodo nuevo que va a devolver la funcion
			}
		}
	}

	for (unsigned int i = 0; i < indysA.size(); i++) {
		for (unsigned int j = 0; j < canibA.size(); j++) {
			// copio todos los vectores para poder modificarlos sin perder los originales (que voy a necesitar para cada iteracion)
			vector<unsigned int> iA (indysA);
			vector<unsigned int> iB (indysB);
			vector<unsigned int> cA (canibA);
			vector<unsigned int> cB (canibB);

			unsigned int new_vel = vel + max(iA[i], cA[j]); // nueva velocidad

			// los meto en su respectivos vectores contrarios
			iB.push_back(iA[i]);
			cB.push_back(cA[j]);

			// los elimino de sus vectores originales
			iA.erase(iA.begin() + i);
			cA.erase(cA.begin() + j);

			if (!nodo_visitado(movimientos, iA, iB, cA, cB, !ida)) {
				agregar_nodo(movimientos, iA, iB, cA, cB, !ida);
				Nodo* res = cruzar_puente(iB, cB, iA, cA, !ida, movimientos, new_vel, velocidad_minima); // hago la recursion
				movimientos.pop_back();
				if (res->valido) // si es solucion
					new_nodo->ac.push_back(res); // lo guardo en el nodo nuevo que va a devolver la funcion
			}
		}
	}
	// si todos sus vectores de ramas estan vacios quiere decir que ninguno fue solucion, entonces este nodo tampoco lo es
	// caso contrario, por default valido = true
	new_nodo->valido = !(new_nodo->aa.empty() and new_nodo->cc.empty() and new_nodo->ac.empty() and new_nodo->c.empty() and new_nodo->a.empty());
	return new_nodo;
}

int main(int argc, char const *argv[]) {
	
	vector<unsigned int> indysA;
	vector<unsigned int> indysB;

	vector<unsigned int> canibA;
	vector<unsigned int> canibB;

	unsigned int cantidad_arqueologos;
	unsigned int cantidad_canibales;

	string entrada;
	getline(cin, entrada, '\n'); // tomo toda la linea de entrada como string

	// saco el 1er y 3er elemento, esto es medio harcodeado por dos cosas
	// 1. asumo que no me van a pasar numeros mayores a 6 y por lo tanto no van a tener dos digitos, por eso [0] y [2] y no algo mas unsigned int
	// 2. como cada numero esta en 'char' tengo que pasarlo a 'unsigned int', '0' = 48. Ej. '2' = 50, 2 = '2' - 48
	cantidad_arqueologos = (unsigned int) entrada[0] -48;
	cantidad_canibales = (unsigned int) entrada[2] -48;

	assert(cantidad_arqueologos > 0 and cantidad_arqueologos >= cantidad_canibales); // un assert para no pifiarla
	std::vector<int> numeros;

	if (cantidad_arqueologos > 0) {
		cout << "Ingrese " << cantidad_arqueologos << " arqueologos: ";
		getline(cin, entrada, '\n');

		split(entrada, ' ', numeros);

		for (unsigned int i = 0; i < numeros.size(); i++) {
			indysA.push_back(numeros[i]); // aca la idea es la misma que arriba
		}
	}

	assert(cantidad_arqueologos == indysA.size());
	numeros.clear();

	if (cantidad_canibales > 0) {
		cout << "Ingrese " << cantidad_canibales << " canibales: ";
		getline(cin, entrada, '\n');
		split(entrada, ' ', numeros);

		for (unsigned int i = 0; i < numeros.size(); i++) {
			canibA.push_back(numeros[i]); // aca la idea es la misma que arriba
		}
	}

	assert(cantidad_canibales == canibA.size());

	vector<Estado> movimientos;
	int velocidad = -1;

	Nodo* res = cruzar_puente(indysA, canibA, indysB, canibB, true, movimientos, 0, &velocidad);
	cout << velocidad << endl;

	delete res; // no hay que olvidar de deletear que si no perdemos memoria

	return 0;
}
	