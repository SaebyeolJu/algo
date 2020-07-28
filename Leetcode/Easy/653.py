# 653. Two Sum IV - Input is a BST
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_nums(self, root, nums):
        if not root : return 0
        nums.append(root.val)
        if root.right : self.get_nums(root.right,nums)
        if root.left : self.get_nums(root.left,nums)
        return nums
        
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nums = []
        nums = self.get_nums(root,nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == k : return True
        return False