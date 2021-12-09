class DisjointSetQuickUnion:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find_root(self, a):
        while self.parent[a] != a:
            a = self.parent[a]
        return a

    def union(self, a, b):
        rootA = self.find_root(a)
        rootB = self.find_root(b)
        if rootB != rootA:
            self.parent[rootB] = rootA

    def are_connected(self, a, b):
        return self.find_root(a) == self.find_root(b)


if __name__ == '__main__':
    d = DisjointSetQuickUnion(5)
    print(d.are_connected(1, 2))
    d.union(1, 2)
    print(d.are_connected(1, 2))
    d.union(2, 4)
    print(d.are_connected(1, 4))
