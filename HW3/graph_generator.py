import numpy as np
class GraphGenerator:

    def __init__(self, n=10, p=0.2):
        # n being the number of vertices
        # p being the probability of an edge appearing in the set of edges
        self.n = n
        self. p = p
        self.all_edges = self.generate_edges()

    def generate_graph(self):
        # Iterate through edges and select edges to add to existing edges in graph with respect to p
        g_edges = []
        adj = {}
        for e in self.all_edges:
            include = np.random.choice([True, False], p=[self.p, 1 - self.p])
            if include:
                g_edges.append(e)
        # After getting the edges for the graph construct an adjacency list
        for u, v in g_edges:
            if u not in adj:
                adj[u] = [v]
            else:
                adj[u].append(v)
            if v not in adj:
                adj[v] = [u]
            else:
                adj[v].append(u)
        return set(adj.keys()), g_edges, adj

    def generate_edges(self):
        edges = list()
        for u in range(1, self.n + 1):
            for v in range(u + 1, self.n + 1):
                if v == u:
                    continue
                edges.append((u, v))
        return edges

if __name__ == '__main__':
    g = GraphGenerator()
    v, e, adj = g.generate_graph()
    print(f'G(n, p): G({g.n}, {g.p})')
    print(f'vertices: {v}')
    print(f'edges: {e}')
    print(f'adjacency list: {adj}')