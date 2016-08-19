#include <vector>
#include <iostream>
#include <algorithm>
#include <math.h>  
#include <string>
using namespace std;

vector<int> toBase3(int n){
	std::vector<int> res;
	if(n<3){
		res.push_back(n);
		return res;
	}else{
		res = toBase3(n/3);
		res.push_back(n%3);
		return res;
	}

}

std::vector<int> reverse( std::vector<int> v){
int j=0;
std::vector<int> res;
for (int i = v.size()-1; i >= 0; --i){
	res.push_back(v[i]);
}

return res;
}

std::vector<int> balancear(std::vector<int> v){
	std::vector<int> res(v.size()+1,0);
	v =reverse(v);

	int i = 0;
	for (int j = 0; j < v.size(); ++j){
		/* code */
	  
		if(v[j]==2){
			res[i] = res[i] - 1;
			res[i+1] = res[i+1] + 1;
		}else if(v[j]==1){
			if(res[i]==1){
				res[i] = -1;
				res[i+1] = res[i+1] + 1;
			}else{
				res[i] = 1;
			}
		}

		i++;
	} 


	return res;
}

void imprimirVector(std::vector<int> v){
	for (int i = 0; i < v.size(); ++i)
	{
		cout<< v[i] << " ";
	}
	cout<<endl;
}

void ej2(int n){
std::vector<int> v = balancear(toBase3(n));
std::vector<int> izquierda;
std::vector<int> derecha;


for (int i = 0; i < v.size(); ++i){
	if(v[i]==1){
		izquierda.push_back(pow(3,i));
	}else if(v[i]==-1){
		derecha.push_back(pow(3,i));
	}	
}

cout<< izquierda.size() << " " << derecha.size() << endl;

sort(izquierda.begin(), izquierda.end());
sort(derecha.begin(), derecha.end());



imprimirVector(izquierda);
imprimirVector(derecha);

}

int main(int argc, char *argv[])
{


	int t = atoi(argv[1]);
	ej2(t);

	return 0;
}