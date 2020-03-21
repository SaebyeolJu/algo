class Solution:
    def judgeCircle(self, moves: str) -> bool:
        state = [0,0]
        for letter in moves :
            if (letter == "U" or letter == "D"): 
                if (letter == "U"): state[0] -= 1
                else : state[0] += 1
            else: 
                if(letter =="L") : state[1] += 1
                else : state[1] -= 1
        return print(state[0] == 0 and state[1] == 0)

t = Solution()
t.judgeCircle("UD")