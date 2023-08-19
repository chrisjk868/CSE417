from collections import deque
import graph_generator

def calc_diameter(adj):
    # Start BFS at every node
    diameter = 0 
    for start in adj:
        diameter = max(diameter, bfs(adj, start))
    return diameter

def bfs(adj, start):
    visited = set()
    frontier = deque()
    order = list()
    d = 0
    frontier.append((start, d))
    while frontier:
        curr_node, dist = frontier.popleft()
        visited.add(curr_node)
        order.append((curr_node, dist))
        for nei in adj[curr_node]:
            if nei not in visited:
                frontier.append((nei, dist + 1))
    return order[-1][-1]

if __name__ == '__main__':
    f = open('./q5_results.txt', 'w')
    g = graph_generator.GraphGenerator(1000)
    for i in range(5000, 501, -500):
        p = 1 / i
        g.p = p
        v, e, adj = g.generate_graph()
        d = calc_diameter(adj)
        f.write(f'{1}/{i}, {d}\n')
        print(f'{1}/{i} done')