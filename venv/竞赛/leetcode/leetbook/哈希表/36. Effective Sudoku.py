# __project_ = 'pythonProject'
# __author_ = 'baibe'
# __time_ = '2022/3/26 17:33'

import time
from typing import List


class Solution:
    # 方法一:模拟
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col, row, matrix = [[] for _ in range(9)], [[] for _ in range(9)], [[[] for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] not in col[j]:
                    col[j].append(board[i][j])
                elif board[i][j] != ".":
                    return False
                if board[i][j] not in row[i]:
                    row[i].append(board[i][j])
                elif board[i][j] != ".":
                    return False
                if board[i][j] not in matrix[i // 3][j // 3]:
                    matrix[i // 3][j // 3].append(board[i][j])
                elif board[i][j] != ".":
                    return False
        return True


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
