class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t output = 0; // store the reversed bits
        for (int i = 0; i < 32; ++i) { // iterate 32 times since we are dealing with a 32-bit integer
            // Approach 1: check in order by shifting n to the right, both time & space O(1)
            output = (output << 1) | (n & 1);
            // shift output to the left to make room for the next bit
            // (n & 1) extracts the least significant bit of n
            // | (bitwise OR) sets the least significant bit of output to the extracted bit
            n >>= 1;
            // shift n to the right by 1 to process the next bit



            // // Approach 2: set output based on reverse order
            // // check if the i-th bit in n is 1
            // if (n & (1 << i)) {
            //     // if 1, set the (31 - i)-th bit in output to 1
            //     output |= (1 << (31 - i));
            // }
        }
        return output;
    }
};