class Solution:
    def runningSum(self, nums) :
        ans = []
        for i in range(len(nums)) : 
            ans.append(sum(nums[:i+1]))
        print(ans)

T = Solution()
T.runningSum([1,1,1,1,1])