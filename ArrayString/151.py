class Solution:
    def reverseWords(self, s: str) -> str:
        # Approach1: using a stack
        output = []
        temp = ""
        #go through every char in the str
        for char in s:
            #if space, put temp string in the stack
            if char == " " and temp != "":
                output.insert(0,temp)
                temp = ""
            #append to temp
            elif char != " ":
                temp += char
        #add the last word
        if temp != "":
            output.insert(0,temp)

        #join the stack
        return ' '.join(output)



        # Approach2: super fast 2-liners using built-in split()
        # s = s.split()
        # return " ".join(s[::-1])



        # Approach3: reverse in-place
        # output = []
        # temp = ""
        # #go through every char in the str
        # for char in s:
        #     #if space, put temp string in the stack
        #     if char == " " and temp != "":
        #         output.append(temp[::-1])
        #         temp = ""
        #     #append to temp
        #     elif char != " ":
        #         temp += char
        # #add the last word
        # if temp != "":
        #     output.append(temp[::-1])

        # #join the stack
        # return ' '.join(output)[::-1]