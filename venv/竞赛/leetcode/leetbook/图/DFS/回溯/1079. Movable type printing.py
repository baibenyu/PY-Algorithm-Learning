# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/10 8:23'

import time


class Solution:
    # 方法一:DFS--经典去重
    def numTilePossibilities(self, tiles: str) -> int:
        res = 0
        if not tiles:
            return res
        length, tiles = len(tiles), sorted(tiles)  # 要排序，把所有相同的字母放在一起

        def backtrack(used):
            nonlocal res

            for i in range(length):
                if used[i]:
                    continue
                # tiles[i] == tiles[i - 1] 同一层有重复
                # used[i - 1] 同一树枝的元素是否使用过
                # used[i - 1] == True，说明同一树支tiles[i - 1]使用过
                # used[i - 1] == False 说明同一树层tiles[i - 1]使用过
                # 同一层前一个元素与当前元素相同，且，前一个元素使用过
                if i > 0 and tiles[i] == tiles[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                res += 1
                backtrack(used)
                used[i] = False

        backtrack([False] * length)
        return res


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
