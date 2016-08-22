#pragma once
#include <iostream>
#include <vector>

using namespace std;

#define INF 999 // alguna cota lo suficientemente grande

struct Nodo {

	Nodo();
	~Nodo();

	bool valido;

	vector<Nodo*> aa; // vector de ramas del movimiento AA
	vector<Nodo*> cc; // vector de ramas del movimiento CC
	vector<Nodo*> ac; // vector de ramas del movimiento AC

	vector<Nodo*> a; // vector de ramas del movimiento A
	vector<Nodo*> c; // vector de ramas del movimiento C

	int vel; // la velocidad la guardo en cada nodo
};

// Contructor de Nodo
Nodo::Nodo() {
	vector<Nodo*> vacio;
	this->aa = vacio;
	this->cc = vacio;
	this->ac = vacio;

	this->a = vacio;
	this->c = vacio;

	this->vel = 0;
	this->valido = true; // por default todos los nodos son soluciones validas
}

// Destructor de Nodo, es recursivo
// borro cada nodo de cada vector
Nodo::~Nodo() {
	for (int i = 0; i < this->aa.size(); ++i) delete this->aa[i];
	for (int i = 0; i < this->cc.size(); ++i) delete this->cc[i];
	for (int i = 0; i < this->ac.size(); ++i) delete this->ac[i];

	for (int i = 0; i < this->a.size(); ++i) delete this->a[i];
	for (int i = 0; i < this->c.size(); ++i) delete this->c[i];
}
