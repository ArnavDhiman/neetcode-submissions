class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = collections.defaultdict(set)
        incoming = collections.defaultdict(int)
        for word in words:
            for c in word:
                incoming[c] = 0
        prev_word = words[0]
        for word in words[1:]:
            for i in range(min(len(word), len(prev_word))):
                if word[i] != prev_word[i]:
                    if word[i] not in adj_list[prev_word[i]]:
                        adj_list[prev_word[i]].add(word[i])
                        incoming[word[i]] += 1
                    prev_word = word
                    break
                elif i == min(len(word), len(prev_word))-1:
                    if len(word) < len(prev_word):
                        incoming[prev_word[i]] = -1
                        break
        queue = deque()
        # print(adj_list, incoming)
        res = []
        for key, val in incoming.items():
            if val == 0:
                queue.append(key)
        while queue:
            # print(queue, res, incoming, adj_list)
            curr = queue.popleft()
            res.append(curr)
            for child in adj_list[curr]:
                incoming[child] -= 1
                if incoming[child] == 0:
                    queue.append(child)
        if len(res) == len(incoming):
            return "".join(res)
        return ""