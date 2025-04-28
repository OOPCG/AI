# Graph Coloring using Backtracking and Branch and Bound

def graph_coloring(graph, m):
    n = len(graph)  # number of vertices
    colors = [0] * n  # color assignment for each vertex (0 = no color yet)

    # Check if current color assignment is safe
    def is_safe(vertex, color):
        for neighbor in graph[vertex]:
            if colors[neighbor] == color:
                return False
        return True

    # Recursive function to solve coloring problem
    def solve(vertex):
        if vertex == n:
            return True  # All vertices are assigned

        for color in range(1, m+1):  # Try all colors
            if is_safe(vertex, color):
                colors[vertex] = color
                if solve(vertex + 1):
                    return True
                # Backtrack
                colors[vertex] = 0

        return False  # No valid color found

    if solve(0):
        return colors
    else:
        return None  # No solution found

# Example usage

# Graph as adjacency list
# Example Graph:
# 0 -- 1
# |  / |
# 2 -- 3
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

m = 3  # Number of colors

solution = graph_coloring(graph, m)

print(f"Graph Coloring using {m} colors:")
if solution:
    for vertex, color in enumerate(solution):
        print(f"Vertex {vertex} --> Color {color}")
else:
    print("No solution exists with the given number of colors.")


#_____________________________________________________________________________

#Only backtracking :-

# Graph Coloring using only Backtracking

def graph_coloring_backtracking(graph, m):
    n = len(graph)  # number of vertices
    colors = [0] * n  # color assignment (0 = not colored)

    # Check if it is safe to assign color to vertex
    def is_safe(vertex, color):
        for neighbor in graph[vertex]:
            if colors[neighbor] == color:
                return False
        return True

    # Main backtracking function
    def backtrack(vertex):
        if vertex == n:
            return True  # All vertices colored successfully

        for color in range(1, m + 1):  # Try all colors
            if is_safe(vertex, color):
                colors[vertex] = color
                if backtrack(vertex + 1):
                    return True
                colors[vertex] = 0  # Backtrack

        return False  # No color fits

    if backtrack(0):
        return colors
    else:
        return None

# Example usage

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

m = 3  # Number of colors

solution = graph_coloring_backtracking(graph, m)

print(f"Graph Coloring using only Backtracking with {m} colors:")
if solution:
    for vertex, color in enumerate(solution):
        print(f"Vertex {vertex} --> Color {color}")
else:
    print("No solution exists.")
