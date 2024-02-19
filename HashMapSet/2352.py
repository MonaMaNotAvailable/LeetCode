class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        #Approach 1: transpose & list -> tuple & use counter
        #transpose the matrix & hash cols
        tpse = Counter(zip(*grid))                 
        #hash rows & converting lists to tuples (immutable and hashable)
        #lists are mutable and cannot be hashed, cannot be used as keys in a dictionary 
        grid = Counter(map(tuple,grid))             
        #compute the number of identical pairs
        return  sum(tpse[t]*grid[t] for t in tpse)



        # #Approach 2: list -> string & use counter
        # rowMerge = []
        # for row in grid:
        #     rowMerge.append(','.join(str(num) for num in row))

        # colMerge = []
        # for i in range(0, len(grid)):
        #     #initialize new column
        #     col = []
        #     #record column as other rows
        #     for row in grid:
        #         col.append(row[i])
        #     colMerge.append(','.join(str(num) for num in col))

        # # can't put row & col in the same dict due to the possibility of row==row
        # rowCounts = Counter(rowMerge)
        # colCounts = Counter(colMerge)
        # intersected_keys = rowCounts.keys() & colCounts.keys()
        # max_intersection = [rowCounts[key]*colCounts[key] for key in intersected_keys]
        # return sum(max_intersection)