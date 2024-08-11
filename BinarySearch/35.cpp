class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int i = 0;
        int j = nums.size() - 1;
        // Approach 1: binary search, both approaches have time O(logn) and space O(1)
        // condition i <= j in the while loop allows the algorithm to determine 
        // the correct insertion position without additional checks outside the loop. 
        // When the loop ends, i will naturally point to the correct insertion index.
        while (i <= j) {
            int mid = i + (j - i) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                i = mid + 1;
            } else {
                j = mid - 1;
            }
        }



        // // Approach 2: my approach
        // // directly handles the insertion position: might be marginally quicker 
        // // in certain scenarios where the target is close to the extremes of the array 
        // while(i < j){
        //     int mid = (i + j) / 2;
        //     if(nums[mid] == target){
        //         return mid;  // found the target, return the index
        //     }else if(nums[mid] < target){
        //         i = mid + 1;  // move the left pointer right since target is larger
        //     }else{
        //         j = mid - 1;  // move the right pointer left since target is smaller
        //     }
        // }
        // // after the loop, check if the current element is less than the target
        // if(nums[i] < target){
        //     return i + 1;  // target should be inserted after the current index
        // }
        return i;  // target should be inserted at the current index
    }
};
