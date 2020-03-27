# Happy Number
# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n):
        nums = str(n)
        if nums < 10 : nums = str(n * n)
        while len(nums)!=1:
            result = 0
            for num in nums:
                result += int(num) * int(num)
            nums = str(result)
        if (nums == '1'): print("True")
        else: print("False")

t = Solution()
t.isHappy(1111111)