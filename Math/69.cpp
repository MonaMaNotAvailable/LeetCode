class Solution {
public:
    int mySqrt(int x) {
        // Approach 1: Newton's method, time O(logx), space O(1)
        long long r = x; // initialize r to x; r is our guess for the square root of x where sqrt(x) <= (x+1)/2 is true for all nonnegative integers
        while (r * r > x) // continue iterating as long as r squared is greater than x
            r = (r + x / r) / 2; // update r using the average of r and x/r
        return r;



        // // Approach 2: the sum of the first n odd numbers is n^2, time O(sqrt(x)), space O(1)
        // long long y = 0, i = 3, cnt = 0; // initialize y to 0, i to 3 (to represent the incremental odd numbers), and cnt to 0 (to count the steps)
        // while(x > y) { // continue the loop as long as x is greater than y
        //     y += i; // add the current odd number i to y
        //     i += 2; // increment i by 2 to get the next odd number
        //     cnt++; // increment the counter for each iteration
        // }
        // return cnt;



        // // Approach 3: binary search with 2 pointers, time O(logx), space O(1)
        // if (x < 2){ // handle cases where x is 0 or 1
        //     return x; // the square root of 0 is 0 and the square root of 1 is 1
        // }
        // int i = 0; // initialize the lower bound of the search range
        // int j = x; // initialize the upper bound of the search range
        // while(i < j){ // perform binary search within the range
        //     int mid = (j + i) / 2; // calculate the midpoint of the current range
        //     if(mid > x / mid){ // if mid squared is greater than x (to avoid overflow, use division)
        //         j = mid - 1; // adjust the upper bound to mid - 1
        //     }else{ 
        //         i = mid + 1; // adjust the lower bound to mid + 1
        //     }
        // }
        // if(i > x / i){ // after exiting the loop, check if i is too large
        //     return i - 1; // if so, return i - 1
        // }
        // return i; // otherwise, return i
    }
};