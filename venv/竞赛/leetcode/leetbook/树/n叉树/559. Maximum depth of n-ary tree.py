# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/16 10:04'

import time


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root:
            return max((self.maxDepth(child) for child in root.children), default = 0) + 1
        else:
            return 0


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
