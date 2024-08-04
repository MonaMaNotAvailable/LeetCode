class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Approach 1: using tuples for global uniqueness check, iterate over each cell only once
        # time O(328) = O(1), space O(243) = O(1)
        res = []  # initialize an empty list to store unique identifiers for the elements
        for i in range(9):  # iterate over each row
            for j in range(9):  # iterate over each column
                element = board[i][j]  # get the current element in the board
                if element != '.':  # if the element is not an empty cell
                    # add tuple identifiers for the row, column, and 3x3 subgrid to the result list
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        # check if the number of unique identifiers matches the total identifiers
        return len(res) == len(set(res))



        # # Approach 2: separate the 3 checks, visit each cell 3 times
        # time O(486) = O(1), space O(324) = O(1)
        # # helper function checking repeated element
        # def isRepeat(section: List[str]) -> bool:
        #     rowSet = set(section)
        #     count = 1
        #     for item in section:
        #         if item != ".":
        #             count += 1
        #     if len(rowSet) != count:
        #         return True
        #     return False

        # boardCopy = [[] for _ in range(9)]
        # # check row
        # for row in board:
        #     if isRepeat(row):
        #         return False
        #     for i in range(9):
        #         boardCopy[i].append(row[i])
        # # check col
        # for row in boardCopy:
        #     if isRepeat(row):
        #         return False
        # # check 3x3 boxes
        # for j in range(3):
        #     for k in range(3):
        #         nineCells = []
        #         for m in range(3):
        #             for n in range(3):
        #                 nineCells.append(board[3*j+m][3*k+n])
        #         if isRepeat(nineCells):
        #             return False
        # return True