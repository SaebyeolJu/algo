# -*- coding: utf-8 -*- 
# 문자열 내 마음대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915#

def solution(strings, n):
    letter_set = []
    for string in strings:
        order = []
        for letter in string : 
            order += [ord(letter)]
        letter_set.append((string, order))

    for letter, num_list in letter_set :
        num_list[n]
        
solution(["sun","bed","car"], 2)