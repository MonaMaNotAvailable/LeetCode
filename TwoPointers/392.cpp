class Solution {
public:
    bool isSubsequence(string s, string t) {
        int j = 0, i = 0;
        
        //Go through the longer str once
        //While faster than for-loop
        while(i < s.size() && j < t.size()) {
            if(s[i] == t[j]) {
                i++;
            }
            j++;
        }
        // for (int i = 0; i<t.size();i++){
        //     if(t[i]==s[j]){
        //         j++;
        //     }
        // }

        //Check index increment match substr length
        return i == s.size() ? 1 : 0;
        // if(j==s.size()){
        //     return 1;
        // }else{
        //     return 0;
        // }
    }
};