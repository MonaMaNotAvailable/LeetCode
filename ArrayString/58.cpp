class Solution {
public:
    int lengthOfLastWord(string s) {
        // Approach 1: while loop and maintain the count only, time O(n), space O(1)
        int len = 0;
        int tail = s.length() - 1;
        // skip any trailing spaces at the end of the string
        while (tail >= 0 && s[tail] == ' ') {
            tail--;
        }
        // count the characters in the last word until a space or the beginning of the string is reached
        while (tail >= 0 && s[tail] != ' ') {
            len++;   // increment the length count
            tail--;  // move to the previous character
        }
        return len;



        // Approach 2: for loop and explicitly store the last word, time O(n), space O(m) where m = len(lastWord)
        // create a vector to store characters of the last word
        vector<char> lastWord;
        // iterate through the string from the end to the beginning
        for(int i = s.size() - 1; i >= 0; i--) {
            // if the current character is not a space, add it to the lastWord vector
            if(s[i] != ' ') {
                lastWord.push_back(s[i]);
            } 
            // if a space is encountered after collecting some characters, break the loop
            else if(!lastWord.empty()) {
                break;
            }
        }
        return lastWord.size();
    }
};