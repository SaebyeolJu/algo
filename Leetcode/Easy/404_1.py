# 404. Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/
# recursive method

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        nums = []
        def traverse(root, nums):
            if not root : return 0
            if root.right : traverse(root.right, nums)
            if root.left : 
                if not root.left.right and not root.left.left : 
                    nums.append(root.left.val)
                traverse(root.left, nums)
            return sum(nums)
        return traverse(root, nums)