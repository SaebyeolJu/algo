'''
1374. Generate a String With Characters That Have Odd Counts
https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
'''
import random
class Solution:
    def generateTheString(self, n: int) -> str:
        t = ""
        state = 0
        while(n != 0):
            state = random.randrange(1,n+1,2)
            letter = (random.randint(ord('a'),ord('z'))) # random letter 
            if(chr(letter) in t) : continue
            t += state*(chr(letter))
            n -= state
        return print(t)

t = Solution()
t.generateTheString(4)