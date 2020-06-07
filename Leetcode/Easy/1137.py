# 1137
# https://leetcode.com/problems/n-th-tribonacci-number/submissions/
# this code is failed bevause of the time limit

class Solution:
    def tribonacci(self, n):
        num_set = [0,1,1]
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

t = Solution()
t.tribonacci(4)