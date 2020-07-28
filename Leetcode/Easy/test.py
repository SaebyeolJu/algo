def solution(s, n):
    nums = []
    for letter in s : 
        if ord("a") <= ord(letter) <= ord("z") or ord("A") <= ord(letter) <= ord("Z"):
            if ord(letter) + n >= ord("z") : 
                nums.append(chr(ord(letter) + n - ord("z")))
            nums.append(chr(ord(letter) + n))
        else : nums.append(letter)
    print("".join(nums))

s = solution("a B z",4)