'''
# 888. Fair Candy Swap
# https://leetcode.com/problems/fair-candy-swap/
'''

class Solution:        
    def fairCandySwap(self, A, B):
        sum_a, sum_b = sum(A), sum(B)
        av = (sum_a + sum_b) * 1/2

        if sum_a > sum_b : state = 1
        else : state = 0

        for i in range(len(A)):
          for j in range(len(B)):
            if state == 1:
              if (A[i] - B[j]) == (sum_a - av):
                ans = [A[i],B[j]]
            else:
              if (B[j] - A[i]) == (sum_b - av):
                ans = [A[i],B[j]]
                
        return(ans)

T = Solution()
T.Solution([1,1],[2,2])