class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Approach 1: stack and conversion to empty string, time & space O(n)
        s = list(s)  # convert the string to a list for easier manipulation
        stack = []  # use a stack to store the indices of unmatched left parentheses
        # iterate over the characters in the string
        for i, c in enumerate(s):
            if c == "(":  # if the character is a left parenthesis
                stack.append(i)  # push its index onto the stack
            elif c == ")":  # if the character is a right parenthesis
                if stack:  # if there's a matching left parenthesis in the stack
                    stack.pop()  # pop the matching left parenthesis index from the stack
                else:  # if there's no matching left parenthesis
                    s[i] = ""  # mark the unmatched right parenthesis for removal by setting it to an empty string
        # remove any remaining unmatched left parentheses
        while stack:
            s[stack.pop()] = ""  # pop the index of the unmatched left parenthesis from the stack and set it to an empty string
        return "".join(s)  # join the list back into a string and return it



        # # Approach 2: stack and set to keep track of item to be removed
        # # use a stack to store the indices of unmatched left parentheses
        # stack = []
        # toRemove = set()  # use a set to store indices of characters to remove
        # # first pass to identify unmatched right parentheses and unmatched left parentheses
        # for i, char in enumerate(s):
        #     if char == '(':
        #         stack.append(i)  # push index of left parenthesis onto stack
        #     elif char == ')':
        #         if stack:
        #             stack.pop()  # pop a matching left parenthesis from the stack
        #         else:
        #             toRemove.add(i)  # add index of unmatched right parenthesis to set
        # # add any remaining indices of unmatched left parentheses to set
        # toRemove.update(stack)
        # # if nothing to remove, return the original string
        # if not toRemove:
        #     return s
        # # build the result string excluding characters at indices in toRemove
        # result = []
        # for i, char in enumerate(s):
        #     if i not in toRemove:
        #         result.append(char)
        # return ''.join(result)



        # # Approach 3: list processing
        # output = []  # initialize the list to store the valid characters
        # numLeft = 0  # counter for left parentheses
        # numRight = 0  # counter for right parentheses
        # for char in s:
        #     if char != ")":  # if the character is not a right parenthesis
        #         output.append(char)  # add the character to the output list
        #         if char == "(":  # if the character is a left parenthesis
        #             numLeft += 1  # increment the left parenthesis counter
        #     elif numRight < numLeft:  # if there are more left parentheses than right parentheses
        #         output.append(char)  # add the right parenthesis to the output list
        #         numRight += 1  # increment the right parenthesis counter
        # # post-processing
        # if numLeft > numRight:  # if there are more left parentheses than right parentheses
        #     for _ in range(numLeft - numRight):  # iterate the difference
        #         output.reverse()  # reverse the output list to remove the last occurrence
        #         output.remove("(")  # remove the first left parenthesis found (which is the last in the original order)
        #         output.reverse()  # reverse the list back to the original order
        # return "".join(output)  # join the list into a string and return it