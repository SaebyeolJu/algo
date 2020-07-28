# 897. Increasing Order Search Tree
# https://leetcode.com/problems/increasing-order-search-tree/

# method : after making inorder array then making tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        val = []
        def inorder(node: TreeNode):
            if not node : return []
            inorder(node.left)
            val.append(node.val)
            inorder(node.right)
        inorder(root)
        
        N_tree = TreeNode(val[0])
        node = N_tree
        
        for i in range(1,len(val)) :
            node.right = TreeNode(val[i])
            node = node.right
        return N_tree
    # using shallow copy