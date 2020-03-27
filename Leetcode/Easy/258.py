class Solution:
    def addDigits(self, num):
        nums = str(num)
        while len(nums) != 1:
            result = 0
            for i in nums:
                result += int(i)
            nums = str(result)
        print(nums) 


t = Solution()
t.addDigits(38)