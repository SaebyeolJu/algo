# 404. Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        n_sum, stack = 0, [root]
        while stack : 
            if not root: return 0
            root = stack.pop()
            if root.right : stack.append(root.right)
            if root.left : 
                if not root.left.right and not root.left.left : n_sum += root.left.val
                stack.append(root.left)
        return n_sum