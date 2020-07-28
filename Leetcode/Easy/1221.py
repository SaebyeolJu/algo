class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt_R, cnt_L, ans = 0, 0, 0
        for ch in s :
            if ch == 'R': cnt_R += 1
            elif ch == 'L': cnt_L += 1
            if cnt_R == cnt_L : 
                cnt_R, cnt_L = 0, 0
                ans += 1
        return ans