# -*- coding: utf-8 -*- 
import collections
def solution(participant, completion):
    part, complet = {}, {}
    for n in sorted(participant) :
        part[n] = part.get(n, 0) + 1
    for n in sorted(completion) :
        complet[n] = complet.get(n, 0) + 1
    t = collections.Counter(participant)
    print(t)
    print(type(t))

solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])