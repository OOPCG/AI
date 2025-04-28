# DFS Recursive Implementation
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    print(node, end=' ')  # Process the node (printing here)
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Example Undirected Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Depth First Search (DFS) starting from node A:")
dfs_recursive(graph, 'A')
'''
______________________________________________________________________________________
'''

from collections import deque

# BFS Iterative Implementation
def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    visited.add(start_node)

    while queue:
        node = queue.popleft()
        print(node, end=' ')  # Process the node (printing here)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("\n\nBreadth First Search (BFS) starting from node A:")
bfs(graph, 'A')
