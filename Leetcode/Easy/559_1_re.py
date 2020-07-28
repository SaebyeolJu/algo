"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# BFS using stack

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None: return 0
        maxdepth = 1
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop(0)
            maxdepth = max(maxdepth, depth)
            for children in node.children:
                stack.append((children, depth + 1))
        return maxdepth