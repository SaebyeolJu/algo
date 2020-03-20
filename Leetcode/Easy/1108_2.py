class Solution:
    def defangIPaddr(self, address: str) -> str:
        return print("[.]".join(address.split(".")))

Test = Solution()
Test.defangIPaddr("1.1.1.1")