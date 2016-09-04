#include <vector>
#include <iostream>
#include <algorithm>
#include <math.h>  
#include <string>

using namespace std;

/*vector<int> toBase3(int n){
	vector<int> res;
	if(n < 3){
		res.push_back(n);
	} else {
		res = toBase3(n / 3);
		res.push_back(n % 3);
	}
	return res;
} */

vector<int> reverse(vector<int> v){
	int j = 0;
	vector<int> res;
	for(int i = v.size()-1; i >= 0; --i){
		res.push_back(v[i]);
	}
	return res;
}

vector<int> toBase3(int n){
	vector<int> res;

	while(n>=3){
		res.push_back(n % 3);
		n/=3;
	}
	
	if(n < 3){
		res.push_back(n);
		return res;
	} 
}

vector<int> balancear(vector<int> v){
	vector<int> res(v.size() + 1, 0);
	//v =reverse(v);

	int i = 0;
	for(int j = 0; j < v.size(); ++j){
		if(v[j] == 2){
			res[i] = res[i] - 1;
			res[i+1] = res[i+1] + 1;
		} else if(v[j] == 1){
			if(res[i] == 1){
				res[i] = -1;
				res[i+1] = res[i+1] + 1;
			} else {
				res[i] = 1;
			}
		}
		i++;
	} 
	return res;
}

void imprimirVector(vector<int> v){
	if(v.size() == 0) return; // si no tiene nada, que no imprima nada
	for(int i = 0; i < v.size(); ++i){
		cout << v[i] << " ";
	}
	cout << endl;
}

void ej2(int n){
	vector<int> v = balancear(toBase3(n));
	vector<int> izquierda;
	vector<int> derecha;

	for(int i = 0; i < v.size(); ++i){
		if(v[i] == 1){
			izquierda.push_back(pow(3, i));
		}else if(v[i] == -1){
			derecha.push_back(pow(3, i));
		}	
	}

	// cout << izquierda.size() << " " << derecha.size() << endl;

	sort(izquierda.begin(), izquierda.end());
	sort(derecha.begin(), derecha.end());

	// imprimirVector(izquierda);
	// imprimirVector(derecha);
}

int main(int argc, char *argv[]){
	// int t = atoi(argv[1]);
	int t;
	cin >> t;
	ej2(t);

	return 0;
}