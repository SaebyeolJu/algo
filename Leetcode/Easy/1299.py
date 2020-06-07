# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr):
        max = 0
        for i in range(len(arr)): 
            if arr[i] > max : max = arr[i]
        arr[-1] = -1
        
        return arr
            

t = Solution()
t.replaceElements([17,18,5,4,6,1])