#include <iostream>
#include <cassert>
#include "nodo.h"

using namespace std;

// Lo declaro primero porque si no no compila. La funcion ida() la usa y si no esta arriba, no sabe que es.
Nodo* vuelta(vector<int> indysA, vector<int> canivA, vector<int> indysB, vector<int> canivB, int vel);

Nodo* ida(vector<int> indysA, vector<int> canivA, vector<int> indysB, vector<int> canivB, int vel, bool antiLoop) {
	// No importa cual sea el escenario siempre voy a necesitar un nodo nuevo
	Nodo* new_nodo = new Nodo(); // Por default su vel = 0 y valido = true
	
	// Si hay mas canivales que arqueologos de algun lado (y cantidad de arqueologos != 0) perdi
	if ((!indysA.empty() and indysA.size() < canivA.size()) || (!indysB.empty() and indysB.size() < canivB.size())) {
		new_nodo->valido = false; // Marco en el nodo que NO es solucion
		new_nodo->vel = vel; // Seteo la valocidad (podria no hacerlo, al no ser una solucion nunca la voy mirar)
		return new_nodo;

	// Si no hay mas arqueologos ni canivales del lado A, gane
	} else if (indysA.empty() && canivA.empty()) {
		new_nodo->vel = vel; // Seteo su velocidad
		return new_nodo;
	}

	int vel_min = INF; // variable para encontrar la velocidad minima

	// Si la cantidad de arqueologos del lado A es mayor a 1, es decir, 2 o mas arqueologos
	// quiere decir que el movimiento AA esta disponible
	if (indysA.size() > 1) {

		// Doble for() para generar todas las convinaciones posibles entre los arqueologos
		// j = i + 1, ya que de esta manera evito convidar un arquologo con sigo mismo y duplicar convidaciones (A1 y A2 / A2 y A1)
		for (int i = 0; i < indysA.size(); i++) {
			for (int j = i + 1; j < indysA.size(); j++) {

				// copio los vectores para modificarlos sin perder los originales
				vector<int> iA (indysA);
				vector<int> iB (indysB);

				int new_vel = vel + max(iA[i], iA[j]); // sumo a la velocidad actual el maximo entre los dos arqueologos

				// Los agrego al vector del otro lado
				iB.push_back(iA[i]);
				iB.push_back(iA[j]);

				// los saco del vector
				iA.erase(iA.begin() + i);
				iA.erase(iA.begin() + (j - 1)); // el -1 es porque ya sace el iA[i] entonces hay un elemento menos

				Nodo* res = vuelta(iA, canivA, iB, canivB, new_vel); // hago la recursion
				if (res->valido) { // si es solucion
					new_nodo->aa.push_back(res); // lo guardo en el nodo nuevo que va a devolver la funcion
					if (res->vel < vel_min) vel_min = res->vel; // me fijo si su velocidad es minima
				}
			}
		}
	}

	// es igual que el de arriba pero con dos canivales
	if (canivA.size() > 1) {
		for (int i = 0; i < canivA.size(); i++) {
			for (int j = i + 1; j < canivA.size(); j++) {
				vector<int> cA (canivA);
				vector<int> cB (canivB);

				int new_vel = vel + max(cA[i], cA[j]);

				cB.push_back(cA[i]);
				cB.push_back(cA[j]);

				cA.erase(cA.begin() + i);
				cA.erase(cA.begin() + (j - 1));

				Nodo* res = vuelta(indysA, cA, indysB, cB, new_vel);
	
				if (res->valido) {
					new_nodo->cc.push_back(res);
					if (res->vel < vel_min) vel_min = res->vel;
				}
			}
		}
	}


	// Si la cantidad de arqueologos y canivales es mayor a 0
	// quiere decir que tengo disponible el movimiento AC
	if (canivA.size() > 0 && indysA.size() > 0 and !antiLoop) {
		// Doble for() para generar todas las convinaciones entre arqueologos y canivales
		for (int i = 0; i < indysA.size(); i++) {
			for (int j = 0; j < canivA.size(); j++) {
				// copio todos los vectores para poder modificarlos sin perder los originales (que voy a necesitar para cada iteracion)
				vector<int> iA (indysA);
				vector<int> iB (indysB);
				vector<int> cA (canivA);
				vector<int> cB (canivB);

				int new_vel = vel + max(iA[i], cA[j]); // nueva velocidad

				// los meto en su respectivos vectores contrarios
				iB.push_back(iA[i]);
				cB.push_back(cA[j]);

				// los elimino de sus vectores originales
				iA.erase(iA.begin() + i);
				cA.erase(cA.begin() + j);

				Nodo* res = vuelta(iA, cA, iB, cB, new_vel); // hago la recursion

				if (res->valido) { // si es solucion
					new_nodo->ac.push_back(res); // lo guardo en el vector correspondiente del nuevo nodo
					if (res->vel < vel_min) vel_min = res->vel; // si es minimo lo guardo
				}
			}
		}
	}

	new_nodo->vel = vel_min; // seteo la velocidad del nuevo vector con el minimo obtenido
	// si todos sus vectores de ramas estan vacios quiere decir que ninguno fue solucion, entonces este nodo tampoco lo es
	// caso contrario, por default valido = true
	if (new_nodo->aa.empty() and new_nodo->cc.empty() and new_nodo->ac.empty()) new_nodo->valido = false;
	return new_nodo;
}


// Este el escenario donde estan volviendo del lado B a A
// la logica es exactamente la misma que la de arriba, solo que considera unicamente los movimientos A y C
Nodo* vuelta(vector<int> indysA, vector<int> canivA, vector<int> indysB, vector<int> canivB, int vel) {
	Nodo* new_nodo = new Nodo();

	if ((!indysA.empty() and indysA.size() < canivA.size()) || (!indysB.empty() and indysB.size() < canivB.size())) {
		new_nodo->valido = false;
		new_nodo->vel = vel;
		return new_nodo;
	} else if (indysA.empty() && canivA.empty()) {
		new_nodo->vel = vel;
		return new_nodo;
	}


	int vel_min = INF;

	if (indysB.size() > 0) {
		for (int i = 0; i < indysB.size(); i++) {
			vector<int> iA (indysA);
			vector<int> iB (indysB);

			int new_vel = vel + iB[i];
			iA.push_back(iB[i]);

			iB.erase(iB.begin() + i);
			
			Nodo* res = ida(iA, canivA, iB, canivB, new_vel, false);

			if (res->valido) {
				new_nodo->a.push_back(res);
				if (res->vel < vel_min) vel_min = res->vel;
			}
		}
	}

	if (canivB.size() > 0) {

		for (int i = 0; i < canivB.size(); i++) {	
			vector<int> cA (canivA);
			vector<int> cB (canivB);

			int new_vel = vel + cB[i];
			cA.push_back(cB[i]);

			cB.erase(cB.begin() + i);
			
			Nodo* res = ida(indysA, cA, indysB, cB, new_vel, false);

			if (res->valido) {
				new_nodo->c.push_back(res);
				if (res->vel < vel_min) vel_min = res->vel;
			}
		}
	}

	// Si ningun movimiento anterior resulto valido pruebo de hacer un movimiento AC (PARCHE PARA 3 Y 3)
	if (new_nodo->c.empty() && new_nodo->a.empty())
		// Si la cantidad de arqueologos y canivales es mayor a 0
		// quiere decir que tengo disponible el movimiento AC
		if (canivB.size() > 0 && indysB.size() > 0) {
			// Doble for() para generar todas las convinaciones entre arqueologos y canivales
			for (int i = 0; i < indysB.size(); i++) {
				for (int j = 0; j < canivB.size(); j++) {
					// copio todos los vectores para poder modificarlos sin perder los originales (que voy a necesitar para cada iteracion)
					vector<int> iA (indysA);
					vector<int> iB (indysB);
					vector<int> cA (canivA);
					vector<int> cB (canivB);

					int new_vel = vel + max(iB[i], cB[j]); // nueva velocidad

					// los meto en su respectivos vectores contrarios
					iA.push_back(iB[i]);
					cA.push_back(cB[j]);

					// los elimino de sus vectores originales
					iB.erase(iB.begin() + i);
					cB.erase(cB.begin() + j);

					Nodo* res = ida(iA, cA, iB, cB, new_vel, true); // hago la recursion

					if (res->valido) { // si es solucion
						new_nodo->ac.push_back(res); // lo guardo en el vector correspondiente del nuevo nodo
						if (res->vel < vel_min) vel_min = res->vel; // si es minimo lo guardo
					}
				}
			}
		}

	new_nodo->vel = vel_min;
	if (new_nodo->a.empty() and new_nodo->c.empty() and new_nodo->ac.empty()) new_nodo->valido = false;
	return new_nodo;
}

int main(int argc, char const *argv[]) {
	
	vector<int> indysA;
	vector<int> indysB;

	vector<int> canivA;
	vector<int> canivB;

	int cantidad_arqueologos;
	int cantidad_canivales;

	string entrada;
	getline(cin, entrada, '\n'); // tomo toda la linea de entrada como string

	// saco el 1er y 3er elemento, esto es medio harcodeado por dos cosas
	// 1. asumo que no me van a pasar numeros mayores a 6 y por lo tanto no van a tener dos digitos, por eso [0] y [2] y no algo mas inteligente
	// 2. como cada numero esta en 'char' tengo que pasarlo a 'int', '0' = 48. Ej. '2' = 50, 2 = '2' - 48
	cantidad_arqueologos = (int) entrada[0] -48;
	cantidad_canivales = (int) entrada[2] -48;

	assert(cantidad_arqueologos > 0 and cantidad_arqueologos >= cantidad_canivales); // un assert para no pifiarla

	if (cantidad_arqueologos > 0) {
		cout << "Ingrese " << cantidad_arqueologos << " arqueologos: ";
		getline(cin, entrada, '\n');

		for (int i = 0; i < entrada.length(); i++) {
			indysA.push_back((int) entrada[i] -48); // aca la idea es la misma que arriba
			i++;
		}
	}

	assert(cantidad_arqueologos == indysA.size());

	if (cantidad_canivales > 0) {
		cout << "Ingrese " << cantidad_canivales << " canivales: ";
		getline(cin, entrada, '\n');
		for (int i = 0; i < entrada.length(); i++) {
			canivA.push_back((int) entrada[i] -48); // aca la idea es la misma que arriba
			i++;
		}
	}

	assert(cantidad_canivales == canivA.size());

	Nodo* res = ida(indysA, canivA, indysB, canivB, 0, false); // Where the magic happens!!
	// cout << "Resultado: " << res->valido << endl;
	// cout << "Velocidad minima: " << res->vel << endl;
	
	cout << res->vel << endl;

	delete res; // no hay que olvidar de deletear que si no perdemos memoria

	return 0;
}


