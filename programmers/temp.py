# -*- coding: utf-8 -*- 

def solution(seoul):
    for index, name in enumerate(seoul) :
        if name == "Kim" : return("김서방은 {}에 있다".format(index))

solution(["Jame","Kim"])