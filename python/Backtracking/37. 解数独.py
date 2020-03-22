from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowUsed = [[False] * 10 for _ in range(9)]
        colUsed = [[False] * 10 for _ in range(9)]
        boxUsed = [[[False]* 10 for _ in range(3)] for _ in range(3)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    rowUsed[i][num] = True
                    colUsed[j][num] = True
                    boxUsed[i//3][j//3][num] = True

        self.board = board
        self.backtracking(0, 0, rowUsed, colUsed, boxUsed)
        print(self.board)

    def backtracking(self, col, row, rowUsed, colUsed, boxUsed):
        if col == len(self.board[0]):
            col = 0
            row += 1
            if row == len(self.board):
                return True
        if self.board[row][col] == '.':
            for c in range(1,10):
                canUsed = not(rowUsed[row][c] or colUsed[col][c] or boxUsed[row//3][col//3][c])
                if canUsed:
                    rowUsed[row][c] = True
                    colUsed[col][c] = True
                    boxUsed[row//3][col//3][c] = True

                    self.board[row][col] = str(c)
                    if self.backtracking(col+1, row, rowUsed, colUsed, boxUsed):
                        return True

                    self.board[row][col] = '.'
                    rowUsed[row][c] = False
                    colUsed[col][c] = False
                    boxUsed[row//3][col//3][c] = False
        else:
            return self.backtracking(col+1, row, rowUsed, colUsed, boxUsed)


board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
print(Solution().solveSudoku(board))



