# 589. N-ary Tree Preorder Traversal
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

# method 2. Iterative

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]: