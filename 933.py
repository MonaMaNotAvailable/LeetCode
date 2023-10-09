class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        queue = self.queue
        start = t - 3000
        #get rid of useless record out of the range
        while(queue and queue[0] < start):
            queue.popleft()
        queue.append(t)
        return len(queue)

    # # 66 / 68 testcases passed
    # def __init__(self):
    #     self.requests = [] #historical requests
    #     # reqrange = [] #maintain range

    # def ping(self, t: int) -> int:

    #     requests.append(t)
    #     # reqrange = [t-3000, t]

    #     temp = 0
    #     for r in self.requests:
    #         if r>= t-3000 and r<=t:
    #             temp +=1
    #     return temp