# -*- coding: utf-8 -*- 

# 1. make the same Capital letter, small letter
# 2. dealing special letter("space, %$#@ stuff")
# 3. check whether it is same
# 4. string can't be modify

import re

class Solution:
    def isPalindrome(self, s):
        s = re.sub("[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\'|\(\)\[\]\<\>`\'…》]","",s)
        s = s.replace(" ","")
        print(s)
        for i in range(len(s)//2):
            if abs(ord[i] - ord[len(s)-1-i]) != 0 and abs(ord[i] - ord[len(s)-1-i]) != 32: 
                print("False")
        return True

T = Solution()
T.isPalindrome("A man, a plan, a canal: Panama")