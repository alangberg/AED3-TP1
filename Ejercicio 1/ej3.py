import sys
def knapsack(val, wt, W): 
	K = [[0 for i in xrange(len(val)+1)] for y in xrange(W+1)]
	for i in xrange(0,len(val)+1):
	 	for j in xrange(0,W+1):
	 	 	if i==0 or j==0:
	 	 	 	K[i].append(0)
	 	 	else:

	 	 		if j - wt[i-1] >= 0:
	 	 			K[i][j] = max(K[i-1][j], K[i-1][j-wt[i-1]] + val[i-1])
	 	 		else:
	 	 			K[i][j] = K[i-1][j]
	return K[len(val)][W]


we= [1,3,4,5]
We=7
va=[1,4,5,7]

print knapsack(va,we,We)









   public int bottomUpDP(int val[], int wt[], int W){
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