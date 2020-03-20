class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_add = ""
        for letter in address:
            if(letter == ".") : 
                new_add = new_add + "[.]"
            else : 
                new_add = new_add + letter
        return print(new_add)

Test = Solution()
Test.defangIPaddr("1.1.1.1")