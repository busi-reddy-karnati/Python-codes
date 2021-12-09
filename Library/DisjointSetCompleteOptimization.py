class DisjointSetCompleteOptimization:
    def __init__(self, size):
        self.rank = [1 for i in range(size)]
        self.parent = [i for i in range(size)]

    def find_root(self, a):
        if a == self.parent[a]:
            return a
        self.parent[a] = self.find_root(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        rootA = self.find_root(a)
        rootB = self.find_root(b)
        if rootB != rootA:
            if self.rank[rootA] > self.rank[rootB]:
                self.parent[rootB] = rootA
            elif self.rank[rootB] > self.rank[rootA]:
                self.parent[rootA] = rootB
            else:
                self.parent[rootA] = rootB
                self.rank[rootB] += 1

    def are_connected(self, a, b):
        return self.find_root(a) == self.find_root(b)


if __name__ == '__main__':
    uf = DisjointSetCompleteOptimization(10)
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.find_root(1),uf.find_root(5))
    print(uf.are_connected(1, 5))
    print(uf.are_connected(5, 7))
    print(uf.are_connected(4, 9))
    uf.union(9, 4)
    print(uf.are_connected(4, 9))