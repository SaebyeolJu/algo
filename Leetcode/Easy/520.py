# 520. Detect Capital
# https://leetcode.com/problems/detect-capital/submissions/
# 실수 : range의 마지막은 포함 안됨
# 하나밖에 없을 때 ( 극단적인 case 생각해야함 )

class Solution:
    def detectCapitalUse(self, word):
        big = list(range(ord("A"),ord("Z")+1))
        # big
        if len(word) == 1 : return True
        if ord(word[0]) in big and ord(word[1]) in big:
            for i in range(len(word[2:])):
                if not ord(word[i+2]) in big : return False
            return True
        # small
        else : 
            for i in range(len(word[1:])):
                if ord(word[i+1]) in big : return False
            return True
             
t = Solution()
t.detectCapitalUse("uZfa")