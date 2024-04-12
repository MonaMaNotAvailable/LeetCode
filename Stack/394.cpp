class Solution {
public:
    string decodeString(string s) {
        // My approach: without using actual stack but just string
        // Consume less memory, runtime relatively the same
        string stack = "";
        for(int i = 0; i<s.size(); i++){
            // push everything to stack unless encounter ]
            if(s[i]!=']'){
                stack+=s[i];
            }else{
                // decode the inner most layer
                int j = stack.size()-1;
                // locate the repeating part
                while(stack[j]!='['){
                    j--;
                }
                string temp = stack.substr(j+1);
                // find the digit
                int k = j-1;
                while(k >= 0 && isdigit(stack[k])){
                    k--;
                }
                // convert str to int
                int digit = stoi(stack.substr(k+1,j-k-1));
                // remove anything after
                stack.erase(k+1);

                for(int l = 0; l < digit; l++){
                    stack+=temp;
                }
            }
        }
        return stack;

        // // Other's appoach: using the actual stack structure
        // stack<char> st;
        // for(int i = 0; i < s.size(); i++){
        //     if(s[i] != ']') {
        //         st.push(s[i]);
        //     }
        //     else{
        //         string curr_str = "";
                
        //         while(st.top() != '['){
        //             curr_str = st.top() + curr_str ;
        //             st.pop();
        //         }
                
        //         st.pop();   // for '['
        //         string number = "";
                
        //         // for calculating number
                
        //         while(!st.empty() && isdigit(st.top())){
        //             number = st.top() + number;
        //             st.pop();
        //         }
        //         int k_time = stoi(number);    // convert string to number
                
        //         while(k_time--){
        //             for(int p = 0; p < curr_str.size() ; p++)
        //                 st.push(curr_str[p]);
        //         }
        //     }
        // }
        
        // // convert stack to string
        // s = "";
        // while(!st.empty()){
        //     s = st.top() + s;
        //     st.pop();
        // }
        // return s;
    }
};