'''
# 1342. Number of Steps to Reduce a Number to Zero
# Given a non-negative integer num, return the number of steps to reduce it to zero. 
# If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

[Solution]
using recursive
time complexity : 
'''
class Solution :
    count = 0
    def numberOfSteps(self,num: int):
        if(num == 0): return self.count
        elif(num % 2 == 0) :
            self.count += 1
            print(f"{num} is even; divide by 2 and obtain {num//2}.")
            return self.numberOfSteps(num//2)
        else : 
            self.count += 1
            print(f"{num} is odd; subtract 1 and obtain {num-1}.")
            return self.numberOfSteps(num-1)

num = Solution()
num.numberOfSteps(8)