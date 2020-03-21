class Solution:
    def reverseString(self, s):
        temp = s[:]
        for index in range(0, (len(s)-1)//2):
            temp[index] = s[len(s)-1-index]
            temp[len(s)-1-index] = s[index]
        return print(temp)

t = Solution()
t.reverseString(["H","a","n","n","a","h"])