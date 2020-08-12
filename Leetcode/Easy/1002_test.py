input_data = ["cool","lock","cook"]

class Solution:
    def commonChars(self, A):
        dic = {}
        for i in range(len(A)):
            A[i] = list(A[i])
            dic[i] = self.checkLetter(A[i])     
        return dic
        
    def checkLetter(self, Letter_list) : 
        letter_cnt = {}
        for l in Letter_list:
            if l in letter_cnt : letter_cnt[l] += 1
            else : letter_cnt[l] = 1
        return letter_cnt

s = Solution()
o = s.commonChars(input_data)
print(o)

our_list = list(o.values())
all_sets = list(map(lambda x: set(([(k, v) for k, v in x.items()])), our_list))
print(all_sets)

_final = all_sets[0].intersection(*all_sets[1:])
print(_final)

in_list = [] 
in_list = [elem for elem, count in _final for each in  range(0,count)]
print(in_list)