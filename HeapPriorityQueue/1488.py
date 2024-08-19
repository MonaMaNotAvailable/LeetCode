class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # Approach 1: min-heap, time O(nlogm), space O(n) where n = len(rains) and m = num of zeros (len of the heap)
        closest = []  # min-heap to keep track of the earliest future rains that will cause floods
        locs = collections.defaultdict(collections.deque)  # dictionary to map each lake to a deque of its rain days
        # populate locs with each lake's rain days
        for i, lake in enumerate(rains):
            locs[lake].append(i)
        ret = []  # list to store the output
        # iterate over each day in the rains list
        for i, lake in enumerate(rains):
            if closest and closest[0] == i:
                # if today is the day a lake would flood and there's no way to prevent it
                return []  # impossible to avoid flooding
            if not lake:
                # it's a dry day (lake == 0)
                if not closest:
                    # if there's no lake that needs drying, we can dry any lake, defaulting to lake 1
                    ret.append(1)
                    continue
                nxt = heapq.heappop(closest)  # pick the earliest lake that will flood next
                ret.append(rains[nxt])  # use the dry day to prevent that lake from flooding
            else:
                # it's a rainy day for a specific lake
                l = locs[lake]  # get the deque of rain days for this lake
                l.popleft()  # remove today's rain day from the deque
                if l:
                    # if the lake will rain again in the future
                    nxt = l[0]  # get the next day it will rain
                    heapq.heappush(closest, nxt)  # push that day onto the heap to keep track of it
                ret.append(-1)  # record that it's a rainy day for this lake
        return ret  # return the final sequence of actions



        # # Approach 2: linear search and tracking, time O(n*m), space O(n)
        # lake = {}
        # zeroIndex = []
        # n = len(rains)
        # output = [-1 for _ in range(n)]
        # for i in range(n):
        #     num = rains[i]
        #     if num == 0:
        #         zeroIndex.append(i)
        #         output[i] = 1  # default to drying any lake (can be adjusted later)
        #     else:
        #         if num in lake:
        #             # we need to dry this lake before it rains again, dry day must be after last rain
        #             foundDryDay = False
        #             for j in range(len(zeroIndex)): #binary search is unnecessary since the appropriate dry day is often located near the left end 
        #                 if zeroIndex[j] > lake[num]:  # dry day must be after last rain
        #                     output[zeroIndex[j]] = num  # use this day to dry the lake
        #                     zeroIndex.pop(j)  # remove this dry day from available dry days
        #                     foundDryDay = True
        #                     break
        #             if not foundDryDay:
        #                 return []  # no available dry day; flood occurs
        #         lake[num] = i  # update last filled day for the current lake
        # return output