# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/5/7 20:09'

import time
from typing import List


class Solution:
    # 方法一:单调栈--局部单调递减,总体递增
    # 栈弹出的值相当于对树从左往右画右斜线
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        new_min = float('-inf')  # 初始化下限值
        for i in range(len(preorder)):
            if preorder[i] < new_min:
                return False
            while stack and preorder[i] > stack[-1]:
                new_min = stack.pop()
            stack.append(preorder[i])
        return True


if __name__ == '__main__':
    start = time.clock()
    end = time.clock()
    print(end - start)
