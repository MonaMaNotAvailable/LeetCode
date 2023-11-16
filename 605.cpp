class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        //no new flower added, assume flowerbed follows no-adjacent-flowers rule
        if (n == 0) {
            return true;
        }
        for (int i = 0; i < flowerbed.size(); i++) {
            if (flowerbed[i] == 0 && (i == 0 || flowerbed[i-1] == 0) && (i == flowerbed.size()-1 || flowerbed[i+1] == 0)) {
                flowerbed[i] = 1;
                n--;
                if (n == 0) {
                    return true;
                }
            }
        }
        return false;

        // int count = 0;

        // if(flowerbed.size()==1 && flowerbed[0]==0){
        //     count+=1;
        // }

        // if(flowerbed.size()>1 && flowerbed[0]==0 && flowerbed[1]==0){
        //     flowerbed[0]=1;
        //     count+=1;
        // }

        // for (size_t i = 1; i < flowerbed.size()-1; ++i) {
        //     cout << flowerbed[i] << " ";
        //     if(flowerbed[i]==0 && flowerbed[i-1]==0 && flowerbed[i+1]==0){
        //         flowerbed[i]=1;
        //         count+=1;
        //     }
        // }

        // if(flowerbed.size()>2 && flowerbed[flowerbed.size()-2]==0 && flowerbed[flowerbed.size()-1]==0){
        //     count+=1;
        // }

        // return n<=count;
    }
};