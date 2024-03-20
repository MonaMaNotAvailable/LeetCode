class Solution {
public:
    string predictPartyVictory(string senate) {
        // Approach1: maintain 2 queues
        queue<int> r, d;
        int n = senate.length();
        // add index to 2 queues
        for(int i = 0; i <senate.size(); i++){
            if(senate[i]=='R'){
                r.push(i);
            }else{
                d.push(i);
            }
        }
        // increment n to keep track of index
        while(!r.empty()&&!d.empty()){
            if(r.front()<d.front()){
                r.push(n++); //push the current index and then increment
            }else{
                d.push(n++);
            }
            r.pop();
            d.pop();
        }
        return (r.empty())?("Dire"):("Radiant");

        // // Approach2: erase from senate
        // while(senate.size()>1){
        //     char tempParty = senate[0];
        //     senate.erase(0, 1);
        //     int tempLength = senate.size();
        //     for(int i = 0; i <senate.size(); i++){
        //         if(senate[i]!=tempParty){
        //             senate.erase(i, 1);
        //             senate += tempParty;
        //             // cout << senate << endl;
        //             break;
        //         }
        //     }
        // }
        // string output = "";
        // if(senate[0]=='R'){
        //     output += "Radiant";
        // }else if(senate[0]=='D'){
        //     output += "Dire";
        // }

        // return output;
    }
};