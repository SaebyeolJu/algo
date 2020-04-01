class Solution:
    def reverseString(self, s):
        for i in range(0,len(s)//2):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
        return s

t = Solution()
t.reverseString(["h","e","l","l","o"])