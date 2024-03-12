# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/18 20:16'

import time
from typing import List


class Solution:
    # 方法一:按排列回溯
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():  # 生成符合条件的棋盘
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):  # 按行尝试
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:  # 同列不可能放置
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        solutions = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()  # 对角线1
        diagonal2 = set()  # 对角线2
        row = ["."] * n
        backtrack(0)
        return solutions


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
