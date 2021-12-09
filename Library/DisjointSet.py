class DisjointSet:
    def __init__(self, n):
        self.parent = [0] * n
        for i in range(n):
            self.parent[i] = i

    def are_connected(self, a, b):
        if self.find(a) == self.find(b):
            return True
        return False

    def union(self, a, b):
        root1 = self.find(a)
        root2 = self.find(b)
        if root2 == root1:
            return
        self.parent[root1] = b

    def find(self, node):
        while self.parent[node] != node:
            node = self.parent[node]
        return node
