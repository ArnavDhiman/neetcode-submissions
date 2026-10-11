class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord) != len(endWord):
            return 0

        adj_list = collections.defaultdict(list)
        for i, word in enumerate(wordList):
            for j, word_t in enumerate(wordList[i+1:]):
                if self.dist(word, word_t) == 1:
                    adj_list[word].append(word_t)
                    adj_list[word_t].append(word)
        if endWord not in adj_list:
            return 0
        
        if beginWord not in adj_list:
            for i,word in enumerate(wordList):
                if self.dist(word, beginWord) == 1:
                    adj_list[beginWord].append(word)
        # print(adj_list)
        seen = set()
        queue = deque([(beginWord, 1)])
        seen.add(beginWord)
        while queue:
            # print(queue)
            word, step = queue.popleft()
            if word == endWord:
                return step
            for child in adj_list[word]:
                if child not in seen:
                    queue.append((child, step+1))
                    seen.add(child)
        return 0

        

    def dist(self, word1, word2):
        d = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                d+=1
        return d