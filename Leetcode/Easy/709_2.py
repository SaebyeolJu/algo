class Solution:
    def toLowerCase(self, A: str) -> str:
        return "".join(A.split())

        for letter in A:
            if(ord("A")<=ord(letter)<=ord("Z")):
                lower = lower + chr(ord(letter)+32)
            else: lower = lower + letter
        return lower