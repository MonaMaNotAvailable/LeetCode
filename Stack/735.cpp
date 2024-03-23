class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        int n = asteroids.size();

        // Approach 1: using index
        // keep track of the position where the next surviving asteroid should be placed in the array
        int j = 0;

        // check if it will collide with the asteroids that are already placed in the array
        for (int i = 0; i < n; i++) {
            int asteroid = asteroids[i];

            // if collision happens, comparing until destroyed
            while (j > 0 && asteroids[j - 1] > 0 && asteroid < 0 && asteroids[j - 1] < abs(asteroid)) {
                j--;
            }

            // empty or opposite direction
            if (j == 0 || asteroid > 0 || asteroids[j - 1] < 0) {
                asteroids[j++] = asteroid;
            } else if (asteroids[j - 1] == abs(asteroid)) { //both got destroyed
                j--;
            }
        }

        vector<int> result(asteroids.begin(), asteroids.begin() + j);

        return result;

        // // Approach 2: using stack
        // stack<int> s;

        // for(int i = 0; i < n; i++) {
        //     if(asteroids[i] > 0 || s.empty()) {
        //         s.push(asteroids[i]);
        //     }
        //     else{
        //         // + in stack got destryoed by -
        //         while(!s.empty() and s.top() > 0 and s.top() < abs(asteroids[i])) {
        //             s.pop();
        //         }
        //         // + in stack got destryoed by - given the same value
        //         if(!s.empty() and s.top() == abs(asteroids[i])) {
        //             s.pop();
        //         }
        //         else {
        //             // stack is empty and no more + on the left for any -
        //             if(s.empty() || s.top() < 0) {
        //                 s.push(asteroids[i]);
        //             }
        //         }
        //     }
        // }

        // // // pass 107/275, [-2,-1,1,2] should return [-2,-1,1,2] due to the direction of asteroids
        // // stack<int> s;

        // // for(int a:asteroids){
        // //     bool isDestroyed = false;
        // //         // opposite sign and the positive is on the left
        // //         while(!s.empty() && s.top()*a<0){
        // //             // determine which has greater absolute value
        // //             int tempTop = abs(s.top());
        // //             if(tempTop > abs(a)){
        // //                 break;
        // //             }// <= then pop anyway
        // //             else{
        // //                 s.pop();
        // //                 isDestroyed = true;
        // //             }
        // //         }//same sign

        // //         if((!isDestroyed && (s.empty() || s.top() * a > 0))){
        // //             s.push(a);
        // //         }
        // // }

        // vector<int> output(s.size());
        // for (int i = output.size() - 1; i >= 0; --i) {
        //     output[i] = s.top();
        //     s.pop();
        // }

        // return output;
    }
};