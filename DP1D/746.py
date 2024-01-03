class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Approach 1
        cost.append(0) # top [10,15,20,0]
        
        for i in range(len(cost) - 4, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
            
        return min(cost[0], cost[1])

        # Approach 2
        # cur=0
        # dp0=cost[0]
        # dp1=cost[1]
        
        # for i in range(2, len(cost)):
        #     cur=cost[i] + min(dp0,dp1)
        #     dp0=dp1
        #     dp1=cur
            
        # return min(dp0,dp1)



        # Approach 3: pass 259/283
        # def minCost(n):
        #     if n<2:
        #         return cost[n]
        #     return cost[n] + min(minCost(n-1), minCost(n-2))
        
        # return min(minCost(len(cost)-1), minCost(len(cost)-2))


        # start = [0,0]

        # for j in range(2):
        #     start[j] = cost[j]
        #     i = j

        #     while i<len(cost)-2:
        #         if cost[i+1] > cost[i+2]:
        #             print(j, i, cost[i+2])
        #             start[j] += cost[i+2]
        #             i+=2
        #         else:
        #             print(j, i, cost[i+1])
        #             start[j] += cost[i+1]
        #             i+=1
        
        # print(start)
        # return min(start)