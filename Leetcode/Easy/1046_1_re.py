# using priority queue

import heapq

class Solution:
    def lastStoneWeight(self, stones):
        stones = [-val for val in stones]
        heapq.heapify(stones)
        print(stones)
        while len(stones) > 1 :
            x1 = heapq.heappop(stones)
            x2 = heapq.heappop(stones)
            if x1 != x2 : 
                heapq.heappush(stones, x1 - x2)
            if len(stones) == 0 : return 0
        return -stones[0]

t = Solution()
t.lastStoneWeight([2,2])