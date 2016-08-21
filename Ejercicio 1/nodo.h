#pragma once
#include <iostream>
#include <vector>

using namespace std;

#define INF 999 // alguna cota lo suficientemente grande

struct Nodo {

	Nodo();
	~Nodo();

	bool valido;

	vector<Nodo*> aa;
	vector<Nodo*> cc;
	vector<Nodo*> ac;

	vector<Nodo*> a;
	vector<Nodo*> c;

	int vel;
};


Nodo::Nodo() {
	vector<Nodo*> vacio;
	this->aa = vacio;
	this->cc = vacio;
	this->ac = vacio;

	this->a = vacio;
	this->c = vacio;

	this->vel = 0;
	this->valido = true;
}

Nodo::~Nodo() {
	for (int i = 0; i < this->aa.size(); ++i) delete this->aa[i];	
	for (int i = 0; i < this->cc.size(); ++i) delete this->cc[i];
	for (int i = 0; i < this->ac.size(); ++i) delete this->ac[i];

	for (int i = 0; i < this->a.size(); ++i) delete this->a[i];
	for (int i = 0; i < this->c.size(); ++i) delete this->c[i];
}
