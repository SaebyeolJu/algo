# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        if not root: return []
        current_node = [root]
        result = []
        while current_node :
            level_node = []
            next_level = []
            for node in current_node :  
                level_node.append(node.val)
                if node.right : next_level.append(node.right)
                if node.left : next_level.append(node.left)
            result.append(sum(level_node) / len(level_node))
            current_node = next_level
        return result