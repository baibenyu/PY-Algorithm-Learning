# __project_ = '算法学习'
# __author_ = 'baibe'
# __time_ = '2022/8/2 10:06'
import collections
import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 方法一:DFS
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, value):
            if not root:
                return 0
            if not root.left and not root.right:
                return value
            left = 0
            right = 0
            if root.left:
                left = dfs(root.left, value * 10 + root.left.val)
            if root.right:
                right = dfs(root.right, value * 10 + root.right.val)
            return left + right

        return dfs(root, root.val)

    # 方法二:BFS
    def sumNumbers2(self, root: TreeNode) -> int:
        if not root:
            return 0

        total = 0
        nodeQueue = collections.deque([root])
        numQueue = collections.deque([root.val])

        while nodeQueue:
            node = nodeQueue.popleft()
            num = numQueue.popleft()
            left, right = node.left, node.right
            if not left and not right:
                total += num
            else:
                if left:
                    nodeQueue.append(left)
                    numQueue.append(num * 10 + left.val)
                if right:
                    nodeQueue.append(right)
                    numQueue.append(num * 10 + right.val)

        return total


if __name__ == '__main__':
    start = time.perf_counter()

    end = time.perf_counter()
    print(end - start)
