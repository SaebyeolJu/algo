import random
class Solution:
    def sumZero(self, n):
        nums = []
        nums = random.sample(range(1,10),n-1)
        nums.append(-sum(nums))
        print(nums)
        return nums