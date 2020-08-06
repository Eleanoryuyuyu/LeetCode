from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        distance = self.bfs(beginWord, wordSet)
        self.res = []
        self.dfs(beginWord, endWord, wordSet, distance, [beginWord])
        return self.res

    def bfs(self, beginWord, wordSet):
        queue = [beginWord]
        distance = {}
        distance[beginWord] = 0
        while queue:
            level = len(queue)
            for _ in range(level):
                curWord = queue.pop(0)
                for nextWord in self.get_next_word(curWord, wordSet):
                    if nextWord not in distance:
                        distance[nextWord] = distance[curWord] + 1
                        queue.append(nextWord)
        return distance

    def dfs(self, curWord, endWord, wordSet, distance, path):
        if curWord == endWord:
            self.res.append(path)
            return
        for nextWord in self.get_next_word(curWord, wordSet):
            if distance[nextWord] != distance[curWord] + 1:
                continue
            self.dfs(nextWord, endWord, wordSet, distance, path + [nextWord])

    def get_next_word(self, curWord, wordSet):
        import string
        next_words = []
        for i in range(len(curWord)):
            for c in string.ascii_lowercase:
                nextWord = curWord[:i] + c + curWord[i + 1:]
                if nextWord != curWord and nextWord in wordSet:
                    next_words.append(nextWord)
        return next_words


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(Solution().findLadders(beginWord, endWord, wordList))
