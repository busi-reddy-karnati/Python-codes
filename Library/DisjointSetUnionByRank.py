class DisjointSetUnionByRank:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1 for i in range(size)]

    def find_root(self, a):
        while self.parent[a] != a:
            a = self.parent[a]
        return a

    def union(self, a, b):
        """
        You need to update the rank of the root only because that's what we use next for reference
        :param a:
        :param b:
        """
        rootA = self.find_root(a)
        rootB = self.find_root(b)
        if self.rank[rootB] > self.rank[rootA]:
            self.parent[rootA] = rootB
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        else:
            self.parent[rootA] = rootB
            self.rank[rootB] += 1

    def are_connected(self, a, b):
        rootA = self.find_root(a)
        rootB = self.find_root(b)
        return rootB == rootA


if __name__ == '__main__':
    d = DisjointSetUnionByRank(5)
    print(d.are_connected(1, 2))
    d.union(1, 2)
    print(d.are_connected(1, 2))
    d.union(2, 4)
    print(d.are_connected(1, 4))

