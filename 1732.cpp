class Solution {
public:
    int largestAltitude(vector<int>& gain) {

        int currMax = 0, tempSum = 0;

        //same runtime & memory
        for(auto i:gain){
            tempSum+= i;
            currMax = max(currMax, tempSum);
        }

        // initial sol
        // for(int i = 0; i<gain.size(); i++){
        //     tempSum+=gain[i];
        //     currMax = max(currMax, tempSum);
        // }

        // fancy solution but actually use more memory
        // accumulate on gain itself and search the max
        // for(int i=1;i<gain.size();i++) gain[i]=gain[i-1]+gain[i];
        // return max(0,*max_element(gain.begin(),gain.end()));

        return currMax;
    }
};