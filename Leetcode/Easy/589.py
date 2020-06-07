# 589. N-ary Tree Preorder Traversal
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

# method 1. Recursive

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def __init__(self) :
        self.pre = []
        
    def preorder_1(self, root):
        if not root : return None
        self.pre.append(root.val)
        for i in range(len(root.children)): self.preorder(root.children[i])
        return self.pre

    def preorder_2(self, root):
        if not root : return None
        self.pre.append(root.val)
        for node in root.children: self.preorder(node)
        return self.pre

