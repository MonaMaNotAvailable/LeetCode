class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        // Approach 1: early return, both approaches have time O(n), space O(n) in case of overflow
        int n = digits.size() - 1; // get the index of the last digit in the array
        for (int i = n; i >= 0; --i) { // loop through the digits array from the end to the beginning
            if (digits[i] == 9) {  // check if the current digit is 9
                digits[i] = 0; // set the current digit to 0 because 9 + 1 results in a carry over
            } else {
                digits[i] += 1; // increment the current digit by 1 if it is not 9
                return digits; // return the updated digits array as there's no need for further changes
            }
        }
        digits.push_back(0); // add a 0 to the end of the array to make space for the carry over
        digits[0] = 1; // set the first digit to 1 to handle the case where all digits were 9
        return digits; // return the updated digits array



        // // Approach 2: keep carry a global variable
        // int carry = 1; // start with a carry of 1, as we need to add one to the number
        // for(int i = digits.size()-1; i > -1; i--){ // loop through the digits array from the end to the beginning
        //     int currentNum = digits[i]; // get the current digit
        //     if(currentNum + carry != 10){ // if adding carry to current digit doesn't result in 10
        //         digits[i] = currentNum + carry; // update the current digit with the new value
        //         carry = 0; // reset carry to 0 since there's no overflow
        //     }else{ 
        //         digits[i] = 0; // set current digit to 0 if it overflows (i.e., 9 + 1 = 10)
        //     }
        // }
        // if(digits[0] == 0){ // after the loop, if the most significant digit is 0, we had an overflow
        //     digits.insert(digits.begin(), 1); // insert 1 at the beginning of the array to handle the overflow
        // }
        // return digits; // return the updated digits array
    }
};