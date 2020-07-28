# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# < BFS solution >
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_d = 0
        stack = [(root,1)]
        while stack : 
            root, depth = stack.pop()
            if max_d < depth : max_d = depth
            if not root : return 0
            if root.right : stack.append((root.right, depth+1))
            if root.left: stack.append((root.left, depth +1))
        return max_d