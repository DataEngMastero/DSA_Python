from graph_adjency_list import graph

def dfs(graph, source):
    # Implenting stacks as array
    stack = []
    visited_nodes = []

    # Add source node 
    stack.append(source)

    while len(stack):
        node = stack.pop(-1)
        visited_nodes.append(node)
        print(f"Node Visited : {node}")

        for neighbour in graph.edges[node]:
            # Dont process if already visited
            if neighbour not in visited_nodes:
                stack.append(neighbour)


dfs(graph, 0)