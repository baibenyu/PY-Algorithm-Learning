# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/20 15:20'

import time


class TicTacToe:
    # 方法一:模拟
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = [[None] * n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        flag = 'X' if player == 1 else '0'
        self.board[row][col] = flag
        n = len(self.board)

        # 判断player是否通过第col列都是flag来赢
        win = 1
        for i in range(n):
            if self.board[i][col] != flag:
                win = 0
        if win == 1:
            return player

        # 判断player是否通过第row行都是flag来赢
        win = 1
        for j in range(n):
            if self.board[row][j] != flag:
                win = 0
        if win == 1:
            return player

        # 判断player是否通过斜对角线j-i=(col-row)都是flag来赢
        if row == col:
            win = 1
            for i in range(n):
                if 0 <= i + col - row < n:
                    if self.board[i][i + col - row] != flag:
                        win = 0
            if win == 1:
                return player

        # 判断player是否通过斜对角线j+i=n-1都是flag来赢
        if row + col == n - 1:
            win = 1
            for i in range(n):
                if 0 <= col + row - i < n:
                    if self.board[i][col + row - i] != flag:
                        win = 0
            if win == 1:
                return player
        return 0


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
