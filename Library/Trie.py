
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

