Given = [0,0,1,1,1,2,2,3,3,4]
state = [0]

for i in Given:
  for j in state:
    if(Given[i] != state[j]): 
      state.append(Given[i])

print(state)
print(len(state))