# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/2/23 15:49'
import itertools
from typing import List


class Solution:
    # 方法一:利用哈希表存储数字及其映射,若输入的是多个输入的可迭代序列(如放在列表中的多个输入)要在变量前加*,表示多个输入
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans = []
        groups = (phoneMap[digit] for digit in digits)
        for combination in itertools.product(*groups):  # product以元组类型输出笛卡尔积
            # print(combination)
            ans.append("".join(combination))  # join可将元组转为字符串
        return ans

    # 方法二:回溯遍历所有可能组合,为什么要回溯呢?因为每个数字对应多种可能,而一个字符串有多个数字的对应字符组成,每次只能遍历一个
    def letterCombinations2(self, digits: str) -> List[str]:
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):  # 每完成一个字符串
                combinations.append("".join(combination))
            else:
                digit = digits[index]  # 取出对应位置的数字
                for letter in phoneMap[digit]:  # 遍历数字对应的可能字符
                    combination.append(letter)
                    backtrack(index + 1)  # 换下一个数字
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations

    # 方法三:暴力
    def letterCombinations3(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        conversion = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                      '9': 'wxyz'}
        product = ['']
        for k in digits:  # 结果字符串是由前身加上当前数字组合而成的
            product = [i + j for i in product for j in conversion[k]]
        return product
