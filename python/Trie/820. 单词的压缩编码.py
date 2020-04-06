from typing import List


class Trie:
    def __init__(self):
        self.root = {}
        self.end_of_word = "#"
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]
        node[self.end_of_word] = self.end_of_word
    def search(self, word):
        node = self.root
        for w in word:
            node = node[w]
        return len(node) == 1



class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        goods = set(words)
        for word in words:
            for k in range(1, len(word)):
                goods.discard(word[k:])
        return sum(len(word)+1 for word in goods)
    # 字典树
    def minimumLengthEncoding2(self, words: List[str]) -> int:
        if not words:
            return 0
        trie = Trie()
        for word in set(words):
            trie.insert(word[::-1])
        print(trie.root)
        cnt = 0
        for word in words:
            if trie.search(word[::-1]):
                cnt += len(word)+1
        return cnt

words = ["time", "me", "bell"]
print(Solution().minimumLengthEncoding2(words))
