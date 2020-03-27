# https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1#ExpectOP
from __future__ import print_function

def bfs(g,N):
    visited = []
    queue  = []
    
    queue.append(0)
    visited.append(0)

    while (not len(queue) == 0):
        node = queue.pop(0)
        print(node, end = ' ')

        for neighbour in g: 
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

    print()
    
bfs([0,1,0,2,0,3,2,4],4)
bfs([0,1,0,2],4)