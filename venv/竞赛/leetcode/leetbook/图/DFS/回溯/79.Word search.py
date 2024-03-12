# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/6 9:03'
from typing import List


class Solution:
    # 方法一:回溯
    # 此题明显是全排列题目,必须遍历所有可能性才能知道是否存在,用回溯法
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            visited.add((i, j))
            result = False
            for di, dj in directions:  # 上下左右四个方向都要尝试
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:  # 要跳过已访问的坐标
                        if check(newi, newj, k + 1):
                            result = True
                            break

            visited.remove((i, j))  # 回溯
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):  # 尝试从每一个点出发
            for j in range(w):
                if check(i, j, 0):
                    return True

        return False

