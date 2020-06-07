class Solution:
    def selfDividingNumbers(self, left, right):
        def self_check(n):
            for d in str(n):
                if '0' in str(n) or n % int(d) != 0 : return False
            return True
            
        div_n = []
        for n in range(left, right+1):
            if self_check(n): div_n.append(n)
        return div_n


T = Solution()
T.selfDividingNumbers(1,22)