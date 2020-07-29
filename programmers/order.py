# -*- coding: utf-8 -*- 
# 문자열 내 마음대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915#

def solution(strings, n):
    def compare(List1,List2, n):
        if List1[][], List2[][]

    letter_set = []
    for string in strings:
        order = []
        for letter in string : 
            order += [ord(letter)]
        letter_set.append((string, order))

    letter = []
    for i in range(len(letter_set)-1) :
        if letter_set[i][1][n] < letter_set[i+1][1][n] : 
            letter.append(letter_set)
        else : 
            self.compare(letter_set[i], letter_set[i+1], n-1)
 
solution(["sun","bed","car"], 2)