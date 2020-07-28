# 637. Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# failed

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root : return 0
        lev = [1]
        stack = [(root, lev)]
        nums = []
        new_set = [0] * 4
        
        while stack : 
            root, lev = stack.pop()
            nums.append(new_set)
            if root.right : stack.append((root.right, lev + [lev[-1] +1]))
            if root.left : stack.append((root.left, lev + [lev[-1] + 1]))
            new_set[lev[-1]] = [new_set[lev[-1]]] + [root.val]
        print(nums[0])
        self.sumNode(nums[0])
        
    def sumNode(self, num_list):
        ans = []
        for i in range(1,len(num_list)):
            if type(num_list[i]) == list:
                n = self.sumNode(num_list[i])
            else : 
                ans.append(num_list[1])
                print(ans)
                return num_list[1]