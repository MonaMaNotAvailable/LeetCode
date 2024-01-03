class Solution:
    def reverseVowels(self, s: str) -> str:
        i1 = 0
        i2 = len(s)-1
        vowels = set('aeiouAEIOU')
	#python string is immutable
        output = list(s)

        while i1<i2:
            if output[i1] in vowels and output[i2] in vowels:
                if output[i1] != output[i2]: #no need to swap: the same vowel
                    output[i1], output[i2] = output[i2], output[i1]
                i1 += 1
                i2 -= 1
            elif output[i1] not in vowels:
                i1+=1
            elif output[i2] not in vowels:
                i2-=1

        return ''.join(output)