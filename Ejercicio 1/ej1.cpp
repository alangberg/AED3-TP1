#include <iostream>
#include <cassert>
#include "nodo.h"

using namespace std;

Nodo* vuelta(vector<int> indysA, vector<int> canivA, vector<int> indysB, vector<int> canivB, int vel);

Nodo* ida(vector<int> indysA, vector<int> canivA, vector<int> indysB, vector<int> canivB, int vel) {
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

	if (indysA.size() > 1) {
		for (int i = 0; i < indysA.size(); i++) {
			for (int j = i + 1; j < indysA.size(); j++) {

				vector<int> iA (indysA);
				vector<int> iB (indysB);

				int new_vel = vel + max(iA[i], iA[j]);

				iB.push_back(iA[i]);
				iB.push_back(iA[j]);

				iA.erase(iA.begin() + i);
				iA.erase(iA.begin() + (j - 1));

				Nodo* res = vuelta(iA, canivA, iB, canivB, new_vel);
				if (res->valido) {
					new_nodo->aa.push_back(res);
					if (res->vel < vel_min) vel_min = res->vel;
				}
			}
		}
	}

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

	if (canivA.size() > 0 && indysA.size() > 0) {
		for (int i = 0; i < indysA.size(); i++) {
			for (int j = 0; j < canivA.size(); j++) {
				vector<int> iA (indysA);
				vector<int> iB (indysB);
				vector<int> cA (canivA);
				vector<int> cB (canivB);

				int new_vel = vel + max(iA[i], cA[j]);

				iB.push_back(iA[i]);
				cB.push_back(cA[j]);

				iA.erase(iA.begin() + i);
				cA.erase(cA.begin() + j);

				Nodo* res = vuelta(iA, cA, iB, cB, new_vel);

				if (res->valido) {
					new_nodo->ac.push_back(res);
					if (res->vel < vel_min) vel_min = res->vel;
				}
			}
		}
	}

	new_nodo->vel = vel_min;
	if (new_nodo->aa.empty() and new_nodo->cc.empty() and new_nodo->ac.empty()) new_nodo->valido = false;
	return new_nodo;
}

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
			
			Nodo* res = ida(iA, canivA, iB, canivB, new_vel);

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
			
			Nodo* res = ida(indysA, cA, indysB, cB, new_vel);

			if (res->valido) {
				new_nodo->c.push_back(res);
				if (res->vel < vel_min) vel_min = res->vel;
			}
		}
	}

	new_nodo->vel = vel_min;
	if (new_nodo->a.empty() and new_nodo->c.empty()) new_nodo->valido = false;
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
	getline(cin, entrada, '\n');

	cantidad_arqueologos = (int) entrada[0] -48;
	cantidad_canivales = (int) entrada[2] -48;

	assert(cantidad_arqueologos > 0 and cantidad_arqueologos >= cantidad_canivales);

	if (cantidad_arqueologos > 0) {
		cout << "Ingrese " << cantidad_arqueologos << " arqueologos: ";
		getline(cin, entrada, '\n');

		for (int i = 0; i < entrada.length(); i++) {
			indysA.push_back((int) entrada[i] -48);
			i++;
		}
	}

	assert(cantidad_arqueologos == indysA.size());

	if (cantidad_canivales > 0) {
		cout << "Ingrese " << cantidad_canivales << " canivales: ";
		getline(cin, entrada, '\n');
		for (int i = 0; i < entrada.length(); i++) {
			canivA.push_back((int) entrada[i] -48);
			i++;
		}
	}

	assert(cantidad_canivales == canivA.size());

	Nodo* res = ida(indysA, canivA, indysB, canivB, 0);
	cout << "Resultado: " << res->valido << endl;

	cout << "Velocidad minima: " << res->vel << endl;

	delete res;

	return 0;
}


