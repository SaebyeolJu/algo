# 590. N-ary Tree Postorder Traversal
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

''' 
Note:
postorder : left > right > root
method ) recursive
* 혼자서 짠게 아니라 Discuss 참고해서 코드 짬
'''

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root : return None
        def recursion(root, ans):
            for node in root.children : 
                recursion(node,ans)
            ans.append(root.val)
        recursion(root,ans)
        return ans