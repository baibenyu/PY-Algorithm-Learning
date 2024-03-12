# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/17 7:48'
from typing import List


class Solution:
    # 方法一:集合中的每个元素都只有两个状态,在子集中和不在子集中,对应于1和0.因为有n个元素所以对应的状态序列(即01序列)有2**n个,一个序列对应一个子集(非空子集只需减去全0)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        mask = 2 ** length
        res = []
        for i in range(mask):
            string = bin(i).replace("0b", "")
            length2 = len(string)
            temp = []
            for j in range(length2):
                if string[length2 - j - 1] == "1":  # 倒取二进制位
                    temp.append(nums[j])
            res.append(temp)
        return res

    # 方法二:迭代,每一次将新元素进入res列表中时,都将新元素与res列表中的每一个重新组合成新列表,确保了不会重复.又因为每一个只增加了一个新元素的集合,它的子集就是在之前的每个子集上加入新元素,子集数量翻倍

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

    # 方法三:回溯递归算法--回溯的本质就是暴力枚举,不过是有方向的枚举
    class Solution:
        def subsets(self, nums: List[int]) -> List[List[int]]:
            def backtrack(index, tmp):
                res.append(tmp)
                for i in range(index, n):  # 尝试子集与剩下元素的组合
                    backtrack(i + 1, tmp + [nums[i]])  # 产生一个新子集

            n = len(nums)
            res = []
            backtrack(0, [])
            return res
