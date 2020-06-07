# 617. Merge Two Binary Trees
# https://leetcode.com/problems/merge-two-binary-trees/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2 :
            t3 = TreeNode(t1.val + t2.val)
            t3.left = self.mergeTrees(t1.left, t2.left)
            t3.right = self.mergeTrees(t1.right, t2.right)
            return t3
        else: return t1 or t2

test = Solution()

t1 = [1,3,2,5]
t2 = [2,1,3,None,4,None,7]