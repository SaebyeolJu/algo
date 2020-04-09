class Solution:
    def tribonacci(self, n):
        if n <2 : return n

        num_set = [0,1,1]
        for i in range(3,n+1):
            num_set.append(num_set[i-1] + num_set[i-2] + num_set[i-3])
        return num_set[n]

t = Solution()
t.tribonacci(4)