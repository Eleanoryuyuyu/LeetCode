from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rx, ry = i, j
        dx, dy = [0, 1, 0, -1 ], [1, 0, -1, 0 ]
        res = 0
        for i in range(4):
            step = 0
            while True:
                tx, ty = rx + dx[i]*step, ry + dy[i]*step
                if tx < 0 or tx >= 8 or ty < 0 or ty >= 8 or board[tx][ty] == 'B':
                    break
                if board[tx][ty] == 'p':
                    res += 1
                    break
                step += 1
        return res

board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]

print(Solution().numRookCaptures(board))