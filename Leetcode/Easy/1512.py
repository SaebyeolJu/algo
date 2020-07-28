# 1512. Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)-1):
            for n in nums[i+1:]: 
                if nums[i] == n : cnt += 1
        return cnt