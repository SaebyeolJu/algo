class Solution:
    def sortedSquares(self, A):
        for i in range(len(A)): A[i] = A[i] ** 2
        A.sort()
        return A

t = Solution()
t.sortedSquares([-4,-1,0,3,10])