class Solution {
public:
    int minNumberOperations(vector<int>& target) {
        // Approach 1: 1d dp to record moves needed so far, time O(n), space O(n)
        int n = target.size(); // get the size of the target array
        int dp[n]; // create a dp array to store the minimum operations required up to each index
        dp[0] = target[0]; // initialize the first element of dp with the first element of target
        // iterate through the target array starting from the second element
        for(int i = 1; i < n; i++){
            // no additional operations are needed, dp[i] is the same as dp[i-1]
            if(target[i] <= target[i - 1]){
                dp[i] = dp[i - 1];
            } else {
                // if the current element is greater than the previous one, the difference between the two is added to dp[i-1] to get dp[i]
                dp[i] = dp[i - 1] + target[i] - target[i - 1];
            }
        }
        // return the last element of dp which contains the total minimum operations required
        return dp[n - 1];



        // Approach 2: imagine the target as a wall of bricks, time O(n), space O(1)
        // initialize count with the first element since we need to build up to at least this height
        int count = target[0];
        // iterate through the target starting from the second element
        for (int i = 1; i < target.size(); i++)
            // add the difference between the current and previous element to count, represents the additional operations needed to increase the height
            count += max(target[i] - target[i - 1], 0);
        return count;



        // Approach 3: keep track of the previous number encountered, time O(n), space O(1)
        // initialize count to store the minimum number of operations
        int count = 0;
        // track the previous number
        int previousNum = 0;
        // iterate through the target starting from the first element
        for (int i = 0; i < target.size(); i++){
            // get the current number
            int currentNum = target[i];
            // if the current number is greater than the previous number, increment count by the difference (currentNum - previousNum)
            if (currentNum > previousNum){
                count += currentNum - previousNum;
            }
            // update previousNum to the current number for the next iteration
            previousNum = currentNum;
        }
        return count;
    }
};
