# DFS method
class Solution:
    def isSameTree(self, r_1, r_2):
        stack = [(r_1, r_2)]
        while stack :
            r_1, r_2= stack.pop()
            if (not r_1 and r_2) or (r_1 and not r_2) : return False
            if not r_1 and not r_2 : continue
            if r_1.val != r_2.val : return False
            stack.append((r_1.right, r_2.right))
            stack.append((r_1.left, r_2.left))
        return True