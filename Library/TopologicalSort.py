from Library.Graph import Graph

g = Graph(6,[[0,1],[1,2],[2,4],[3,1],[1,5],[5,2]])
def topological_sort(graph):
    visited = set()
    stack = []
    for vertex in graph.vertices:
        if vertex not in visited:
            visit(graph, vertex, stack, visited)
    print(stack[::-1])

def visit(graph, node, stack, visited):
    for child in graph.children[node]:
        if child not in visited:
            visited.add(child)
            visit(graph, child, stack, visited)
    stack.append(node)

topological_sort(g)