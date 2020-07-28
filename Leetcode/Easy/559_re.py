# 559. Maximum Depth of N-ary Tree
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = []

    def add_node(self, node):
        self.children.append(node)

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root : return 0
        if not root.children : return 1
        D_set = []
        for node in root.children :
            D_set.append(self.maxDepth(node))
        return max(D_set) + 1

class Solution_2:
    def maxDepth(self, root: 'Node') -> int:
        if not root : return 0
        if not root.children : return 1
        D_set = [self.maxDepth(node) for node in root.children]
        return max(D_set) + 1

# Tree = Node(1)
# Tree_1 = Node(2)
# Tree_2 = Node(3)
# Tree_3 = Node(4)
# Tree.add_node(Tree_1)
# Tree.add_node(Tree_2)
# Tree.add_node(Tree_3)
# Tree_4 = Node(5)
# Tree_5 = Node(6)
# Tree_1.add_node(Tree_4)
# Tree_1.add_node(Tree_5)

# T = Solution()
# T.maxDepth(Tree)