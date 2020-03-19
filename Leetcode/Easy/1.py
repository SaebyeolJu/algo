'''
1.Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
https://leetcode.com/problems/two-sum/
'''

class Solution(object):
    def twoSum(self, nums, target):
        wait_list = {}
        finish = {}
        for i in range(len(nums)):
            if (target - nums[i]) not in wait_list:
                wait_list[nums[i]] = i
            else:
                finish = [min(wait_list.get(target - nums[i]),i),max(wait_list.get(target - nums[i]),i)]
        return print(finish)

test = Solution()
test.twoSum([1,7,11,8,15],9)