class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        // Approach 1: fast (beat 100%) but sacrifice memory by addtional p & q counters
        string final="";
        int p=word1.size();
        int q=word2.size();
        int n=max(p,q);
        for(int i=0;i<n;i++){
            if(p){
                final+=word1[i];
                p--;
            }
            if(q){
                final+=word2[i];
                q--;
            }
        }
        return final;
        }

        // Approach 2: slow
        // int l1 = word1.length();
        // int l2 = word2.length();
        // int limit = min(l1, l2);
        // string output = "";

        // for(int i=0;i<limit;i++){
        //     output+=word1[i];
        //     output+=word2[i];
        // }

        // if(l1>l2){
        //     output+=word1.substr(limit,l1-1);
        // }else{
        //     output+=word2.substr(limit,l2-1);
        // }
        // return output;
        // }
};