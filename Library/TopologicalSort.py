from Library.Graph import Graph

g = Graph(6, [[2, 3], [3, 1], [4, 0], [4, 1], [5, 2], [5, 1]])


def topological_sort(graph):
    visited = set()
    stack = []
    for vertex in graph.vertices:
        if vertex not in visited:
            stack = dfs(vertex, graph, visited, stack)
    print(stack)


def dfs(root, graph, visited, stack):
    visited.add(root)
    for child in graph.children[root]:
        if child not in visited:
            visited.add(child)
            stack = dfs(child, graph, visited, stack)
    stack.append(root)
    return stack


topological_sort(g)

