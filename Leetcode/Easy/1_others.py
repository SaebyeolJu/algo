class Solution(object):
    def twoSum(self, nums, target):
        table={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in table:
                return [table[complement],i]
            table[nums[i]]=i
        return [-1,-1]

        