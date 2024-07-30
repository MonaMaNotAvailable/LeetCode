class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Approach 1: Trie with dfs, time O(K*L+M^2*N^2), space (K*L+M*N) 
        # where K = num of words, L = avg len of word, M = num of row, N = num of col
        # define a DFS function to traverse the board and search for words
        def dfs(x, y, root):
            # get the letter at the current position on the board
            letter = board[x][y]
            # traverse the trie to the next node
            cur = root[letter]
            # check if the node has a word in it
            word = cur.pop('#', False)
            if word:
                # if a word is found, add it to the results list
                res.append(word)
            # mark the current position on the board as visited
            board[x][y] = '*'
            # recursively search in all four directions
            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = x + dirx, y + diry
                # check if the next position is within the board and the next letter is in the trie
                if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur:
                    dfs(curx, cury, cur)
            # restore the original value of the current position on the board
            board[x][y] = letter
            # if the current node has no children, remove it from the trie
            if not cur:
                root.pop(letter)
        # build a trie data structure from the list of words
        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})
            cur['#'] = word
        # get the dimensions of the board
        m, n = len(board), len(board[0])
        # initialize a list to store the results
        res = []
        # traverse the board and search for words
        for i in range(m):
            for j in range(n):
                # check if the current letter is in the trie
                if board[i][j] in trie:
                    dfs(i, j, trie)
        return res



        # # Failed approach, TLE pass 42/65, dfs along, time O(K*M*N), space (L+M*N) 
        # m = len(board)  # number of rows in the board
        # n = len(board[0])  # number of columns in the board
        # # create a dictionary to store positions of each letter on the board
        # # with maximum 26 keys and 144 values
        # wordPos = {}
        # for row in range(m):
        #     for col in range(n):
        #         letter = board[row][col]
        #         if letter not in wordPos:
        #             wordPos[letter] = set()
        #         wordPos[letter].add((row, col))  # add the position of the letter to the set
        # def dfs(word, i, r, c, visited):
        #     if i == len(word):  # if all characters are matched
        #         return True
        #     if r < 0 or r >= m or c < 0 or c >= n or (r, c) in visited or board[r][c] != word[i]:  # boundary and validity checks
        #         return False
        #     visited.add((r, c))  # mark the current position as visited
        #     # recursively check all four possible directions
        #     found = (dfs(word, i+1, r+1, c, visited) or
        #             dfs(word, i+1, r-1, c, visited) or
        #             dfs(word, i+1, r, c+1, visited) or
        #             dfs(word, i+1, r, c-1, visited))
        #     visited.remove((r, c))  # backtrack by removing the position from visited set
        #     return found
        # output = []  # list to store the found words
        # for word in words:
        #     if word[0] in wordPos:  # check if the first character of the word exists on the board
        #         for startPos in wordPos[word[0]]:  # start a dfs from each position of the first character
        #             if dfs(word, 0, startPos[0], startPos[1], set()):
        #                 output.append(word)  # add the word to output if found
        #                 break  # stop searching further for this word
        # return output  # return the list of found words