class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Approach: iterative DP, time and space both O(N^2)
        # initialize the first row
        output = [[1]]

        # start from the second row
        for _ in range(numRows-1):
            newRow = [1]
            prevRow = output[-1]
            # iterate through the previous row to calculate the middle elements
            for i in range(len(prevRow)-1):
                # each new element is the sum of two adjacent elements in the previous row
                newRow.append(prevRow[i]+prevRow[i+1])
            newRow.append(1)
            output.append(newRow)
        
        return output


        # Approach 2: binomial coefficient
        # Pascal's Triangle is a triangular array of the binomial coefficients. Each element in row n and column k of Pascal's Triangle corresponds to comb(n, k)
        # triangle = []
        
        # for n in range(numRows):
        #     row = []
        #     for k in range(n+1):
        #         row.append(math.comb(n, k))
        #     triangle.append(row)
        
        # return triangle