# __project_ = 'reptile'
# __author_ = 'baibe'
# __time_ = '2022/3/6 10:21'
from typing import List


class Solution:
    # 方法一:单调栈
    # 跟84题作对比,将矩阵中的每一行都枚举为底座,列中连续的1作为柱子的高度
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        # 记录当前位置上方连续“1”的个数
        pre = [0] * (n + 1)  # 多一个末尾的0,是为了将栈中所有有效高度都弹出并计算对应矩形的面积
        res = 0
        for i in range(m):
            for j in range(n):
                # 前缀和
                pre[j] = pre[j] + 1 if matrix[i][j] == "1" else 0

            # 单调栈
            stack = [-1]  # 防止栈为空
            for k, num in enumerate(pre):
                while stack and pre[stack[-1]] > num:
                    index = stack.pop()
                    res = max(res, pre[index] * (k - stack[-1] - 1))  # 宽度=右边比自身低的柱子下标-左边比自身低的柱子下标-1
                stack.append(k)
        return res
