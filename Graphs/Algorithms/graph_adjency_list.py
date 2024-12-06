class GraphAdjacenyList:
    
    def __init__(self, graph_size) -> None:
        self.nodes = [ n for n in range(graph_size)]
        self.edges = { n: [] for n in range(graph_size)}

    def add_edge(self, start_node, end_node) -> None:
        self.edges[start_node].append(end_node)
        self.edges[end_node].append(start_node)

    def display(self) -> None:
        print("Adjaceny List: ")
        for node, edge in self.edges.items():
            print(f" Node {node} : {edge} ")


graph = GraphAdjacenyList(7)

# print("Initialised Graph", graph.display())

graph.add_edge(0, 1)
graph.add_edge(0, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 2)
graph.add_edge(3, 6)
graph.add_edge(6, 5)


print("After Adding Vertices")
graph.display()