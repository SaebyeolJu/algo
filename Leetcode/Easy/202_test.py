class Solution:
    def isHappy(self, n):
        nums = str(n)
        while len(nums)!=1:
            result = 0
            for num in nums:
                result += int(num) * int(num)
            nums = str(result)
        if (nums == '1'): print("True")
        else: print("False")

t = Solution()
t.isHappy(7)