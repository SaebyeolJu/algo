'''
# 1342. Number of Steps to Reduce a Number to Zero
# Given a non-negative integer num, return the number of steps to reduce it to zero. 
# If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

[Solution]
iterative way, using while loop
time complexity : 
'''
class Solution :
    def numberOfSteps(self,num):
        count = 0
        while(num != 0):
            if(num %2 != 0):
                num -= 1
                count += 1
                if(num ==0): return count
            num /= 2
            count += 1
        return count

num = Solution()
num.numberOfSteps(8)