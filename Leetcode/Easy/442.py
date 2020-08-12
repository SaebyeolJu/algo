# 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        num, ans = {}, []
        for n in nums : 
            num[n] = num.get(n,0) + 1
            if num[n] > 1 : ans.append(n)
        return ans