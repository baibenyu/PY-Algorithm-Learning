# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/17 9:20'

import time


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = 0

    # 方法一:DFS--设每层递归时,都必须用到根结点
    def longestUnivaluePath(self, root: TreeNode) -> int:

        def maxLen(node):
            if node is None:
                return 0
            left = maxLen(node.left)
            right = maxLen(node.right)
            if node.left:
                left = left + 1 if node.left.val == node.val else 0
            if node.right:
                right = right + 1 if node.right.val == node.val else 0

            self.res = max(self.res, left + right)
            return max(left, right)

        maxLen(root)
        return self.res


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
