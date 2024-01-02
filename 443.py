class Solution:
    def compress(self, chars: List[str]) -> int:
        #Approach 1: 2 pointers, without using pop()
        #handle counting and convertion together
        #Time O(n)
        #Space O(1)
        ans = 0
        i = 0

        while i < len(chars):
            letter = chars[i]
            count = 0
            # count for each char
            while i < len(chars) and chars[i] == letter:
                count += 1
                #move the pointer for the next diff char
                i += 1
            chars[ans] = letter
            ans += 1
            #count conversion
            if count > 1:
                for c in str(count):
                    chars[ans] = c
                    ans += 1
            #print(chars)

        return ans



        # #Approach 2: separate the tasks of counting and convert int to chars
        # #modify the chars using pop()
        # #Time O(n)
        # #Space O(1)
        # i = 1
        # currentElement = chars[0]
        # counter = 1

        # #go through chars while modifying it
        # while i < len(chars):
        #     if chars[i] == currentElement:
        #         counter+=1
        #         chars[i] = counter
        #         if counter > 2:
        #             chars.pop(i-1)
        #             i-=1
        #     else:
        #         #switch to a new char
        #         counter = 1
        #         currentElement = chars[i]
        #     i+=1

        # # turn int into str or multiple strs
        # i = 0
        # while i < len(chars):
        #     c = chars[i]
        #     if isinstance(c, int):
        #         if c < 10:
        #             chars[i] = str(c)
        #         else:
        #             temp = list(str(c)) #"12" to "1","2"
        #             chars.pop(i)
        #             for j in range(len(temp)):
        #                 chars.insert(i+j, temp[j])
        #             i+=len(temp)-1
        #     i+=1
        
        # #print(chars)
        # return len(chars)