class DisjointSetQuickFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find_root(self, a):
        return self.root[a]

    def union(self, a, b):
        rootA = self.find_root(a)
        rootB = self.find_root(b)
        if rootA != rootB:
            for i in range(len(self.root)):
                if self.root[i] == rootB:
                    self.root[i] = rootA

    def are_connected(self, a, b):
        return self.find_root(a) == self.find_root(b)


if __name__ == '__main__':
    d = DisjointSetQuickFind(5)
    print(d.are_connected(1, 2))
    d.union(1, 2)
    print(d.are_connected(1, 2))
    d.union(2, 4)
    print(d.are_connected(1, 4))
