# 1351. Count Negative Numbers in a Sorted Matrix
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# method 1. Brute force

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        for n_list in grid:
            for n in n_list:
                if n < 0 : cnt += 1
        return cnt