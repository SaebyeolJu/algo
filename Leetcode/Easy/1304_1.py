class Solution:
    def sumZero(self, n):
        nums = [0] * n
        for i in range(0,len(nums)//2):
            nums[i] = 2 * (i+1)
            nums[len(nums)-1-i] = -nums[i]
        return nums

t = Solution()
t.sumZero(7)

#  0  1  2  3  4  5  6
#  3  2  1  0 -1 -2 -3
# -7 -6 -5 -4 -3 -2 -1