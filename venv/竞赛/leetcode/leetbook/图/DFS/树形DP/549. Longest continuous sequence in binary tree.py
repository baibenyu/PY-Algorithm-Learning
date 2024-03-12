# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/17 8:39'

import time


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = None

    # 方法一:DFS--后序遍历汇总式
    def dfs(self, rt: TreeNode):
        if rt is None:
            return 0, 0
        inc, dec = 1, 1  # 自上往下看，是升序还是降序
        if rt.left:
            L_inc, L_dec = self.dfs(rt.left)
            if rt.left.val == rt.val + 1:
                inc = L_inc + 1
            elif rt.left.val == rt.val - 1:
                dec = L_dec + 1
        if rt.right:
            R_inc, R_dec = self.dfs(rt.right)
            if rt.right.val == rt.val + 1:
                inc = max(inc, R_inc + 1)
            elif rt.right.val == rt.val - 1:
                dec = max(dec, R_dec + 1)
        self.res = max(self.res, inc + dec - 1)
        return inc, dec

    def longestConsecutive(self, root: TreeNode) -> int:
        # 分上升和下降2种情况
        self.res = 0
        self.dfs(root)
        return self.res


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
