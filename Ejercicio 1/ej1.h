#pragma once
#include "nodo.h"

using namespace std;

void test();

Nodo* vuelta(vector<unsigned int> indysA, vector<unsigned int> canibA, vector<unsigned int> indysB, vector<unsigned int> canibB, int vel);
Nodo* ida(vector<unsigned int> indysA, vector<unsigned int> canibA, vector<unsigned int> indysB, vector<unsigned int> canibB, int vel, bool antiLoop);
void split(const string &s, char delim, vector<string> &elems);