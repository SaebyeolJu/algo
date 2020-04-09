class Solution:
    def fib(self, N):
        if(N <2) : return N
        return self.fib(N-1) + self.fib(N-2)