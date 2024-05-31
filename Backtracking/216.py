class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = []

        def backtrack(currentNum, currentComb, remainingValue):
            # base/stopping condition: if the combination is of the desired length k
            if len(currentComb)==k:
                # if the sum of the combination is equal to the target n
                if remainingValue==0: #sum(currentComb)==n
                    output.append(currentComb)
                else:
                    return

            # generate combination: iterate from currentNum to 9
            for i in range(currentNum,10):
                if i <= remainingValue:
                    # recursively call backtrack with the updated combination and remaining value
                    backtrack(i+1, currentComb+[i], remainingValue-i)

        # start the backtracking with 1
        backtrack(1, [], n)
        return output