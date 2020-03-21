class Solution:
    def fib(self, N: int) -> int:
        state = 0
        if(N == 0): state += 0
        elif(N == 1): state += 1
        return fib(N-1) + fib(N-2)
    
t = Solution()
t.fib(2)
# F(2) = F(1) + F(0) = 1 + 0 = 1
# F(3) = F(2) + F(1) = 1 + 1 = 2
# F(4) = F(3) + F(2) = 2 + 1 = 3
# F(5) = F(4) + F(3) = 3 + 2 = 5
# F(6) = F(5) + F(4) = 5 + 3 = 8