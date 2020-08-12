# 1337. The K Weakest Rows in a Matrix
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
"""
# Bubble sort(Brute force)
Time : O(n^2) - 시간이 너무 오래 걸린다.
Space : O(n)
코드리뷰
반복문이 너무 여러개 쓰인다. -> 합칠 수 있는 방법을 생각해야함
시간복잡도는 O(n^2)는 피하고, 버블 소트말고 다른 효율적인 소트 방법을 쓰자
"""
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n, ans = [], []
        for i in range(len(mat)):
            n.append([i,sum(mat[i])])
            
        for i in range(len(n)-1, 0, -1):
            for j in range(i):
                if n[j+1][1] < n[j][1] :n[j+1], n[j] = n[j], n[j+1]
                    
        for i in range(0,k):
            ans.append(n[i][0])
            
        return ans