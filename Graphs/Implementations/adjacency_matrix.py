class Vertex:
    def __init__(self, node) -> None:
        self.id = node 
        self.visited = False 

    def add_neighbor(self, neighbor, G):
        G.addEdge(self.id, neighbor)

    def get_connections(self, G):
        return G.adj_matrix[self.id]
    
    def get_vertex_id(self):
        return self.id 
    
    def set_vertex_id(self, id):
        self.id = id
    
    def set_visited(self):
        self.visited = True 

    def __str__(self) -> str:
        return str(self.id)
    
class Graph:
    def __init__(self, no_of_vertices, cost = 0) -> None:
        self.adj_matrix = [[-1] * no_of_vertices for _ in range(no_of_vertices)]
        self.no_of_vertices = no_of_vertices
        self.vertices = []
        
        for i in range(0, no_of_vertices):
            new_vertex = Vertex(i)
            self.vertices.append(new_vertex)

    def set_vertex(self, vertex, id):
        if 0 <= vertex < self.no_of_vertices:
            self.vertices[vertex].set_vertex_id(id)

    def get_vertex(self, n):
        for i in range(0, self.no_of_vertices):
            if n == self.vertices[i].get_vertex_id():
                return i 
        else:
            return -1 
        
    def add_edge(self, start, dest, cost = 0):
        if self.get_vertex(start) != -1 and self.get_vertex(dest) != -1:
            self.adj_matrix[self.get_vertex(start)][self.get_vertex(dest)] = cost 
            self.adj_matrix[self.get_vertex(dest)][self.get_vertex(start)] = cost 

    def get_vertices(self):
        vertices = []
        for i in range(0, self.no_of_vertices):
            vertices.append(self.vertices[i].get_vertex_id())
        return vertices 

    def print_matrix(self):
        for u in range(0, self.no_of_vertices):
            row = []
            for v in range(0, self.no_of_vertices):
                row.append(self.adj_matrix[u][v])
            print(row)

    def get_edges(self):
        edges = []
        for v in range(0, self.no_of_vertices):
            for u in range(0, self.no_of_vertices):
                if self.adj_matrix[u][v] != -1:
                    vid = self.vertices[v].get_vertex_id()
                    uid = self.vertices[u].get_vertex_id()
                    edges.append((vid, uid, self.adj_matrix[u][v]))
        return edges


if __name__ == "__main__":
    G = Graph(5)
    G.set_vertex(0, 'a')
    G.set_vertex(1, 'b')
    G.set_vertex(2, 'c')
    G.set_vertex(3, 'd')
    G.set_vertex(4, 'e')

    G.add_edge('a', 'e', 10)
    G.add_edge('a', 'c', 20)
    G.add_edge('c', 'd', 30)
    G.add_edge('b', 'e', 40)
    G.add_edge('e', 'd', 50)
    # G.add_edge('f', 'e', 60)

    print(G.print_matrix())
    print(G.get_edges())


    