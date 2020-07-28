# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root : return ""
        stack = [[root, ""]]
        ans = []
        while stack :
            root, nums = stack.pop()
            nums += str(root.val)
            if root.right : stack.append([root.right,nums + "->"])
            if root.left : stack.append([root.left,nums + "->"])
            if not root.left and not root.right : ans.append(nums)
        return ans