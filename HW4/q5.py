import graph_generator

def color_graph(adj, asc):
    # An array that tracks the colors used for each vertex:
    #   - vertex[i] is the color at vertex i
    vertex = [0 for i in range(1001)]
    # Color choices
    colors = set()
    # Colored vertices
    colored = set()
    # Order of vertex traversal
    order_v = []
    for node, nei in adj.items():
        order_v.append((node, len(nei)))
    order_v.sort(reverse=asc, key=lambda x: x[1])
    for curr_node, degree in order_v:
        if curr_node in colored:
            continue
        next_available_color = 1
        for nei in adj[curr_node]:
            if vertex[nei] == next_available_color:
                next_available_color += 1
        vertex[curr_node] = next_available_color
        colored.add(curr_node)
        if next_available_color not in colors:
            colors.add(next_available_color)
    return len(colors)

if __name__ == '__main__':
    f = open('./results/q5_results.txt', 'w')
    
    for i in range(500, 49, -50):
        p = 1 / i
        sum_c1, sum_c2 = 0, 0
        for j in range(10):
            g = graph_generator.GraphGenerator(n=1000, p=p)
            v, e, adj = g.generate_graph()
            # Increasing order of vertex degreee
            sum_c1 += color_graph(adj, False)
            print(f'   {j}-th c1 done')
            # Decreasing order of vertex degreee
            sum_c2 += color_graph(adj, True)
            print(f'   {j}-th c2 done')
        f.write(f'{1}/{i}, {sum_c1 / 10}, {sum_c2 / 10}\n')
        print(f'{1}/{i} done')
