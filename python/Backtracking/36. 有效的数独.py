from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) < 9:
            return False
        return self.solved(board)

    def solved(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in range(ord('1'), ord('9') + 1):
                        if self.isValid(board, i, j, chr(c)):
                            board[i][j] = chr(c)
                            if self.solved(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def isValid(self, board, row, col, c):
        for i in range(9):
            if board[i][col] != '.' and board[i][col] == c:
                return False
            if board[row][i] != '.' and board[row][i] == c:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] != '.' and board[3 * (row // 3) + i // 3][
                3 * (col // 3) + i % 3] == c:
                return False
        return True

board = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
print(Solution().isValidSudoku(board))