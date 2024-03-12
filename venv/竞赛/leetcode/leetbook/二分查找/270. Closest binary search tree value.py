# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/7/14 17:01'

import time


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res = root.val
        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val

            if root.val == target:
                return root.val
            elif target < root.val:  # 贪心 向target所在的区间走
                root = root.left
            else:
                root = root.right
        return res


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
