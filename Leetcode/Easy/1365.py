'''
# 1365. How Many Numbers Are Smaller Than the Current Number
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
'''

class Solution:
    def smallerNumbersThanCurrent(self, nums) :
        check = []
        for set_num in nums:
            state = 0
            for com_num in nums: 
                if(set_num>com_num) : state += 1
            check.append(state)
        return print(check)
        
Test = Solution()
Test.smallerNumbersThanCurrent([8,1,2,2,3])