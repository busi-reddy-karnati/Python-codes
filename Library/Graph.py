from collections import defaultdict

class Graph:
    def __init__(self, num_vertices, edges):
        self.vertices = [i for i in range(num_vertices)]
        self.num_vertices = num_vertices
        self.children = defaultdict(list)
        for edge in edges:
            self.children[edge[0]].append(edge[1])
