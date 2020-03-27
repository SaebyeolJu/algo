class Solution:
    def isHappy(self, n ):
        checked = []
        nums = str(n)

        while nums != 1 and not (nums in checked): 
            checked.append(nums)
            result = 0
            for num in nums:
                result += int(num) * int(num)
            nums = str(result)
        if nums == '1' : print("True")

t = Solution()
t.isHappy(19)