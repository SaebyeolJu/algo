class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newList = []
        for i in range(0,n):
            print(nums[i]," ",nums[i+1])


t = Solution()
t.shuffle([2,5,1,3,4,7],3)