class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Approach 1: bidriectional bfs with set
        # time O(n*l) for all 3 approaches, where n is len(wordList) and l is len(beginWord), space O(n) due to 4 sets
        wordSet = set(wordList)  # convert the word list to a set for faster lookup
        if endWord not in wordSet:  # if the end word is not in the word list, return 0
            return 0
        beginSet = {beginWord}  # initialize the begin set with the begin word
        endSet = {endWord}  # initialize the end set with the end word
        distance = 1  # start with a distance of 1
        while beginSet and endSet:  # continue while both sets are not empty
            wordSet -= beginSet  # remove all words in the begin set from the word list
            distance += 1  # increment the distance
            newSet = set()  # initialize a new set for the next level
            for word in beginSet:  # iterate through each word in the begin set
                for i in range(len(word)):  # iterate through each character in the word
                    for c in string.ascii_lowercase:  # iterate through all lowercase letters
                        new_word = word[:i] + c + word[i + 1:]  # form a new word by replacing the character
                        if new_word in wordSet:  # if the new word is in the word list
                            if new_word in endSet:  # if the new word is in the end set
                                return distance  # return the distance
                            newSet.add(new_word)  # add the new word to the new set
            if len(beginSet) > len(endSet):  # swap to the smaller set if needed
                beginSet = endSet
                endSet = newSet
            else:
                beginSet = newSet
        return 0  # return 0 if no transformation sequence is found



        # # Approach 2: bfs with pre-computed dict, space O(n*l) due to dict
        # # if the endWord is not in the wordList, there is no valid transformation
        # if endWord not in wordList:
        #     return 0
        # # length of each word
        # L = len(beginWord)
        # # dictionary to hold all possible generic transformations of words
        # # defaultdict avoids check to see if that key exists
        # allComboDict = defaultdict(list)
        # # populate the dictionary with all combinations of words in the wordList
        # for word in wordList:
        #     for i in range(L):
        #         # key is the generic word, value is a list of words which have the same intermediate generic form
        #         allComboDict[word[:i] + "*" + word[i+1:]].append(word)
        # # queue for BFS
        # queue = deque([(beginWord, 1)])
        # # visited to make sure we don't process the same word more than once
        # visited = set()
        # visited.add(beginWord)
        # # perform BFS
        # while queue:
        #     currentWord, level = queue.popleft()
        #     # process all intermediate words for the current word
        #     for i in range(L):
        #         intermediateWord = currentWord[:i] + "*" + currentWord[i+1:]
        #         # iterate through all words which share the same intermediate state
        #         for word in allComboDict[intermediateWord]:
        #             # if we find the end word, return the answer
        #             if word == endWord:
        #                 return level + 1
        #             # if this word has not been visited, mark it visited and add it to the queue
        #             if word not in visited:
        #                 visited.add(word)
        #                 queue.append((word, level + 1))
        # # if we never find the end word, return 0
        # return 0



        # # Approach 3: TLE: pass 34/51, space O(n) due to queue
        # # if the endWord is not in the wordList, there is no valid transformation
        # if endWord not in wordList:
        #     return 0
        # # initialize the queue with the beginWord and the initial transformation count of 1
        # queue = deque([(beginWord, 1)])
        # # initialize the visited set with the beginWord to avoid revisiting
        # visited = set([beginWord])
        # # list of all possible single character transformations (a to z)
        # transformations = string.ascii_lowercase
        # while queue:
        #     # dequeue the current word and its transformation count
        #     currentWord, tranformationCount = queue.popleft()
        #     # if the current word is the endWord, return the transformation count
        #     if currentWord == endWord:
        #         return tranformationCount
        #     # this nested for loop results in 25*len(beginWord) iterations
        #     # iterate over each character position in the current word
        #     for i in range(len(beginWord)):
        #         # iterate over each possible transformation character (a to z)
        #         for char in transformations:
        #             # only create a new word if the transformation character is different
        #             if currentWord[i] != char:
        #                 # create the new word by replacing the character at position i
        #                 newWord = currentWord[:i] + char + currentWord[i+1:]
        #                 # if the new word is in the wordList and hasn't been visited
        #                 if newWord in wordList and newWord not in visited:
        #                     # add the new word to the queue with the incremented transformation count
        #                     queue.append((newWord, tranformationCount + 1))
        #                     # mark the new word as visited
        #                     visited.add(newWord)
        # # if no transformation sequence reaches the endWord, return 0
        # return 0