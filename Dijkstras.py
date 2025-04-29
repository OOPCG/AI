import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    min_heap = [(0, start)]

    while min_heap:
        current_dist, u = heapq.heappop(min_heap)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(min_heap, (dist[v], v))

    return dist

# Example usage
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

start_node = 0
distances = dijkstra(graph, start_node)

print(f"Shortest distances from node {start_node}:")
for node in distances:
    print(f"Node {node} : Distance {distances[node]}")
