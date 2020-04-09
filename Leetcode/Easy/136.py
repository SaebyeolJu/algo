class Solution:
    def singleNumber(self, nums):
        count = {}
        for num in nums:
            if num in count.keys(): count[num] += 1
            else: count[num] = 0
        for num in count: 
            if count[num]== 0 : return num