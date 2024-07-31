class Solution {
public:
    bool isPalindrome(int x) {
        // Approach 1: reverse the entire number using modulo & shifting
        // both approaches have time O(n) & space O(1) where n = num of digits
        if(x < 0){
            return false; // negative numbers are not palindromes
        }   
        unsigned int copyOfX = x; // make a copy of the input number
        unsigned int reverse = 0; // variable to store the reversed number
        while(copyOfX > 0){
            reverse *= 10; // shift the digits in reverse left by one place
            reverse += copyOfX % 10; // add the last digit of copyOfX to reverse
            copyOfX /= 10; // remove the last digit from copyOfX
        }
        return reverse == x; // check if the reversed number is equal to the original number



    //     // Approach 2: reverse half of the input
    //     if(x < 0 || (x != 0 && x % 10 == 0)){
    //         return false; // negative numbers and numbers ending with 0 (except 0 itself) are not palindromes
    //     }   
    //     int reversed = 0; // variable to store the reversed half of the number
    //     while (x > reversed) {
    //         reversed = reversed * 10 + x % 10; // build the reversed number from the end
    //         x /= 10; // remove the last digit from the original number
    //     }
    //     return x == reversed || x == reversed / 10; // check if the number is a palindrome
    // }