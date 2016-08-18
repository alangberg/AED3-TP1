#include <vector>
#include <iostream>

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

	return reverse(res);
}

void imprimirVector(std::vector<int> v){
	for (int i = 0; i < v.size(); ++i)
	{
		cout<< v[i] << " ";
	}
	cout<<endl;
}

int main(int argc, char const *argv[])
{
	imprimirVector(toBase3(17));
	imprimirVector(balancear(toBase3(17)));

	return 0;
}