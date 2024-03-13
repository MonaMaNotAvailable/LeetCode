class Solution {
public:
    string removeStars(string s) {
        // Approach 1: Using one loop
        string output = "";
        for(int i=0; i<s.size(); i++){
            if(s[i]=='*'){
                output.pop_back();
            }else{
                output+=s[i];
            }
        }
        return output;

        // // Approach 2: Using actual stack
        // stack<char> tempStack;
        // // maintain a stack
        // for(char c : s){
        //     if(c!='*'){
        //         tempStack.push(c);
        //     }else if (!tempStack.empty()){
        //         tempStack.pop();
        //     }
        // }
        // // return the output
        // string output;
        // while (!tempStack.empty())
        // {
        //     output += tempStack.top();
        //     tempStack.pop();
        // }
        // // reverse in correct order
        // reverse(output.begin(), output.end());
        // return output;
    }
};