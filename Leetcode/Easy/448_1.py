# 
class Solution:
    def findDisappearedNumbers(self, nums):
        index = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] > 0 : nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]

        # for i in range(len(nums)):
        #     if nums[i] > 0 : index.append(i+1)
        
        for i, v in enumerate(nums):
            if v > 0 : index.append(i + 1)
        # enumerate 를 사용하면 index와 value 를 둘다 사용가능
        return index

t = Solution()
t.findDisappearedNumbers([4,3,2,7,8,2,3,1])