'''
 # 1281
 # Subtract the Product and Sum of Digits of an Integer
 # Given an integer number n, return the difference between the product of its digits and the sum of its digits.
'''
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = list(str(n))
        pro_d = 1
        sum_d = 0

        for i in num:
            pro_d *= int(i)
            sum_d += int(i)

        return print(pro_d - sum_d)

test = Solution()
test.subtractProductAndSum(4421)