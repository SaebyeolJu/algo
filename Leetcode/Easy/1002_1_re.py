from collections import Counter

class Solution:
    def commonChars(self, A):
        d1 = Counter(A[0])
        for i in range(1,len(A)):
            d1 &= Counter(A[i])
        print(d1.elements())

t = Solution()
t.commonChars(["beclla","lacbel","rolcler"])