class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict={"(":")", "{":"}", "[":"]"} #O(1) average time complexity for lookups
        
        for char in s:
            # Approach 1: ChatGPT's improved version, better separation of logic but slower for the current 98 testcases
            if char in dict:
                # if the character is an opening bracket, push to stack
                stack.append(char)
            else:
                # if the stack is empty or the top of the stack does not match the closing bracket
                if not stack or dict[stack.pop()] != char:
                    return False
        
            # Approach 2: My initial approach
            # # if stack is non-empty and char is left parenthesis/bracket
            # if stack and char not in dict:
            #     lastItem = stack.pop()
            #     if dict.get(lastItem) != char:
            #         return False
            # else: # if stack is empty or char is right parenthesis/bracket
            #     stack.append(char)
        
        # if at the end the stack is empty
        return not stack