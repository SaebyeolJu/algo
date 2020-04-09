class Solution:
    def fib(self, N):        
        num_list = [0,1]
        for i in range(2, N+1):
            num_list.append(num_list[i-1]+num_list[i-2])
        return num_list[N]