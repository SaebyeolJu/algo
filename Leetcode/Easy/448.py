# 448. Find All Numbers Disappeared in an Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# hint : 1 ≤ a[i] ≤ n (n = size of array) -> each element can be used as index

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = list(range(0,len(nums)+1))
        for n in nums:
            if n in nums_set : nums_set.remove(n)
        return nums_set
# time complexity : O(n^2) -> Time Limit Exceeded
# if input num list is too big -> it can't be finished in limitied time
# wrong answer