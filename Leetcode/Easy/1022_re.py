# 1022. Sum of Root To Leaf Binary Numbers
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 내가 푼거 아님
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        stack = [[root,""]]
        result = 0
        while stack : 
            root, path = stack.pop()
            if root.right : stack.append([root.right,path + str(root.val)])
            if root.left : stack.append([root.left,path + str(root.val)])
            if not root.left and not root.right : 
                path = path + str(root.val)
                result += int(path,2)
        return result