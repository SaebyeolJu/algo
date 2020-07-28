# 1431. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        ans = []
        for i in range(len(candies)):
            ans.append(bool(candies[i] + extraCandies >= max(candies)))
        return ans

T = Solution
T.kidsWithCandies([2,3,5,1,3], 3)