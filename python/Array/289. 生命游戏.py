from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        def isValid(i, j):
            return 0<=i<n and 0<=j<m
        def mapping(i,j):
            direct = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            tmp = [board[i+d[0]][j+d[1]] for d in direct if isValid(i+d[0], j+d[1])]
            cnt = sum(tmp)
            if cnt == 2:
                return board[i][j]
            elif cnt == 3:
                return 1
            else:
                return 0
        board[:] = [[mapping(i,j) for j in range(m)] for i in range(n)]
        print(board)

board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Solution().gameOfLife(board)
