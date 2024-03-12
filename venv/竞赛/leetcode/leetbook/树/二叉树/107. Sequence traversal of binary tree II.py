# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/3 7:41'
import collections
import time

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:BFS--在原层序遍历基础上,用栈存储结果 or 直接反转
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levelOrder = list()
        if not root:
            return levelOrder

        q = collections.deque([root])
        while q:
            level = list()
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levelOrder.append(level)

        return levelOrder[::-1]


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
