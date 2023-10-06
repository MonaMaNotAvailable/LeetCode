class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {

        //faster: 1 while loop utilize same memory
        double ans=0;
        int sum=0,maxx=INT_MIN;
        int i=0,j=0,n=nums.size();
        while(j<n){
            sum+=nums[j];
            if(j-i+1<k){
                j++;
            }
            else if(j-i+1==k){
                maxx=max(maxx,sum);
                sum-=nums[i];
                i++;
                j++;
            }
        }
        return maxx/(double)k;

        //slower: 2 for loops
        // int output = 0, temp = 0;

        // for(int i = 0;i<k;i++){
        //     temp += nums[i];
        // }

        // output = temp;

        // for(int j=k;j<nums.size();j++){
        //     temp+=nums[j];
        //     temp-=nums[j-k];
        //     output = max(output, temp);
        // }
        // return output/double(k);
    }
};