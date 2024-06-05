class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the min can be 1 instead of min(piles) given sufficient h
        # but output must be greater than or equal to the average speed
        leftLimit, rightLimit = ceil(sum(piles)/h), max(piles)

        while leftLimit < rightLimit:
            # integer middle point of the current range
            # medium = leftLimit + (rightLimit-leftLimit)//2
            medium = (rightLimit+leftLimit)//2
            tempCount = 0
            for pile in piles:
                # pile//medium + (pile%medium > 0)
                # ceil to round up to the nearest whole hour
                tempCount += ceil(pile/medium)
            # if the total hours spent is less, then output can be smaller
            if tempCount <= h:
                rightLimit = medium
            else: # narrow the range too eat more!
                leftLimit = medium + 1
        # converge to the minimum valid eating speed
        return rightLimit