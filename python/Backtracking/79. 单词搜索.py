from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) < 1:
            return False
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if self.DFS(board, i, j, rows, cols, 0, word, visited):
                    return True
        return False

    def DFS(self, board, i, j, rows, cols, pathLenght, word, visited):
        if pathLenght == len(word):
            return True
        hasPath = False
        if 0 <= i < rows and 0 <= j < cols and word[pathLenght] == board[i][j] and not visited[i][j]:
            pathLenght += 1
            visited[i][j] = True
            hasPath = self.DFS(board, i - 1, j, rows, cols, pathLenght, word, visited) or \
                      self.DFS(board, i + 1, j, rows, cols, pathLenght, word, visited) or \
                      self.DFS(board, i, j - 1, rows, cols, pathLenght, word, visited) or \
                      self.DFS(board, i, j + 1, rows, cols, pathLenght, word, visited)
            if not hasPath:
                pathLenght -= 1
                visited[i][j] = False
        return hasPath

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

print(Solution().exist(board, "ABCB"))
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.