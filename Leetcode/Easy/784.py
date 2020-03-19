'''
# 784. Letter Case Permutation
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  
Return a list of all possible strings we could create.

[Solution]
using ASCII Code
'''

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.S = S
        letter = set(self.S)
        num_list = []
        for i in letter:
            # if it's number
            if(48<= ord(list[i])<=57):
                for i in range(0, 2**(len(letter))):
                    num_list.append()
            else: 
                self.S.upper()
                self.S.lower()

