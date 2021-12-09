class DisjointSetPathCompression:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find_root(self, a):
        """
        Here is where the path compression works. We do a recursive call and update the parent with the root.
        :param a:
        :return:
        """
        if a == self.parent[a]:
            return a
        self.parent[a] = self.find_root(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        rootA = self.find_root(a)
        rootB = self.find_root(b)
        if rootB != rootA:
            self.parent[rootB] = rootA

    def are_connected(self, a, b):
        rootA = self.find_root(a)
        rootB = self.find_root(b)
        return rootB == rootA


if __name__ == '__main__':
    d = DisjointSetPathCompression(5)
    print(d.are_connected(1, 2))
    d.union(1, 2)
    print(d.are_connected(1, 2))
    d.union(2, 4)
    print(d.are_connected(1, 4))

