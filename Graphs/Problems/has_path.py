graph_directed = {
    "A": ["B", "C"],
    "B": ["F", "D"],
    "C": [],
    "D": ["I", "G"],
    "E": ["H"],
    "F": ["E"],
    "G": ["H"],
    "H": [],
    "I": []
}

def has_path_directed(graph, src, dest) -> bool:
    if src == dest:
        return True
    
    ans = False 
    for neighbour in graph[src]:
        ans = ans or has_path_directed(graph, neighbour, dest)
    return ans

print("---------- Has Path in Directed Graph ---------------")
print(has_path_directed(graph_directed, "A", "H"))
print(has_path_directed(graph_directed, "C", "D"))
print(has_path_directed(graph_directed, "B", "G"))

graph_undirected = {
    "A": ["B", "C"],
    "B": ["F", "D", "A"],
    "C": ["A"],
    "D": ["I", "G", "B"],
    "E": ["H", "F"],
    "F": ["E", "B"],
    "G": ["H", "D"],
    "H": ["E", "G"],
    "I": ["D"]
}

def has_path_undirected(graph, src, dest, visited) -> bool:
    if src == dest:
        return True
    
    visited.add(src)
    ans = False 
    for neighbour in graph[src]:
        if neighbour not in visited:
            ans = ans or has_path_undirected(graph, neighbour, dest, visited)
    return ans 

print("---------- Has Path in Undirected Graph ---------------")
print(has_path_undirected(graph_undirected, "A", "H", set()))
print(has_path_undirected(graph_undirected, "C", "I", set()))


