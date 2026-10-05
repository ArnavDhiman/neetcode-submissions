class PrefixTree:

    def __init__(self):
        self.head = Trie()

    def insert(self, word: str) -> None:
        node = self.head
        for c in word:
            if c not in node.hmap:
                node.hmap[c] = Trie()
            node = node.hmap[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.head
        for c in word:
            if c not in node.hmap:
                return False
            node = node.hmap[c]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.head
        for c in prefix:
            if c not in node.hmap:
                return False
            node = node.hmap[c]
        return True
        
class Trie:
    def __init__(self):
        self.hmap = {}
        self.is_end = False