class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        B = list()
        for num in A:
            if(num %2 != 0): B.append(num)
            else: B.insert(0,num)
        return B