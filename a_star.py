import heapq

# A* Algorithm Implementation
def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    
    # Directions: up, down, left, right
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    # Heuristic Function: Manhattan Distance
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    # Priority Queue for open nodes
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start))  # (f(n), g(n), node)
    
    came_from = {}  # To reconstruct path
    g_score = {start: 0}
    
    while open_set:
        _, cost, current = heapq.heappop(open_set)
        
        if current == goal:
            # Reconstruct Path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for dir in directions:
            neighbor = (current[0] + dir[0], current[1] + dir[1])
            
            # Check bounds and obstacles
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, tentative_g, neighbor))
                    
    return None  # No path found

# Example Grid
# 0 = free cell
# 1 = obstacle
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)  # top-left corner
goal = (4, 4)   # bottom-right corner

# Run A*
path = astar(grid, start, goal)

# Print the result
print("Path from start to goal:")
if path:
    for step in path:
        print(step)
else:
    print("No path found!")
