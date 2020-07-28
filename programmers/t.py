def solution(s):
    st = [0]  * len(s)
    for i in range(len(s)-1):
        for j in range(len(s)-1):
            if ord(s[j]) >= ord(s[j+1]) : st[j], st[j+1] = s[j+1], s[j]
            else : st[j], st[j+1] = s[j], s[j+1]
    print(st)

t = solution("Zbcdefg")