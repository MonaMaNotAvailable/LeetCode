class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        
        // O(n) method
        int j = 0;
        for(int i = 0; i<nums.size();i++){
            if(nums[i]!=0){
                nums[j] = nums[i];
                j++;
            }
        }
        for(;j < nums.size(); j++){
            nums[j] = 0;
        }

        // slow because of swap? But it's only O(1)!
        // for(int i=0,next=0;i<nums.size();++i)
		// if(nums[i])
		// 	swap(nums[i],nums[next++]);
    }
};