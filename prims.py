import heapq

def prim_mst(graph, start):
    visited = set()
    min_heap = [(0, start)]  # (cost, vertex)
    total_cost = 0

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        total_cost += cost

        for v, weight in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (weight, v))

    return total_cost

# Example usage
graph = {
    0: [(1, 4), (2, 3)],
    1: [(0, 4), (2, 1), (3, 2)],
    2: [(0, 3), (1, 1), (3, 4)],
    3: [(1, 2), (2, 4)]
}

print("Total cost of MST (Prim's):", prim_mst(graph, 0))
