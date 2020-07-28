# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf_1 = self.leaf(root1)
        leaf_2 = self.leaf(root2)
        
        if len(leaf_1) != len(leaf_2) : return False        
        for i in range(len(leaf_1)) : 
            if leaf_1[i] != leaf_2[i] : return False
            
        return True
            
        
    def leaf(self, root):
        stack = [root]
        leaf = []
        while stack : 
            root = stack.pop()
            if not root : return 0
            if root.right : stack.append(root.right)
            if root.left : stack.append(root.left)
            if not root.left and not root.right : leaf.append(root.val)
        return leaf