graph = {
    1: [3, 7],
    2: [],
    3: [1, 7],
    4: [9],
    5: [8, 10],
    6: [8, 10],
    7: [1, 3],
    8: [5, 6],
    9: [4], 
    10: [5, 6]
}

vertices = [ i for i in range(1, 11) ]

print(vertices)

print(graph)

def dfs(graph, vertix, visited):
    stack = []
    stack.append(vertix)


    while len(stack):
        elem = stack.pop(-1)
        visited.append(elem)

        for neighbor in graph[elem]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.append(elem)


def no_of_provinces(graph, vertices):
    visited = []
    provinces = 0
    for i in vertices:
        if i not in visited:
            print("Calling DFS on ", i)
            dfs(graph, i, visited)
            provinces += 1
    return provinces
            
print(no_of_provinces(graph, vertices))