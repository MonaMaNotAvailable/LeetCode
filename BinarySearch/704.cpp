class Solution {
public:
    int search(vector<int>& nums, int target) {
        int leftIndex = 0;
        int rightIndex = nums.size()-1;
        while(leftIndex <= rightIndex){
            // avoid potential integer overflow when leftIndex and rightIndex are large
            int midIndex = leftIndex+(rightIndex - leftIndex)/2;
            if(nums[midIndex] == target){
                return midIndex;
            }else if(nums[midIndex] < target){
                leftIndex = midIndex+1;
            }else{
                rightIndex = midIndex-1;
            }
        }
        return -1;   
    }
};