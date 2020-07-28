# 100. Same Tree
# https://leetcode.com/problems/same-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, r_1, r_2):
        if not r_1 and not r_2: return True
        if not r_1 or not r_2: return False
        return r_1.val == r_2.val and self.isSameTree(r_1.left, r_2.left) and self.isSameTree(r_1.right, r_2.right)