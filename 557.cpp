class Solution {
public:
    string reverseWords(string s) {
        //inplace swap with moving pointers
        int i = 0;
        for (int j = 0; j < s.size(); ++j) {
            if (s[j] == ' ') {
                reverse(s.begin() + i, s.begin() + j);
                i = j + 1;
            }
        }
        reverse(s.begin() + i, s.end());
        return s;

        // //slow
        // string output = "";
        // string temp = "";

        // for (char c : s) {
        //     //check space
        //     if (!isspace(c)) {
        //         temp = c+temp;
        //     }else{
        //         output+=temp;
        //         output+=c;
        //         temp = "";
        //     }
        // }

        // //add the final reverse word
        // output+=temp;
        // return output;
    }
};