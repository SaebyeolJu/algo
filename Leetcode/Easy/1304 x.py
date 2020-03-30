# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
import random

class Solution:
    def sumZero(self, n):
        nums = [0] * n
        if n == 1 : return nums
        n_sum = 0
        for i in range(len(nums)):
            nums[i] = random.randint(-10,10)
            if i == n-1: nums[i] = -(n_sum)
            if nums[i] in nums: i -= 1
            n_sum += nums[i]
        return nums

t = Solution()
t.sumZero(5)