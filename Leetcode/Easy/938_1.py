# 938. Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/

# method 2: recursive
# using Ternary operators, backslash

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root :return 0
        return self.rangeSumBST(root.right, L, R) + \
            self.rangeSumBST(root.left, L, R) + \
                (root.val if L <= root.val <= R else 0)
    
test = Solution()

nums = [10,5,15,3,7,None,18]
node = TreeNode(10)
node.left = TreeNode(5)
node.right = TreeNode(15)
node.left.left = TreeNode(3)
node.left.right = TreeNode(7)
node.right.left = TreeNode(None)
node.right.right = TreeNode(18)

test.rangeSumBST(node, L = 7, R = 15)