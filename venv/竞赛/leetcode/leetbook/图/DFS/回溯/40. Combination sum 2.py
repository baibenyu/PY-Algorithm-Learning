# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/4/23 17:25'
import collections
import time
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(candidates, target, sum, startIndex):
            if sum == target:
                res.append(path[:])
            for i in range(startIndex, len(candidates)):  # 要对同一树层使用过的元素进行跳过
                if sum + candidates[i] > target:
                    return
                if i > startIndex and candidates[i] == candidates[i - 1]:
                    continue  # 直接用startIndex来去重,要对同一树层使用过的元素进行跳过

                sum += candidates[i]
                path.append(candidates[i])
                backtrack(candidates, target, sum, i + 1)  # i+1:每个数字在每个组合中只能使用一次
                sum -= candidates[i]  # 回溯
                path.pop()  # 回溯

        candidates = sorted(candidates)  # 首先把给candidates排序，让其相同的元素都挨在一起。
        backtrack(candidates, target, 0, 0)
        return res


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
