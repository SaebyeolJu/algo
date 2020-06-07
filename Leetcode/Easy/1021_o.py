# 1021. Remove Outermost Parentheses
# https://leetcode.com/problems/remove-outermost-parentheses/

# method 1.
# using left, right
class Solution:
    def removeOuterParentheses(self, S):
        rm = ""
        l,r = 0, 0
        for i in range(len(S)):
            if S[i] == "(" : l += 1
            else : r += 1            
            if (S[i] == "(" and l - r == 1 ) or (l == r): continue
            rm = rm + S[i]
        return rm

# method 2.
# using cnt without left, right 
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        cnt, rm = 0, ""
        for i in range(len(S)):
            if S[i] == "(" : cnt += 1
            else : cnt -= 1
            if S[i] == "(" and cnt == 1 or cnt == 0 : continue
            rm = rm + S[i]
        return rm

# metod 2 -> enumerate function apply
class Solution:
    def removeOuterParentheses(self, S:str) -> str:
        cnt = 0
        rm = ""
        for i in enumerate(S):
            if S[i] == "(" : cnt += 1
            else : cnt -= 1
            if S[i] == "(" and cnt == 1 or cnt == 0 : continue
            rm = rm + S[i]
        return rm
        
t = Solution()
t.removeOuterParentheses("(()())(())")