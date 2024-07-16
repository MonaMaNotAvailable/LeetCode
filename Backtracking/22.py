class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Approach 1: recursive backtrack with stack
        # both time and space O(4^n/sqrt(n)) because generating all valid combinations of parentheses corresponds to the n-th Catalan number
        # initialize an empty list to hold the current combination of parentheses
        s = []
        # initialize a list to store all valid combinations
        result = []
        def backtrack(left, right):
            # if the current combination has reached the maximum length (2 * n)
            if left == right == n:
                # add the current combination to the result list as a string
                result.append("".join(s))
                return
            # if the number of '(' is less than n, add '('
            if left < n:
                s.append("(")
                backtrack(left + 1, right)
                # backtrack: remove the last added '(' to explore other possibilities
                s.pop()
            # if the number of ')' is less than the number of '(', add ')'
            if right < left:
                s.append(")")
                backtrack(left, right + 1)
                # backtrack: remove the last added ')' to explore other possibilities
                s.pop()
        # start backtracking with 0 counts for '(' and ')'
        backtrack(0, 0)
	# # len(result) = 1430 for n = 8
        return result



        # # Approach 2: iterative combination generation with queue
        # # both time and space O(4^n/sqrt(n))
        # # n = 1 ()
        # # n = 2 (()), ()()
        # # n = 3 ((())), (()()), (())(), ()(()), ()()()
        # output = deque(["()"])
        # # set to keep track of unique combinations
        # unique = set()
        # # loop to generate parenthesis from 2 to n
        # for _ in range(2, n+1):
        #     # get the current level size
        #     levelSize = len(output)
        #     for _ in range(levelSize):
        #         # get the previous combination
        #         prev = output.popleft()
        #         # loop to insert "()" at every possible position
        #         for i in range(2*n):
        #             # create a new combination
        #             tempString = prev[:i] + "()" + prev[i:]
        #             # check if the combination is unique
        #             if tempString not in unique:
        #                 # add the combination to the unique set
        #                 unique.add(tempString)
        #                 # append the combination to the output
        #                 output.append(tempString)
        # return output