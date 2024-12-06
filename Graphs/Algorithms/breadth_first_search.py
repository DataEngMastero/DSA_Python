from graph_adjency_list import graph


def bfs(graph, source):
    # Implenting queue as array
    queue = []
    visited_nodes = []

    # Add source node 
    queue.append(source)

    while len(queue):
        node = queue.pop(0)
        visited_nodes.append(node)
        print(f"Node Visited : {node}")

        for neighbour in graph.edges[node]:
            # Dont process if already visited
            if neighbour not in visited_nodes:
                queue.append(neighbour) 


bfs(graph, 0)