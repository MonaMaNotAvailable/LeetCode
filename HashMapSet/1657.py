class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #Optimial Solution: 116ms(O(NlogN + MlogM)) + 17.5mb(O(N + M))
        #count the frequency of each character in both
        frequency_word1 = Counter(word1)
        frequency_word2 = Counter(word2)
        #compare frequencies regardless of the character
        sorted_values_word1 = sorted(frequency_word1.values())
        sorted_values_word2 = sorted(frequency_word2.values())
        #the set of keys has to be the same
        keys_match = set(frequency_word1.keys()) == set(frequency_word2.keys())
        return sorted_values_word1 == sorted_values_word2 and keys_match



        #My approach: 123ms + 17.7mb
        # #Length has to be the same
        # if len(word1) != len(word2):
        #     return False
        # #The unique chars have to be the same
        # #Using subset instead of length
        # if not set(word1) <= set(word2):
        # # if len(set(word1).intersection(set(word2))) != len(set(word1)):
        #     return False
        # #Hash table has matching occurances
        # counter1 = Counter(word1)
        # counter2 = Counter(word2)

        # print(sorted(counter1.values()))
        # print(sorted(counter2.values()))

        # # Check if they have the same frequency distribution
        # return sorted(counter1.values()) == sorted(counter2.values())

        # # # Sorting by count in descending order
        # # sorted_items_desc1 = counter1.most_common()
        # # sorted_items_desc2 = counter2.most_common()
        # # # Extract counts from the sorted_items_desc lists
        # # counts1 = [count for item, count in sorted_items_desc1]
        # # counts2 = [count for item, count in sorted_items_desc2]
        # # # If occurences not matching
        # # if counts1 != counts2:
        # #     return False
        # # Default true
        # # return True