'''
1313. Decompress Run-Length Encoded List
https://leetcode.com/problems/decompress-run-length-encoded-list/
'''
class Solution:
    def decompressRLElist(self, nums):
        new_set = []
        for i in range(0,len(nums)-1,2):
            new_set.extend(nums[i] * [nums[i+1]])
        return new_set
        

t = Solution()
t.decompressRLElist([1,2,3,4])