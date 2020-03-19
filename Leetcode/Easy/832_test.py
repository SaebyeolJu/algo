'''
# 832. Flipping an Image
# https://leetcode.com/problems/flipping-an-image/
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
'''
import copy
B = [[1,1,0],[1,0,1],[0,0,0]]
temp = copy.deepcopy(B)
for i in range(len(B)):
    for n in range(len(B[i]) // 2): # flip
        temp[i][len(B[i])-1-n] = B[i][n]
        B[i][n] = temp[i][len(B[i])-1-n]
        temp[i][n] = B[i][len(B[i])-1-n]

    for n in range(len(temp[i])):
        if(temp[i][n] == 0): temp[i][n] = 1
        else: temp[i][n] = 0

print(temp)
