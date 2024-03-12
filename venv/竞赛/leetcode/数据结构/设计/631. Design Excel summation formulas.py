# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/29 15:59'

import time
from typing import List, Tuple

Location = Tuple[int, int]  # [x, y]


class Excel:
    # 方法一:递归+模拟
    class SumCell(object):
        def __init__(self, dependencies: List[Tuple[Location, Location]]):
            self.dependencies = dependencies

    class ValueCell(object):
        def __init__(self, value: int):
            self.value = value

    def __init__(self, height: int, width: str):
        rows, cols = self._get_grid_loc(height, width)
        self.grid = [[Excel.ValueCell(0) for _ in range(cols + 1)] for _ in range(rows + 1)]

    def set(self, row: int, column: str, val: int) -> None:
        x, y = self._get_grid_loc(row, column)
        self.grid[x][y] = Excel.ValueCell(val)

    def get(self, row: int, column: str) -> int:
        x, y = self._get_grid_loc(row, column)
        return self._get_by_loc(x, y)

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        x, y = self._get_grid_loc(row, column)
        dependencies = []

        def trans_colrow_to_loc(colrow: str) -> Location:
            col, row = colrow[0], colrow[1:]
            return self._get_grid_loc(int(row), col)

        for expression in numbers:
            if ':' not in expression:
                cur_x, cur_y = trans_colrow_to_loc(expression)
                dependencies.append(((cur_x, cur_y), (cur_x, cur_y)))
            else:
                start, end = expression.split(':')
                start_x, start_y = trans_colrow_to_loc(start)
                end_x, end_y = trans_colrow_to_loc(end)
                dependencies.append(((start_x, start_y), (end_x, end_y)))
        self.grid[x][y] = Excel.SumCell(dependencies)
        return self._get_by_loc(x, y)

    def _get_grid_loc(self, row: int, column: str) -> Location:
        return row - 1, ord(column) - ord('A')

    def _get_by_loc(self, x: int, y: int) -> int:
        if isinstance(self.grid[x][y], Excel.ValueCell):
            return self.grid[x][y].value
        else:
            return self._calc_sum(self.grid[x][y])

    def _calc_sum(self, cell: 'Excel.SumCell') -> int:
        """
        calc recursively, some cell may be another sum formula,
        and there's can't be a cycle
        """
        cur_sum = 0
        for (sx, sy), (ex, ey) in cell.dependencies:
            for x in range(sx, ex + 1):
                for y in range(sy, ey + 1):
                    cur_sum += self._get_by_loc(x, y)
        return cur_sum


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
