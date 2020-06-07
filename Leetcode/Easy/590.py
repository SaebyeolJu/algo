# 590. N-ary Tree Postorder Traversal
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

'''
Note: 
postorder ) left > right > root
method ) recursive
made init function in Solution class to save traversal node 
'''
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.pos = []
        
    def postorder(self, root: 'Node') -> List[int]:
        if not root : return None
        for node in root.children : self.postorder(node)
        self.pos.append(root.val)
        return self.pos