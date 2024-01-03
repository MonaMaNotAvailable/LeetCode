class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = []

        def backtrack(currentNum, currentComb, remainingValue):

            #base/stopping condition
            if len(currentComb)==k:
                if remainingValue==0: #sum(currentComb)==n
                    output.append(currentComb)
                else:
                    return

            #generate combination
            for i in range(currentNum+1,10):
                if i <= remainingValue:
                    backtrack(i, currentComb+[i], remainingValue-i)

        #start
        backtrack(0, [], n)
        return output