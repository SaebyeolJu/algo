# 171. Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, s):
        n_sum = 0
        for i in range(len(s)):
            letter_num = (ord(s[i])-64)
            s_len = (26 * (len(s) - i-1))
            n_sum += letter_num * s_len
        print(n_sum)

t = Solution()
t.titleToNumber("AA")