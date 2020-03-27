graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

def graph(graph, node):
    visited = []
    queue = []
    
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop()

        for neighbor in graph[s]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
        

graph(graph, 'A')

