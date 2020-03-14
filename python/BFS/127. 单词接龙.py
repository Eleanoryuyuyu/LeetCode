from typing import List
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or len(beginWord) != len(endWord) or not beginWord\
                or not endWord or not wordList:
            return 0
        l = len(beginWord)
        gen_dict = defaultdict(list)
        for word in wordList:
            for i in range(l):
                gen_dict[word[:i]+'*'+word[i+1:]].append(word)
        queue = []
        queue.append((beginWord,1)) # 记录（单词，层数）
        visited = defaultdict(bool)
        visited[beginWord] = True
        while queue:
            cur, level = queue.pop(0)
            for i in range(l):
                model = gen_dict[cur[:i] + '*' + cur[i+1:]]
                for word in model:
                    if word == endWord:
                        return level+1
                    if not visited[word]:
                        visited[word] = True
                        queue.append((word,level+1))
        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(Solution().ladderLength(beginWord,endWord, wordList))


