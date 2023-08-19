import numpy as np
class GraphGenerator:

    def __init__(self, n=10, p=0.2):
        # n being the number of vertices
        # p being the probability of an edge appearing in the set of edges
        self.n = n
        self. p = p
        self.all_edges = self.generate_edges()

    def generate_graph(self):
        adj = {}
        for u, v in self.all_edges:
            if u not in adj:
                adj[u] = [v]
            else:
                adj[u].append(v)
            if v not in adj:
                adj[v] = [u]
            else:
                adj[v].append(u)
        return set(adj.keys()), self.all_edges, adj

    def generate_edges(self):
        edges = list()
        for u in range(1, self.n + 1):
            for v in range(u + 1, self.n + 1):
                if v == u:
                    continue
                include = np.random.choice([True, False], p=[self.p, 1 - self.p])
                if include:
                    edges.append((u, v))
        return edges

if __name__ == '__main__':
    g = GraphGenerator(1000, 0.002)
    v, e, adj = g.generate_graph()
    print(f'G(n, p): G({g.n}, {g.p})')
    print(f'vertices: {v}')
    print(f'edges: {e}')
    print(f'adjacency list: {adj}')