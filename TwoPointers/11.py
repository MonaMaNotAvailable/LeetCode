class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Approach 1: optimal by shifting left/right one at a time
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            minHeight = min(height[left], height[right])
            currentArea = minHeight * (right - left)
            maxArea = max(maxArea, currentArea)
            if height[left] < height[right]:
                left += 1
                while height[left]<minHeight:
                    left += 1
            else:
                right -= 1
                while height[right]<minHeight:
                    right -= 1
        return maxArea



        #Approach 2: TLE, pass 53/63, not optimal because trying to skip index
        # l = len(height)
        # left = 0
        # right = l-1
        # width = right-left
        # minHeight = min(height[left],height[right])
        # maxArea = width*minHeight

        # while width>0:
        #     currentMax = height[left]
        #     for newLeft in range(left+1,right):
        #         if height[newLeft] > height[left] and height[newLeft] > currentMax:
        #             width = right-newLeft
        #             minHeight = min(height[newLeft],height[right])
        #             maxArea = max(maxArea, width*minHeight)
        #             currentMax = max(height[newLeft], currentMax)
        #             # print(newLeft, right, width, maxArea)
        #     currentMax = height[right]
        #     for newRight in range(right-1, left, -1):
        #         if height[newRight] > height[right] and height[newRight] > currentMax:
        #             width = newRight-left
        #             minHeight = min(height[left],height[newRight])
        #             maxArea = max(maxArea, width*minHeight)
        #             currentMax = max(height[newRight], currentMax)
        #             # print(left, newRight, width, maxArea)

        #     #shift to the next interested region
        #     if height[left] > height[right]:
        #         #left does not change, shift right
        #         while height[right-1] < height[right]:
        #             right-=1
        #         right-=1
        #     else:
        #         #right does not change, shift left
        #         while height[left+1] < height[left]:
        #             left+=1
        #         left+=1
        #     width = right-left
        #     print(width)
        #     minHeight = min(height[left],height[right])
        #     maxArea = max(maxArea, width*minHeight)
        
        # return maxArea