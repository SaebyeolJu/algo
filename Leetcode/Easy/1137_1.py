class Solution:
    def tribonacci(self, n):
        num_set = [0,1,1]
        if n <3 : return num_set[n]
        for i in range(3,n+1):
            num_set.append(num_set[i-1] + num_set[i-2] + num_set[i-3])
        return num_set[n]

t = Solution()
t.tribonacci(5)