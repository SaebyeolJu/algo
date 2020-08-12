# 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/

# priority queue
# high number : high priority
# new stone : y-x (y>x)
# if x == y : del

# priority queue
# high number : high priority
# new stone : y-x (y>x)
# if x == y : del

class Solution:
    def lastStoneWeight(self, stones):
        stones.sort(reverse = True)
        i = 0
        
        while len(stones) != 1:
            if stones[i] - stones[i+1] == 0 : del stones[i:i+1+1]
            else : 
                stones[i] = abs(stones[i] - stones[i+1])
                del stones[i+1]
                stones.sort(reverse = True)
            if not stones : stones.append(0)
        return stones[0]

t = Solution()
t.lastStoneWeight([2,7,4,1,8,1])