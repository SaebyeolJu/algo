class Solution:
    def tribonacci(self, n):
        num_set = [0,1,1]
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

t = Solution()
t.tribonacci(4)