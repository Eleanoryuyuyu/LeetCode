from typing import List

class Trie:
    def __init__(self):
        self.root = {}
        self.end_of_word = '#'
    def insert(self, word):
        node = self.root
        for char in word:
            node[char] = node.setdefault(char, {})
            node = node[char]
        node[self.end_of_word] = self.end_of_word
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

class Solution:
    # 1. DFS, python会超时
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not len(board) or not len(board[0]) or not words:
            return []
        rows = len(board)
        cols = len(board[0])
        result = set()
        for word in words:
            visited = [[False] * cols for _ in range(rows)]
            for i in range(rows):
                for j in range(cols):
                    if self.DFS(board, i, j, rows, cols, 0, word, visited):
                        result.add(word)
        return list(result)
    def DFS(self, board, i, j, rows, cols, pathLength, word, visited):
        if pathLength == len(word):
            return True
        hasPath = False
        if 0<=i<rows and 0<=j<cols and board[i][j] == word[pathLength] and not visited[i][j]:
            pathLength += 1
            visited[i][j] = True
            hasPath = self.DFS(board, i-1, j, rows, cols, pathLength, word, visited) or \
                      self.DFS(board, i+1, j, rows, cols, pathLength, word, visited) or \
                      self.DFS(board, i, j-1, rows, cols, pathLength, word, visited) or \
                      self.DFS(board, i, j+1, rows, cols, pathLength, word, visited)
            if not hasPath:
                pathLength -= 1
                visited[i][j] = False
        return hasPath

    # 2. 字典树
    def findWords2(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(board) < 1 or len(board[0]) < 1 or len(words) < 1:
            return []
        trie = Trie()
        for word in words:
            trie.insert(word)
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        self.result = set()
        for i in range(rows):
            for j in range(cols):
                self._DFS(board, i, j, rows, cols, "", trie, visited)
        return list(self.result)
    def _DFS(self, board, i, j, rows, cols, path, trie, visited):
        if i < 0 or i >= rows or j < 0 or j >=cols:
            return
        if visited[i][j]:
            return
        path += board[i][j]
        if not trie.startsWith(path):
            return
        if trie.search(path):
            self.result.add(path)
        visited[i][j] = True
        self._DFS(board, i - 1, j, rows, cols, path, trie, visited)
        self._DFS(board, i + 1, j, rows, cols, path, trie, visited)
        self._DFS(board, i, j - 1, rows, cols, path, trie, visited)
        self._DFS(board, i, j + 1, rows, cols, path, trie, visited)
        visited[i][j] = False




board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
print(Solution().findWords2(board, words))