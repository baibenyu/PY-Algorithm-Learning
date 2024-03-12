# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/18 9:04'

import time


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:DFS--每个结点都尝试向左和向右走,方向与上一个相反,若不能满足条件了,说明应该重新赋值长度
    def longestZigZag(self, root: TreeNode) -> int:
        maxans = 0

        def dfs(o, direction, length):
            if not o:
                return

            nonlocal maxans
            maxans = max(maxans, length)
            if direction == 0:
                dfs(o.left, 1, length + 1)
                dfs(o.right, 0, 1)
            else:
                dfs(o.right, 0, length + 1)
                dfs(o.left, 1, 1)

        dfs(root, 0, 0)
        dfs(root, 1, 0)
        return maxans


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
