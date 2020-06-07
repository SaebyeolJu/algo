'''
# 784. Letter Case Permutation
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  
Return a list of all possible strings we could create.

[Solution]
using ASCII Code
'''

class Solution:
    def letterCasePermutation(self, S):
        ans = []
        n = []
        letter = []
        cnt = 0

        for l in S:
            if 48 <= ord(l)<= 57: 
                n.append(l)
            else : 
                cnt += 1
                letter.append(l) 
                if ord(l) < 97: letter.append(chr(ord(l) + 32))
                else : letter.append(chr(ord(l) - 32))

        for i in range(0,len(letter)):
            for num in n:
                ans[i] = num + letter[i]
                ans[i+1] = num + letter[i]
        print(ans)


t = Solution()
t.letterCasePermutation("a1b2")