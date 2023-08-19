import graph_generator

def color_graph(adj):
    # An array that tracks the colors used for each vertex:
    #   - vertex[i] is the color at vertex i
    vertex = [0 for i in range(1001)]

    # Color choices
    colors = set()

    # Colored vertices
    colored = set()

    for curr_node in adj:
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
    f = open('./results/q4_results_new.txt', 'w')
    for i in range(500, 49, -50):
        sum_c = 0
        p = 1 / i
        for j in range(10):
            g = graph_generator.GraphGenerator(n=1000, p=p)
            v, e, adj = g.generate_graph()
            sum_c += color_graph(adj)
            print(f'   {j}-th done')
        f.write(f'{1}/{i}, {sum_c / 10}\n')
        print(f'{1}/{i} done')
