class Vertex:
    def __init__(self, node) -> None:
        self.id = node 
        self.adjacent = {}
        self.distance = float("inf")
        self.visited = False 
        self.previous = None 

    def add_neighbor(self, neighbor, weight = 0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()
    
    def get_vertex_id(self):
        return self.id
    
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    
    def set_distance(self,dist):
        self.distance = dist 

    def get_distance(self):
        return self.distance
    
    def set_previous(self, prev):
        self.previous = prev 

    def set_visited(self):
        self.visited = True 

    def __str__(self) -> str:
        return str(self.id) + ' adjacent : ' + str([x.id for x in self.adjacent])
    

class Graph:
    def __init__(self) -> None:
        self.vertices = {}
        self.no_of_vertices = 0 

    def __iter__(self):
        return iter(self.vertices.values())
    
    def add_vertex(self, node):
        self.no_of_vertices += 1
        new_vertex = Vertex(node)
        self.vertices[node] = new_vertex
        return new_vertex
    
    def get_vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None
        
    def add_edge(self, start, dest, cost = 0):
        if start not in self.vertices:
            self.add_vertex(start)
        if dest not in self.vertices:
            self.add_vertex(dest)
        self.vertices[start].add_neighbor(self.vertices[dest], cost)
        self.vertices[dest].add_neighbor(self.vertices[start], cost)

    def get_vertices(self):
        return self.vertices.keys()
    
    def get_edges(self, G):
        edges = []
        for v in G:
            for w in v.get_connections():
                vid = v.get_vertex_id()
                wid = w.get_vertex_id()
                edges.append((vid, wid, v.get_weight(w)))
        return edges 
    
if __name__ == "__main__":
    G = Graph()
    G.add_vertex('a')
    G.add_vertex('b')
    G.add_vertex('c')
    G.add_vertex('d')
    G.add_vertex('e')

    G.add_edge('a', 'b', 4)
    G.add_edge('a', 'c', 1)
    G.add_edge('c', 'b', 2)
    G.add_edge('b', 'e', 4)
    G.add_edge('c', 'd', 4)
    G.add_edge('d', 'e', 4)

    print(G.get_edges(G))



