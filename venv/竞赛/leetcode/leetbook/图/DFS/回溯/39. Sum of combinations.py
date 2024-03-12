# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/24 20:12'
from typing import List


class Solution:
    # 方法一:回溯+剪枝--在元素可以重复但顺序无所谓的情况下,要按特定分类来遍历所有可能
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def traceback(sum: int, startIdx: int):  # 按以某个元素为开头(至少包含一个)来分类遍历,需要限制后续递归中的组合能使用的元素
            if sum > target:
                return
            if sum == target:
                res.append(path[:])
                return
            for i in range(startIdx, len(candidates)):
                if sum + candidates[i] > target:  # 剪枝,对于已经超过结果的分支提前返回,不计算剩下部分,大大节省时间
                    return
                path.append(candidates[i])
                traceback(sum + candidates[i], i)
                path.pop()

        res, path = [], []
        candidates = sorted(candidates)
        target = target
        traceback(0, 0)
        return res
