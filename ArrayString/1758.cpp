class Solution {
public:
    int minOperations(string s) {
        int zeroFirst = 0;
        // zeroFirst + oneFirst == n, where oneFirst would be the number of operations if we start with '1'
        int n = s.length();

        for (int i = 0; i < n; i++) {
            // Approach 1: explicitly using even/odd index for alternating, time O(n), space O(1)
            if (i % 2 == 0) { 
                // check if character at even index is '1' (it should be '0')
                if (s[i] == '1') {
                    zeroFirst++;
                }
            } else {
                // check if character at odd index is '0' (it should be '1')
                if (s[i] == '0') {
                    zeroFirst++;
                }
            }
            // Approach 2: convert character to int and compare with index directly, combine the checks into a single line
            // if (s[i] - '0' != i % 2) {
            //     zeroFirst++;
            // }
        }
        // return the minimum number of operations needed to make the string alternating
        // either starting with '0' (zeroFirst) or starting with '1' (n - zeroFirst)
        return min(zeroFirst, n - zeroFirst);
    }
};