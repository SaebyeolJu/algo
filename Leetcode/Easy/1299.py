# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr):
        for i in range(len(arr)):
            max_n = i
            for j in range(i+1,len(arr)): # find biggest num
                if arr[max_n] < arr[j]: max_n = j
            arr[i], arr[max_n] = arr[max_n], arr[i]
        arr[-1] = -1
        for i in range(1,len(arr)-1):
            arr[i] = 

t = Solution()
t.replaceElements([17,18,5,4,6,1])