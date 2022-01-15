from collections import deque
from Library.Graph import Graph

g = Graph(7, [[0, 1], [1, 4], [0, 2], [0, 3], [2, 5], [3, 6]])


def bfs(graph, root):
    visited = [False]*graph.num_vertices
    distance = [graph.num_vertices]*graph.num_vertices
    distance[root] = 0
    visited[root] = True
    parent = [i for i in range(graph.num_vertices)]
    queue = deque([root])
    while queue:
        node = queue.popleft()
        for child in graph.children[node]:
            if not visited[child]:
                visited[child] = True
                queue.append(child)
                parent[child] = node
                distance[child] = distance[node] + 1
    # This gives the shortest path between root and all other nodes
    print(distance)
    print(parent)

    # If we want path between 0 and other node, use the parent
    path = []
    destination = 4
    node = destination
    while node != root:
        path.append(node)
        node = parent[node]
    path.append(root)
    print(path[::-1])


bfs(g, 0)
