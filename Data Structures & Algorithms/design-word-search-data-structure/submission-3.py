class WordDictionary:

    def __init__(self):
        self.head = Trie()

    def addWord(self, word: str) -> None:
        node = self.head
        for c in word:
            if c not in node.hmap:
                node.hmap[c] = Trie()
            node = node.hmap[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        queue = deque() 
        queue.append((0, self.head))
        # print("START ---- ", word)
        while queue:
            idx, node = queue.popleft()
            # print(idx, node.hmap, node.is_end, queue)
            if idx == len(word):
                return node.is_end
            if word[idx] == ".":
                for key in node.hmap:
                    queue.append((idx+1, node.hmap[key]))
            else:
                if word[idx] not in node.hmap:
                    continue
                if idx == len(word)-1:
                    return node.hmap[word[idx]].is_end
                queue.append((idx+1, node.hmap[word[idx]]))
                
        return idx == len(word)
        
class Trie:
    def __init__(self):
        self.hmap = {}
        self.is_end = False