class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1: return True
        elif num == 0 or num %4 != 0: return False
        return self.isPowerOfFour(num // 4)

t = Solution()
t.isPowerOfFour(16)