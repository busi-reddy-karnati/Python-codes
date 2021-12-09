class DisjointSet:
    def __init__(self, n):
        self.parent = [0]*n
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


class TrieNode:
    def __init__(self):
        self.children = []
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string):
        root = self.root
        for char in string:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
        root.is_end = True

    def is_there(self, string):
        root = self.root
        for char in string:
            if char not in root.children:
                return False
            root = root.children[char]
        return root.is_end

    def is_prefix(self, string):
        root = self.root
        for char in string:
            if char not in root.children:
                return False
            root = root.children[char]
        return True


def first_occurance(a, target):
    """

    :param a: array
    :param target: target integer
    :return: index of first occurance of a number or -1
    """
    hi = len(a) - 1
    lo = 0
    ans = -1
    while lo <= hi:
        mid = int((lo + hi) / 2)
        if a[mid] == target:
            ans = mid
            hi = mid - 1
        elif a[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1

    return ans


def last_occurance(nums, target):
    """

    :param nums: array
    :param target: the target integer
    :return: index of last occurance or -1
    """
    ans = -1
    hi = len(nums) - 1
    lo = 0
    while hi >= lo:
        mid = int((lo + hi) / 2)
        if nums[mid] == target:
            ans = mid
            lo = mid + 1
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return ans


def generate_permutations(nums, start):
    """

    :param nums: array
    :param start: index from which the permutations should start
    :return: a list of lists that is permutations
    """
    if start == len(nums):
        return [[]]
    ret = []
    for i in range(start, len(nums)):
        nums[start], nums[i] = nums[i], nums[start]
        perms = generate_permutations(nums, start + 1)
        for perm in perms:
            perm.append(nums[start])
        ret.extend(perms)
        # In the step before, you swapped [1,2,3] => [2,1,3] Now 2 and 3 will get swapped, which is not expected, so
        # Swap again
        nums[start], nums[i] = nums[i], nums[start]
    return ret


def main():
    d = DisjointSet(5)
    print(d.are_connected(1, 2))
    print("Adding 1,2")
    d.union(1, 2)
    print(d.are_connected(1, 2))


if __name__ == '__main__':
    main()

