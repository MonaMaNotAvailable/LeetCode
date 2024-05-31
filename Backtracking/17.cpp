class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if(digits.empty()){
            return {};
        }

        // map each digit to its corresponding letters on a phone keypad
        string phoneMap[] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> combinations = {""};

        for (char digit: digits){
            // temporary vector to store new combinations
            vector<string> newComb;
            // iterate over each existing combination
            for(string comb: combinations){
                // add each possible letter for the current digit to the existing combinations
                for(char letter: phoneMap[digit-'2']){
                    newComb.push_back(comb+letter);
                }
            }
            combinations = newComb;
        }
        return combinations;
    }
};