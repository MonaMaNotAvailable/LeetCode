class Solution {
public:
    int tribonacci(int n) {
        // update a single list
        int dp[] ={0,1,1};
        for(int i=3;i<=n;i++){
            dp[i%3]=dp[0]+dp[1]+dp[2];
        }
        return dp[n%3];

        // use variables instead of array/list/queue
        // int n0 = 0, n1 = 1, n2 = 1, temp;

        // if(n==0){
        //     return n0;
        // }else if(n==1 || n==2){
        //     return n1;
        // }else{
        //     for (int i=3;i<=n;i++){
        //     temp = n0+n1+n2;
        //     n0 = n1;
        //     n1 = n2;
        //     n2 = temp;
        //     }
        //     return n2;
        // }

        // c++ does not have a built-in sum method
        // queue<int>  tri;
        // tri.push(0);
        // tri.push(1);
        // tri.push(1);

        // for (int i=3;i<=n;i++){
        //     tri.push(sum(tri));
        //     tri.pop();
        // }

        // return sum(tri);   
    }
};