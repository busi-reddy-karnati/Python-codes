class Graph:
    def __init__(self, n):
        self.vertices = {i for i in range(n)}
        self.neighbours = {}
        for i in range(n):
            self.neighbours[i] = set()

    def get_vertices(self):
        return self.vertices

    def add_edge(self, a, b):
        self.neighbours[a].add(b)


def traverse_graphs(G, node, visited):
    print(node)
    for neighbour in G.neighbours[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            traverse_graphs(G, neighbour, visited)


def traverse_directed_acyclic_graph(G, node):
    """
    Used for traversing a tree like structure. When there are no cycles.
    Tree ensures no cycles which means we don't need to track the visited nodes
    :param G: Graph with vertices, neighbours
    :param node: The source from which we need to do the DFS
    """
    print(node)
    for neighbour in G.neighbours[node]:
        traverse_directed_acyclic_graph(G, neighbour)


def traverse_graph_starter():
    """
    Traverse a Graph, when there can be loops in the graph
    :return: None
    """
    G2 = Graph(8)
    G2.add_edge(0, 4)
    G2.add_edge(4, 1)
    G2.add_edge(1, 6)
    G2.add_edge(1, 2)
    G2.add_edge(5, 6)
    G2.add_edge(6, 7)
    G2.add_edge(2, 3)
    G2.add_edge(3, 4)
    G2.add_edge(4, 5)
    G2.add_edge(4, 0)
    G2.add_edge(6, 3)
    traverse_graphs(G2, 0, {0})


def traverse_tree_starter() -> None:
    """
    Traverse a Tree like DS. No loops
    """
    G = Graph(5)
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(1, 4)
    G.add_edge(2, 3)
    traverse_directed_acyclic_graph(G, 0)


class Main:
    def __init__(self):
        # traverse_tree_starter()
        traverse_graph_starter()


if __name__ == '__main__':
    Main()
