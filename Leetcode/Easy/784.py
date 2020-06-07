'''
# 784. Letter Case Permutation
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  
Return a list of all possible strings we could create.

[Solution]
using ASCII Code
'''

class Solution:
    def letterCasePermutation(self, S):
        res = []
        letter = []
        cnt = 0

        for l in list(S):
            if not 48 <= ord(l)<= 57: 
                cnt += 1
                letter.append(chr(ord(l)))
                if ord(l) < 97: letter.append(chr(ord(l) + 32))
                else : letter.append(chr(ord(l) - 32))

        for n in range(0,len(letter)):
            temp = ''
            for n in list(S):
                if 48 <= ord(n)<= 57: temp += n
                else: temp += letter[i]
            res.append(temp)
        print(res)

        # for i in range(0,len(letter)):
        #     temp = ''
        #     for n in list(S):
        #         if 48 <= ord(n)<= 57: temp += n
        #         else: temp += letter[i]
        #     res.append(temp)
        # print(res)

t = Solution()
t.letterCasePermutation("a1b2")
# ["a1b2", "a1B2", "A1b2", "A1B2"]