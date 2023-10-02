class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> output(n+1);
        output[0] = 0;
        for (int i=1; i<=n;i++){
            //simple solution
            // countBits(N) = countBits(2N)
            // countBits(N)+1 = countBits(2N+1)
            // output[i] = output[i/2]+i%2;

            //optimal solution: use XOR
            // output[i] = output[i&(i-1)]+1;

            //an even faster solution: 
            // shifting >> 1 equivalent to i/2
            // & 1 equivalent to i%2
            output[i] = output[i >> 1] + (i & 1);
        }
        return output;
    }
};