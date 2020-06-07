class Solution:
    def selfDividingNumbers(self, left: int, right: int):
      num = set(range(left, right+1))
      rm_n = set()

      for n in num:
        for s in str(n):
          if '0' in str(n) or n % int(s) != 0 : 
            rm_n.add(n)
            break
      return sorted(list(num - rm_n))