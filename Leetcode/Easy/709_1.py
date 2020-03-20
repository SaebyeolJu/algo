class Solution:
    def toLowerCase(self, A: str) -> str:
        lower = ""
        for letter in A:
            if(64<ord(letter)<91):
                lower = lower + chr(ord(letter)+32)
            else: lower = lower + letter
        return lower