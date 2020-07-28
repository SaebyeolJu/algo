# 590. N-ary Tree Postorder Traversal
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    # left > right > root
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root == None : return []
        
        stack, counters, retList = [root], [0], []
        
        while stack :
            while counters[-1] < len(stack[-1].children):
                stack.append(stack[-1].children[counters[-1]])
                counters.append(0)
            retList.append(stack.pop().val)
            counters.pop()
            if len(counters) != 0: counters[-1] += 1
        return retList

n = Node(1,[3,2,4])

T = Solution()
T.postorder(n)