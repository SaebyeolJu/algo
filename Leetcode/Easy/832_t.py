# single list transform

B = [0,0,1]
temp = B[:]

for n in range(len(B)//2): # flip
    temp[len(B)-1-n] = B[n]
    B[n] = temp[len(B)-1-n]
    temp[n] = B[len(B)-1-n]

for n in range(len(temp)):
    if(temp[n] == 0): temp[n] = 1
    else: temp[n] = 0

print(temp)
