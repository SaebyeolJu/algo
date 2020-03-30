# import random

class Solution:
    def replaceElements(self, arr):
        for i in range(len(arr)):
            max_n = i
            for j in range(i+1,len(arr)): # find biggest num
                if arr[max_n] < arr[j]: max_n = j
            arr[i], arr[max_n] = arr[max_n], arr[i]
       
        left = arr[0] + 1
        arr[1] = left
        for num in range(2,len(arr)):
            arr[num] = 0
        # for num in range(1,len(arr)):
        #     arr[num] = random.randrange(1,left)
        #     left -= arr[num]
        arr[-1] = -1
        print(arr)

t = Solution()
t.replaceElements([17,18,5,4,6,1])