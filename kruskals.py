class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX
            return True
        return False

def kruskal_mst(edges, n):
    edges.sort(key=lambda x: x[2])  # sort by weight
    ds = DisjointSet(n)
    total_cost = 0

    for u, v, weight in edges:
        if ds.union(u, v):
            total_cost += weight

    return total_cost

# Example usage
edges = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4)
]

print("Total cost of MST (Kruskal's):", kruskal_mst(edges, 4))
