class GraphAdjacenyMatrix:

    def __init__(self, graph_size) -> None:
        self.matrix = [ [0 for n in range(graph_size)] for n in range(graph_size)]

    def add_edge(self, start_node, end_node):
        self.matrix[start_node][end_node] = 1
        self.matrix[end_node][start_node] = 1 

    def display(self):
        print("Adjaceny Matrix") 
        for node in self.matrix:
            print(node)


graph = GraphAdjacenyMatrix(7)
print("Initialised Graph", graph.display())

graph.add_edge(0, 1)
graph.add_edge(0, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 2)
graph.add_edge(3, 6)
graph.add_edge(6, 5)


print("After Adding Vertices", graph.display())