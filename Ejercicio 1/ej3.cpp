/*   public int bottomUpDP(int val[], int wt[], int W){
        int K[][] = new int[val.length+1][W+1];
        for(int i=0; i <= val.length; i++){
            for(int j=0; j <= W; j++){
                if(i == 0 || j == 0){
                    K[i][j] = 0;
                    continue;
                }
                if(j - wt[i-1] >= 0){
                    K[i][j] = Math.max(K[i-1][j], K[i-1][j-wt[i-1]] + val[i-1]);
                }else{
                    K[i][j] = K[i-1][j];
                }
            }
        }
        return K[val.length][W];
}
*/
#include <iostream>
#include <vector>
using namespace std;

int max(int a, int b){
    if(a>b){
        return a;
    }else{
        return b;
    }
}

int bottomUpDP(std::vector<int> val, std::vector<int> wt, int W){
        
        std::vector<int> v;
        for(int i=0;i<W+1;i++){
        v.push_back(0);}

       vector<vector<int> > K (val.size()+1,v);
    
        for(int i=0; i <= val.size(); i++){
            for(int j=0; j <= W; j++){
                if(i == 0 || j == 0){
                    K[i][j] = 0;
                    
                }
                if(j - wt[i-1] >= 0){
                    K[i][j] = max(K[i-1][j], K[i-1][j-wt[i-1]] + val[i-1]);
                }else{
                    K[i][j] = K[i-1][j];
                }
            }
        }
        return K[val.size()][W];
}


int main(int argc, char const *argv[])
{
    std::vector<int> wt ={1,3,4,5};
    int W=7;
    std::vector<int> val={1,4,5,7};
    //int vl=4;
    cout<< bottomUpDP(val, wt, W);
    return 0;
}