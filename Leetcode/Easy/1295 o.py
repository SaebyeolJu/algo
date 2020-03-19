# 1295. Find Numbers with Even Number of Digits
# Given an array nums of integers, 
# return how many of them contain an even number of digits.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count_e = 0
        for i in range(0,len(nums)):
            if len(str(nums[i])) %2 == 0 : count_e += 1
        return count_e

test = Solution()
test.findNumbers([12,345,2,6,7896])