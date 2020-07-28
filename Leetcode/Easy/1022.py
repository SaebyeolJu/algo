# 1022. Sum of Root To Leaf Binary Numbers
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root):
        n = ""
        stack = [(root,"")]
        nums = []
        while stack:
            root, n = stack.pop()
            n += str(root.val)
            if root.right : 
                stack.append((root.right,str(root.right.val)))
            if root.left : 
                stack.append((root.left,str(root.left.val)))
            if not root.left and not root.right : 
                nums.append(n)
                n = ""
        print(nums)