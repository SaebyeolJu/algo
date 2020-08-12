# -*- coding: utf-8 -*- 

# 1002. Find Common Characters
# https://leetcode.com/problems/find-common-characters/

# 1. 문자열을 알파벳으로 쪼개기
# 2. 알파벳 종류 마다 count
# 3. 공통된 알파벳만 출력
# 4. 같은 알파벳 여러번 출력한 경우

# 단순하게 알파벳 종류별로 count해서 배열 길이로 나누면 4번을 처리하지 못함
# dictionary 사용 (Hash)

class Solution:
    def commonChars(self, A):
        dic = {}
        for i in range(len(A)):
            A[i] = list(A[i])
            dic[i] = self.checkLetter(A[i])
        print(dic)
        
    def checkLetter(self, Letter_list) : 
        letter_cnt = {}
        for l in Letter_list:
            if l in letter_cnt : letter_cnt[l] += 1
            else : letter_cnt[l] = 1
        return letter_cnt

t = Solution()
t.commonChars(["bella","label","roller"])