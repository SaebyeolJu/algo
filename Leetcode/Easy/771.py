'''
# 771. Jewels and Stones
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
Each character in S is a type of stone you have.  
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".
'''

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = list(J)
        S = list(S)
        count = 0

        for i in range(len(S)):
            for j in range(len(J)):
                if J[j] == S[i] : count += 1
        return count

test = Solution()
test.numJewelsInStones('aA', 'aAAaabbbb')